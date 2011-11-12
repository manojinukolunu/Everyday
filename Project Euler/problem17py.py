def genWords(num):
    wordlist={}
    wordlist[1]="one"
    wordlist[2]="two"
    wordlist[3]="three"
    wordlist[4]="four"
    wordlist[5]="five"
    wordlist[6]="six"
    wordlist[7]="seven"
    wordlist[8]="eight"
    wordlist[9]="nine"
    wordlist[10]="ten"
    wordlist[11]="eleven"
    wordlist[12]="twelve"
    wordlist[13]="thirteen"
    wordlist[14]="fourteen"
    wordlist[15]="fifteen"
    wordlist[16]="sixteen"
    wordlist[17]="seventeen"
    wordlist[18]="eighteen"
    wordlist[19]="nineteen"  
    st=""
    dig=str(num)
    digu=dig[-1]
    if len(dig)==2:
        digt=dig[-2]
    if len(dig)==3:
        digt=dig[-2]
        digh=dig[-3]
    if dig=="1000":
        st=st+"one thousand"
    if len(dig)==1:
        st=st+wordlist[int(digu)]
    if len(dig)==2:
         if int(digt)>=2:
            if int(digt)==2:
                st=st+"twenty"
            elif int(digt)==3:
                st=st+"thirty"
            elif int(digt)==4:
                st=st+"forty"
            elif int(digt)==5:
                st=st+"fifty"
            elif int(digt)==6:
                st=st+"sixty"
            elif int(digt)==7:
                st=st+"seventy"
            elif int(digt)==8:
                st=st+"eighty"
            elif int(digt)==9:
                st=st+"ninety"
            if int(digu)!=0:
                st=st+" "+wordlist[int(digu)]
         if int(digt)<2 and digu!=0:
            st=wordlist[int(digt+digu)]
    hundreds=["one hundred","two hundred","three hundred","four hundred","five hundred","six hundred","seven hundred","eight hundred","nine hundred"]
    if len(dig)==3:
        if int(digh)==1:
            st=st+"one hundred and "
            if int(digt)==0 and int(digu)==0:
                st="one hundred"
        elif int(digh)==2:
            st=st+"two hundred and "
            if int(digt)==0 and int(digu)==0:
                st="two hundred"
        elif int(digh)==3:
            st=st+"three hundred and "
            if int(digt)==0 and int(digu)==0:
                st="three hundred"
        elif int(digh)==4:
            st=st+"four hundred and "
            if int(digt)==0 and int(digu)==0:
                st="four hundred"
        elif int(digh)==5:
            st=st+"five hundred and "
            if int(digt)==0 and int(digu)==0:
                st="five hundred"
        elif int(digh)==6:
            st=st+"six hundred and "
            if int(digt)==0 and int(digu)==0:
                st="six hundred"
        elif int(digh)==7:
            st=st+"seven hundred and "
            if int(digt)==0 and int(digu)==0:
                    st="seven hundred"
        elif int(digh)==8:
            st=st+"eight hundred and "
            if int(digt)==0 and int(digu)==0:
                st="eight hundred"
        elif int(digh)==9:
            st=st+"nine hundred and "
            if int(digt)==0 and int(digu)==0:
                st="nine hundred"
        
        if int(digt)>=2 and st not in hundreds:
            if int(digt)==2:
                st=st+"twenty"
            elif int(digt)==3:
                st=st+"thirty"
            elif int(digt)==4:
                st=st+"forty"
            elif int(digt)==5:
                st=st+"fifty"
            elif int(digt)==6:
                st=st+"sixty"
            elif int(digt)==7:
                st=st+"seventy"
            elif int(digt)==8:
                st=st+"eighty"
            elif int(digt)==9:
                st=st+"ninety"
            if int(digu)!=0:
                st=st+" "+wordlist[int(digu)]
        if int(digt)<2 and st not in hundreds:
            st=st+wordlist[int(digt+digu)]
    return st


def findLetters(num):
    return len(genWords(num).replace(" ",""))

sum=0
print findLetters(18)
for i in range(1,1001):
    sum=sum+findLetters(i)
print sum

