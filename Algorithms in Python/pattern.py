def contains(str1,str2):
    for i in range(0,len(str2)-len(str1)):
        j=0
        while (j<len(str1) and str2[i+j]==str1[j]):
            j+=1
        if j==len(str1):
            return i
    return "There is no substring"


print contains("abcd","efasdfabcd")
    
