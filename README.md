# Autômato Finito
Este repositório contém a implementação de um programa desenvolvido em Python que simula a execução de autômatos finitos não-determinísticos.

### Introdução
O programa foi desenvolvido por Cláudia Sampedro, Lucas Ribeiro, Thaís Zorawski e Vitor Bueno, alunos do curso Bacharelado em Ciência da Computação da Universidade Tecnológica Federal do Paraná – *câmpus* Campo Mourão (UTFPR-CM). Tal programa foi desenvolvido no semestre 2018/2, para a disciplina Linguagens Formais, Autômatos e Computabilidade, ministrada pelo professor Marco Aurélio Graciotto Silva, do Departamento de Computação da UTFPR-CM (DACOM).

### Sobre o Autômato Finito
Um *Autômato Finito* é um modelo teórico parecido com o funcionameto de máquinas de Turing. Uma MT é uma máquina que manipula símbolos em uma fita, de acordo com um conjunto de regras e transições. Assim como uma máquina de Turing, um Autômato Finito possui um alfabeto, que será o conjunto de símbolos aceitáveis pelo autômato, um conjunto de estados possíveis, uma palavra de entrada e um conjunto de transições que indicam o que acontecerá com a autômato e com a pilha de acordo com o valor que é lido na entrada do autômato.

### Sobre o funcionamento do programa
Este programa segue a mesma lógica da Máquina de Turing desenvolvida anteriormente pelos mesmos alunos, que está disponível [neste link](https://github.com/claudiaps/TuringMachine). Antes de começar a fazer a abordagem lógica do autômato, é verificado se na palavra inserida existe algum caractere inválido (fora do alfabeto de entrada) e sabendo que uma palavra pode ser composta de caracteres do alfabeto de entrada e por ε's, retiramos da palavra os ε's se houver (uma vez que não há necessidade deles durante o programa). Após essas verificações, é criada a configuração atual do autômato, contendo seu estado atual, a palavra de entrada e um indicador de qual posição da palavra já foi consumida. Assim, essa configuração inicial é adicionada na pilha de execução e é iniciada a procura numa lista de transições os caminhos que são possíveis tomar. Para cada possibilidade, é adicionado o resultado dessa possível transição na fila (buscando de forma linear, e *não* por profundidade). Para uma transição ser considerada um possível caminho, é necessário cumprir 2 requisitos:

- o estado atual da configuração atual deve ser a mesma que na transição (*transitions\[i]\[0]*);
- a 1ª letra da palavra de entrada da configuração atual deve ser o mesmo símbolo do alfabeto de entrada da transição (*transitions\[i]\[1]*), \[se houver 1ª letra na palavra na configuração atual] ou se o símbolo do alfabeto de entrada da transição for um ε.

Se uma transição for aprovada como possível caminho a ser tomado, são realizadas a cópia da configuração atual e a alteração das seguintes propriedades:
- se o alfabeto de entrada da transição for diferente de ε, é realizada a consumição da 1ª letra da palavra (movemos o indicador para a próxima letra da palavra).

Após realizar as alterações adiciona-se na fila de execução e depois de verificar todas as transições para o estado atual, ele é tirado da fila, e logo em seguida é executado o próximo elemento da fila com sua própria configuração e assim o processo se repete.

Para verificar se a computação foi aceita o tamanho da palavra deve ser 0 e se foi atingido algum estado de aceitação/final.

#### Observação (Tratamento de *loop*)

Embora não tivesse sido obrigado tratar *looping*, o software está programado para rodar uma quantidade de 5000 vezes por item de profundidade. Quando o limite for alcançado, o programa perguntará se o usuário vai querer continuar com a execução ou parará por ali, informando a configuração neste ponto.

### Variáveis *config = {}*
Durante a execução do programa foi armazenado a configuração do autômato na variável *config*, em que as informações estão armazenadas da seguinte forma:
config\[1]: alfabeto de entrada
config\[2]: símbolo a ser considerado para representar epsilon ou lambda (não deve pertencer ao alfabeto de entrada)
config\[3]: conjunto de estados
config\[4]: estado inicial
config\[5]: conjunto de estados de aceitação
	
### Como executar

- O formato de instrução para execução do programa é:  
	`python main.py “automato.txt” “entrada”`
    
  **Exemplo:**  
  `python main.py ./exemplos/exemplo.txt 01`

- Para testes, no diretório *"exemplos"* deste repositório existem alguns exemplos de arquivos com Autômatos Finitos no formato que deve ser usado como entrada para o programa (*.txt*).

- O formato de saída do programa é:  
  `{'current_state', 'head_word', 'counter'}`

  Em que, *‘current_state’* indica o estado no qual o autômato se encontra ao final da execução e  *‘head_word’* indica a posição da palavra consumida até o momento e *‘counter’* o contador em ordem decrescente que verifica um possível *looping*.
  
  Além disso, na saída do programa haverá uma linha indicando o resultado final de execução do Autômato, podendo ser:
  `0: Computação terminada e aceita.`
  `-1: Computação terminada e rejeitada.`
  `-3: Valor inserido na palavra incorreto`

  **Exemplo de Saída:**  
  `0: Computação terminada e aceita.`  
  `{'current_state': 'c', 'head_word': 2, 'counter': 4998}`
  
- Para converter Autômatos Finito do formato *.jff* para *.txt* (formato aceito pelo programa), use o arquivo *jflap-pda2utfpr.py*, da seguinte forma:

  `python jflap-pda2utfpr.py arquivo_entrada.jff arquivo_saida.txt`
  
### Considerações Finais
Com o desenvolvimento deste programa, os autores puderam compreender afundo o funcionamento e propósito geral dos Autômatos Finito.