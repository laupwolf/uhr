import time;
#start und end des jahres, year=Länge des Jahres
start = 1420070400
end = 1428796799
year = 31535999
print("Es ist gerade ")
print(time.strftime("%H:%M:%S, %d. %B", time.localtime((time.time()-start)/(end-start)*year)))
#time.sleep(20)
#Zurückrechnen auf den Geburtstag (braucht Eingabe)
#Eingabe durch Konsole
while True:
    tag = input("Umrechnung: Tag.Monat? ")
    tag = tag+".1970 00:00:00"
    pattern ='%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(tag, pattern)))
    # Länge des neuen Jahres: end-start
    gebuneu = int((epoch/year)*(end-start)+start)
    print("Umgerechnet: " + time.strftime("%H:%M:%S, %d. %B", time.localtime(gebuneu)))
    print("Weiter?")

#Eventuell auch noch:
#Uhr laufen lassen (braucht Grafik)