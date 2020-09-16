s14 = set()
s15 = set()
s2obj = set()
sinsense = set()
s5 = set()
s6 = set()
s7 = set()

cnt = 0
pre_lines = [line.rstrip('\n') for line in open('14ProvenCasts.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s14.add(val)
print cnt
cnt = 0

pre_lines = [line.rstrip('\n') for line in open('15ProvenCasts.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s15.add(val)
print cnt
cnt = 0

pre_lines = [line.rstrip('\n') for line in open('2objProven.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  s2obj.add(val)
print cnt
cnt = 0

pre_lines = [line.rstrip('\n') for line in open('insenseProvenCasts.facts')]
for i,val in enumerate(pre_lines):
  cnt = cnt+1
  sinsense.add(val)
print cnt
cnt = 0

s5 = (s14 & s15 & s2obj) - sinsense

print len(s5)

for i,val in enumerate(s5):
  cnt = cnt+1
  print(val)
print cnt
cnt = 0

