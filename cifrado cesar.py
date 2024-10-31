palabra = ""
cifrado = ""

print("Ingrese una palabra:")
palabra = input()

for x in palabra:
    ascii=ord(x)+2
    
    if x.islower() and ascii>ord("z"):
        ascii=ascii-26 
        
    letra = chr(ascii)
    cifrado=cifrado+letra

print("Palabra cifrada:", cifrado)