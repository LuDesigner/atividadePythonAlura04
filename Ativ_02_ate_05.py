import os

def exibir_nome():
    print("""
████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄─▄─██▀▄─██▄─██─▄█▄─▄▄▀██▀▄─██▄─▀█▄─▄█─▄─▄─█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─▄█▀█▄▄▄▄─███─████─▀─███─██─███─▄─▄██─▀─███─█▄▀─████─████─▄█▀█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

class Restaurantes_Cadastrados:
    restaurante = []

    def __init__(self, nome, categoria, nota, status, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.nota = nota
        self.status = status
        self.ativo = ativo
        Restaurantes_Cadastrados.restaurante.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.nota} | {self.status} | {self.ativo}'

    def listar_restaurantes():
        for list_restaurantes in Restaurantes_Cadastrados.restaurante:
            print(f'{list_restaurantes.nome} | {list_restaurantes.categoria} | {list_restaurantes.nota} | {list_restaurantes.status} | {list_restaurantes.ativo}')
 
def informacoes_restaurantes():
    print(f"""\n
{''.ljust(30)}𝓛𝓲𝓼𝓽𝓪 𝓭𝓮 𝓡𝓮𝓼𝓽𝓪𝓾𝓻𝓪𝓷𝓽𝓮𝓼{''.ljust(30)}
\n""")
    print(f'{'Restaurantes'}{''.ljust(3)} | {'Categoria'}{''.ljust(1)} | {''.ljust(8)}{'Nota'}{''.ljust(8)} | {''.ljust(3)}{'Status'}{''.ljust(3)} | {''.ljust(3)}{'Delivery'}{''.ljust(3)}\n' )
    restaurante_01 = Restaurantes_Cadastrados('Hot-Dog da tia'.ljust(15), 'Hot-Dog'.ljust(10), 'Nota - 9'.ljust(20), 'Ativo'.ljust(12), True)
    restaurante_02 = Restaurantes_Cadastrados('Batata Show'.ljust(15), 'Burguer'.ljust(10), 'Nota - 10'.ljust(20), 'Inativo'.ljust(12), False)

    Restaurantes_Cadastrados.listar_restaurantes()

class Clientes_Cadastrados:
    restaurante = []

    def __init__(self, nome, idade, email, telefone, ativo=False):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.ativo = ativo
        Clientes_Cadastrados.restaurante.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone} | {self.ativo}'

    def listar_clientes():
        for list_restaurantes in Clientes_Cadastrados.restaurante:
            print(f'{list_restaurantes.nome} | {list_restaurantes.idade} | {list_restaurantes.email} | {list_restaurantes.telefone} | {list_restaurantes.ativo}')
 
def informacoes_clientes():
    print(f"""\n
{''.ljust(30)}𝓛𝓲𝓼𝓽𝓪 𝓭𝓮 𝓬𝓵𝓲𝓮𝓷𝓽𝓮𝓼{''.ljust(30)}
\n""")
    print(f'\n{''.ljust(4)}{'Clientes'}{''.ljust(4)} | {''.ljust(3)}{'Idade'}{''.ljust(3)} | {''.ljust(7)}{'E-mail'}{''.ljust(7)} | {''.ljust(3)}{'Telefone'}{''.ljust(2)} | {''.ljust(3)}{'Status'}{''.ljust(3)}\n' )
    restaurante_01 = Clientes_Cadastrados('Maria'.ljust(16), '75 Anos'.ljust(11), 'maria@maria.com'.ljust(20), '(00)0000-0000'.ljust(12), True)
    restaurante_02 = Clientes_Cadastrados('Carlinhos'.ljust(16), '32 Anos'.ljust(11), 'carlos@gmail.com'.ljust(20), '(00)0000-0000'.ljust(12), False)

    Clientes_Cadastrados.listar_clientes()

def main():
    os.system('cls')
    exibir_nome()
    informacoes_restaurantes()
    informacoes_clientes()

if __name__ == '__main__':
    main()