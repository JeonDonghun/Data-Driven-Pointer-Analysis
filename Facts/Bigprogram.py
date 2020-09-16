
import copy
import os
import subprocess
import re
import sys
import json


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




cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar' 
dooppath = '/home/minseokjeon/doop'   











'''




print("feature 0 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature0.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast0chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast0chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast0lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast0lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast0eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast0eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast0antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast0antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  







print("feature 1 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature1.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast1chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast1chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast1lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast1lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast1eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast1eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast1antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast1antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  








print("feature 2 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature2.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast2chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast2chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast2lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast2lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast2eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast2eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast2antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast2antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  







print("feature 3 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature3.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast3chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast3chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast3lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast3lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast3eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast3eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast3antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast3antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  






print("feature 4 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature4.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast4chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast4chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast4lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast4lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast4eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast4eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast4antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast4antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  






print("feature 5 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature5.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast5chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast5chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast5lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast5lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast5eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast5eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast5antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast5antlr.facts')



print("cache clear")    
os.system("rm -r cache/*")  





'''

print("feature 6 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature6.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast6chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast6chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast6lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast6lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast6eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast6eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast6antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast6antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  








print("feature 7 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature7.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast7chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast7chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast7lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast7lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast7eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast7eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast7antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast7antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  



print("feature 8 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature8.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast8chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast8chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast8lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast8lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast8eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast8eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast8antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast8antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  






print("feature 9 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature9.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast9chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast9chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast9lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast9lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast9eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast9eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast9antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast9antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  






print("feature 10 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature10.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast10chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast10chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast10lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast10lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast10eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast10eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast10antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast10antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  




print("feature 11 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature11.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast11chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast11chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast11lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast11lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast11eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast11eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast11antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast11antlr.facts')







print("cache clear")    
os.system("rm -r cache/*")  








print("feature 12 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature12.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast12chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast12chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast12lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast12lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast12eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast12eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast12antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast12antlr.facts')




print("cache clear")    
os.system("rm -r cache/*")  


print("feature 13 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature13.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast13chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast13chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast13lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast13lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast13eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast13eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast13antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast13antlr.facts')






print("cache clear")    
os.system("rm -r cache/*")  


print("feature 14 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature14.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast14chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast14chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast14lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast14lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast14eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast14eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast14antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast14antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 15 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature15.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast15chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast15chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast15lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast15lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast15eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast15eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast15antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast15antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 16 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature16.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast16chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast16chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast16lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast16lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast16eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast16eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast16antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast16antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 17 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature17.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast17chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast17chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast17lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast17lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast17eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast17eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast17antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast17antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  






print("feature 18 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature18.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast18chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast18chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast18lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast18lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast18eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast18eclipse.facts')
  
cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast18antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast18antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  



print("feature 19 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature19.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast19chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast19chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast19lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast19lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast19eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast19eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast19antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast19antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  






print("feature 20 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature20.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast20chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast20chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast20lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast20lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast20eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast20eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast20antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast20antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  







print("feature 21 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature21.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast21chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast21chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast21lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast21lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast21eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast21eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast21antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast21antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 22 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature22.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast22chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast22chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast22lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast22lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast22eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast22eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast22antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast22antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  







print("feature 23 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature23.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast23chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast23chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast23lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast23lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast23eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast23eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast23antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast23antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  




print("feature 24 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature24.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')


cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast24chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast24chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast24lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast24lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast24eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast24eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast24antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast24antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  









print("feature 25 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature25.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast25chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast25chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast25lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast25lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast25eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast25eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast25antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast25antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  



print("feature 26 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature26.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast26chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast26chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast26lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast26lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast26eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast26eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast26antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast26antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  






print("feature 27 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature27.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast27chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast27chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast27lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast27lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast27eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast27eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast27antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast27antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  



print("feature 28 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature28.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast28chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast28chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast28lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast28lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast28eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast28eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast28antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast28antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 29 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature29.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast29chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast29chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast29lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast29lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast29eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast29eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast29antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast29antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  




print("feature 30 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature30.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast30chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast30chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast30lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast30lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast30eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast30eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast30antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast30antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  




print("feature 31 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature31.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast31chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast31chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast31lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast31lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast31eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast31eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast31antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast31antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 32 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature32.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast32chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast32chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast32lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast32lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast32eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast32eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast32antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast32antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 33 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature33.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast33chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast33chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast33lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast33lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast33eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast33eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast33antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast33antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 34 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature34.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast34chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast34chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast34lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast34lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast34eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast34eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast34antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast34antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  







print("feature 35 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature35.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast35chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast35chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast35lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast35lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast35eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast35eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast35antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast35antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  






print("feature 36 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature36.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast36chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast36chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast36lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast36lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast36eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast36eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast36antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast36antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  





print("feature 37 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature37.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/chart.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast37chart.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast37chart.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast37lusearch.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast37lusearch.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/eclipse.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast37eclipse.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast37eclipse.facts')

cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
if(analysisTime == 'timeout'):
  f = open("BigProgram/ProvenCast37antlr.facts","w")
  f.close()
else:
  os.system('bloxbatch -db last-analysis -query ProvenCast | sort > BigProgram/ProvenCast37antlr.facts')


print("cache clear")    
os.system("rm -r cache/*")  












































