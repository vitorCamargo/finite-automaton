# Linha 1: alfabeto de entrada
# Linha 2: simbolo a ser considerado para representar epsilon ou lambda (não deve pertencer ao alfabeto de entrada)
# Lista 3: conjunto de estados
# Linha 4: estado inicial
# Linha 5: conjunto de estados de aceitação
# Linhas 6 em diante: transicoes, uma por linha, cada qual no seguinte formato: estado atual, simbolo do alfabeto de entrada ou epsilon, estado destino

# return -1 = computação termianda e não aceita
# return -2 = computação interrompida por loop
# return -3 = palavra com alfabeto fora do esperado

# Preenche word com valores do arquivo
def valid_word(word, config):
    valide_value = config[1] + config[2]

    for i in word:
        if i not in valide_value:
            print ("-3: Valor inserido na palavra incorreto")
            return -3
        
    # Remove epsilons da palavra
    i = 0
    while (i < len(word)):
        if (word[i] == config[2][0]):
            word = word[:i] + word[i + 1:]
            i -= 1
        i += 1

    return word

def machine(config, word, transitions):
    # Cria fila para controle do fluxo
    q = []
    word = valid_word(word, config)
    
    if (word == -3): # Valores inválidos na palavra
        return -3
    
    # Configurações da máquina
    setting = {
        "current_state": config[4][0],
        "head_word": 0,
        "counter": 5000 # Contador que 'verifica' looping
    }
    
    # Insere elemento no final da fila
    q.append(setting)

    while True:        
        # Encontrou estado final
        if ((q[0]['current_state'] in config[5]) and (q[0]['head_word'] == len(word))):
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

        # Pega posição da palavra na configuração atual
        head = q[0]['head_word']

        # Encontra transições possíveis
        for i in range(1, len(transitions) + 1):
            # Se estado_atual_maquina == estado_atual_fita e (simbolo_atual == ε ou simbolo_atual == simbolo_transicao)
            if ((transitions[i][1] != config[2][0]) and (len(word) <= q[0]['head_word'])):
                break
            elif ((q[0]['current_state'] == transitions[i][0]) and
                ((transitions[i][1] == config[2][0]) or (word[head] == transitions[i][1]))):

                # Nova posição da head da fita
                new_head_word = head

                # Se transição é diferente de ε, vai para próximo símbolo
                if ((transitions[i][1] != config[2][0]) or (word[head] == config[2][0])):
                    new_head_word += 1 # Moveu para direita

                new_setting = {
                    "current_state": transitions[i][2],
                    "head_word": new_head_word,
                    "counter": q[0]['counter'] - 1
                }

                q.append(new_setting) # Insere no final da fila
        
        # Encerrou as opções possíveis e não encontrou estado final
        if (len(q) == 1): # q só tem q[0]
            print ("-1: Computação terminada e rejeitada.")
            print (setting)
            return -1
        
        # Configura máquina para próximo estado
        setting['current_state'] = q[1]['current_state']
        setting['head_word'] = q[1]['head_word']
        setting['counter'] = q[1]['counter']
        q.pop(0) # Tira estado atual da fila
