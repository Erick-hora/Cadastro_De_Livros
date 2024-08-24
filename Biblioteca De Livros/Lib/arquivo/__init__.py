from Lib.interface import *

def cria_arquivo(n):
    try:
        a = open(n, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar um arquivo')
    else:
        print(f'Arquivo {n} Criado com sucesso')


def arquivo_existe(n):
    try:
        a = open(n, 'rt')
        a.close()
    except FileNotFoundError:
        return 0
    else:
        return 1


def ler_arquivo(n):
    a = None
    try:
        a = open(n, 'rt')
    except:
        print('Problema na leitura do arquivo')
    else:
        cabecalho('Livros cadastrados')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{"Autor(a)"} {dado[1]:<10}')
    finally:
        a.close()


def cadastra_livro(n, l='Desconhecido', a='Desconhecido'):
    try:
        n = open(n, 'at')
    except:
        print('Houve um problema durante do cadastro')
    else:
        try:
            n.write(f'{l};{a}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'O registro de {l} foi feito com sucesso')