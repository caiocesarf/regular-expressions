from graphviz import Digraph


class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.transition_function[current_state]:
                current_state = self.transition_function[current_state][char]
            else:
                return False
        return current_state in self.accept_states

    def plot(self, filename):
        dot = Digraph()

        # Adiciona os estados
        for state in self.states:
            if state in self.accept_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)

        # Adiciona o estado inicial
        dot.node('', shape='none')
        dot.edge('', self.start_state)

        # Adiciona as transições
        for state, transitions in self.transition_function.items():
            for symbol, next_state in transitions.items():
                dot.edge(state, next_state, label=symbol)

        # Salva o gráfico como um arquivo JPG
        dot.format = 'jpg'
        dot.render(filename)


# a) (ab*c*)*
dfa_a = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b', 'c'},
    transition_function={
        'q0': {'a': 'q1'},
        'q1': {'b': 'q1', 'c': 'q2'},
        'q2': {'c': 'q2'}
    },
    start_state='q0',
    accept_states={'q1', 'q2'}
)

# b) aaa(b|c)*|(b|c)*aaa
dfa_b = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
    alphabet={'a', 'b', 'c'},
    transition_function={
        'q0': {'a': 'q1', 'b': 'q4', 'c': 'q4'},
        'q1': {'a': 'q2'},
        'q2': {'a': 'q3'},
        'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3'},
        'q4': {'a': 'q5', 'b': 'q4', 'c': 'q4'},
        'q5': {'a': 'q6'},
        'q6': {'a': 'q3'},
        'q7': {'b': 'q7', 'c': 'q7', 'a': 'q8'},
        'q8': {'a': 'q9'},
        'q9': {'a': 'q3'}
    },
    start_state='q0',
    accept_states={'q3'}
)

# Define the DFA for a* b | ab*
dfa_c =DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transition_function={
        'q0': {'a': 'q0', 'b': 'q1'},
        'q1': {'b': 'q1'},
        'q2': {'b': 'q2'}
    },
    start_state='q0',
    accept_states={'q1', 'q2'}
)

# d) a*b*(a|ac*)
dfa_d = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b', 'c'},
    transition_function={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q1', 'b': 'q2', 'c': 'q4'},
        'q2': {'a': 'q3', 'b': 'q2'},
        'q3': {'c': 'q4'},
        'q4': {'c': 'q4'}
    },
    start_state='q0',
    accept_states={'q1', 'q3', 'q4'}
)

accepted_strings_a = [
    'aabbcc',
    'aab',
    'aac',
    'aabcc',
    'aabb',
    'aabbbc',
    'aabccc',
    'aabbbcc',
    'aabbbccc',
    'aabbbccc',
    'aabbbcccc',
    'aabbbcccc',
    'aabbbccccc',
    'aabbbccccc',
    'aabbbcccccc',
    'aabbbcccccc',
    'aabbbccccccc',
    'aabbbccccccc',
    'aabbbcccccccc',
    'aabbbcccccccc',
    'aabbbccccccccc',
    'aabbbccccccccc',
    'aabbbcccccccccc',
    'aabbbcccccccccc',
    'aabbbccccccccccc',
    'aabbbccccccccccc',
    'aabbbcccccccccccc',
    'aabbbcccccccccccc',
    'aabbbccccccccccccc'
]

print("Automato para A) (ab*c*)*")
for string in accepted_strings_a:
    print(f"String '{string}' is accepted by DFA a: {dfa_a.accepts(string)}")  # True
for string in accepted_strings_a:
    print(f"String '{string}' is accepted by DFA a: {dfa_a.accepts(string)}")  # False
print()

accepted_strings_b = ["aaab", "aaac", "aaa", "aaabb", "aaacc", "aaabbb", "aaaccc", "aaabbbc", "aaacccc", "aaabbbcc",
                      "aaaccccc", "aaabbbccc", "aaacccccc", "aaabbbcccc", "aaaccccccc", "aaabbbccccc", "aaacccccccc",
                      "aaabbbcccccc", "aaaccccccccc", "aaabbbccccccc", "aaacccccccccc", "aaabbbcccccccc",
                      "aaaccccccccccc", "aaabbbccccccccc", "aaacccccccccccc", "aaabbbcccccccccc", "aaaccccccccccccc",
                      "aaabbbccccccccccc", "aaacccccccccccccc", "aaabbbcccccccccccc", "aaaccccccccccccccc",
                      "aaabbbccccccccccccc", "aaacccccccccccccccc", "aaabbbcccccccccccccc", "aaaccccccccccccccccc",
                      "aaabbbccccccccccccccc", "aaacccccccccccccccccc", "aaabbbcccccccccccccccc",
                      "aaaccccccccccccccccccc", "aaabbbccccccccccccccccc", "aaacccccccccccccccccccc",
                      "aaabbbcccccccccccccccccc", "aaaccccccccccccccccccccc", "aaabbbccccccccccccccccccc",
                      "aaacccccccccccccccccccccc", "aaabbbcccccccccccccccccccc", "aaaccccccccccccccccccccccc",
                      "aaabbbccccccccccccccccccccc", "aaacccccccccccccccccccccccc"]
