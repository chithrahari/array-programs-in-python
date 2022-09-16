l=[4,7,23,8,5,3,3,6,3,7,8,9,4]
l1=[]
for i in l:
    if i not in l1:
        l1.append (i)
    else:
        print (i,end='')
        
