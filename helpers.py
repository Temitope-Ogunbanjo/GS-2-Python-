import string
import re

def Normalizar(Texto):
    Texto = Texto.lower().strip()

    Caracteres = {"á": "a", "à": "a", "ã": "a", "â": "a", "é": "e", "ê": "e","í": "i", "ó": "o", "õ": "o", "ô": "o", "ú": "u", "ç": "c"}
    
    Acentos = str.maketrans(Caracteres)
    Texto = Texto.translate(Acentos)

    Pontuacoes = str.maketrans("", "", string.punctuation + "¨")
    Texto = Texto.translate(Pontuacoes)

    return Texto

def Normalizar_Lista(Lista):
    ListaNormalizada = []
    for Item in Lista:
        ListaNormalizada.append(Normalizar(Item))
    return ListaNormalizada

def Palavras(Texto):
    Texto = Normalizar(Texto)
    return Texto.split()

def GuardrailAssistente(Texto):
    if not Texto or not Texto.strip():
        return False
    
    Texto= Texto.strip()
    
    if "@" in Texto:
        return False
        
    if re.search(r'\d{8,}', Texto):
        return False
        
    proibidos = [
        "meu nome é", "me chamo", "meu cpf", "meu telefone", 
        "meu email", "meu e-mail", "meu rg", "whatsapp"
    ]
    
    texto_minusculo = Texto.lower()
    for termo in proibidos:
        if termo in texto_minusculo:
            return False

    return True