# MT para uma linguagem sobre o alfabeto {a, b},
# que reconheça strings com um número ímpar de 'a’s.
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
tape = "abb "  # Adicione um espaço em branco no final para indicar o fim da fita
initial_state = 'q0'
final_states = {'q_accept', 'q_reject'}
transitions = {
    ('q0', 'a'): ('q1', 'a', 'R'),
    ('q0', 'b'): ('q0', 'b', 'R'),
    ('q0', ' '): ('q_reject', ' ', 'R'),

    ('q1', 'a'): ('q0', 'a', 'R'),
    ('q1', 'b'): ('q1', 'b', 'R'),
    ('q1', ' '): ('q_accept', ' ', 'R')
}

# Criação e execução da máquina de Turing
tm = TuringMachine(tape, initial_state, final_states, transitions)
result = tm.run()
print(f"Resultado: {tape}-", result)
