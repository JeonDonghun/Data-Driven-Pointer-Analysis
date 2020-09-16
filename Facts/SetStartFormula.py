

def makecontent(contentantlr,contentpmd,contentluindex,contentlusearch):
  content = []
  a=0
  for i in range(0,len(contentantlr)):
    if contentantlr[i] in content:continue
    else:
      content = content + [contentantlr[i]]
      a = a+1
  for i in range(0,len(contentpmd)):
    if contentpmd[i] in content:continue
    else:
      content = content + [contentpmd[i]]
      a = a+1
  for i in range(len(contentluindex)):
    if contentluindex[i] in content: continue
    else:
      content = content + [contentluindex[i]]
      a = a+1
  for i in range(0,len(contentlusearch)):
    if contentlusearch[i] in content: continue
    else:
      content = content + [contentlusearch[i]]
  return content

def ImportantQuery(contentMax,ContentMin):
  ImportantContent = []
  for i in range(0,len(contentMax)):
    if contentMax[i] in contentMin:continue
    else:
      ImportantContent = ImportantContent + [contentMax[i]]
  print("importantcontent")
  print(len(ImportantContent))
  return ImportantContent
  
 
def makingFormula(content,ImportantContent,Fset):
  makformula = []
  formula = []
  print(len(Fset))
  for i in range(0,len(ImportantContent)):
    for j in range(0,len(Fset)):

      if ImportantContent[i] in content[j]:
        makformula = makformula + [Fset[j]]
    formula = formula + [makformula]
    makformula = []

  return formula


def deletePdxClause(formula):
  deletePdx=[]
  for i in range(0,len(formula)):
    if (len(formula[i]) ==29 ):continue
    else:
      deletePdx = deletePdx + [formula[i]]
  return deletePdx


def delete01(formula):
  delete1011 = []
  for i in range(0,len(formula)):
    if 'Feature14' in formula[i]:
      if 'Feature15' in formula[i]:continue
      else:
        #print(1)
        delete1011 = delete1011 + [formula[i]]
    else:
      delete1011 = delete1011 + [formula[i]]
  return delete1011
  

def delete3637(formula):
  delete1011 = []
  for i in range(0,len(formula)):
    if 'Feature36' in formula[i]:
      if 'Feature37' in formula[i]:continue
      else:
        delete1011 = delete1011 + [formula[i]]
    else:
      delete1011 = delete1011 + [formula[i]]
  return delete1011

def makheuristic(startFormula):
  fa = open("recentHeuristic.logic","w")
  for k in range(0,len(startFormula)): 
    for p in range(0,len(startFormula[k])):
      fa.writelines(startFormula[k][p])
      fa.write(" ")
    fa.write("\n")    
  fa.close()
  
  f = open("heuristic.logic","w")
  f.write("D3(?meth) -> MethodSignatureRef(?meth).\n\n\n")

  print("lenstartformula")
  print(len(startFormula))
  for i in range(0,len(startFormula)):
    f.write("D3(?meth)<-\n")
    for j in range(0,len(startFormula[i])):
      f.write(startFormula[i][j]+"(?meth),\n")
    f.write("MethodSignatureRef(?meth).\n\n\n")
    
  f.close()



def searchSmallSet(formula,startFormula):
  
  longlen =0
  inum =0
  for i in range(0,len(formula)):
    if longlen < len(formula[i]):
      longlen = len(formula[i])
      inum = i
    else: continue
  if (formula ==[]):
    print("startFormula")
    for i in range(0,len(startFormula)):
      print(startFormula[i])
    makheuristic(startFormula)
    #return
    return startFormula
  else:
    startFormula = startFormula + [formula[inum]]
    print(formula[inum])
    deleteSet(formula,formula[inum],startFormula)
    
  


def deleteSet(formula,smallSet,startFormula):
  deletedset = []
  
  for i in range(0,len(formula)):
    for j in range(0,len(formula[i])):
      if formula[i][j] in smallSet: continue
      else:
        deletedset = deletedset + [formula[i]]
        break
  searchSmallSet(deletedset,startFormula)  

f=open("ProvenCast/ProvenCast0antlr.facts","r")
content0antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast0pmd.facts","r")
content0pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast0luindex.facts","r")
content0luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast0lusearch.facts","r")
content0lusearch = f.readlines()
f.close()