rejected_strings_b = ["", "a", "b", "c", "ab", "ac", "ba", "ca", "bb", "cc", "bca", "cab", "bac", "cba", "babc", "cbac",
                      "bacb", "cbca", "bacbc", "cbcac", "bacbac", "cbcbac", "bacbacb", "cbcbacb", "bacbacbc",
                      "cbcbacbc", "bacbacbcc", "cbcbacbcc", "bacbacbccc", "cbcbacbccc", "bacbacbcccc", "cbcbacbcccc",
                      "bacbacbccccc", "cbcbacbccccc", "bacbacbcccccc", "cbcbacbcccccc", "bacbacbccccccc",
                      "cbcbacbccccccc", "bacbacbcccccccc", "cbcbacbcccccccc", "bacbacbccccccccc", "cbcbacbccccccccc",
                      "bacbacbcccccccccc", "cbcbacbcccccccccc", "bacbacbccccccccccc", "cbcbacbccccccccccc",
                      "bacbacbcccccccccccc", "cbcbacbcccccccccccc", "bacbacbccccccccccccc", "cbcbacbccccccccccccc"]

print("Automato para B) aaa(b|c)*|(b|c)*aaa")
for string in accepted_strings_b:
    print(f"String '{string}' is accepted by DFA b: {dfa_b.accepts(string)}")  # True
for string in accepted_strings_b:
    print(f"String '{string}' is accepted by DFA b: {dfa_b.accepts(string)}")  # False
print()

accepted_strings_c = [
    'abb',
    'abbb',
    'abbbb',
    'abbbbb',
    'abbbbbb',
    'abbbbbbb',
    'abbbbbbbb',
    'abbbbbbbbb',
    'abbbbbbbbbb',
    'abbbbbbbbbbb',
    'abbbbbbbbbbbb',
    'abbbbbbbbbbbbb',
    'abbbbbbbbbbbbbb',
    'abbbbbbbbbbbbbbb',
    'abbbbbbbbbbbbbbbb',
    'abbbbbbbbbbbbbbbbb'
]

print("Automato para C) a*b|ab*")
for string in accepted_strings_c:
    print(f"String '{string}' is accepted by DFA c: {dfa_c.accepts(string)}")  # True
for string in accepted_strings_c:
    print(f"String '{string}' is accepted by DFA c: {dfa_c.accepts(string)}")  # False
print()

rejected_strings_d = [
    'ab',
    'aab',
    'aaab',
    'b',
    'bb',
    'bbb',
    'aab',
    'ab',
    'aab',
    'aaab',
    'aaaab',
    'aaaaab',
    'aaaaaab',
    'aaaaaaab',
    'aaaaaaaab',
    'aaaaaaaaab',
    'aaaaaaaaaab',
    'abc',
    'aabc',
    'aaabc',
    'aaaabc',
    'aaaaabc',
    'aaaaaabc',
    'aaaaaaabc',
    'aaaaaaaabc',
    'aaaaaaaaabc',
    'aaaaaaaaaabc',
    '',
    'c',
    'bc',
    'abc',
    'bca',
    'cab',
    'bacb',
    'cbac',
    'ca',
    'bb',
    'cc',
    'bca',
    'cab',
    'cba',
    'babc',
    'cbac',
    'bacb',
    'cbca',
    'bacbc',
    'cbcac',
    'bacbac',
    'cbcbac',
    'bacbacb',
    'cbcbacb',
    'bacbacbc',
    'cbcbacbc',
    'bacbacbcc',
    'cbcbacbcc',
    'bacbacbccc',
    'cbcbacbccc',
    'bacbacbcccc',
    'cbcbacbcccc',
    'bacbacbccccc',
    'cbcbacbccccc',
    'bacbacbcccccc',
    'cbcbacbcccccc',
    'bacbacbccccccc',
    'cbcbacbccccccc',
    'bacbacbcccccccc',
    'cbcbacbcccccccc',
    'bacbacbccccccccc',
    'cbcbacbccccccccc',
    'bacbacbcccccccccc',
    'cbcbacbcccccccccc',
    'bacbacbccccccccccc',
    'cbcbacbccccccccccc'
]

accepted_strings_d = [
    'a',
    'aa',
    'aaa',
    'aac',
    'aacc',
    'aaac',
    'aaacc',
    'aaaa',
    'aaaaa',
    'aaaaaa',
    'aaaaaaa',
    'aaaaaaaa',
    'aaaaaaaaa',
    'aaaaaaaaaa',
    'aaaaaaaaaaa',
    'aaaaaaaaaaaa',
    'aaaaaaaaaaaaa',
    'ac',
    'aac',
    'aaac',
    'aaaac',
    'aaaaac',
    'aaaaaac',
    'aaaaaaac',
    'aaaaaaaac',
    'aaaaaaaaac',
    'aaaaaaaaaac',
    'ac',
    'bac',
    'ba',
    'bac'
]

print("Automato para D) a*b*(a|ac*)")
for string in accepted_strings_d:
    print(f"String '{string}' is accepted by DFA d: {dfa_d.accepts(string)}")  # True
for string in rejected_strings_d:
    print(f"String '{string}' is accepted by DFA d: {dfa_d.accepts(string)}")  # False
print()


# Plotando os autômatos
dfa_a.plot('dfa_a')
dfa_b.plot('dfa_b')
dfa_c.plot('dfa_c')
dfa_d.plot('dfa_d')