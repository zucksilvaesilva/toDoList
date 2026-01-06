def v_user_action(action):
    #Verifica se não é vazio
    if action is None:
        print("Selecione uma das opções válidas. ")
        print(type(action))
        return False

    #Verifica se é um número
    elif type(action) == str:
        print("Selecione uma das opções válidas ")
        print(type(action))
        return False
    
    #Estando tudo certo, prossegue
    else: 
        return True
    
def v_create_task(name):

    #Verifica se não é vazio
    if name is None:
        print("Sua tarefa não pode ser nula.")
        return False

    clean_task = name.strip()
    
    if not clean_task:
        print("Sua tarefa não pode ser vazia")
        return False

    #Verifica caracteres mínimos
    elif len(clean_task) < 3:
        print("Sua tarefa é muito curta")
        return False
    
    #Estando tudo certo, prossegue
    else: 
        return True

def v_delete_task(id):
    pass

def v_conclude_task(id):
    pass