f=open("ProvenCast/ProvenCastMinantlr.facts","r")
contentMinantlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCastMinpmd.facts","r")
contentMinpmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCastMinluindex.facts","r")
contentMinluindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCastMinlusearch.facts","r")
contentMinlusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast1antlr.facts","r")
content1antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast1pmd.facts","r")
content1pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast1luindex.facts","r")
content1luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast1lusearch.facts","r")
content1lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast2antlr.facts","r")
content2antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast2pmd.facts","r")
content2pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast2luindex.facts","r")
content2luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast2lusearch.facts","r")
content2lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast10antlr.facts","r")
content10antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast10pmd.facts","r")
content10pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast10luindex.facts","r")
content10luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast10lusearch.facts","r")
content10lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast3antlr.facts","r")
content3antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast3pmd.facts","r")
content3pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast3luindex.facts","r")
content3luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast3lusearch.facts","r")
content3lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast4antlr.facts","r")
content4antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast4pmd.facts","r")
content4pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast4luindex.facts","r")
content4luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast4lusearch.facts","r")
content4lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast5antlr.facts","r")
content5antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast5pmd.facts","r")
content5pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast5luindex.facts","r")
content5luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast5lusearch.facts","r")
content5lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast6antlr.facts","r")
content6antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast6pmd.facts","r")
content6pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast6luindex.facts","r")
content6luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast6lusearch.facts","r")
content6lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast7antlr.facts","r")
content7antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast7pmd.facts","r")
content7pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast7luindex.facts","r")
content7luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast7lusearch.facts","r")
content7lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast8antlr.facts","r")
content8antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast8pmd.facts","r")
content8pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast8luindex.facts","r")
content8luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast8lusearch.facts","r")
content8lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast9antlr.facts","r")
content9antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast9pmd.facts","r")
content9pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast9luindex.facts","r")
content9luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast9lusearch.facts","r")
content9lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast11antlr.facts","r")
content11antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast11pmd.facts","r")
content11pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast11luindex.facts","r")
content11luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast11lusearch.facts","r")
content11lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast12antlr.facts","r")
content12antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast12pmd.facts","r")
content12pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast12luindex.facts","r")
content12luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast12lusearch.facts","r")
content12lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast13antlr.facts","r")
content13antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast13pmd.facts","r")
content13pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast13luindex.facts","r")
content13luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast13lusearch.facts","r")
content13lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast14antlr.facts","r")
content14antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast14pmd.facts","r")
content14pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast14luindex.facts","r")
content14luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast14lusearch.facts","r")
content14lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast15antlr.facts","r")
content15antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast15pmd.facts","r")
content15pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast15luindex.facts","r")
content15luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast15lusearch.facts","r")
content15lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast16antlr.facts","r")
content16antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast16pmd.facts","r")
content16pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast16luindex.facts","r")
content16luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast16lusearch.facts","r")
content16lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast17antlr.facts","r")
content17antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast17pmd.facts","r")
content17pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast17luindex.facts","r")
content17luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast17lusearch.facts","r")
content17lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast18antlr.facts","r")
content18antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast18pmd.facts","r")
content18pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast18luindex.facts","r")
content18luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast18lusearch.facts","r")
content18lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast19antlr.facts","r")
content19antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast19pmd.facts","r")
content19pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast19luindex.facts","r")
content19luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast19lusearch.facts","r")
content19lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast20antlr.facts","r")
content20antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast20pmd.facts","r")
content20pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast20luindex.facts","r")
content20luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast20lusearch.facts","r")
content20lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast21antlr.facts","r")
content21antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast21pmd.facts","r")
content21pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast21luindex.facts","r")
content21luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast21lusearch.facts","r")
content21lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast22antlr.facts","r")
content22antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast22pmd.facts","r")
content22pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast22luindex.facts","r")
content22luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast22lusearch.facts","r")
content22lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast23antlr.facts","r")
content23antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast23pmd.facts","r")
content23pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast23luindex.facts","r")
content23luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast23lusearch.facts","r")
content23lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast24antlr.facts","r")
content24antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast24pmd.facts","r")
content24pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast24luindex.facts","r")
content24luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast24lusearch.facts","r")
content24lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast25antlr.facts","r")
content25antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast25pmd.facts","r")
content25pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast25luindex.facts","r")
content25luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast25lusearch.facts","r")
content25lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast26antlr.facts","r")
content26antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast26pmd.facts","r")
content26pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast26luindex.facts","r")
content26luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast26lusearch.facts","r")
content26lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast27antlr.facts","r")
content27antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast27pmd.facts","r")
content27pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast27luindex.facts","r")
content27luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast27lusearch.facts","r")
content27lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast28antlr.facts","r")
content28antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast28pmd.facts","r")
content28pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast28luindex.facts","r")
content28luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast28lusearch.facts","r")
content28lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast29antlr.facts","r")
content29antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast29pmd.facts","r")
content29pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast29luindex.facts","r")
content29luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast29lusearch.facts","r")
content29lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast30antlr.facts","r")
content30antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast30pmd.facts","r")
content30pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast30luindex.facts","r")
content30luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast30lusearch.facts","r")
content30lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast31antlr.facts","r")
content31antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast31pmd.facts","r")
content31pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast31luindex.facts","r")
content31luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast31lusearch.facts","r")
content31lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast32antlr.facts","r")
content32antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast32pmd.facts","r")
content32pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast32luindex.facts","r")
content32luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast32lusearch.facts","r")
content32lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast33antlr.facts","r")
content33antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast33pmd.facts","r")
content33pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast33luindex.facts","r")
content33luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast33lusearch.facts","r")
content33lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast34antlr.facts","r")
content34antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast34pmd.facts","r")
content34pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast34luindex.facts","r")
content34luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast34lusearch.facts","r")
content34lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast35antlr.facts","r")
content35antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast35pmd.facts","r")
content35pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast35luindex.facts","r")
content35luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast35lusearch.facts","r")
content35lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast36antlr.facts","r")
content36antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast36pmd.facts","r")
content36pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast36luindex.facts","r")
content36luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast36lusearch.facts","r")
content36lusearch = f.readlines()
f.close()

