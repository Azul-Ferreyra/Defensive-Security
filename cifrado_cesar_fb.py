import string
from langdetect import detect

ALFABETO = string.ascii_lowercase

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    texto_plano= ""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra
        else:
            indice_letra_cifrada = ALFABETO.index(letra)
            indice_letra_descifrada = indice_letra_cifrada - clave_descifrado
            texto_plano += ALFABETO[indice_letra_descifrada]
    return texto_plano

def fuerza_bruta(texto_cifrado):
    espacio_claves=range(len(ALFABETO))
    for clave in espacio_claves:
        texto_plano = algoritmo_descifrado(texto_cifrado, clave)
        lenguaje = detect(texto_plano)
        if lenguaje == "es":
            print(f"El texto descifrado es: {texto_plano}")
            print(f"La clave de descifrado es: {clave}")
            return
        

if __name__ =="__main__":
    texto_cifrado = input("Por favor introduce el texto cifrado: ").lower()
    fuerza_bruta(texto_cifrado)
   