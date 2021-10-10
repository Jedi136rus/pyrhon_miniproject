def shifr(st,n):                                                            #функция шифрования
    stres = ""
    for i in range (len(st)):
        if 	1040 <= ord(st[i]) <= 1071:
            if (ord(st[i]))+ n > 1071:
                stres =stres + chr(1039+(int(ord(st[i]))+n-1071))
            else:
                stres =stres + chr(ord(st[i])+n)
        elif  1072<=ord(st[i])<=1103:
             if (ord(st[i])+n)>1103:
                  stres =stres + chr(1071+(ord(st[i])+n-1103))
             else:
                  stres =stres + chr(ord(st[i])+n)
        elif  65<=ord(st[i])<=90:
             if (ord(st[i])+n)>90:
                  stres =stres + chr(64+(ord(st[i])+n-90))
             else:
                  stres =stres + chr(ord(st[i])+n)
        elif  97<=ord(st[i])<=122:
             if (ord(st[i])+n)>122:
                  stres =stres + chr(96+(ord(st[i])+n-122))
             else:
                  stres =stres + chr(ord(st[i])+n)
        else:
            stres = stres + st[i]
    return stres


def rashifr(st,n):                                                      #функция расшифрования
    stres = ""
    for i in range (len(st)):
        if 	1040 <= ord(st[i]) <= 1071:
            if ord(st[i]) - n < 1040:
                stres += chr(1072-(1040 - (ord(st[i]) - n)))
            else:
                stres += chr(ord(st[i]) - n)
        elif  1072<=ord(st[i])<=1103:
             if ord(st[i]) - n < 1072:
                  stres += chr(1104-(1072 - (ord(st[i]) - n)))
             else:
                  stres += chr(ord(st[i]) - n)
        elif  65<=ord(st[i])<=90:
             if ord(st[i]) - n < 65:
                  stres += chr(91-(65 - (ord(st[i]) - n)))
             else:
                  stres += chr(ord(st[i]) - n)
        elif  97<=ord(st[i])<=122:
             if ord(st[i]) - n < 97:
                  stres += chr(123-(97 - (ord(st[i]) - n)))
             else:
                  stres += chr(ord(st[i]) - n)
        else:
            stres = stres + st[i]
    return stres


print (shifr("Day, mice. "Year" is a mistake!",17))
print ("Hawnj pk swhg xabkna ukq nqj.")
for i in range(1,26):
    print (rashifr("Hawnj pk swhg xabkna ukq nqj.", i))
