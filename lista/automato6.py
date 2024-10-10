# 6. Construa um autômato finito não-determinístico (AFN) que aceite strings que contenham pelo menos um ‘0’ sobre o alfabeto {0, 1}.

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

class NFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.alphabet = {'0', '1'}
        self.transition_function = {
            'q0': {'0': {'q1'}, '1': {'q0'}},
            'q1': {'0': {'q1'}, '1': {'q1'}}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1'}

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

# Testando o AFN
nfa = NFA()
test_strings = ['0', '10', '111', '1011', '001']
for string in test_strings:
    print(f"String '{string}' é aceita? {nfa.accept(string)}")

