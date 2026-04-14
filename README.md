🏭 Sistema de Gestão de Peças, Qualidade e Armazenamento
Descrição
Sistema desenvolvido em Python para automação do controle de qualidade de peças industriais. O programa recebe os dados de cada peça produzida, avalia automaticamente se ela atende aos critérios de qualidade, armazena as peças aprovadas em caixas com capacidade limitada e gera relatórios consolidados de produção.
Critérios de Qualidade
Uma peça é aprovada somente se atender a todos os critérios abaixo:
Critério	Valor Aceito
Peso	Entre 95g e 105g
Cor	Azul ou Verde
Comprimento	Entre 10cm e 20cm
Caso a peça falhe em qualquer critério, ela é reprovada e o sistema informa o motivo.
Funcionalidades (Menu Interativo)
Cadastrar nova peça — Insere uma peça com ID, peso, cor e comprimento. O sistema avalia e classifica automaticamente.
Listar peças aprovadas/reprovadas — Exibe todas as peças cadastradas separadas por status.
Remover peça cadastrada — Remove uma peça pelo ID.
Listar caixas fechadas — Mostra as caixas que atingiram 10 peças e a caixa atual.
Gerar relatório final — Exibe totais de aprovadas, reprovadas (com motivos) e caixas utilizadas.
Como Rodar o Programa
Pré-requisitos
Python 3.6 ou superior instalado (Download)
Passo a passo
Clone o repositório:
```bash
   git clone https://github.com/seu-usuario/sistema-qualidade-pecas.git
   cd sistema-qualidade-pecas
   ```
Execute o programa:
```bash
   python sistema_qualidade.py
   ```
O menu interativo será exibido no terminal. Digite o número da opção desejada.
Exemplos de Entradas e Saídas
Cadastro de peça aprovada
```
   ID da peça: P001
   Peso (g): 100
   Cor: azul
   Comprimento (cm): 15

   ✅ Peça 'P001' APROVADA!
   ✅ Peça adicionada à caixa atual (1/10)
```
Cadastro de peça reprovada
```
   ID da peça: P002
   Peso (g): 80
   Cor: vermelho
   Comprimento (cm): 25

   ❌ Peça 'P002' REPROVADA!
      - Peso fora do padrão (80.0g - esperado: 95g a 105g)
      - Cor inválida (vermelho - esperado: azul ou verde)
      - Comprimento fora do padrão (25.0cm - esperado: 10cm a 20cm)
```
Relatório final
```
   Total de peças cadastradas: 12
   ✅ Aprovadas: 10
   ❌ Reprovadas: 2

   📦 Caixas fechadas: 1
   📂 Caixa atual: 0/10 peças
   📊 Total de caixas utilizadas: 1
```
Tecnologias Utilizadas
Python 3
Estruturas de dados: listas e dicionários
Funções com parâmetros e retorno
Estruturas condicionais (if/elif/else)
Estruturas de repetição (while/for)
Tratamento de exceções (try/except)
Autor
Desenvolvido como trabalho da disciplina de Algoritmos e Lógica de Programação — UniFECAF.