f=open("ProvenCast/ProvenCast37antlr.facts","r")
content37antlr = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast37pmd.facts","r")
content37pmd = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast37luindex.facts","r")
content37luindex = f.readlines()
f.close()
f=open("ProvenCast/ProvenCast37lusearch.facts","r")
content37lusearch = f.readlines()
f.close()









Fset = ['Feature0','Feature1','Feature2','Feature3','Feature4','Feature5','Feature6','Feature7','Feature8','Feature9','Feature10','Feature11','Feature12','Feature13','Feature14','Feature15','Feature16','Feature17','Feature18','Feature19','Feature20','Feature21','Feature22','Feature23','Feature24','Feature25','Feature26','Feature27','Feature28','Feature29','Feature30','Feature31','Feature32','Feature33','Feature34','Feature35','Feature36','Feature37']

contentMin = makecontent(contentMinantlr,contentMinpmd,contentMinluindex,contentMinlusearch)

content0 = makecontent(content0antlr,content0pmd,content0luindex,content0lusearch)
content1 = makecontent(content1antlr,content1pmd,content1luindex,content1lusearch)
content2 = makecontent(content2antlr,content2pmd,content2luindex,content2lusearch)
content3 = makecontent(content3antlr,content3pmd,content3luindex,content3lusearch)
content4 = makecontent(content4antlr,content4pmd,content4luindex,content4lusearch)
content5 = makecontent(content5antlr,content5pmd,content5luindex,content5lusearch)
content6 = makecontent(content6antlr,content6pmd,content6luindex,content6lusearch)
content7 = makecontent(content7antlr,content7pmd,content7luindex,content7lusearch)
content8 = makecontent(content8antlr,content8pmd,content8luindex,content8lusearch)
content9 = makecontent(content9antlr,content9pmd,content9luindex,content9lusearch)
content10 = makecontent(content10antlr,content10pmd,content10luindex,content10lusearch)
content11 = makecontent(content11antlr,content11pmd,content11luindex,content11lusearch)
content12 = makecontent(content12antlr,content12pmd,content12luindex,content12lusearch)
content13 = makecontent(content13antlr,content13pmd,content13luindex,content13lusearch)
content14 = makecontent(content14antlr,content14pmd,content14luindex,content14lusearch)
content15 = makecontent(content15antlr,content15pmd,content15luindex,content15lusearch)
content16 = makecontent(content16antlr,content16pmd,content16luindex,content16lusearch)
content17 = makecontent(content17antlr,content17pmd,content17luindex,content17lusearch)
content18 = makecontent(content18antlr,content18pmd,content18luindex,content18lusearch)
content19 = makecontent(content19antlr,content19pmd,content19luindex,content19lusearch)
content20 = makecontent(content20antlr,content20pmd,content20luindex,content20lusearch)
content21 = makecontent(content21antlr,content21pmd,content21luindex,content21lusearch)
content22 = makecontent(content22antlr,content22pmd,content22luindex,content22lusearch)
content23 = makecontent(content23antlr,content23pmd,content23luindex,content23lusearch)
content24 = makecontent(content24antlr,content24pmd,content24luindex,content24lusearch)
content25 = makecontent(content25antlr,content25pmd,content25luindex,content25lusearch)
content26 = makecontent(content26antlr,content26pmd,content26luindex,content26lusearch)
content27 = makecontent(content27antlr,content27pmd,content27luindex,content27lusearch)
content28 = makecontent(content28antlr,content28pmd,content28luindex,content28lusearch)
content29 = makecontent(content29antlr,content29pmd,content29luindex,content29lusearch)
content30 = makecontent(content30antlr,content30pmd,content30luindex,content30lusearch)
content31 = makecontent(content31antlr,content31pmd,content31luindex,content31lusearch)
content32 = makecontent(content32antlr,content32pmd,content32luindex,content32lusearch)
content33 = makecontent(content33antlr,content33pmd,content33luindex,content33lusearch)
content34 = makecontent(content34antlr,content34pmd,content34luindex,content34lusearch)
content35 = makecontent(content35antlr,content35pmd,content35luindex,content35lusearch)
content36 = makecontent(content36antlr,content36pmd,content36luindex,content36lusearch)
content37 = makecontent(content37antlr,content37pmd,content37luindex,content37lusearch)







