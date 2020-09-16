s1 = set()
s2 = set()
s3 = set()
s4 = set()

cnt = 0
pre_lines = [line.rstrip('\n') for line in open('tiantan.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s1.add(val)
print cnt
cnt = 0

pre_lines = [line.rstrip('\n') for line in open('minseok.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s2.add(val)
print cnt
cnt = 0
'''
pre_lines = [line.rstrip('\n') for line in open('s1objT.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s4.add(val)
print cnt
cnt = 0

pre_lines = [line.rstrip('\n') for line in open('1objT.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s5.add(val)
print cnt

cnt = 0
pre_lines = [line.rstrip('\n') for line in open('1callTB.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s6.add(val)
print cnt
cnt = 0
'''

#s7 = s1 & s2 & s3 & s4 & s5 & s6 
print len(s1 & s2)
s3 = s2 & s1
#print len(s3)
for i,val in enumerate(s3):
  cnt = cnt+1
  print(val)
print cnt
cnt = 0

