# Exemplo 3: AFN que aceita strings que contêm o padrão "ab" em qualquer parte da string
# Descrição: Esse AFN aceita strings que contenham o padrão "ab" em qualquer parte da string.

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

    def _epsilon_closure(self, states):
        return states

    def accept(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            current_states = self._move(current_states, symbol)
        return bool(current_states & self.accept_states)

# Definição do autômato
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transition_function = {
    'q0': {'a': {'q1'}},
    'q1': {'b': {'q2'}},
    'q2': {}
}
start_state = 'q0'
accept_states = {'q2'}

# Inicializando o AFN
nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

# Testando o AFN
test_strings = ['ab', 'aab', 'baba', 'bba', 'abab']
for string in test_strings:
    print(f"String '{string}' é aceita? {nfa.accept(string)}")

# Exemplo 3: Aceita strings que contêm o padrão "ab" em qualquer parte da string.