content0 = ImportantQuery(content0,contentMin)
content1 = ImportantQuery(content1,contentMin)
content2 = ImportantQuery(content2,contentMin)
content3 = ImportantQuery(content3,contentMin)
content4 = ImportantQuery(content4,contentMin)
content5 = ImportantQuery(content5,contentMin)
content6 = ImportantQuery(content6,contentMin)
content7 = ImportantQuery(content7,contentMin)
content8 = ImportantQuery(content8,contentMin)
content9 = ImportantQuery(content9,contentMin)
content10 = ImportantQuery(content10,contentMin)

content11 = ImportantQuery(content11,contentMin)
content12 = ImportantQuery(content12,contentMin)
content13 = ImportantQuery(content13,contentMin)
content14 = ImportantQuery(content14,contentMin)
content15 = ImportantQuery(content15,contentMin)
content16 = ImportantQuery(content16,contentMin)
content17 = ImportantQuery(content17,contentMin)
content18 = ImportantQuery(content18,contentMin)
content19 = ImportantQuery(content19,contentMin)
content20 = ImportantQuery(content20,contentMin)

content21 = ImportantQuery(content21,contentMin)
content22 = ImportantQuery(content22,contentMin)
content23 = ImportantQuery(content23,contentMin)
content24 = ImportantQuery(content24,contentMin)
content25 = ImportantQuery(content25,contentMin)
content26 = ImportantQuery(content26,contentMin)
content27 = ImportantQuery(content27,contentMin)
content28 = ImportantQuery(content28,contentMin)
content29 = ImportantQuery(content29,contentMin)
content30 = ImportantQuery(content30,contentMin)

content31 = ImportantQuery(content31,contentMin)
content32 = ImportantQuery(content32,contentMin)
content33 = ImportantQuery(content33,contentMin)
content34 = ImportantQuery(content34,contentMin)
content35 = ImportantQuery(content35,contentMin)
content36 = ImportantQuery(content36,contentMin)
content37 = ImportantQuery(content37,contentMin)







maxFormula = []

maxFormula = makecontent(content0,content1,content2,content3)
maxFormula = makecontent(maxFormula,content4,content5,content6)
maxFormula = makecontent(maxFormula,content7,content8,content9)
maxFormula = makecontent(maxFormula,content10,content11,content12)
maxFormula = makecontent(maxFormula,content13,content14,content15)
maxFormula = makecontent(maxFormula,content16,content17,content18)
maxFormula = makecontent(maxFormula,content19,content20,content21)
maxFormula = makecontent(maxFormula,content22,content23,content24)
maxFormula = makecontent(maxFormula,content25,content26,content27)
maxFormula = makecontent(maxFormula,content28,content29,content30)
maxFormula = makecontent(maxFormula,content31,content32,content33)
maxFormula = makecontent(maxFormula,content34,content35,content36)
maxFormula = makecontent(maxFormula,content36,content37,content37)




ImportantContent = ImportantQuery(maxFormula,contentMin)


content = [content0]+[content1]+[content2]+[content3]+[content4]+[content5]+[content6]+[content7]+[content8]+[content9]+[content10]+[content11]+[content12]+[content13]+[content14]+[content15]+[content16]+[content17]+[content18]+[content19]+[content20]+[content21]+[content22]+[content23]+[content24]+[content25]+[content26]+[content27]+[content28]+[content29]+[content30]+[content31]+[content32]+[content33]+[content34]+[content35]+[content36]+[content37]

formula = []


formula = makingFormula(content,ImportantContent,Fset)


print("makingFormula end")



startFormula = []



startFormula = searchSmallSet(formula,startFormula)





filename = 'recentHeuristic.logic'
with open(filename) as data:
  startFormula = [[i for i in line.split()] for line in data.readlines()]






