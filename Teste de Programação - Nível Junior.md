<h1 align="center">Teste de Programação - Nível Junior</h1>

<p align="center"><i>Aplicação: Controle de Abastecimentos</i></p>

![Static Badge](https://img.shields.io/badge/python-blue)
![Static Badge](https://img.shields.io/badge/orm-django-3fb950)

## Descrição Geral

  Você foi contratado para analisar e desenvolver um software para gerenciar os abastecimentos e tanques de combustíveis do posto ABC. 
  
  O gerente do posto forneceu as seguintes informações e requisitos:

- ### 1 - Requisitos Funcionais
    #### 1.1 - Registro de Abastecimentos:

    Controle dos abastecimentos feitos durante cada dia.
   
    Identificação da bomba utilizada, quantidade de litros e valor abastecido.

    Registro do imposto de 13% sobre o valor abastecido.

    #### 1.2 - Estrutura dos Tanques e Bombas:
    
    O posto ABC possui dois tanques: um de gasolina e um de óleo diesel.
    
    Cada tanque possui duas bombas de combustível associadas.

    #### 1.3 - Relatórios (Opcional):

    Relatório de abastecimentos agrupados por dia, tanque, bomba e valor.
    
    Exibição da soma total do período no relatório.

- ### 2 - Requisitos Não Funcionais
    #### 2.1 - Boas Práticas:
    
    Utilize boas práticas de desenvolvimento e padrões de código limpo.

    Utilize o Git para controle de versão e publique o projeto no GitHub.

    #### 2.2 - Testes (Opcional):
    
    Crie testes unitários e/ou funcionais para a aplicação.

    #### 2.3 - Tecnologia:
    
    Utilize Python e Django.

## Instruções para Entrega

- ### 1 - Configuração do Ambiente:
  Crie um repositório no GitHub e configure o projeto Django com um ambiente virtual.
  
  Adicione as dependências necessárias no arquivo requirements.txt.

- ### 2 - Modelagem do Banco de Dados:
  Crie modelos Django para representar tanques, bombas e abastecimentos.
  
  Defina as relações apropriadas entre os modelos.

- ### 3 - Funcionalidades:
  Implemente a lógica para registrar os abastecimentos com os detalhes necessários.
  
  Calcule e registre o imposto de 13% sobre o valor abastecido.

- ### 4 - Relatórios (Opcional):
  Implemente a funcionalidade para gerar relatórios em PDF utilizando o PyPDF.
  
  Os relatórios devem ser agrupados por dia, tanque, bomba e valor, com a soma total do período.

- ### 5 - Testes (Opcional):
  Crie testes unitários para validar a lógica dos modelos e das funcionalidades.

  Crie testes funcionais para verificar a usabilidade da aplicação.

- ### 6 - Publicação no GitHub:
  Suba o projeto em um repositório público no GitHub.

  Inclua um arquivo README.md com instruções claras sobre como configurar e rodar a aplicação.