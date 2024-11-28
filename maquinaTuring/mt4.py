#MT que aceita qualquer string binária que comece e termine com o mesmo caractere.
class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transitions):
        self.tape = list(tape)  # A fita é representada como uma lista de caracteres
        self.head = 0           # A cabeça começa na posição inicial
        self.state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def step(self):
        char = self.tape[self.head]  # Lê o caractere atual
        if (self.state, char) in self.transitions:
            new_state, write_char, move = self.transitions[(self.state, char)]
            self.tape[self.head] = write_char  # Escreve o novo caractere na fita
            self.state = new_state             # Atualiza o estado
            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1
        else:
            self.state = 'q_reject'  # Transição inválida leva ao estado de rejeição

    def run(self):
        while self.state not in self.final_states:
            self.step()
        return self.state

# Definição da fita, estados e transições
tape = "0111100010 "  # Exemplo de entrada (a fita termina com um espaço em branco)
initial_state = 'q0'
final_states = {'q_accept', 'q_reject'}
transitions = {
    # Estado inicial: verificar o primeiro caractere
    ('q0', '0'): ('q1', '0', 'R'),  # Se for '0', marcar para verificação
    ('q0', '1'): ('q2', '1', 'R'),  # Se for '1', marcar para verificação
    ('q0', ' '): ('q_reject', ' ', 'R'),  # String vazia é rejeitada

    # Verificar correspondência do último caractere para '0'
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', ' '): ('q3', ' ', 'L'),  # Ao chegar no espaço, volte para verificar

    # Verificar correspondência do último caractere para '1'
    ('q2', '0'): ('q2', '0', 'R'),
    ('q2', '1'): ('q2', '1', 'R'),
    ('q2', ' '): ('q4', ' ', 'L'),

    # Verificação do último caractere para '0'
    ('q3', '0'): ('q_accept', '0', 'R'),  # Aceita se o último for '0'
    ('q3', '1'): ('q_reject', '1', 'R'),  # Rejeita se não for

    # Verificação do último caractere para '1'
    ('q4', '0'): ('q_reject', '0', 'R'),  # Rejeita se não for
    ('q4', '1'): ('q_accept', '1', 'R'),  # Aceita se o último for '1'

}

# Criação e execução da máquina de Turing
tm = TuringMachine(tape, initial_state, final_states, transitions)
result = tm.run()
print(f"Resultado: {tape}-", result)
