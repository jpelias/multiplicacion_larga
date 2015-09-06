# Multiplicacion larga de forma humana en python
# dominio publico . by @_Bigwig_
# En pruebas ... 

mu1 = "22234708789787811545622331277852345234585243845847857857857851374916333771"

mu2 = "50051341324555554523452345234523452345245254329"

lmu1 = list (mu1)
lmu2 = list (mu2)

llevo = 0
ceros = " " * 100
raya = "_" * 100

lmu1.reverse()
lmu2.reverse()


resul=[[] for i in xrange(88)]
f = 0

print 
print ceros[:len(lmu2)],mu1
print ceros[:len(lmu1)-1] + "x " + mu2 
print ceros[:len(lmu2)]+raya[:len(lmu1)+2]


for m2 in lmu2:

    for m1 in lmu1:

        m1 = int (m1)
        m2 = int (m2)

        mm = m1*m2 + llevo

        llevo = int (mm/10)

        r = mm - llevo*10
        
        resul[f].append (r)  
    if llevo == 0: llevo = " "
    resul[f].append (llevo)
    
    resul[f].extend(ceros[:len(lmu2)-f])
    resul[f].reverse()
    resul[f].extend(ceros[:f])
    
    print "".join(str(x) for x in resul[f])
    largo = len (resul[f])
    llevo = 0
    f = f + 1

suma = 0

total = []

for m1 in range(largo)[::-1]:

    for m2 in range(len(mu2))[::1]:
        if resul[m2][m1] <> " ":
            suma = suma + int(resul[m2][m1])

        
    
    llevo = int (suma/10)    
    
    total.append(suma - llevo*10)

    suma = llevo


total.reverse()

if total[0] == 0 : 
    total[0] = " "
    if total[1] == 0 : total[1] = " "

print raya[:len(total)]
print "".join(str(x) for x in total)
print
print
