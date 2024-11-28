# Máquina de Turing para uma linguagem sobre o alfabeto {a, b},
# que reconhece strings com um número ímpar de 'a's.
class TuringMachine:
    def __init__(self, fita, estado_inicial, estados_finais, transicoes):
        # Inicializa os atributos da Máquina de Turing
        self.fita = list(fita)  # Converte a fita em uma lista para facilitar as alterações
        self.cabecote = 0  # Define a posição inicial do cabeçote
        self.estado = estado_inicial  # Define o estado inicial da máquina
        self.estados_finais = estados_finais  # Conjunto de estados finais (aceitação e rejeição)
        self.transicoes = transicoes  # Dicionário de transições da máquina

    def passo(self):
        # Executa um único passo da Máquina de Turing
        caractere = self.fita[self.cabecote]  # Lê o caractere na posição atual do cabeçote
        if (self.estado, caractere) in self.transicoes:  # Verifica se há uma transição válida
            # Obtém os detalhes da transição
            novo_estado, escrever_caractere, movimento = self.transicoes[(self.estado, caractere)]
            self.fita[self.cabecote] = escrever_caractere  # Escreve o caractere na fita
            self.estado = novo_estado  # Atualiza o estado da máquina
            # Move o cabeçote de acordo com a direção especificada
            if movimento == 'R':  # Direita
                self.cabecote += 1
            elif movimento == 'L':  # Esquerda
                self.cabecote -= 1
        else:
            # Caso não exista transição válida, vai para o estado de rejeição
            self.estado = 'q_rejeitar'

    def executar(self):
        # Executa a máquina até alcançar um estado final
        while self.estado not in self.estados_finais:  # Continua enquanto o estado atual não for final
            self.passo()  # Executa um passo
        return self.estado  # Retorna o estado final (aceitar ou rejeitar)


# Definição da fita, estados e transições
fita = "aaabb "  # Adiciona um espaço em branco no final para indicar o fim da fita
estado_inicial = 'q0'  # Estado inicial da máquina
estados_finais = {'q_aceitar', 'q_rejeitar'}  # Estados finais
transicoes = {
    # Estado q0: número par de 'a's
    ('q0', 'a'): ('q1', 'a', 'R'),  # Lê 'a', alterna para número ímpar
    ('q0', 'b'): ('q0', 'b', 'R'),  # Ignora 'b', mantém estado
    ('q0', ' '): ('q_rejeitar', ' ', 'R'),  # Rejeita caso chegue ao fim com número par de 'a's

    # Estado q1: número ímpar de 'a's
    ('q1', 'a'): ('q0', 'a', 'R'),  # Lê 'a', alterna para número par
    ('q1', 'b'): ('q1', 'b', 'R'),  # Ignora 'b', mantém estado
    ('q1', ' '): ('q_aceitar', ' ', 'R')  # Aceita caso chegue ao fim com número ímpar de 'a's
}

# Criação e execução da máquina de Turing
mt = TuringMachine(fita, estado_inicial, estados_finais, transicoes)
resultado = mt.executar()
print(f"Resultado: {fita}-", resultado)
