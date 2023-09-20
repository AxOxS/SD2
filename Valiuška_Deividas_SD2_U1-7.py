import os
import time
#Išvalomas komandos langas, jeigu programa leidžiama dar kartą. Programos prisistatymas, turinio parodymas ir vartotojo prašymas pasirinkti programą.
#Prašomas integer tipo skaitmuo, jeigu bus įvesta kažkas kitokio - programa sustos
while True:
    os.system('cls')
    x = int(input("Sveiki! pasirinkite pageidaujamą programą!\n\n" +
    "1. Darbo užmokesčio skaičiuoklė\n" + 
    "2. Temperatūros konvertavimas tarp °F ir °C\n" +
    "3. Atstumo konvertavimas tarp mi ir km\n" + 
    "4. Stačiojo trikampio ploto skaičiuoklė\n" + 
    "5. Skaičiaus rūšies nustatymas\n" + 
    "6. Skaičiaus rūšies įvedimo kiekio apskaičiavimas\n" + 
    "7. Įvestų skaičių aritmetinio vidurkio apskaičiavimas\n\n" +
    "[1-7]: "))

    #Išvaloma consolė
    os.system('cls')

    #pasirenkama pirma programa
    if x == 1:
        #programa prašo įvesti reikalingus float tipo duomenis
        x = float(input("Įveskite išdirbtas valandas: "))
        y = float(input("Įveskite valandinį užmokestį: "))
        #Išvaloma consolė
        os.system('cls')
        #if logika tikrina ar bent vienas iš duotų skaičių yra mažesnis už 0, jeigu taip - programa terminuojama
        if x < 0 or y < 0:
            print("Veskite tik teigiamus skaičius!")
        #Jeigu atitinka duotą kriterijų ir praeina iki else'o - apskaičiuojamas atlyginimas
        else:
            pay = x * y
            #Apskaičiuotas float skaitmuo suapvalinamas iki šimtųjų
            rounded_pay = round(pay, 2)
            print("Mokėtina suma:", rounded_pay, "Eur")
            
    #pasirenkama antra programa       
    elif x == 2:
        F_or_C = int(input("Pasirinkite kokią operaciją norite atlikti: \n\n" +
        "1. Konvertavimas iš °F į °C\n" + 
        "2. Konvertavimas iš °C į °F\n\n" + 
        "[1-2]: "))
        #Išvaloma consolė
        os.system('cls')
        
        if F_or_C == 1:
            F = float(input("Įveskite temperatūrą, kurią norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            if(F >= -459):
                C = 5/9 * (F - 32)
                rounded_C = round(C, 2)
                print(F,"°F yra lygu", rounded_C, "°C")
            elif(F < -459):
                print("Jūsų įvesta temperatūra yra mažesnė už 0K, pagal termodinaminius dėsnius tai nėra įmanoma, bandykite dar kartą!")
            else:
                print("Bloga įvestis! Įveskite skaičių!")
                
        elif F_or_C == 2:
            C = float(input("Įveskite temperatūrą, kurią norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            if(C >= -273):
                F = C * (9/5) + 32
                rounded_F = round(F, 2)
                print(C,"°C yra lygu", rounded_F, "°F")
            elif(C < -273):
                print("Jūsų įvesta temperatūra yra mažesnė už 0K, pagal termodinaminius dėsnius tai nėra įmanoma, bandykite dar kartą!")
            else:
                print("Bloga įvestis! Įveskite skaičių!")
                
        else:
            print("Rinkitės skaičių tarp 1 ir 2!")
    
    #pasirenkama trečia programa       
    elif x == 3:
        mi_or_km = int(input("Pasirinkite kokią operaciją norite atlikti: \n\n" +
        "1. Konvertavimas iš mi į km\n" + 
        "2. Konvertavimas iš km į mi\n\n" + 
        "[1-2]: "))
        #Išvaloma consolė
        os.system('cls')
       
        if mi_or_km == 1:
           mi = float(input("Įveskite atstumą, kurį norite konvertuoti: "))
           #Išvaloma consolė
           os.system('cls')
           if mi >= 0:
               km = mi * 1.61
               rounded_km = round(km, 2)
               print(mi, "mi yra lygu", rounded_km, "km")
           else:
               print("Įveskite teigiamą skaičių!")
               
        elif mi_or_km == 2:
            km = float(input("Įveskite atstumą, kurį norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            if km >= 0:
               mi = km * 0.621371
               rounded_mi = round(mi, 2)
               print(km, "km yra lygu", rounded_mi, "mi")
            else:
               print("Įveskite teigiamą skaičių!")
               
        else:
            print("Rinkitės skaičių tarp 1 ir 2!")
    
    #pasirenkama ketvirta programa
    elif x == 4:
        #programa prašo įvesti trikampio a ir b kraštines
        x = float(input("Įveskite stačiojo trikampio kraštinę a (cm): "))
        y = float(input("Įveskite stačiojo trikampio kraštinę b (cm): "))
        
        #Išvaloma consolė
        os.system('cls')
        
        #if logika tikrina ar bent vienas iš duotų skaičių yra mažesnis ar lygus 0, jeigu taip - programa terminuojama
        if x <= 0 or y <= 0:
            print("Veskite tik teigiamus skaičius!")
            
        #Jeigu atitinka duotą kriterijų ir praeina iki else'o - apskaičiuojamas plotas
        else:
            S = (x * y) / 2
            #Apskaičiuotas float skaitmuo suapvalinamas iki šimtųjų
            rounded_S = round(S, 2)
            print("Stačiojo trikampio plotas:", rounded_S, "cm²")
    
    #pasirenkama penkta programa        
    elif x == 5:
        #Vartotojas įveda norimą skaičių
        x = float(input("Įveskite skaičių: "))
        
        #Išvaloma consolė
        os.system('cls')
        
        #Tikrina ar įvestas skaičius lygus, didesnis arba mažesnis už nulį
        if x > 0:
            print("Įvestas skaičius yra teigiamas.")
        elif x < 0:
            print("Įvestas skaičius yra neigiamas.")
        else:
            print("Įvestas skaičius yra lygus nuliui.")
            
    #pasirenkama šešta programa
    elif x == 6:
        #aprašomi...
        teigiami = 0
        neigiami = 0
        nuliai = 0
        
        print("Įveskite 10 skaičių \n")
        #time.sleep(5)
        #os.system('cls')
        for i in range(10):
            x = float(input(f"Įveskite skaičių nr {i + 1}: "))
            
            if x > 0:
                teigiami += 1
            elif x < 0:
                neigiami += 1
            else:
                nuliai += 1
        os.system('cls')
        print(f"Teigiami skaičiai: {teigiami}")
        print(f"Neigiami skaičiai: {neigiami}")
        print(f"Nuliai: {nuliai}")
        
    #Duodamas pasirinkimas grįžti į programų sąrašą arba terminuoti programą       
    restart = input("Programa darbą baigė, ar norite paleisti ją iš naujo? [y/n]: ")
    #Programa restartuojama
    if 'y' in restart:
        continue
    #Programa terminuojama
    else:
        os.system('cls')
        print("Viso gero")
        break