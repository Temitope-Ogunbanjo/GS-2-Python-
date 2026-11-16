import json
from orientacao import Orientacao
from helpers import Palavras
from helpers import Normalizar
from helpers import Normalizar_Lista

class BaseConhecimento:
    def __init__(self, Path):
        self.Path = Path
        self.Data = []
        self.CategoriasAtendidas = []
        self.DataCategorias = None

    def Carregar(self):
        try:
            with open(self.Path, "r", encoding="utf-8") as file:
                Data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            Data = [] 
            
        for Item in Data:
            self.Data.append(Orientacao(Item))

        self.Categorias()

    def Categorias(self):
        Resultado = []
        for Item in self.Data:
            if Item.categoria not in Resultado:
                Resultado.append(Item.categoria)

        self.CategoriasAtendidas = Resultado
        self.Por_categoria()

    def Por_categoria(self):
        Resultado = {}
        for Categoria in self.CategoriasAtendidas:
            Resultado[Categoria] = []
            for Item in self.Data:
                if Item.categoria == Categoria:
                    Resultado[Categoria].append(Item)

        self.DataCategorias = Resultado
        print(self.DataCategorias)
        
    def Pontuar(self, Texto, Item):

        Pontos = 0

        Texto = Normalizar(Texto)
        PalavrasChave = Normalizar_Lista(Item.palavras_chave)
        Titulo = Normalizar(Item.titulo)

        for I in PalavrasChave:
            if I in Texto:
                Pontos += 3

        for I in Palavras(Texto):
            if len(I) > 4 and I in Titulo:
                Pontos += 1

        return Pontos
                

    def Buscar(self, Texto):
        Resultado = []
        for Item in self.Data:
            Pontos = self.Pontuar(Texto, Item)
            Resultado.append((Pontos, Item))

        Resultado.sort(key=lambda x: x[0], reverse=True)

        return Resultado    
         