import functions
import database

def user_action(task_item):
    match task_item:

        #Adicionar tarefa
        case 1:
            print("Escreva o nome da sua tarefa:")
            task_name = input()
            
            is_user_item_valid = functions.v_create_task(task_name)

            try:
                if is_user_item_valid:
                    print(database.create_task(task_name,0))
            except Exception as e:
                #Somente para Debug
                print("Erro no user_action")
                print(e)

        #Remove uma das tarefas
        case 2:
            print("Tem que fazer ainda - 1")

        #Lista todas as tarefas
        case 3:
            print("Tem que fazer ainda - 2")

        case None:
            print("Escolha somente uma das opções diposníveis")
            user_action(task_item)
        
        case _:
            print("Escolha somente uma das opções diposníveis")
            user_action(task_item)

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

    action = int(input())

    is_user_action_valid = functions.v_user_action(action)

    try:
        if is_user_action_valid:
            user_action(action)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()