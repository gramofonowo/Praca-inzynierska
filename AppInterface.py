def menu():
    
    try:        
        i=int(input("Co chcesz zrobic?\n1. Dodaj czujnik\n2. Usun czujnik\n3. Wyswietl zainstalowane czujniki\n0. Wyjdz\n-> "))
        if i>3 or i<-1:
            print("Prosze podac nr dostepnej funkcji!")
            menu()
    except (NameError, ValueError, SyntaxError):
        print("Nieprawidlowa wartosc!\n")
        menu()    
    
    if i==0:
        
        print("Zamknieto")        
    elif i==1:
        
        print("Ktory czujnik?")
        try:
            k=input("1. ds18b20\n2. dht11\n3. hcsr501\n")
            if k>3 or k<0:
                print("Prosze podac nr dostepnej funkcji!")
                menu()
        except(NameError, ValueError, SyntaxError):
            print('Nieprawidlowa wartosc!\n')
            menu()
        if k==1:
            
            try:
                name=raw_input("Podaj nazwe obiektu klasy czujnika DS18B20: ")
            except(NameError, ValueError, SyntaxError):
                print('Nieprawidlowa wartosc!\n')    
            obj_name=name            
            name=ds.TempSensorDS18B20()
            lista.append(name)            
            print("Czujnik %s "%name.getName() + 'reprezentowany przez obiekt --%s--'%obj_name)
        elif k==2:
            
            try:
                name=raw_input("Podaj nazwe obiektu: ")
            except(NameError, ValueError, SyntaxError):
                print('Nieprawidlowa wartosc!\n')       
            obj_name=name
            print("Obiekt o nazwie %s "%name + "klasy DHT11")
            i=input("Podaj pin dolaczanego czujnika: [22] ")
            name=dht11.TempHumSensorDHT11(pin=i)
            lista.append(name)            
            print("Czujnik %s "%name.getName() + 'reprezentowany przez obiekt --%s--'%obj_name)            
        elif k==3:
            
            try:
                name=raw_input("Podaj nazwe obiektu: ")
            except(NameError, ValueError, SyntaxError):
                print('Nieprawidlowa wartosc!\n')       
            obj_name=name
            print("Obiekt o nazwie %s "%name + "klasy HCSR501")
            i=input("Podaj pin dolaczanego czujnika: [21] ")
            name=mov.MotionSensorHCSR501(pin=i)
            lista.append(name)
            motion.append(name)            
            print("Czujnik %s "%name.getName() + 'reprezentowany przez obiekt --%s--'%obj_name)           
    elif i==2:
        
        print("Co usunac?")        
        j=0
        for i in lista:
            j+=1
            print(str(j)+'. '+i.getName())
        try:    
            y=int(input("Podaj numer czujnika\n-> "))
            print(lista[y-1].getName()+" przygotowany do usuniecia . . .")            
            lista[y-1].__del__()        
            lista.pop(y-1)
            print("Aktualizacja listy zainstalowanych czujnikow . . .")
            j=0
            for i in lista:
                j+=1
                print(str(j)+'. '+i.getName()) 
        except(IndexError, ValueError, NameError):
                print('Nieprawidlowa wartosc!\n')
                menu()          
    elif i==3:
        
        j=0
        for i in lista:
            j+=1
            print(str(j)+'. '+i.getName())
        print('\n')
        menu()
