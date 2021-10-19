d=input("saisir une date de la forme : jj/mm/aaaa ")
j= int(d[0:2])
m= int(d[3:5])
a=int(d[6:])
test=True
if m in [1,3,5,7,8,10,12]:
    if j<1 or j>31:
        test=false
elif m in [4,6,9,11]:
    if j<1 or j>30 :
       test=False
elif m==2:
    if a%4==0:
       if j<1 or j>29:
           test=False
    else:
        if j<1 or j>28:
            test=False
else:
    test=False
    
if test == True :
    print ("date valide")
else:
    print ("date n'est pas valide")
    
        
