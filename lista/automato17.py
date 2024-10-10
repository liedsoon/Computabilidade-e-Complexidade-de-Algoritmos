# 17. Implemente em Python a conversão de um AFN para um AFD para um autômato que reconhece strings terminadas em ‘01’.

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
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.transition_function = {
            'q0': {'0': {'q1'}, '1': {'q0'}},
            'q1': {'1': {'q2'}},
            'q2': {}
        }
        self.start_state = 'q0'
        self.accept_states = {'q2'}

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

# Função para converter AFN para AFD
def convert_nfa_to_dfa(nfa):
    dfa_states = {frozenset([nfa.start_state])}
    dfa_transition_function = {}
    dfa_start_state = frozenset([nfa.start_state])
    dfa_accept_states = set()

    unprocessed_states = [frozenset([nfa.start_state])]

    while unprocessed_states:
        current_dfa_state = unprocessed_states.pop()
        dfa_transition_function[current_dfa_state] = {}

        for symbol in nfa.alphabet:
            new_dfa_state = frozenset(
                nfa._move(current_dfa_state, symbol)
            )
            dfa_transition_function[current_dfa_state][symbol] = new_dfa_state

            if new_dfa_state not in dfa_states:
                dfa_states.add(new_dfa_state)
                unprocessed_states.append(new_dfa_state)

            if new_dfa_state & nfa.accept_states:
                dfa_accept_states.add(new_dfa_state)

    return DFA(dfa_states, nfa.alphabet, dfa_transition_function, dfa_start_state, dfa_accept_states)

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            current_state = self.transition_function[current_state][symbol]
        return current_state in self.accept_states

# Convertendo o AFN para AFD
nfa = NFA()
dfa = convert_nfa_to_dfa(nfa)

# Testando o AFD convertido
test_strings = ['01', '101', '1101', '010']
for string in test_strings:
    print(f"String '{string}' é aceita? {dfa.accept(string)}")
