#1
#print("Ülesanne 1")
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus==o_vastus: 
#        break
#    else:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#print("Õige vastus! Katsed oli ...",k )
#print()
#
#2
#print("Ülesanne 2")
#x=0
#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x== 30:
#        break 
#print()
#print("For:")
#for x in range(0,30,1):
#    if x%2==1: 
#        print(x, end=" ")
print()
print()
print()
print("Vigade otsing -2")
print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) #Lisatud lõppu 2 sulgu
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a #Eemaldatud 2 lisa
    paaris=0 #Eemaldas lisa
    paaritu=0 #Eemaldas lisa
    while b > 0: #Semikoolon muudetud käärsooleks
        if b % 2 == 0: #Lisatud teine ​​võrdne
            paaris += 1 #Vahetage pluss ja võrdne
        else:
            paaritu += 1 #Vahetage pluss ja võrdne
        b = b // 10 #Esimeselt b-lt eemaldati lisaruum
            #Eemaldatud lisaruumid
    print("Paarisarvud:",paaris) #Lisas koma
    print("Paarituid numbreid:",paaritu) #Lisas koma
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud number")
    print()
    b=0
    while a > 0: #Lisan koolon
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #Eemaldatud lisaruum #Vahetage pluss ja võrdne
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #Eemaldatud lisasulgud
    print()
    if c % 2 == 0: #Lisatud teine ​​võrdne
        print("с- paarisarv. Jagage poolt 2.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2.")
    while c != 1:   
            if c % 2 == 0: ##Lisatud teine ​​võrdne
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(c, end=" ") #Lisatud lõputsitaadid
    print()
    print("Hüpotees on õige") #Üksikud jutumärgid muudeti topeltjutumärkideks