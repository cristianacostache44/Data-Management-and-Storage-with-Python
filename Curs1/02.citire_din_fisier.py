
file_name = "numar.txt"


#----- VERSIUNEA 1 - INVECHITA

file_handler = open(file_name,"r") # deschidem pentru a citi -> r = read
continut = file_handler.read()
print(continut)
file_handler.close()


#----- VERSIUNEA 2 - RECOMANDATA 

with open(file_name,"r") as file_handler:
    continut = file_handler.read()
    print(continut)
# se foloseste keywordul "with" ceea ce reduce inchiderea manuala a fisierului