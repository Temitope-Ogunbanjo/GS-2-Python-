from helpers import GuardrailAssistente
import time
from datetime import date
import json
import csv
import os

class Assistente:
    def __init__(self, Nome, Base):
        self.nome = Nome
        self.base = Base
        self.Data = {
            "ListaSemSolucoes" : [],
            "Tentativas" : 0
        }

    def perguntar(self):

        Tempo = time.time()

        pergunta = input("Faça uma pergunta ao assistente: ")
        print("\n")

        if pergunta.lower() in ["0", "voltar"]:
            print("\n")
            return

        while not GuardrailAssistente(pergunta):
            print("\n")
            pergunta = input("Não compartilhe dados pessoais e informações sigilosas ou privadas. Estou aqui somente para te ajudar com dúvidas e questionamentos. Faça a sua pergunta:")
            print("\n")

        Resultado = self.base.Buscar(pergunta)
        Avaliacao = ""

        Recomendacoes = ""

        Confianca = ""
        Pontuacao, Item = Resultado[0][0], Resultado[0][1]

        if Pontuacao >= 6:
            Confianca = "Alta"
        elif Pontuacao >= 3 and Pontuacao < 6:
            Confianca = "Média"
        elif Pontuacao < 3:
            Confianca = "Baixa"

        def Header():
            print("\n")
            print("=" * 25)
            print(f"Confiança da resposta: {Confianca} ({Pontuacao} pontos) ")
            print(f"\n")


        def Feedback():
            FeedbackTable = {
                "sim" : "s",
                "não" : "n",
                "s" : "s",
                "n" : "n"
            }
            
            Resultado = input("Essa orientação respondeu sua dúvida? (s/n): ")

            while Resultado.lower().strip() not in ["s","n"] or FeedbackTable[Resultado.lower().strip()] not in ["s","n"]:
                Resultado = input("Essa orientação respondeu sua dúvida? (s/n): ")

            Avaliacao = Resultado

            return Avaliacao

        self.Data["Tentativas"] += 1


        if Confianca.lower() == "baixa":
            Header()
            Recomendacoes = [
                "Não conseguimos encontrar uma resposta satisfatória para sua pergunta. Recomendamos que você consulte os canais oficiais do TSE ou do seu cartório eleitoral para obter informações precisas e atualizadas!. \n",
                f"\n",
                f">> Nossos usuários também perguntam sobre: {', '.join(Item.palavras_chave)}",
                f">> Faça perguntas com base nas categorias: {'| '.join(self.base.CategoriasAtendidas)}",
                f"\n"
            ]

            self.Data["ListaSemSolucoes"].append(pergunta)

            for I in Recomendacoes:
                print(I)

            Ajudou = Feedback()
            self.registrar({"Orientacao" : Item, "TempoInicial" : Tempo, "Pergunta" : pergunta, "Ajudou" : Ajudou, "Encontrou" : False})

            return
        
        Header()
        print("\n")
        Item.exibir()
        Ajudou = Feedback()

        self.registrar({"Orientacao" : Item, "TempoInicial" : Tempo, "Pergunta" : pergunta, "Ajudou" : Ajudou, "Encontrou" : True})

    def navegar(self, categoria):
        print(f"Conteúdos sobre {categoria}")

        for Item in self.base.DataCategorias[categoria]:
            print(f">> {Item.titulo}")


    def registrar(self,Resultado):

        Path = "data/historico.json"

        Data = {
            "data" : str(date.today()),
            "origem" : Resultado["Orientacao"].categoria,
            "pergunta" : Resultado["Pergunta"],
            "id" : Resultado["Orientacao"].id,
            "ajudou" : Resultado["Ajudou"],
            "encontrou" : Resultado["Encontrou"],
            "tempo" : round(time.time() - Resultado["TempoInicial"], 1)
        }

        if os.path.exists(Path):
            with open("data/historico.json", "r", encoding="utf-8") as arquivo:
                try:
                    Current = json.load(arquivo)
                    if not isinstance(Current, list):
                        Current = [Current]
                except json.JSONDecodeError:
                    Current = []
        else:
            Current = []

        Current.append(Data)

        with open("data/historico.json", "w", encoding="utf-8") as arquivo:
            json.dump(Current,arquivo,ensure_ascii=False, indent = 4)

    def indicadores(self):
        with open("data/historico.json", "r", encoding="utf-8") as JSON:
            try:
                Data = json.load(JSON)
            except json.JSONDecodeError:
                Data = []

        if not Data:
            print("\n Histórico vazio.")
            return
        
        TempoTotal = 0
        Encontradas = 0
        AjudouSim = 0

        for Atendimento in Data:
            TempoTotal += Atendimento.get("tempo", 0)
            if Atendimento.get("encontrou") == True:
                Encontradas += 1
            if str(Atendimento.get("ajudou")).lower() in ["s", "sim"]:
                AjudouSim += 1

        TotalAtendimentos = len(Data)
        TempoMedio = TempoTotal / TotalAtendimentos
        TaxaResposta = (Encontradas / TotalAtendimentos) * 100
        TaxaAcerto = (AjudouSim / TotalAtendimentos) * 100

        print('\n')
        print(f"=== INDICADORES DE ATENDIMENTO ===")
        print(f"% de Respostas Encontradas: {TaxaResposta:.2f} %")
        print(f"Taxa de Acertos (Respostas Satisfatórias) : {TaxaAcerto:.2f} %")
        print(f"Tempo Médio: {TempoMedio:.2f} segundos")
        print(f"Tentativas Totais Realizadas: {self.Data.get('Tentativas', 0)}")
        print(f"Facilidade de Uso: {self.Data.get('Facilidade', 'Não avaliado')}")
        print(f"Dúvidas sem Solução:")
        if self.Data["ListaSemSolucoes"]:
            for I in self.Data["ListaSemSolucoes"]:
                print(f"> {I}")
        else:
            print("> Nenhuma dúvida sem solução registrada.")

    def exportar_csv(self):
        with open("data/historico.json", "r", encoding="utf-8") as JSON:
            Data = json.load(JSON)

        Header = Data[0].keys()

        with open('data/atendimentos.csv', "w", newline="",encoding="utf-8") as CSV:
            Controlador = csv.DictWriter(CSV, fieldnames=Header)
            Controlador.writeheader()
            Controlador.writerows(Data)
            