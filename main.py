"""
    INTEGRANTES

    - Temitope Kuku da Silva Ogunbanjo (RM: 573772 )
    - Gustavo de Souza Abreu (RM : 574080)
    - Gabriel Oliveira Gusmãos Florencio dos Santos (RM: 573747)
"""
from base_conhecimento import BaseConhecimento
from assistente import Assistente

flag = True

base = BaseConhecimento('data/base_conhecimento.json')
base.Carregar()

assistente = Assistente("Assistente Eleitoral", base)

def Header():
    print("==" * 50)
    print(f"Olá, sou o assistente {assistente.nome}. Embora não seja um canal oficial, posso responder as suas principais dúvidas sobre a votação eleitoral para jovens e adolescentes!")
    print("\n")

def Opcoes():
    print(">>  1 - Fazer uma Pergunta")
    print(">>  2 - Navegar as Categorias")
    print(">> 3 - Encerrar o programa")
    print("\n")

def Categorias():
    Contador = 0

    print("==" * 50)
    print(">> Atualmente, respondo perguntas relacionadas aos temas:")
    print("\n")

    for I in assistente.base.CategoriasAtendidas:
        Contador += 1 
        print(f"> 1. {I}") 

    print("\n")
    
def Lock(Texto, Range):
    while True:
        Resultado = input(Texto).strip()
        if Resultado.isdigit():
            Valor = int(Resultado)
            if Range[0] <= Valor <= Range[1]:
                return Valor
        print(f"[!] Opção inválida. Digite um número entre {Range[0]} e {Range[1]}.")

def MenuCategorias():

    while True:
        Categorias()

        Acao = Lock("\n Escolha o número da categoria (ou 0 para Voltar): ", [0, len(assistente.base.CategoriasAtendidas)])

        if Acao == 0:
            break
        else:
            Categoria = assistente.base.CategoriasAtendidas[Acao - 1]
            assistente.navegar(Categoria)

Header()

while flag:
    Opcoes()
    Acao = Lock("Escolha a sua opção: ", [1, 3])

    match Acao:
        case 1:
            print("\n(Digite 'voltar' ou '0' a qualquer momento para retornar ao menu)")
            assistente.perguntar()
        case 2:
            MenuCategorias()
        case 3:
            print("\n")
            Facilidade = Lock("Para finalizar | Digite a Nota de facilidade de uso do assistente (1 a 5): ", [1,5])
            print("\n")
            assistente.Data["Facilidade"] = Facilidade

            assistente.indicadores()
            assistente.exportar_csv()

            print("\nEncerrando o programa. Até logo!")
            break

    