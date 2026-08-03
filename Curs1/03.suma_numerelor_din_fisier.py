
#---- VARIANTA 1 ----- folosirea de read

with open("suma.txt","r") as file_reader:
    content = file_reader.read()
    nr_str = content.split("\n") # numere stringuri transformate in lista, separate de \n
    suma = 0
    for i in nr_str:
        suma += int(i)
    print(suma)


#---- VARIANTA 2 ----- folosirea de readlines

with open("suma.txt","r") as file_reader:
    content = file_reader.readlines()
    suma = 0
    for i in nr_str:
        suma += int(i)
    print(suma)
