def leiaint(msg):
    while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('\033[0;31mHouve um problema com os valores informados\033[m')
            except KeyboardInterrupt:
                print('\033[0;31mO usuário preferiu não digitar a opção\033[m\n')
                return 3
            else:
                return n


def linha(tam=42):
    return ('=' * tam)


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista, msg='Menu'):
    cabecalho(msg)
    c = 1
    for op in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{op}\033[m')
        c += 1
    print(linha())
    resp = leiaint('\033[0;32mDigite sua opção: \033[m')
    return resp

