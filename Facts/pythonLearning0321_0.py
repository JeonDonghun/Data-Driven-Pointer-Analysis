import copy
import os
import subprocess
import re
import sys
import json




#precision check funcion just return 4 program precision's sum
def precisionChange(startFormula):
  precisionCheck =0

  f = open("ChangedAlarm_Numluindex.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)


  f = open("ChangedAlarm_Numlusearch.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)


  f = open("ChangedAlarm_Numpmd.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)


  f = open("ChangedAlarm_Numantlr.facts","r")
  alarmNum = f.readlines()
  f.close()
  precisionCheck = precisionCheck + len(alarmNum)

  return precisionCheck



#main funcion which do one minimality learning 
def oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed):
  startFormula = makheuristic(startFormula)

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
    
    return backUpFormula
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numluindex.facts')



  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numlusearch.facts')

  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numpmd.facts')


  cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
  analysisTime = runDoop(cmd,dooppath)
  if(analysisTime == 'timeout'):
    print("timeout")
    
    os.system('cp backupluindex.facts ChangedAlarm_Numluindex.facts')
    os.system('cp backuplusearch.facts ChangedAlarm_Numluinsearch.facts')
    os.system('cp backuppmd.facts ChangedAlarm_Numpmd.facts')
    os.system('cp backupantlr.facts ChangedAlarm_Numantlr.facts') 
    return backUpFormula
  os.system('bloxbatch -db last-analysis -query Stats:Simple:PotentiallyFailingCast | sort > ChangedAlarm_Numantlr.facts')


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


  if(changedAlarmNum < bestPrecision ):#alarmNum +1 < bestPrecision
    print("changed")
    return startFormula
  else:
    print("notchanged")
    for t in range(0,len(backUpFormula)):
      print(backUpFormula[t])
    return backUpFormula
  



#check time
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

#making heuristic.logic with clauses
def makheuristic(startFormula):
 

  f = open("heuristic.logic","w")
  f.write("D3(?meth) -> MethodSignatureRef(?meth).\n\n\n")
    
  for i in range(0,len(startFormula)):
    f.write("D3(?meth)<-\n")
    for j in range(0,len(startFormula[i])):
      f.write(startFormula[i][j]+"(?meth),\n")
    f.write("MethodSignatureRef(?meth).\n\n\n")  
  f.close()
  os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')


  return startFormula


os.system('cp logic/depth0and3.logic logic/context-sensitive.logic')
os.system('python SetStartFormula.py')
os.system('cp heuristic.logic logic/3-object-sensitive+3-heap/heuristic.logic')

os.system('cp logic/depth0and3.logic logic/context-sensitive.logic')

filename = 'recentHeuristic.logic'

#filename = 'recentHeuristic9.logic'

with open(filename) as data:
  startFormula = [[i for i in line.split()] for line in data.readlines()]



for i in range(0,len(startFormula)):
  print(startFormula[i])
startFormula = makheuristic(startFormula)



backUpFormula = copy.deepcopy(startFormula)



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




bestCost = timeRepository




bestPrecision = precissionRepository




for i in range(0,len(startFormula)):
  print(backUpFormula[i])

print("precision and cost at starting point")
print(bestPrecision)
print(bestCost)
print("start Learning \n\n\n\n")

#for i in range(1,len(startFormula)):




changed = 0
precisionCheck = bestPrecision

precisionRepository = bestPrecision

j_change = 0
checkFeatureNum = 0

clauseFixPrecision = precisionCheck

for i in range(0,len(startFormula)):
  for util in range(0,len(startFormula[i])): 
    if(j_change==1):
      j_change=0
      break

    for j in range(0,len(startFormula[i])):
      if(bestPrecision<2200):
        break
      print(startFormula[i])
      print("cache clear")
      os.system("rm -r cache/*")
      deletedFeature = startFormula[i][j]
      del startFormula[i][j]
      startFormula = oneMimimalLearning (backUpFormula,startFormula,bestCost,bestPrecision,cmd,dooppath,changed)
    
      print("backupcheck")
      print()
      for q in range(0,len(startFormula)):
        print(startFormula[q])
      
      precisionCheck = precisionChange(startFormula)

      
      if(precisionCheck < bestPrecision):
        bestPrecision = precisionCheck
        checkFeatureNum = j
        
      print("backup for loop ")
      startFormula = copy.deepcopy(backUpFormula)
      print("this time Feature ="+deletedFeature)
      print(startFormula[i])
    
      ## precision 1 is not good
      
      if(bestPrecision+4 < precisionRepository):
        
        print("\n\n\n\n\n\nprecision refine")
        print(startFormula)
        print(startFormula[i][checkFeatureNum]+" will be disappear")
        #bestPrecision = precisionChange(startFormula)
        clauseFixPrecision = bestPrecision
        del startFormula[i][checkFeatureNum]
        backUpFormula = copy.deepcopy(startFormula)
      
        print("best precision changed to ")
        print(bestPrecision)
        #handle precisionRepository
        precisionRepository = bestPrecision

        print("precisionRepository , bestPrecision")
        print(precisionRepository)
        print(bestPrecision)
        break
      if(j+1 == len(startFormula[i])):   
        j_change=1

print("0and3 divided hahahahhahahah")
print("\n\n\n\n\n")

backUpFormula = copy.deepcopy(startFormula)


Emptyset = set([])
DeleteSoon = []

for i in range(0,len(startFormula)):
 for j in range(len(startFormula),0,-1):
    if(i==j-1): 
      continue
    if( len(set(startFormula[i])-set(startFormula[j-1])) ==0):
      DeleteSoon = DeleteSoon + [j-1]

print(DeleteSoon)

for i in range(0,len(DeleteSoon)):
  del startFormula[DeleteSoon[i]]



for q in range(0,len(startFormula)):
  print(startFormula[q])


'''
for i in range(len(startFormula),0,-1):
  changedAlarmNum =0
  print("cache clear")
  os.system("rm -r cache/*")
  del startFormula[i-1]
  makheuristic(startFormula)
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
  
  if(changedAlarmNum != bestPrecision):
    startFormula = copy.deepcopy(backUpFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
  elif(changedAlarmNum == bestPrecision):
    backUpFormula = copy.deepcopy(startFormula)
    for t in range(0,len(startFormula)):
      print(startFormula[t])
    continue
  else:
    print("some thing wrong!!!!!!!!")


'''









#make 0/3 heurisitic
makheuristic(startFormula)



fa = open("recentHeuristic1.logic","w")
for k in range(0,len(startFormula)): 
  for p in range(0,len(startFormula[k])):
    fa.writelines(startFormula[k][p])
    fa.write(" ")
  fa.write("\n")    
fa.close()







filename = 'recentHeuristic1.logic'
with open(filename) as data:
  startFormula = [[i for i in line.split()] for line in data.readlines()]





