g= open("prep.lexc","w")
for lin in open('preposition','r'):
     g.write(lin.strip()+"+prep:"+lin.strip()+" #;\n")

