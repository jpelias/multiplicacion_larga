# Division larga, a la forma manual en Python
# dominio publico . by @_Bigwig_  2014

#d1 = "2567298"
d1 = "26"
d2 = "34"

co = ""


ceros = " " * 100


print d1 , d2

a = 1

vd2 = int(d2)

while a <= len (d1):
  
  vd1 = int(d1[:a])
  
  if vd2 < vd1 :
    break

  a = a + 1  



while (a <= len(d1)):

    while True:
  
        d = int(vd1)/vd2
        
        if d > 0 :
            break
        co = co + "0"
        vd1 = str(vd1)+(d1[a:a+1])
        print ceros[:2]+vd1
        a = a + 1
    co = co + str (d)
    r = int(vd1) - (vd2*d)
    print (vd2*d)
    vd1 = str(r)+(d1[a:a+1])
    a = a + 1
    print ceros[:2]+vd1

co = co + "."


#print vd1,a,r

while (len (co) < 80 ):

    while True:
        vd1 = str(vd1)+("0")
        d = int(vd1)/int(vd2)
        
        if d > 0 :
            break
        
        vd1 = str(vd1)+("0")
        #print ceros[:2]+vd1
        
    co = co + str (d)
    r = int(vd1) - (vd2*d)
    #print (vd2*d)
    vd1 = str(r)+("0")
    
print co
    




print float(d1)/float(d2),int(d1)%int(d2)
