def combo_string(a, b):
    if len(a)<len(b):
          return a+b+a
            
    elif len(b)<len(a):
          return b+a+b
                  
    if a=="" or b=="":
          return a+a+a
