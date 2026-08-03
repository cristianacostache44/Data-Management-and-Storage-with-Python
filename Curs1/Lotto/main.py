
from number import Number

with open("Lotto/numere_extrase.txt","a+") as file_w:
    continut = file_w.write(str(Number(1,49)) + "\n")
    
