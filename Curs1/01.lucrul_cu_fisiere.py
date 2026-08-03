# introducere primitiva a datelor

x = input("Introduceti un numar: ")
print("Ai introdus: ", x)

# variabila x nu exista in afara programului a.i. sa fie salvat trebuie sa ne folosim de fisiere

file_name = "numar.txt"
# file_handler = open(file_name, "w") by default deschid un fiser pentru a-l citi (r), dar putem sa si scriem (w)

file_handler = open(file_name,"a") # a = append, adaugam info noi la fisierul existent

file_handler.write(x) # scriem in fisier x (suprascriere)
file_handler.write("\n") # trecem pe randul urmator

file_handler.close()


# mereu inchidem fisierul
