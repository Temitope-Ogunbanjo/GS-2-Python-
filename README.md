# Assistente Eleitoral para Jovens

Assistente digital de terminal desenvolvido em Python para orientar jovens que estão participando de sua primeira eleição. O sistema responde dúvidas em linguagem simples com base em informações verificadas do Tribunal Superior Eleitoral (TSE), sem coletar dados pessoais.

**Disciplina:** Pensamento Computacional e Automação com Python (FIAP - GS 2026.2)

---

## 👥 Integrantes da Equipe

* **Temitope Kuku da Silva Ogunbanjo** — RM: 573772
* **Gustavo de Souza Abreu** — RM: 574080
* **Gabriel Oliveira Gusmãos Florencio dos Santos** — RM: 573747

---

## 🎯 Público-Alvo e Problema Escolhido

* **Público:** Jovens (faixa etária de 16 a 20 anos) votando pela primeira vez.
* **Problema e Motivação:** Com a realização recente das eleições presidenciais, grande parte dos estudantes na faixa de 18 a 20 anos enfrentou sua primeira participação obrigatória nas urnas. O projeto busca centralizar orientações práticas sobre emissão do título, uso do aplicativo e-Título, regras da cabine de votação e regularização em caso de ausência, combatendo a desinformação e facilitando o acesso aos serviços eleitorais.
* **ODS Relacionado:** **ODS 16** (Paz, Justiça e Instituições Eficazes) — promovendo o acesso público à informação e o fortalecimento da participação cidadã.

---

## ⚙️ Estrutura do Projeto e Bibliotecas

O sistema foi modularizado utilizando Programação Orientada a Objetos (POO) e apenas bibliotecas nativas do Python:

* `json`, `csv`, `os`: Leitura da base de conhecimento, persistência do histórico de atendimentos e exportação de relatórios.
* `re`, `string`: Normalização de textos (remoção de acentos e pontuações) e regras de bloqueio de dados pessoais (*guardrails*).
* `datetime`, `time`: Registro da data dos atendimentos e cálculo do tempo de resposta.

### Arquivos Principais
```text
citizen-assist-ai/
├── main.py                  # Menu interativo, controle de fluxo e validação de entradas
├── assistente.py            # Lógica de atendimento, guardrails, histórico e indicadores
├── base_conhecimento.py     # Carregamento do JSON, categorização e motor de busca
├── orientacao.py            # Classe modelo para exibição formatada das orientações
└── data/
    ├── base_conhecimento.json
    ├── historico.json
    └── atendimentos.csv
```

## 🧠 Regra de Pontuação e Busca

Como o assistente opera por regras determinísticas (sem uso de LLMs), as perguntas e os registros da base passam por uma função de normalização (letras minúsculas, sem acentos e sem pontuação) e são avaliados da seguinte forma:

* **+3 pontos** para cada `palavra_chave` da orientação encontrada na pergunta do usuário.
* **+1 ponto** para cada palavra da pergunta (com mais de 4 letras) presente no `titulo` da orientação.

### Classificação de Confiança
* **6 pontos ou mais:** Confiança **ALTA** (exibe a orientação completa).
* **3 a 5 pontos:** Confiança **MÉDIA** (exibe a orientação encontrada).
* **Menos de 3 pontos:** Confiança **BAIXA** (informa que não encontrou resposta exata e sugere categorias/palavras-chave).

---

## 🧪 Testes com Usuários e Evolução da Base

Inicialmente, a base foi estruturada com **15 orientações** divididas em **3 categorias** (*Cadastro e Título de Eleitor*, *Preparação e Dia da Votação* e *Urna, Regras e Pós-Eleição*).

### Dúvidas Sem Solução Identificadas nos Testes
Durante os testes práticos com usuários reais, percebemos que perguntas formuladas de maneira mais coloquial ou específicas do cotidiano não atingiam a pontuação mínima por dependerem de termos técnicos exatos. Exemplos registrados:
* *"Tenho 16 anos e não votei. Precisa justificar?"*
* *"Quem não votou pode fazer faculdade?"*
* *"Posso votar usando camisa do Bolsonaro ou Lula?"*
* *"O que acontece se não votar e tiver mais de 18?"*

### Melhorias Aplicadas
* **Expansão da base de conhecimento (`id: 16` em diante):** Inclusão de orientações cobrindo dúvidas reais sobre justificativa pós-eleição, impedimentos acadêmicos/civis por falta de quitação eleitoral e regras sobre vestimenta/manifestação silenciosa.
* **Ampliação de `palavras_chave`:** Adição de variações nos registros existentes para aumentar a taxa de acerto em buscas em linguagem natural.

---

## ⚠️ Limitações do Sistema

* **Dependência Léxica:** Por não utilizar processamento semântico ou embeddings (LLMs), sinônimos não mapeados nas palavras-chave ou erros graves de digitação podem reduzir a pontuação da busca.
* **Caráter Informativo:** O assistente não substitui os canais oficiais da Justiça Eleitoral e exibe avisos de limitação em todas as respostas.

---

## 📚 Fontes Consultadas

* **Tribunal Superior Eleitoral (TSE):** [https://www.tse.jus.br](https://www.tse.jus.br) (Autoatendimento Eleitoral, e-Título e Justificativa).
* **Mapeamento de Dúvidas Frequentes dos Jovens:** Levantamento baseado em discussões reais de eleitores em fóruns (Reddit, X, YouTube) e [matérias informativas do portal **G1**](https://g1.globo.com/politica/eleicoes/2026/noticia/2026/08/07/eleicoes-2026-com-que-idade-e-obrigatorio-votar.ghtml) sobre regras do dia da votação.

---

## 🎥 Vídeo Técnico

* **Link da apresentação no YouTube:** `[INSERIR LINK DO YOUTUBE AQUI]`


