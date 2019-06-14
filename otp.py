#OPT Generetor

string = input()
otp = ''
for i in string:
    if(len(otp)>4):
        break
    if(int(i)%2!=0):
        otp += str(int(i)**2)
print(int(otp[:4]))
