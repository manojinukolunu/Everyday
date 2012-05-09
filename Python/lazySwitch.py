
str1="""AuditAdmin,CacheServerAdmin,Calendar,Category,CMSAdmin,Connection,CrystalReport,Diskunmanaged,Event,EventServerAdmin,Excel,FavoritesFolder,Folder,FileServerAdmin,Ftp,Hyperlink,Inbox,JobServerAdmin,LicenseKey,Managed,ObjectPackage,Overload,PersonalCategory,Pdf,Powerpoint,Profile,Program,Publication,Rtf,Server,Shortcut,Smtp,SSOAdmin,Txt,Universe,User,Usergroup,Webi,Word,NOVALUE"""
a=str1.split(",")
j=0

print """
switch (SIKIND.toInt(object.getKind())){"""
for i in range(len(a)):
    print """case """ +a[j]+""":
    arr["""+str(j) +"""]++;
    break;
    """
    j+=1

print "}"

j=0
print "System.out.println("
for i in range(len(a)):
    print "\" \\n"+a[i]+"= \" "+"+arr["+str(j)+"]+"
    j+=1
print ")"
