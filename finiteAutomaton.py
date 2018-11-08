# Preenche tapes com valores do arquivo
def get_tapes(tapes, config):
    valide_value = config[1]
    valide_value = valide_value + config[3]
    for i in tapes:
        if i not in valide_value:
            print ("-3: Valor inserido na fita incorreto")
            return -3
    return tapes

def machine(config, tapes, transitions):
    # Cria fila para controle do fluxo
    q = []
    tape = get_tapes(tapes, config)

    if (tape == -1): # Valores inválidos na fita
        return -1
    
    # Configurações da máquina
    setting = {
        "tape": tape,
        "current_state": config[5][0],
        "head_tape": 0,
        "counter": 5000 # Contador que 'verifica' looping
    }
    
    # Insere elemento no final da fila
    q.append(setting)

    while True:
        tape = setting['tape']
        
        # Encontrou estado final
        if (q[0]['current_state'] in config[6]):
            print ("0: Computação terminada e aceita.")
            print (setting)
            return 0
            
        # Se a máquina estiver em looping
        if (q[0]['counter'] == 0):
            print (setting)
            while True:
                x = input("Máquina alcançou 500 transições. Deseja continuar? (s - Sim | n - Não): ")
                
                if(x == 'n'):
                    print ("-2: Computação não terminada. (interrupção por looping)")
                    return -2
                
                elif(x == 's'):
                    q[0]['counter'] = 5000
                    break

        # Pega posição da fita na configuração atual
        head = q[0]['head_tape']

        # Encontra transições possíveis
        for i in range(1, len(transitions) + 1, 1):
            # Se estado_atual_maquina == estado_atual_fita e letra_fita == letra_transicao
            if ((q[0]['current_state'] == transitions[i][0]) and (tape[head] == transitions[i][2])):
                # Nova disposição da fita
                new_tape = tape
                # -> Troca letra_fita por nova_letra_transicao
                if (head > 0):
                    new_tape = (tape[0:head] + transitions[i][3]) + tape[head + 1:]
                else:
                    new_tape = transitions[i][3] + tape[head + 1:]

                # Nova posição da head da fita
                new_head_tape = head
                if (transitions[i][4] == 'R'):
                    # Adiciona espaço em branco no final da tape
                    if (new_head_tape == len(new_tape) - 1):
                        new_tape = (new_tape) + config[3][0]
                    
                    new_head_tape = new_head_tape + 1 # Moveu para direita
                elif (transitions[i][4] == 'L'):
                    # Adiciona espaço em branco no início da tape
                    if (new_head_tape == 0):
                        new_tape = config[3][0] + (new_tape)
                        new_head_tape += 1
                    
                    new_head_tape = new_head_tape - 1 # Moveu para esquerda
                else:
                    new_head_tape = new_head_tape # Mantêm na mesma posição

                new_setting = {
                    "tape": new_tape,
                    "current_state": transitions[i][1],
                    "head_tape": new_head_tape,
                    "counter": q[0]['counter'] - 1
                }

                q.append(new_setting) # Insere no final da fila
        
        # Encerrou as opções possíveis e não encontrou estado final
        if (len(q) == 1): # q só tem q[0]
            print ("-1: Computação terminada e rejeitada.")
            print (setting)
            return -1
        
        # Configura máquina para próximo estado
        setting['tape'] = q[1]['tape']
        setting['current_state'] = q[1]['current_state']
        setting['head_tape'] = q[1]['head_tape']
        setting['counter'] = q[1]['counter']
        q.pop(0) # Tira estado atual da fila

