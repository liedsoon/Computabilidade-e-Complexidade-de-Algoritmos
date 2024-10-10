# 5. Implemente em Python um AFD que aceite qualquer string binária que comece e termine com o mesmo caractere.

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
class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transition_function = {
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'0': 'q1', '1': 'q3'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q3', '1': 'q3'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1', 'q2'}

    def accept(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states

# Testando o AFD
dfa = DFA()
test_strings = ['0', '11', '00', '1000']
for string in test_strings:
    print(f"String '{string}' é aceita? {dfa.accept(string)}")
