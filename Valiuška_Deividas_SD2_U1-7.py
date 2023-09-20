#Deividas Valiuška SD2 1-7 užduotys 

import os
#import time

#Išvalomas komandos langas, jeigu programa leidžiama dar kartą. Programos prisistatymas, turinio parodymas ir vartotojo prašymas pasirinkti programą.
#Prašomas integer tipo skaitmuo, jeigu bus įvesta kažkas kitokio - programa sustos. Dėl patogumo sudėjau visas užduotas padaryti programas į vieną bendrą programą. 
#Kartas nuo karto programa išvalo komandos langą, kad jis netaptų persotintas informacija. Visos programos sudėtos į while sąlygą, kad po programos darbo būtų galima iškarto grįžti
#į programų langą arba terminuoti darbą

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
    
    #Ši programa yra skirta sužinoti mokėtiną sumą žinant du kintamuosius: dirbtų valandų skaičių ir valandinį atlyginimą, todėl padariau taip,
    #kad programa dirbtų tik su skaičiais, konkrečiau float tipo teigiamais skaičiais arba 0 (dėl atsakymo konkretumo float, o ne int ir be neigiamų
    #skaičių nes žmogus negali dirbti minusinių valandų arba už minusinį atlyginimą). Bandant įvesti string ar char tipo duomenis - programa terminuosis.
    #Galvojau daugumos šitų programų if logiką ar ciklus apskliausti try/except, kad except mestų klaidą kaip "Veskite tik teisingo tipo duomenis", bet
    #pasirodė neverta, kadangi pati programa terminuodamasi parašo, kad buvo įvesti blogo tipo duomenys. Galutinis atsakymas suapvalinamas iki šimtųjų dėl
    #estetinių sumetimų.
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
            #Komandos lange atspausdinama mokėtina suma
            print("Mokėtina suma:", rounded_pay, "Eur")
            
    #pasirenkama antra programa
    
    #Šios programos tikslas vartotojui pasirinkus, konvertuoti celcijų į fahrenheitą arba fahrenheitą į celcijų. pirmas input priima tik integer tipo duomenis. 
    #Pasirinkus vieną iš dviejų galimų funkcijų programa paprašys įvesti temperatūrą, kurią norite konvertuoti. Šįkart atsakymas jau konvertuojamas į float tipo 
    #skaitmenis dėl tikslumo, todėl vėl gi char/string tipo duomenys netiks ir programa terminuosis. Abejais atvejais programa nekonvertuos temperatūros, jeigu 
    #ji bus žemesnė už 0K. Jeigu vedama temperatūra yra skaičius ir didesnė ar lygi 0K - programa atliks aritmetinius veiksmus, gautąjį atsakymą suapvalins iki 
    #šimtųjų ir jį pateiks vartotojui    
    elif x == 2:
        #Prašymas pasirinkti vieną iš dviejų operacijų. Galima vesti tik integer tipo skaitmenis
        F_or_C = int(input("Pasirinkite kokią operaciją norite atlikti: \n\n" +
        "1. Konvertavimas iš °F į °C\n" + 
        "2. Konvertavimas iš °C į °F\n\n" + 
        "[1-2]: "))
        #Išvaloma consolė
        os.system('cls')
        
        #Pirmo pasirinkimo kodas F to C
        if F_or_C == 1:
            #Prašymas įvesti temperatūrą, atsakymas kovertuojamas į float tipo skaitmenį, todėl programa terminuosis, jeigu gaus char/string tipo duoemnis
            F = float(input("Įveskite temperatūrą, kurią norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            #Jeigu įvesta fahrenheito temperatūra nėra mažesnė už 0K - programa dirbs toliau.
            if(F >= -459):
                #Konvertuojamas fahrenheitas į celcijų
                C = 5/9 * (F - 32)
                #Atsakymas suapvalinamas iki šimtųjų
                rounded_C = round(C, 2)
                #Pateikiamas atsakymas
                print(F,"°F yra lygu", rounded_C, "°C")
            #Jeigu įvesta fahrenehito temperatūra mažesnė už 0K - pranešama vartotojui ir programa terminuojasi
            else:
                print("Jūsų įvesta temperatūra yra mažesnė už 0K, pagal termodinaminius dėsnius tai nėra įmanoma, bandykite dar kartą!")
                
        #Antro pasirinkimo kodas C to F
        elif F_or_C == 2:
            #Prašymas įvesti temperatūrą, atsakymas kovertuojamas į float tipo skaitmenį, todėl programa terminuosis, jeigu gaus char/string tipo duoemnis
            C = float(input("Įveskite temperatūrą, kurią norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            #Jeigu įvesta celcijaus temperatūra nėra mažesnė už 0K - programa dirbs toliau.
            if(C >= -273):
                #Konvertuojamas celcijus į fahrenheitą
                F = C * (9/5) + 32
                #Atsakymas suapvalinamas iki šimtųjų
                rounded_F = round(F, 2)
                #Pateikiamas atsakymas
                print(C,"°C yra lygu", rounded_F, "°F")
             #Jeigu įvesta celcijaus temperatūra mažesnė už 0K - pranešama vartotojui ir programa terminuojasi
            else:
                print("Jūsų įvesta temperatūra yra mažesnė už 0K, pagal termodinaminius dėsnius tai nėra įmanoma, bandykite dar kartą!")
        #Jeigu programos pradžioje vietoj 1 ar 2 pasirenkamas kitoks skaičius - programa veikti nepradeda       
        else:
            print("Rinkitės skaičių tarp 1 ir 2!")
    
    #pasirenkama trečia programa
    
    #Šios programos tikslas vartotojui pasirinkus, konvertuoti kilometrus į mylias arba mylias į kilometrus. pirmas input priima tik integer tipo duomenis. 
    #Pasirinkus vieną iš dviejų galimų funkcijų programa paprašys įvesti atstumą, kurį norite konvertuoti. Šįkart atsakymas jau konvertuojamas į float tipo 
    #skaitmenis dėl tikslumo, todėl vėl gi char/string tipo duomenys netiks ir programa terminuosis. Abejais atvejais programa nekonvertuos atstumo, jeigu 
    #jis bus neigiamos reikšmės. Jeigu vedamas atstumas yra skaičius ir didesnis ar lygus 0 - programa atliks aritmetinius veiksmus, gautąjį atsakymą suapvalins iki 
    #šimtųjų ir jį pateiks vartotojui      
    elif x == 3:
        #Prašymas pasirinkti vieną iš dviejų operacijų. Galima vesti tik integer tipo skaitmenis
        mi_or_km = int(input("Pasirinkite kokią operaciją norite atlikti: \n\n" +
        "1. Konvertavimas iš mi į km\n" + 
        "2. Konvertavimas iš km į mi\n\n" + 
        "[1-2]: "))
        
        #Išvaloma consolė
        os.system('cls')
        
        #Pirmo pasirinkimo kodas mi to km
        if mi_or_km == 1:
           #Prašymas įvesti atstumą, atsakymas kovertuojamas į float tipo skaitmenį, todėl programa terminuosis, jeigu gaus char/string tipo duoemnis
           mi = float(input("Įveskite atstumą, kurį norite konvertuoti: "))
           #Išvaloma consolė
           os.system('cls')
           #Pereinama prie aritmetinių veiksmų, mylių konvertavimą į kilometrus, tik jeigu skaičius yra daugiau arba lygus nuliui.
           if mi >= 0:
               km = mi * 1.61
               #Atsakymas suapvalinamas ir pateikiamas naudotojui
               rounded_km = round(km, 2)
               print(mi, "mi yra lygu", rounded_km, "km")
           #Programa terminuojasi, jeigu įvestas neigiamas skaičius 
           else:
               print("Įveskite teigiamą skaičių!")
               
        #Antro pasirinkimo kodas, km to mi    
        elif mi_or_km == 2:
            #Prašymas įvesti atstumą, atsakymas kovertuojamas į float tipo skaitmenį, todėl programa terminuosis, jeigu gaus char/string tipo duoemnis
            km = float(input("Įveskite atstumą, kurį norite konvertuoti: "))
            #Išvaloma consolė
            os.system('cls')
            #Pereinama prie aritmetinių veiksmų, kilometrų konvertavimą į mylias, tik jeigu skaičius yra daugiau arba lygus nuliui.
            if km >= 0:
               mi = km * 0.621371
               #Atsakymas suapvalinamas ir pateikiamas naudotojui
               rounded_mi = round(mi, 2)
               print(km, "km yra lygu", rounded_mi, "mi")
            #Programa terminuojasi, jeigu įvestas skaičius yra neigiamas
            else:
               print("Įveskite teigiamą skaičių!")
        #Jeigu programos pradžioje vietoj 1 ar 2 pasirenkamas kitoks skaičius - programa veikti nepradeda       
        else:
            print("Rinkitės skaičių tarp 1 ir 2!")
    
    #pasirenkama ketvirta programa
    
    #Kadangi užduotyje nebuvo paminėtas trikampio tipas - pasirinkau statųjį. Vartotojas prašomas įvesti du skaitmenis (prirašiau, cm tipo, kad neklitų nesklandumų ir 
    #vieno skaitmens neįvestų cm, o kito, tarkim m ir atsakymas gautūsi neteisingas), kurie konvertuojami į float dėl atsakymo tikslumo
    #(tuo pačiu char/str tipo įvestis terminuos programą). Po įvesties išvalomas komandos langas, kad nebūtų per daug informacijos vienoje vietoje. Jeigu bent vienas iš 
    #vartotojo pateiktų skaičių yra mažesnis arba lygus nuliui - programa praneša, kad tai netinkama įvestis ir terminuojasi. Jeigu įvesti skaitmenys atitinka kriterijus
    #- apskaičiuojamas stačijo trikampio plotas, atsakymas suapvalinamas iki šimtųjų ir pateikiamas vartotojui
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
            #Apskaičiuotas float skaitmuo suapvalinamas iki šimtųjų ir atsakymas pateikiamas vartotojui
            rounded_S = round(S, 2)
            print("Stačiojo trikampio plotas:", rounded_S, "cm²")
    
    #pasirenkama penkta programa      
    
    #Ši programa yra skirta pasakyti ar vartotojas įvedė teigiamos, neigiamos ar nulinės vertės skaičių. Kadangi gali įvesti ne tik paprastus int tipo skaitmenis - įvestas
    #skaitmuo konvertuojamas į float (vėl string/char terminuos programą). Gautas skaičius praeina tris sąlygas ir skaičiaus tipo atsakymas pateikiamas vartotojui.
    #Jeigu atitinka pirmąją arba antrąją - kitos sąlygos netikrinamos ir išeinama iš if/elif/else logikos. 
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
    
    #Šios programos tikslas - apskaičiuoti kiek iš nustatyto kiekio skaitmenų, kuriuos įveda vartotojas, buvo teigiamos, neigiamos ir nulinės reikšmės. Programoje aprašomi trys
    #reikalingi kintamieji ir vartotojas paprašomas įvesti 10 skaitmenų po vieną. Jie konvertuojami į float tipą, todėl įvedus char/string vertės duomenis - programa neveiks. for cikle,
    #po kiekvieno įvedimo, skaitmuo priskiriamas prie vieno iš trijų nustatytų kintamųjų ir ciklas kartojasi, kol prasisuka 10 kartų. Pasibaigus ciklui išvalomas komandos langas ir
    #vartotojui pateikiama informacija: kiek suvestų skaičių buvo teigiami, neigiami ar nulinės reikšmės
    elif x == 6:
        #Duodami pavadinimai kintamiesiems
        teigiami = 0
        neigiami = 0
        nuliai = 0
        
        print("Įveskite 10 skaičių \n")
        #time.sleep(5)
        #os.system('cls')
        
        #for ciklas, kuris sustos tik tada, kai vartotojas įves 10 skaičių arba bus įvestas char/string, kas terminuos programą
        for i in range(10):
            #Įvestis konvertuojama į float tipą ir parašoma, kelintas sekantis skaitmuo turi būti įvestas
            x = float(input(f"Įveskite skaičių nr {i + 1}: "))
            #if logika priskirianti įvestus skaičius prie teigiamų, neigiamų ir nulių
            if x > 0:
                teigiami += 1
            elif x < 0:
                neigiami += 1
            else:
                nuliai += 1
        #Įvedus visus 10 skaitmenų informacija pašalinama iš komandos lango ir pateikiama informacija vartotojui: įvestų teigiamų, neigiamų ir nulinių skaičių kiekis
        os.system('cls')
        print(f"Teigiami skaičiai: {teigiami}")
        print(f"Neigiami skaičiai: {neigiami}")
        print(f"Nuliai: {nuliai}")
        
    #pasirenkama septinta programa
    
    #Programa apskaičiuoja šešių, vartotojo įvestų skaitmenų, aritmetinį vidurkį. Programos pradžioje aprašomas kintamasis, kuris bus naudojamas sumai saugoti. Vartotojas prašomas
    #suvesti šešis skaitmenis po vieną. Po kiekvieno suvedimo skaitmuo konvertuojamas į float tipą (programa terminuosis vedant char/string tipo duomenis). Įvestas skaičius pridedamas
    #prie esamos sumos reikšmės. Pasibaigus ciklui išvalomas komandos langas, apskaičiuojamas aritmetinis vidurkis. Gautas atsakymas suapvalinamas iki šimtųjų ir pateikiamas vartotojui.
    elif x == 7:
        #aprašomas kintamasi
        suma = 0
        print("Įveskite 6 skaičius\n")
        #for ciklas, kuris sukasi 6 kartus, kol klientas suveda 6 skaitmenis
        for i in range(6):
            #įvestis konvertuojama į float tipą dėl tikslumo. įvedus str/char tipo duomenis programa terminuosis
            x = float(input(f"Įveskite skaičių nr {i + 1}: "))
            #prie praeitos sumos reikšmės pridedamos suvestos reikšmės
            suma += x
        #pasibaigus ciklui - išvalomas komandos langas
        os.system('cls')
        #apskaičiuojamas aritmetinis vidurkis, padalinant sudėtą įvesčių reikšmę iš kiek kartų sukosi ciklas.
        art_vid = suma / 6
        #atsakymas suapvalinamas iki šimtųjų ir pateikiamas vartotojui
        rounded_vidurkis = round(art_vid, 2)
        print("Įvestų skaičių aritmetinis vidurkis yra:", rounded_vidurkis)
    
    #Jeigu pradėjus programą buvo įvestas skaitmuo, neįeinantis į 1-7 - programa terminuojasi   
    else:
        print("Įveskite skaičių tarp 1 ir 7!")       
    #Po kiekvienos programos pabaigos - duodamas pasirinkimas grįžti į programų sąrašą arba terminuoti programą       
    restart = input("Programa darbą baigė, ar norite paleisti ją iš naujo? [y/n]: ")
    #Programa restartuojama
    if 'y' in restart:
        continue
    #Programa terminuojama
    else:
        #išvalomas komandos langas
        os.system('cls')
        print("Viso gero")
        break