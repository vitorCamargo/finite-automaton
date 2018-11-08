import sys
import finiteAutomaton

def read_file():
    aux = 0
    config = []
    transition = {}
    
    file_name = str(sys.argv[1])
    file = open(file_name, 'r')

    for i in range(1, 5):
        conteudo = file.readline().strip('\n').split(' ')
        config[i] = conteudo
    
    for i in file:
        aux = aux + 1
        transition[aux] = i.strip('\n').split(' ')
    return config, transition

def main():
    config, transitions = read_file()
    word = sys.argv[2]
    
    finiteAutomaton.machine(config, word, transitions)

main()
