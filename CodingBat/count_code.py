def xyz_there(st):
    count=list(allindices(st,"xyz"))
    #print count
    list1=[]
    for i in count:
        if i==-1:
            list1.append("False")
        if i==0:
            list1.append("True")
        if st[i-1]==".":
            list1.append("False")
        else :
            list1.append("True")
    if "True" in list1:
        return True
    else:
        return False
        
    

def allindices(string, sub,offset=0):
    listindex=[]
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex

print count_code("abc.xyz")
