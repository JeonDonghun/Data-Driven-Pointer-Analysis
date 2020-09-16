import copy
import os
import subprocess
import re
import sys
import json



def calClauseNum(partFormula,notD0Formula):
 
  
  f = open("heuristic.logic","w")
  f.write("D3(?meth) -> MethodSignatureRef(?meth).\n")
  f.write("D0(?meth) -> MethodSignatureRef(?meth).\n\n\n")

  f.write("D3(?meth)<-\n")
  for i in range(0,len(partFormula)):
    
    f.write(partFormula[i]+"(?meth),\n")
      
  f.write("MethodSignatureRef(?meth).\n\n\n")  
  
  f.write("D0(?meth)<-\n")
  f.write("!NotD0(?meth),\n")
  f.write("MethodSignatureRef(?meth).\n\n\n")

  for i in range(0,len(notD0Formula)):
    f.write("NotD0(?meth)<-\n")
    for j in range(0,len(notD0Formula[i])):
      f.write(notD0Formula[i][j]+"(?meth),\n")
    f.write("MethodSignatureRef(?meth).\n\n\n")  
  f.close()
    
  os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')
  os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar')
  os.system('bloxbatch -db last-analysis -query D3 | sort > sig.facts')
  f = open("sig.facts","r")
  methodNum = f.readlines()
  

  return len(methodNum)



def BiggestClause(clauseMethodNum):
  minimalNum = 0
  biggest =0
  for i in range(0,len(clauseMethodNum)):
    #if(clauseMethodNum[i]==0):continue

    if(clauseMethodNum[i]>biggest):
      biggest = clauseMethodNum[i]
      minimalNum = i

  return minimalNum



