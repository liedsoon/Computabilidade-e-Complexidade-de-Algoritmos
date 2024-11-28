#reconhece strings sobre o alfabeto {0, 1} que contem um número par de 0s e um número par de 1s
class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transitions):
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def step(self):
        char = self.tape[self.head]
        if (self.state, char) in self.transitions:
            new_state, write_char, move = self.transitions[(self.state, char)]
            self.tape[self.head] = write_char
            self.state = new_state
            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1
        else:
            self.state = 'q_reject'

    def run(self):
        while self.state not in self.final_states:
            self.step()
        return self.state

# Definição da fita, estados e transições
tape = "0011 "  # Adicione um espaço em branco no final para indicar o fim da fita
initial_state = 'q0'
final_states = {'q_accept', 'q_reject'}
transitions = {
    ('q0', '0'): ('q1', '0', 'R'),
    ('q0', '1'): ('q2', '1', 'R'),
    ('q0', ' '): ('q_accept', ' ', 'R'),
    ('q1', '0'): ('q0', '0', 'R'),
    ('q1', '1'): ('q3', '1', 'R'),
    ('q1', ' '): ('q_reject', ' ', 'R'),
    ('q2', '0'): ('q3', '0', 'R'),
    ('q2', '1'): ('q0', '1', 'R'),
    ('q2', ' '): ('q_reject', ' ', 'R'),
    ('q3', '0'): ('q2', '0', 'R'),
    ('q3', '1'): ('q1', '1', 'R'),
    ('q3', ' '): ('q_reject', ' ', 'R')
}

# Criação e execução da máquina de Turing
tm = TuringMachine(tape, initial_state, final_states, transitions)
result = tm.run()
print(f"Resultado: {tape}-", result)
