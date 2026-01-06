import functions
import database

def user_action(task_item):
    match task_item:

        #Adicionar tarefa - OK
        case 1:
            print("Escreva o nome da sua tarefa:")
            task_name = input()
            
            is_user_item_valid = functions.v_create_task(task_name)

            try:
                if is_user_item_valid:
                    database.create_task(task_name,0)
            except Exception as e:
                print(e)

        #Remove uma das tarefas - OK
        case 2:
            print("Qual tarefa voce deseja remover?")

            try:
                database.show_all_tasks()
            except Exception as e:
                print("Erro em mostrar todas as tarefas")
                print(e)

            delete_task_number = int(input())

            is_delete_task_number_valid = functions.v_user_action(delete_task_number)

            try:
                if is_delete_task_number_valid:
                    database.delete_task(delete_task_number)
            except Exception as e:
                print("Erro com verificação de tarefa a ser deletada")
                print(e)

        #Lista todas as tarefas - OK
        case 3:
            print("Estas são suas tarefas:")
            try:
                database.show_all_tasks()
                print("\n")
            except Exception as e:
                print("Erro em mostrar todas as tarefas")
                print(e)

        #Muda o status da tarefa para feito
        case 4:
            print("Qual tarefa você deseja marcar como concluída?")
            database.show_all_tasks()
            print("\n")

            change_task_status = int(input())

            is_change_task_status_valid = functions.v_user_action(change_task_status)

            try:
                if is_change_task_status_valid:
                    database.change_task_status(change_task_status)
            except Exception as e:
                print("Erro com tarefa a mudar status")
                print(e)

        case None:
            print("Escolha uma das opções diposníveis")
            user_action(task_item)
        
        case _:
            print("Escolha uma das opções diposníveis")
            user_action(task_item)

def main():

    #Verifica se o DB existe e se esta funcional
    try:
        database.initialize_database()
    except Exception as e:
        print("Erro ao acessar o banco de dados")
        print(e)

    #Início do Programa
    #Casos da escolha do que fazer
    print("Bem vindo a sua lista de tarefas:\n" \
          "O que deseja fazer:\n\n" \
            "1- Adicionar tarefa \n" \
            "2- Excluir tarefa \n" \
            "3- Listar todas as tarefas\n" \
            "4- Marcar tarefa como concluída\n")

    action = int(input())

    is_user_action_valid = functions.v_user_action(action)

    try:
        if is_user_action_valid:
            user_action(action)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()