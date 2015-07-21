num = int(input())
cn = num
c = 1
while cn > 9:
    cn = cn / 10
    c+=1
print("El numero ",num,"tiene",c,'digitos')