def precisionChange(startFormula,notD0Formula):
  precisionCheck =0
  alarmNum=0
  f = open("ChangedAlarm_Numluindex.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)
  print(precisionCheck)

  f = open("ChangedAlarm_Numlusearch.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)
  print(precisionCheck)

  f = open("ChangedAlarm_Numpmd.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)
  print(precisionCheck)

  f = open("ChangedAlarm_Numantlr.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)
  print(precisionCheck)

  return precisionCheck




def oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed,notD0Formula):
  startFormula = makheuristic(startFormula,notD0Formula)
 
  checkTime =0.0
  changedAlarmNum=0
  
  #checking time out
  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    
    return backUpFormula,10000
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numluindex.facts')

  checkTime = checkTime+float(analysisTime)

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula,10000
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numlusearch.facts')
  checkTime = checkTime+float(analysisTime)
  

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula,10000
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numpmd.facts')
  checkTime = checkTime+float(analysisTime)

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula,10000
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numantlr.facts')
  checkTime = checkTime+float(analysisTime)

  #prepare timeout by making backup file

  os.system('cp ChangedAlarm_Numluindex.facts  backupluindex.facts')
  os.system('cp ChangedAlarm_Numlusearch.facts  backuplusearch.facts')
  os.system('cp ChangedAlarm_Numpmd.facts  backuppmd.facts')
  os.system('cp ChangedAlarm_Numantlr.facts  backupantlr.facts')

  #calculus precision

  f = open("ChangedAlarm_Numluindex.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)

  f = open("ChangedAlarm_Numlusearch.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)  

  f = open("ChangedAlarm_Numpmd.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)

  f = open("ChangedAlarm_Numantlr.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)
  
  print("changedAlarmNum")
  print(changedAlarmNum)
  print("bestPrecision")
  print(bestPrecision)
  
  #timeoutCheck = analysisTime


  if(changedAlarmNum < 1756 ):#alarmNum +1 < bestPrecision
    print("changed")
    return startFormula,checkTime
  else:
    print("notchanged")
    for t in range(0,len(backUpFormula)):
      print(backUpFormula[t])
    return backUpFormula,bestCost
  




def runDoop (cmd, dooppath):
  print (cmd)
  cwd = os.getcwd()
  
  os.chdir(dooppath)
  output = subprocess.check_output(dooppath + '/' + cmd + '; exit 0;', stderr=subprocess.STDOUT, shell=True)
  os.chdir(cwd)

  time_pattern = re.compile(r'analysis time:\s+([0-9,\.]+)s')
  m = time_pattern.search(output)
  if m == None:
    print ('Time string doesn\'t exist: {}'.format(output))
    return 'timeout'
  
  return m.group(1)


def makheuristic(startFormula,notD0Formula):
  	

  f = open("heuristic.logic","w")
  f.write("D3(?meth) -> MethodSignatureRef(?meth).\n")
  f.write("D0(?meth) -> MethodSignatureRef(?meth).\n\n\n")


  f.write("D3(?meth)<-\n")
  for j in range(0,len(startFormula)):
    f.write(startFormula[j]+"(?meth),\n")
  f.write("MethodSignatureRef(?meth).\n\n\n")  
  
  
  f.write("D0(?meth)<-\n")
  f.write("!NotD0(?meth),\n")
  f.write("MethodSignatureRef(?meth).\n\n\n")

  for i in range(0,len(notD0Formula)):
    f.write("NotD0(?meth)<-\n")
    for j in range(0,len(notD0Formula[i])):
      f.write(notD0Formula[i][j]+"(?meth),\n")
    f.write("MethodSignatureRef(?meth).\n\n\n")  
  
  
  
  
  f.close()
  os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')


  return startFormula



def makeRecentHeuristic(startFormula,notD0Formula):
  
  fa = open("recentHeuristic23D3.logic","w")
  for k in range(0,len(startFormula)): 
    for p in range(0,len(startFormula[k])):
      fa.writelines(startFormula[k][p])
      fa.write(" ")
    fa.write("\n")    
  fa.close()


  fa = open("recentHeuristic23D0.logic","w")
  for k in range(0,len(notD0Formula)): 
    for p in range(0,len(notD0Formula[k])):
      fa.writelines(notD0Formula[k][p])
      fa.write(" ")
    fa.write("\n")    
  fa.close()





#filename = 'recentHeuristic0.logic'##################################################you must change me later!!!!!

filename1 = 'recentHeuristic1.logic'






with open(filename1) as data:
  startFormula = [[i for i in line.split()] for line in data.readlines()]
os.system('cp logic/depth2and3.logic logic/context-sensitive.logic')


Fset = ['Feature0','Feature1','Feature2','Feature3','Feature4','Feature5','Feature6','Feature7','Feature8','Feature9','Feature10','Feature11','Feature12','Feature13','Feature14','Feature15','Feature16','Feature17','Feature18','Feature19','Feature20','Feature21','Feature22','Feature23','Feature24','Feature25','Feature26','Feature27','Feature28','Feature29','Feature32','Feature33','Feature34','Feature35','Feature36','Feature37']




for i in range(0,len(startFormula)):
  print(startFormula[i])

backUpFormula = copy.deepcopy(startFormula)

notD0Formula = copy.deepcopy(startFormula)


startFormula = []

backUpFormula = copy.deepcopy(startFormula)


makheuristic(startFormula,notD0Formula)

os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')




timeRepository = 0.0
precissionRepository = 0


cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
dooppath = '/home/minseokjeon/doop'
analysisTime = runDoop (cmd,dooppath)
os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > luindexAlarm_Num.facts')

##time out check do!

timeRepository = timeRepository + float(analysisTime)

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar'
analysisTime = runDoop (cmd,dooppath)
os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > lusearchAlarm_Num.facts')

timeRepository = timeRepository + float(analysisTime)

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
analysisTime = runDoop (cmd,dooppath)
os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > pmdAlarm_Num.facts')

timeRepository = timeRepository + float(analysisTime)

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop (cmd,dooppath)
os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > antlrAlarm_Num.facts')

timeRepository = timeRepository + float(analysisTime)

print(timeRepository)

timeRepository = 417.7

f = open("luindexAlarm_Num.facts","r")
alarmNum = f.readlines()
precissionRepository = precissionRepository + len(alarmNum)
f.close()


f = open("lusearchAlarm_Num.facts","r")
alarmNum = f.readlines()
precissionRepository = precissionRepository + len(alarmNum)
f.close()


f = open("pmdAlarm_Num.facts","r")
alarmNum = f.readlines()
precissionRepository = precissionRepository + len(alarmNum)
f.close()


f = open("antlrAlarm_Num.facts","r")
alarmNum = f.readlines()
precissionRepository = precissionRepository + len(alarmNum)
f.close()




bestCost = timeRepository
bestPrecision = precissionRepository

#bestCost =471.5
#bestPrecision = 1718

for i in range(0,len(backUpFormula)):
  print(backUpFormula[i])

print("precision and cost at starting point")
print(bestPrecision)#1718
print(bestCost)
print("start Learning \n\n\n\n")



changed = 0
precisionCheck = bestPrecision

precisionRepository = bestPrecision

checkFeatureNum = 0

clauseFixPrecision = precisionCheck



backUpFormula = copy.deepcopy(startFormula)

'''

#delete useless clause
for i in range(len(startFormula),0,-1):
  changedAlarmNum =0
  print("cache clear")
  os.system("rm -r cache/*")
  del startFormula[i-1]
  makheuristic(startFormula,notD0Formula)
  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numluindex.facts')
    
  f = open("ChangedAlarm_Numluindex.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)


  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numlusearch.facts')
    
  f = open("ChangedAlarm_Numlusearch.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numpmd.facts')
    
  f = open("ChangedAlarm_Numpmd.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)


  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numantlr.facts')
    
  f = open("ChangedAlarm_Numantlr.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)
  
  if(changedAlarmNum != precisionCheck):
    startFormula = copy.deepcopy(backUpFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
  elif(changedAlarmNum == precisionCheck):
    backUpFormula = copy.deepcopy(startFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
    continue
  else:
    print("some thing wrong!!!!!!!!")

'''


afterTopdown =0

#do top down depth 2 and 3
for f in range(0,len(Fset)):
    #for j in range(0,len(startFormula[i])):
      if(Fset[f] in startFormula):
        print(Fset[f]+"is already in")
        continue
      else : startFormula = startFormula + [Fset[f]] 
      print("cache clear")
      os.system("rm -r cache/*")

      print("append check\n")
      for e in range(0,len(startFormula)):
        print(startFormula[e])
      
      oneMimimalLearningReturn = oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed,notD0Formula)
    
      startFormula = copy.deepcopy(oneMimimalLearningReturn[0])
      timeCheck = oneMimimalLearningReturn[1]

      #print("backupcheck")
      #print()
      #for q in range(0,len(startFormula)):
      #  print(startFormula[q])
      
      precisionCheck = precisionChange(startFormula,notD0Formula)
      #timeCheck = timeChange()
      
      print("timeCheck")
      print(timeCheck)
      print("precisionCheck")
      print(precisionCheck)

      if(1756 > precisionCheck):
        print("cost condition pass")
          
        checkFeatureNum = f
        print("cost  refine \n")
        print(Fset[f]+" will be append")
        backUpFormula = copy.deepcopy(startFormula)
        afterTopdown = precisionCheck
          #startFormula = copy.deepcopy(backUpFormula)
          #print("not deleted Feature ="+deletedFeature)
          
        print(startFormula)
      else:
        print(Fset[f]+" not good")
        print("precision not refine\n")

        startFormula = copy.deepcopy(backUpFormula) 
        print(startFormula)









'''
for i in range(len(startFormula),0,-1):
  changedAlarmNum =0
  print("cache clear")
  os.system("rm -r cache/*")
  del startFormula[i-1]
  makheuristic(startFormula,notD0Formula)
  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numluindex.facts')
    
  f = open("ChangedAlarm_Numluindex.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)


  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numlusearch.facts')
    
  f = open("ChangedAlarm_Numlusearch.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numpmd.facts')
    
  f = open("ChangedAlarm_Numpmd.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)


  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
  analysisTime = runDoop(cmd,dooppath)
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numantlr.facts')
    
  f = open("ChangedAlarm_Numantlr.facts","r")
  alarmnum = f.readlines()
  f.close()
  changedAlarmNum = changedAlarmNum +len(alarmnum)
  
  if(changedAlarmNum != afterTopdown):
    startFormula = copy.deepcopy(backUpFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
  elif(changedAlarmNum == precisionCheck):
    backUpFormula = copy.deepcopy(startFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
    continue
  else:
    print("some thing wrong!!!!!!!!")
'''





print("Area 3 is Fixed ")
for i in range(0,len(startFormula)):
  print(startFormula[i])

#make 0/1/3 heurisitic
makheuristic(startFormula,notD0Formula)

makeRecentHeuristic(startFormula,notD0Formula)





