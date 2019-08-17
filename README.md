# Finite Automaton
👨🏽‍💻👏 Assignments for 'Formal Languages, Automata and Computability' subject about a simulation of Finite Automaton.

## More Information
This project is developed using the programming language Python3, however, the speaking language was Portuguese.

### Introduction
The program was developed by [Vitor Camargo](https://github.com/vitorCamargo), [Thaís Zorawski](https://github.com/TZorawski), [Cláudia Sampedro](https://github.com/claudiaps) and [Lucas Ribeiro](https://github.com/lucasvribeiro), students of the Bachelor of Computer Science course at the Federal Technological University of Paraná - *campus* Campo Mourão (UTFPR-CM). This program was developed in the semester 2018/2, for the discipline Formal Languages, Automata and Computability, taught by Professor [Marco Aurélio Graciotto Silva](https://github.com/magsilva), from the Computing Department of UTFPR-CM (DACOM).

### About Finite Automaton
A *Finite Automaton* is a theoretical concept with the performance of Turing machines. A MT is a machine that manipulates symbols on a tape according to a set of rules and transitions. Just like a Turing machine, the Finite automaton has an alphabet, which will be the automaton's eligible set of symbols, a set of possible states, an input word, and a set of transitions that indicate what will happen to an automaton and a stack according to the value that is read on the automaton input.

### How the Program Works
This program follows the same logic as the Turing Machine previously developed by the same students, which is available [at this link](https://github.com/vitorCamargo/turin-machine). Before starting to take the logic approach of the automaton, it is checked whether in the entered word there is any invalid character (outside the input alphabet) and knowing that a word can be composed of characters from the input alphabet and by ε's, we remove from the word the ε's if any (since there is no need for them during the program). After these checks, the automaton's current configuration is created, containing its current state, the input word, and an indicator of which word position has already been consumed. This initial configuration is then added to the execution stack and the search in a list of transitions for the paths that can be taken. For each possibility, the result of this possible transition in the queue is added (searching linearly, and *not* for depth). For a transition to be considered a possible path, 2 requirements must be met:

- the current state of the current setting must be the same as in the transition (*transitions\[i]\[0]*);
- the first letter of the current configuration input word must be the same symbol as the transition input alphabet (*transitions\[i]\[1]*), \[if there is 1st letter in the word in the current setting] or if the transition input alphabet symbol is an ε.

If a transition is approved as a possible path to take, the current configuration is copied and the following properties are changed:
- if the input alphabet of the transition is different from ε, the first letter of the word is consumed (we move the indicator to the next letter of the word).

After making the changes it is added to the execution queue and after checking all transitions to the current state, it is taken from the queue, and then the next element of the queue is executed with its own configuration and the process repeats itself.

To check if the computation has been accepted the word size should be 0 and if any acceptance/final state has been reached.

#### Observation (*loop* Treatment)
Although it was not required to handle *looping*, the software is programmed to run an amount of 5000 times per item deep. When the limit is reached, the program will ask if the user wants to continue execution or stop there, informing the configuration at this point.

### *config = {}* variables
During program execution, the automaton configuration was stored in the variable * config *, where the information is stored as follows:

config\[1]: input alphabet.

config\[2]: symbol to consider to represent epsilon or lambda (must not belong to the input alphabet).

config\[3]: state set.

config\[4]: initial state.

config\[5]: acceptance state set.
	
### How to run the program
- The instruction format for program execution is:
	`python main.py “automata.txt” input`
    
  **Example:**  
  `python main.py ./examples/exemplo.txt 01`

- For testing, in the *"exemplos"* directory of this repository there are some examples of Finite Automaton files in the format that should be used as input to the program (*.txt*).

- The program output format is:
  `{'current_state', 'head_word', 'counter'}`

  Where, *'current_state'* indicates the state in which the automaton is at the end of execution and *'head_word'* indicates the position of the word consumed so far and *'counter'* the descending counter that checks a possible *looping*.
  
  In addition, at the exit of the program there will be a line indicating the final result of the automaton execution, which can be:
  
  `0: Computing done and accepted.`
  
  `-1: Computation terminated and rejected.`
  
  `-3: Value entered in word is incorrect.`

  **Output Example:**  
  `0: Computing done and accepted.`  
  `{'current_state': 'c', 'head_word': 2, 'counter': 4998}`
  
- To convert Stack Automata from *.jff* to *.txt* (format supported by the program), use the *jflap-pda2utfpr.py* file as follows:

  `python jflap-pda2utfpr.py input_file.jff output_file.txt`
