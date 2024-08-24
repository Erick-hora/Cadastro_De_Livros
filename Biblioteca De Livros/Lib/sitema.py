from Lib.arquivo import *
from time import sleep

arq = 'Biblioteca.txt'

if not arquivo_existe(arq):
    cria_arquivo(arq)


while True:
    op = menu(['Verificar Livros', 'Cadastrar Livro', 'Sair'])
    sleep(0.5)
    if op == 1:
        ler_arquivo(arq)
    elif op == 2:
        cabecalho('Cadastro de livro')
        l = str(input('Digite o nome do livro: ')).strip()
        a = str(input('Digite o nome do autor(a): ')).strip()
        cadastra_livro(arq, l, a)
    elif op == 3:
        cabecalho('Fechando o sistema... até logo')
        break
    else:
        print('\033[0;31mDigite uma opção válida!\033[m')
