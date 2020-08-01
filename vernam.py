# -*- coding: cp1254 -*-
def XOR(a,b):
    result=''
    for i in range(len(a)):
        if (a[i]==b[i]):
            result=result+'0'
        else:
            result=result+'1'
    return result;
ita=['00001','00010','00011','00100','00101','00110','00111','01000','01001','01010','01011','01100','01101','01110','01111','10000','10001','10010','10011','10100','10101','10110','10111','11000','11001','11010','11011','11100','11101']
a=['A','B','C','C2','D','E','F','G','G2','H','I2','I','J','K','L','M','N','O','O2','P','R','S','S2','T','U','U2','V','Y','Z']
def Sifrele():
    try:
        metin2=input('Metin:')
        anahtar=input("Anahtar Metin(Girilecek Deger Ornegi:['01111','00111']):")
        metin=[]
        for i in range(len(metin2)):
            if metin2[i]!='2' and i<len(metin2)-1:
                if metin2[i+1]=='2':
                    metin.append(metin2[i]+'2');
                else:
                    metin.append(metin2[i]);
            if metin2[i]!='2' and i==len(metin2)-1:
                metin.append(metin2[i]);
        tabanmetin=[]
        for i in range(len(metin)):
            for j in range(len(a)):
                if metin[i]==a[j]:
                    tabanmetin.append(ita[j])
        if len(metin)!=len(anahtar):
            print('Metin ile Anahtar Metin ayni uzunlukta olmalidir.')
        result=[]
        for i in range(len(tabanmetin)):
            result.append(XOR(tabanmetin[i],anahtar[i]));
        print('Sifreli Metin:'+str(result));
        print('Anahtar Metin:'+str(anahtar))
    except:
        pass;
def Coz():
    try:
        sifremetin=input('Sifreli Metin:')
        anahtarmetin=input('Anahtar Metin:')
        tabanmetin=[]
        for i in range(len(sifremetin)):
            tabanmetin.append(XOR(sifremetin[i],anahtarmetin[i]));
        metin=''
        for i in range(len(tabanmetin)):
            for j in range(len(a)):
                if tabanmetin[i]==ita[j]:
                    metin=metin+a[j]
        print('Metin:'+str(metin))
    except:
        pass;
while True:
    try:
        command=input('Sifrele/Coz(S/C):')
        if command.lower()=='s':
            print('')
            Sifrele()
        if command.lower()=='c':
            print('')
            Coz()
    except:
        print('Sifreleme icin S, Cozme icin C yaziniz.')
