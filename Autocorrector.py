from autocorrect import Speller

corrector = Speller(lang='es')

def corregir(word):

    if not corrector(word) == word: 
        return corrector(word)
    else:
        return word
    
print(corrector(input("Escribe lo que deseas corregir: ")))

## da error, corregir.