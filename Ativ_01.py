import os

def exibir_nome_do_programa():
    print("""
████████████████████████████████████████████████████████████████████████████████
█▄─▄███▄─▄█─▄▄▄▄█─▄─▄─██▀▄─████▄─▄▄▀█▄─▄▄─███─▄▄▄─██▀▄─██▄─▄▄▀█▄─▄▄▀█─▄▄─█─▄▄▄▄█
██─██▀██─██▄▄▄▄─███─████─▀─█████─██─██─▄█▀███─███▀██─▀─███─▄─▄██─▄─▄█─██─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀
""")

class Carros_Cadastrados:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carros_Cadastrados.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    def listar_carros():
        for list_carros in Carros_Cadastrados.carros:
            print(f'{list_carros.modelo} | {list_carros.cor} | {list_carros.ano}')

def mod_texto(texto):   
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'\n {texto} \n')
    print(linha)
    print()

def informacoes():
    #mod_texto('Modelos de Carros cadastrados')
    print(f'{''.ljust(3)}{'Modelo do carro'}{''.ljust(3)} | {''.ljust(4)}{'Cor do carro'}{''.ljust(4)} | {''.ljust(3)}{'Ano do carro'}{''.ljust(3)}\n' )
    carro_01 = Carros_Cadastrados('Fusca'.ljust(21), 'Azul'.ljust(20), 1959)
    carro_02 = Carros_Cadastrados('Fusca'.ljust(21), 'Preto'.ljust(20), 1959)

    Carros_Cadastrados.listar_carros()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    informacoes()

if __name__ == '__main__':
    main()