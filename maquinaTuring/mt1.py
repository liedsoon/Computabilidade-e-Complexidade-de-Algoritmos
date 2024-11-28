# reconhece a linguagem sobre o alfabeto {0, 1}, onde todas as strings terminam com “1”
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
            self.state = 'reject'

    def run(self):
        while self.state not in self.final_states:
            self.step()
        return self.state

# Definição da fita, estados e transições
tape = "0110111 "  # Adicione um espaço em branco no final
initial_state = 'q0'
final_states = {'q_accept', 'q_reject'}
transitions = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q1', '1', 'R'),
    ('q0', ' '): ('q_reject', ' ', 'R'),
    ('q1', '0'): ('q0', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', ' '): ('q_accept', ' ', 'R')
}

# Criação e execução da máquina de Turing
tm = TuringMachine(tape, initial_state, final_states, transitions)
result = tm.run()
print(f"Resultado: {tape}-", result)
