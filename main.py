import redis

db = redis.StrictRedis(host='localhost', port=6379, db=0)

def inserirAtividade(atvd):
    db.rpush('lista', atvd)

def listarAtividades():
    return db.lrange('lista', 0, -1)

def excluirAtividade(indice):
    atvd = db.lindex('lista', indice)
    db.lrem('lista', 0, atvd)

def listarMenu():
    print('----- Menu -----')
    print('1- Inserir atividade')
    print('2- Listar atividades')
    print('3- Excluir atividade')
    print('4- Sair')

opcao = 0
while opcao != 4:
    print('')
    listarMenu()
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            atividade = input('Informe a atividade a ser inserida: ')
            inserirAtividade(atividade)
        case 2:    
            atividades = listarAtividades()  
            for indice, atividade in enumerate(atividades):
                print(f"{indice} - {atividade.decode('utf-8')}")
        case 3:
            indice = input('Informe o índice a ser excluido: ')
            excluirAtividade(indice)
        case 4:
            print('Saindo...')
        case _:
            print('Opção inválida!')