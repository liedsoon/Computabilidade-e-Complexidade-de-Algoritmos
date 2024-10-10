# Exemplo 2: AFN que aceita strings com qualquer quantidade de 'a' e termina com 'b'
# Descrição: Esse AFN aceita strings que contêm qualquer número de 'a' e terminam com 'b'.

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _move(self, current_states, symbol):
        new_states = set()
        for state in current_states:
            if symbol in self.transition_function.get(state, {}):
                new_states.update(self.transition_function[state][symbol])
        return new_states

    def _epsilon_closure(self, state):
        return {state}

    def accept(self, input_string):
        current_states = self._epsilon_closure(self.start_state)
        for symbol in input_string:
            current_states = self._move(current_states, symbol)
        return bool(current_states & self.accept_states)

# Definição do autômato
states = {'q0', 'q1'}
alphabet = {'a', 'b'}
transition_function = {
    'q0': {'a': {'q0'}, 'b': {'q1'}},
    'q1': {}
}
start_state = 'q0'
accept_states = {'q1'}

# Inicializando o AFN
nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

# Testando o AFN
test_strings = ['aab', 'ab', 'b', 'aaaaab', 'aaa']
for string in test_strings:
    print(f"String '{string}' é aceita? {nfa.accept(string)}")

# Exemplo 2: Aceita strings que contenham qualquer quantidade de 'a' e terminem com 'b'.