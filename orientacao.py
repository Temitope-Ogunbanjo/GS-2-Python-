class Orientacao:
    def __init__(self, Data):
        self.id = Data['id']
        self.categoria = Data['categoria']
        self.titulo = Data['titulo']
        self.palavras_chave = Data['palavras_chave']
        self.resposta = Data['resposta']
        self.documentos = Data['documentos']
        self.onde = Data['onde']
        self.fonte = Data['fonte']
        self.verificado_em = Data['verificado_em']

    def exibir(self):
        print(f">> {self.titulo}")
        print("\n")
        print(f"{self.resposta}")
        print("\n")
        print("Documentos necessários:")
        print("\n")
        for I in self.documentos:
            print(f"- {I}")
        print("\n")
        print(f"Onde: {self.onde}")
        print(f"Fonte: {self.fonte}")
        print("\n")
        print("Aviso: O assistente não é fonte oficial de informação. Recomenda-se sempre a consulta de canais e orgãos oficiais para confirmação de informações e procedimentos.")
        print("\n")