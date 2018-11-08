import sys
import turingMachine

def read_file():
    config = {}
    transition = {}
    aux = 0
    file_name = sys.argv[1]
    file_name = str(file_name)
    file = open(file_name, 'r')
    for i in range(1, 8):
        conteudo = file.readline().strip('\n').split(' ')
        config[i] = conteudo
    for i in file:
        aux = aux + 1
        transition[aux] = i.strip('\n').split(' ')
    return config, transition

def read_tapes():
    tape = sys.argv[2]
    return tape

def main():
    read_file()
    read_tapes()
    config = {}
    transitions = {}
    tape = []
    config, transitions = read_file()
    tape = read_tapes()
    turingMachine.machine(config, tape, transitions)

main()
