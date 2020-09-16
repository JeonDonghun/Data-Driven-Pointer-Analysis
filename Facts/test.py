
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
dooppath = '../doop'   

fea = [i for i in range(0,40)]


a = 0

cmd = 'run -jre1.6 context-insensitive jars/dacapo/luindex.jar'
analysisTime = runDoop(cmd, dooppath)
os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCastMinluindex.facts')

cmd = 'run -jre1.6 context-insensitive jars/dacapo/lusearch.jar'
analysisTime = runDoop(cmd, dooppath)
os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCastMinlusearch.facts')

cmd = 'run -jre1.6 context-insensitive jars/dacapo/pmd.jar'
analysisTime = runDoop(cmd, dooppath)
os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCastMinpmd.facts')

cmd = 'run -jre1.6 context-insensitive jars/dacapo/antlr.jar'
analysisTime = runDoop(cmd, dooppath)
os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCastMinantlr.facts')





for i in range(0,len(fea)):
    print("feature "+str(fea[i])+ " start")
    print()

    os.system('cp ../doop/logic/3-object-sensitive+3-heap/featureStore/feature'+str(fea[i])+'.logic  ../doop/logic/3-object-sensitive+3-heap/heuristic.logic ')

    cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar'
    analysisTime = runDoop(cmd, dooppath)
    if(analysisTime == 'timeout'):
      f = open("ProvenCast/ProvenCast"+str(fea[i])+"luindex.facts","w")
      print("time out")
      f.close()
    else:
      os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCast'+str(fea[i])+'luindex.facts')

    cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar' 
    analysisTime = runDoop(cmd, dooppath)
    if(analysisTime == 'timeout'):
      f = open("ProvenCast/ProvenCast"+str(fea[i])+"lusearch.facts","w")
      f.close()
      print("time out")
      a = 1
    else:
      os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCast'+str(fea[i])+'lusearch.facts')

    cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar'
    analysisTime = runDoop(cmd, dooppath)
    if(analysisTime == 'timeout'):
      f = open("ProvenCast/ProvenCast"+str(fea[i])+"pmd.facts","w")
      f.close()
      print('timeout')
    else:
      os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCast'+str(fea[i])+'pmd.facts')
    
    if(a ==1):
        f = open("ProvenCast/ProvenCast"+str(fea[i])+"antlr.facts","w")
        f.close()
        a=0
    else:
        cmd = 'run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar'
        analysisTime = runDoop(cmd, dooppath)
        if(analysisTime == 'timeout'):
           f = open("ProvenCast/ProvenCast"+str(fea[i])+"antlr.facts","w")
           f.close()
           print('time out')
        else:
          os.system('bloxbatch -db ../doop/last-analysis -query ProvenCast | sort > ProvenCast/ProvenCast'+str(fea[i])+'antlr.facts')


    print("cache clear")    
    os.system("rm -r ../doop/cache/*")  








