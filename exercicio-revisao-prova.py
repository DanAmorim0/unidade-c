"""
Exercício Revisão I: Sistema de Gerenciamento de Livros
Considere um sistema de gerenciamento de livros com uma tabela livros que tem os seguintes campos:

id (Chave Primária, Integer)
titulo (Texto)
autor (Texto)
ano_publicacao (Integer)

Você deve criar uma aplicação via terminal para gerenciar essa biblioteca.  Você deve atentar para o seguinte:
@@@ Criar o banco de dados:

Nome do banco de dados: biblioteca.db

@@@ Criar a tabela livros:

Campos: id (autoincremento), titulo (texto), autor (texto), ano_publicacao (inteiro)

@@@ Inserir alguns livros na tabela:

Inserir pelo menos 3 livros diferentes com informações fictícias.
Permitir que o usuário insira novos títulos

@@@ Consultar todos os livros:

Selecionar e exibir todos os livros presentes na tabela.

@@@ Remover livro

O usuário poderá remover um livro da lista

Seu sistema deverá ser operado no terminal e deverá conter um menu em loop

"""

import sqlite3

def criar_banco_dados():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_livro(titulo, autor, ano_publicacao):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    conexao.commit()
    conexao.close()

def consultar_livros():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT * FROM livros
    ''')

    livros = cursor.fetchall()

    if livros:
        print("\n=== Livros na Biblioteca ===")
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano de Publicação: {livro[3]}")
    else:
        print("Não há livros na biblioteca.")

    conexao.close()

def remover_livro(livro_id):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM livros WHERE id = ?
    ''', (livro_id,))

    conexao.commit()
    conexao.close()

def main():
    criar_banco_dados()

    while True:
        print("\n======= MENU =======")
        print("1. Inserir Livro")
        print("2. Consultar Livros")
        print("3. Remover Livro")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")

            try:
                ano_publicacao = int(ano_publicacao)
                inserir_livro(titulo, autor, ano_publicacao)
                print("Livro inserido com sucesso!")
            except ValueError:
                print("Ano de publicação deve ser um número inteiro. Tente novamente.")

        elif opcao == '2':
            consultar_livros()

        elif opcao == '3':
            livro_id = input("Digite o ID do livro que deseja remover: ")

            try:
                livro_id = int(livro_id)
                remover_livro(livro_id)
                print("Livro removido com sucesso!")
            except ValueError:
                print("ID do livro deve ser um número inteiro. Tente novamente.")

        elif opcao == '4':
            print("Encerrando o Sistema de Gerenciamento de Livros. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
