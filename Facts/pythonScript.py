import os




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



print("feature 0 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature0.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast0luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast0lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast0pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast0antlr.facts')



print("feature 1 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature1.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast1luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast1lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast1pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast1antlr.facts')



print("feature 2 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature2.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast2luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast2lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast2pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast2antlr.facts')



print("feature 3 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature3.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast3luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast3lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast3pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast3antlr.facts')


print("feature 4 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature4.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast4luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast4lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast4pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast4antlr.facts')


print("feature 5 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature5.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast5luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast5lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast5pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast5antlr.facts')


print("feature 6 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature6.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast6luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast6lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast6pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast6antlr.facts')



print("feature 7 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature7.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast7luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast7lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast7pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast7antlr.facts')



print("feature 8 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature8.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast8luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast8lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast8pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast8antlr.facts')



print("feature 9 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature9.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast9luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast9lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast9pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast9antlr.facts')



print("feature 10 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature1.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast10luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast10lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast10pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast10antlr.facts')



print("feature 11 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature11.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast11luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast11lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast11pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast11antlr.facts')



print("feature 12 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature12.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast12luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast12lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast12pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast12antlr.facts')



print("feature 13 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature13.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast13luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast13lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast13pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast13antlr.facts')



print("feature 14 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature14.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast14luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast14lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast14pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast14antlr.facts')



print("feature 15 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature15.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast15luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast15lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast15pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast15antlr.facts')



print("feature 16 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature16.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast16luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast16lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast16pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast16antlr.facts')



print("feature 17 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature17.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast17luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast17lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast17pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast17antlr.facts')



print("feature 18 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature18.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast18luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast18lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast18pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast18antlr.facts')



print("feature 19 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature19.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast19luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast19lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast19pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast19antlr.facts')



print("feature 20 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature20.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast20luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast20lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast20pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast20antlr.facts')





print("feature 21 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature21.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast21luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast21lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast21pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast21antlr.facts')


print("feature 22 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature22.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast22luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast22lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast22pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast22antlr.facts')



print("feature 23 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature23.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast23luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast23lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast23pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast23antlr.facts')



print("feature 24 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature24.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast24luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast24lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast24pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast24antlr.facts')


print("feature 25 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature25.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast25luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast25lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast25pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast25antlr.facts')


print("feature 26 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature26.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast26luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast26lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast26pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast26antlr.facts')



print("feature 27 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature27.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast27luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast27lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast27pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast27antlr.facts')


print("feature 28 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature28.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast28luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast28lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast28pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast28antlr.facts')



print("feature 29 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature29.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast29luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast29lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast29pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast29antlr.facts')



print("feature 30 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature30.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast30luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast30lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast30pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast30antlr.facts')





print("feature 31 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature31.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast31luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast31lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast31pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast31antlr.facts')




print("feature 32 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature32.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast32luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast32lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast32pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast32antlr.facts')



print("feature 33 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature33.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast33luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast33lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast33pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast33antlr.facts')



print("feature 34 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature34.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast34luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast34lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast34pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast34antlr.facts')



print("feature 35 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature35.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast35luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast35lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast35pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast35antlr.facts')



print("feature 36 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature36.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast36luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast36lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast36pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast36antlr.facts')





print("feature 37 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature37.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast37luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast37lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast37pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast37antlr.facts')



print("feature 38 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature38.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast38luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast38lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast38pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast38antlr.facts')



print("feature 39 start")
print()

os.system('cp logic/3-object-sensitive+3-heap/feature39.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast39luindex.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast39lusearch.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast39pmd.facts')

os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
os.system('bloxbatch -db last-analysis -query ProvenCast | sort > ProvenCast39antlr.facts')




















#print("feature 39 start")
#print()

#os.system('cp logic/3-object-sensitive+3-heap/feature39.logic  logic/3-object-sensitive+3-heap/heuristic.logic ')

#os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/luindex.jar ')
#os.system('bloxbatch -db last-analysis -query ProvenCast | sort > Divide1and3ProvenCast39luindex.facts')

#os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/lusearch.jar ')
#os.system('bloxbatch -db last-analysis -query ProvenCast | sort > Divide1and3ProvenCast39lusearch.facts')

#os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/pmd.jar ')
#os.system('bloxbatch -db last-analysis -query ProvenCast | sort > Divide1and3ProvenCast39pmd.facts')

#os.system('./run -jre1.6 3-object-sensitive+3-heap jars/dacapo/antlr.jar ')
#os.system('bloxbatch -db last-analysis -query ProvenCast | sort > Divide1and3ProvenCast39antlr.facts')










