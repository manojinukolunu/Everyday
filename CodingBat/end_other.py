def end_other(a,b):
    if b.lower().endswith(a.lower()) or a.lower().endswith(b.lower()):
        return True
    else :
        return False
print end_other('abc', 'abXabc')
