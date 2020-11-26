dict = {}

def meni():
    print("1. Ispisi sve elemente.")
    print("2. Unesi novi element.")
    print("3. Promeni elemenat.")
    print("4. Izbrisi elemenat.")
    print("5. Izadji iz aplikacije.")

def ispisi_elemente():
    for key, value in dict.items():
        print(key, value)

def unesi_element():
    count = 0
    for i in dict.keys():
        count = count + 1

    dict[count+1] = input("Unesite vrednost:")

def promeni_element():

    dict[int(input("Unesite kod elementa:"))] = input("Unesite novu vrednost:")

def obrisi_element():
    key = input("Koji element zelite da obrisite?:")
    del dict[int(key)]

if __name__ == '__main__':
    while True:
        meni()

        opcija = input()

        if opcija == "1":
            ispisi_elemente()
        elif opcija == '2':
            unesi_element()
        elif opcija == '3':
            promeni_element()
        elif opcija == '4':
            obrisi_element()
        elif opcija == "5":
            break