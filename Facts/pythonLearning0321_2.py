import copy
import os
import subprocess
import re
import sys
import json



def calClauseNum(a,partFormula,notD0Formula):
 
  
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




def oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed,notD0Formula,D2Formula):
  startFormula = makheuristic(D2Formula,startFormula,notD0Formula)

  
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


def makheuristic(D2Formula,startFormula,notD0Formula):
  	

  f = open("heuristic.logic","w")
  f.write("D3(?meth) -> MethodSignatureRef(?meth).\n")
  f.write("D2(?meth) -> MethodSignatureRef(?meth).\n")
  f.write("D0(?meth) -> MethodSignatureRef(?meth).\n\n\n")

  f.write("D2(?meth)<-\n")
  for i in range(0,len(D2Formula)):
    f.write(D2Formula[i]+"(?meth),\n")
  f.write("MethodSignatureRef(?meth).\n\n\n")

  for i in range(0,len(startFormula)):
    f.write("D3(?meth)<-\n")
    for j in range(0,len(startFormula[i])):
      f.write(startFormula[i][j]+"(?meth),\n")
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
  
  fa = open("recentHeuristic23D3.logic.logic","w")
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





filename3 = 'recentHeuristic23D3.logic'##################################################you must change me later!!!!!

filename0 = 'recentHeuristic23D0.logic'






with open(filename3) as data:
  startFormula = [[i for i in line.split()] for line in data.readlines()]
#os.system('cp logic/depth2and3.logic logic/context-sensitive.logic')



with open(filename0) as data:
  notD0Formula = [[i for i in line.split()] for line in data.readlines()]

Fset = ['Feature0','Feature1','Feature2','Feature3','Feature4','Feature5','Feature6','Feature7','Feature8','Feature9','Feature10','Feature11','Feature12','Feature13','Feature14','Feature15','Feature16','Feature17','Feature18','Feature19','Feature20','Feature21','Feature22','Feature23','Feature24','Feature25','Feature26','Feature27','Feature28','Feature29','Feature32','Feature33','Feature34','Feature35','Feature36','Feature37']


D2Formula = []


backUpFormula = copy.deepcopy(D2Formula)

os.system('cp logic/depth1and2.logic logic/context-sensitive.logic')
makheuristic(D2Formula,startFormula,notD0Formula)

os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')


timeRepository = 0.0
precissionRepository = 0


cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
dooppath = '/home/minseokjeon/doop'
analysisTime = runDoop (cmd,dooppath)
os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > luindexAlarm_Num.facts')

#time out check do!

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



timeCheck = 0
bestCost = timeRepository
bestPrecision = precissionRepository


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


for f in range(0,len(Fset)):
      print("cache clear")
      os.system("rm -r cache/*")
      
      D2Formula = D2Formula + [Fset[f]]
      
      print("append check\n")
      print(D2Formula)
      
      oneMimimalLearningReturn = oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed,notD0Formula,D2Formula)
    

      
      precisionCheck = precisionChange(startFormula,notD0Formula)
      
      print("timeCheck")
      print(timeCheck)
      print("precisionCheck")
      print(precisionCheck)

      if(1756 > precisionCheck):
        print("cost condition pass")
          
        checkFeatureNum = f
        print("cost  refine \n")
        print(Fset[f]+" will be append")
        backUpFormula = copy.deepcopy(D2Formula)
        
          
        print(D2Formula)
      else:
        print(Fset[f]+" not good")
        print("precision not refine\n")

        D2Formula = copy.deepcopy(backUpFormula) 
        print(D2Formula)



print("Area 2 is Fixed ")
for i in range(0,len(startFormula)):
  print(startFormula[i])


makheuristic(D2Formula,startFormula,notD0Formula)






