# Exemplo 1: AFN que aceita strings que começam com 'a' ou 'b'
# Descrição: Esse AFN aceita strings que começam com 'a' ou 'b' e podem ter qualquer outra combinação de 'a' ou 'b' depois.

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def _epsilon_closure(self, state):
        stack = [state]
        closure = {state}

        while stack:
            current_state = stack.pop()
            if current_state in self.transition_function and '' in self.transition_function[current_state]:
                for next_state in self.transition_function[current_state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def _move(self, states, symbol):
        new_states = set()
        for state in states:
            if state in self.transition_function and symbol in self.transition_function[state]:
                new_states.update(self.transition_function[state][symbol])
        return new_states

    def accept(self, input_string):
        current_states = self._epsilon_closure(self.start_state)

        for symbol in input_string:
            current_states = set.union(*[self._epsilon_closure(s) for s in self._move(current_states, symbol)])

        return bool(current_states & set(self.accept_states))

# Definição do autômato
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'a', 'b', 'c'}
transition_function = {
    'q0': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q3'}},
    'q1': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q3'}},
    'q2': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q3'}},
    'q3': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q3'}},
}
start_state = 'q0'
accept_states = {'q1', 'q2', 'q3'}

# Inicializando o AFN
nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

# Testando o AFN
test_strings = ['acb', 'bac', 'caa', 'bbb', 'abab']
for string in test_strings:
    print(f"String '{string}' é aceita? {nfa.accept(string)}")

# Exemplo 1: Aceita qualquer string que comece com 'a' ou 'b', e permite qualquer outra combinação desses caracteres depois.