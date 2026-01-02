import functions
import database

def user_action(task_item):
    match task_item:

        #Adicionar tarefa
        case 1:
            print("Escreva o nome da sua tarefa:")
            task_name = input()
            
            functions.v_create_task(task_name)

        #Remove uma das tarefas
        case 2:
            print("Tem que fazer ainda - 1")

        #Lista todas as tarefas
        case 3:
            print("Tem que fazer ainda - 2")

        case _:
            print("Escolha somente uma das opções diposníveis")

def main():

    #Verifica se o DB existe e se esta funcional
    try:
        database.initialize_database()
        print("Banco de Dados Inicializado")
    except Exception as e:
        print("Erro ao acessar o banco de dados")

    #Início do Programa
    #Casos da escolha do que fazer
    print("O que deseja fazer: \n\n" \
            "1- Adicionar tarefa \n" \
            "2- Excluir tarefa \n" \
            "3- Listar todas as tarefas")

    action = input()

    user_action(int(action))

if __name__ == "__main__":
    main()