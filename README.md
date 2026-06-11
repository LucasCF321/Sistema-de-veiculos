# Sistema-de-veiculos
# Resumo do Sistema de Cadastro de Veículos

Este programa foi desenvolvido em Python utilizando a biblioteca Tkinter para criar uma interface gráfica e o Psycopg2 para realizar a conexão com um banco de dados PostgreSQL.

## Funcionalidades

### Conexão com o Banco de Dados

A função `conectar()` estabelece a conexão com o banco PostgreSQL utilizando as credenciais configuradas no código.

### Cadastro de Veículos

A função `salvar()` permite inserir informações de um veículo (marca, modelo, ano, cor e preço) na tabela `veiculo` do banco de dados. Além disso, os dados também são armazenados em um arquivo de texto chamado `veiculo.txt`.

### Pesquisa de Veículos

A função `pesquisar()` consulta todos os registros da tabela `veiculo` e exibe os resultados na área de texto da interface gráfica.

### Exclusão de Veículos

A função `excluir()` remove um veículo do banco de dados com base no ID informado pelo usuário.

### Atualização de Dados

A função `alterar()` permite modificar as informações de um veículo já cadastrado utilizando seu ID como referência.

## Interface Gráfica

A interface foi construída com Tkinter e contém:

* Campos para inserção de ID, marca, modelo, ano, cor e preço.
* Botões para salvar, pesquisar, excluir e alterar registros.
* Uma área de texto para exibição dos resultados das consultas.

## Objetivo

O sistema tem como objetivo facilitar o gerenciamento de veículos por meio de operações básicas de cadastro, consulta, atualização e exclusão (CRUD), integrando uma interface amigável com um banco de dados PostgreSQL.

