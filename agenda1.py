def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal=='s':

        opcao= input('''
    ==================================
    Agenda em python 
    Menu: 
    [1] Cadastrar contato
    [2] Listar contato
    [3] Deletar contato
    [4] Buscar contato
    Ou digite qualquer outra tecla para sair.
    ===================================
    Escolha uma opção acima: ''')
        if opcao == '1':
            cadastra_contato()
        elif opcao == '2':
            listar_contato()
        elif opcao == '3':
            del_contato()
        elif opcao == '4':
            buscar_contato()
        else:
            sair()
        voltarMenuPrincipal=input('Deseja voltar ao menu? (s/n)').lower()

def cadastra_contato():
    id = input('Digite o ID do contato: ')
    nome = input('Digite o nome do contato: ')
    numero = input('Digite o número do contato: ')
    email = input('Digite o email do contato: ')
    try:
        agenda = open('agenda1.txt','a')
        dados = f'{id};{nome};{numero};{email} \n'
        agenda.write(dados)
        agenda.close()
        print('Contato gravado com sucesso!')
    except:
        print('O contato não foi gravado, tente novamente')

def listar_contato():
    agenda = open('agenda1.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()


def del_contato():
    nomeDel = input('Quem você quer deletar? ')
    agenda = open('agenda1.txt','r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDel not in aux[i]:
            aux2.append(aux[i])
    agenda = open('agenda1.txt','w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listar_contato()




def buscar_contato():
    nome=input(f'Digite o nome a ser procurado: ').upper()
    agenda = open('agenda1.txt','r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)
        if nome not in contato.split(';')[1].upper():
            print('Este contato não existe na agenda.')

    agenda.close()

def sair():
    print('Até mais!')
    exit()





def main():
    menu()
main()