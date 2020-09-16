




Fset = [524,8,150,0,0,504,74,0,0,6,7,0,0,0,468,504,0,678,0,539,0,0,0,143,0,0,516,1,397,0,35,0,0,163,0,142,0,294,0,116]

print(len(Fset))


startFormula = []
startFormula = startFormula + [Fset[0]+Fset[2]+Fset[5]+Fset[12]+Fset[14]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[33]+Fset[35]+Fset[37]+Fset[39]]
startFormula = startFormula + [Fset[0]+Fset[2]+Fset[5]+Fset[6]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[33]+Fset[35]+Fset[37]+Fset[39]]
startFormula = startFormula + [Fset[0]+Fset[2]+Fset[5]+Fset[10]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[33]+Fset[35]+Fset[37]+Fset[39]]
startFormula = startFormula + [Fset[0]+Fset[2]+Fset[5]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[33]+Fset[35]+Fset[37]+Fset[30]]
startFormula = startFormula + [Fset[0]+Fset[2]+Fset[5]+Fset[9]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[33]+Fset[35]+Fset[37]]
startFormula = startFormula + [Fset[0]+Fset[5]+Fset[6]+Fset[14]+Fset[15]+Fset[17]+Fset[19]+Fset[23]+Fset[26]+Fset[28]+Fset[30]+Fset[37]] 
startFormula = startFormula + [Fset[1]+Fset[5]+Fset[15]+Fset[17]+Fset[19]+Fset[26]+Fset[30]+Fset[35]+Fset[39]]
startFormula = startFormula + [Fset[1]+Fset[12]+Fset[14]+Fset[30]+Fset[33]+Fset[35]+Fset[37]+Fset[39]]
startFormula = startFormula + [Fset[10]+Fset[27]+Fset[33]+Fset[39]]

for i in range(0,len(startFormula)):
  print(startFormula[i])





