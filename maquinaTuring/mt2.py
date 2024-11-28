# Reconhece strings sobre o alfabeto {0, 1}
# que contêm um número par de 0s e número par de 1s.
class TuringMachine:
    def __init__(self, fita, estado_inicial, estados_finais, transicoes):
        self.fita = list(fita)  # Converte a fita em uma lista para facilitar as modificações
        self.cabecote = 0  # Inicializa o cabeçote na posição 0
        self.estado = estado_inicial  # Define o estado inicial da máquina
        self.estados_finais = estados_finais  # Define os estados finais
        self.transicoes = transicoes  # Dicionário com as transições da máquina

    def passo(self):
        # Executa um único passo da Máquina de Turing
        caractere = self.fita[self.cabecote]  # Lê o caractere na posição atual do cabeçote
        if (self.estado, caractere) in self.transicoes:  # Verifica se há uma transição válida
            # Obtém os detalhes da transição
            novo_estado, escrever_caractere, movimento = self.transicoes[(self.estado, caractere)]
            self.fita[self.cabecote] = escrever_caractere  # Escreve o caractere na fita
            self.estado = novo_estado  # Atualiza o estado da máquina
            # Move o cabeçote na direção especificada
            if movimento == 'R':  # Move para a direita
                self.cabecote += 1
            elif movimento == 'L':  # Move para a esquerda
                self.cabecote -= 1
        else:
            # Caso não haja transição válida, vai para o estado de rejeição
            self.estado = 'q_rejeitar'

    def executar(self):
        # Executa a máquina até atingir um estado final
        while self.estado not in self.estados_finais:  # Continua enquanto não chegar a um estado final
            self.passo()  # Executa um passo
        return self.estado  # Retorna o estado final (aceitar ou rejeitar)


# Definição da fita, estados e transições
fita = "0011 "  # Adiciona um espaço em branco no final para indicar o fim da fita
estado_inicial = 'q0'
estados_finais = {'q_aceitar', 'q_rejeitar'}
transicoes = {
    ('q0', '0'): ('q1', '0', 'R'),
    ('q0', '1'): ('q2', '1', 'R'),
    ('q0', ' '): ('q_aceitar', ' ', 'R'),
    ('q1', '0'): ('q0', '0', 'R'),
    ('q1', '1'): ('q3', '1', 'R'),
    ('q1', ' '): ('q_rejeitar', ' ', 'R'),
    ('q2', '0'): ('q3', '0', 'R'),
    ('q2', '1'): ('q0', '1', 'R'),
    ('q2', ' '): ('q_rejeitar', ' ', 'R'),
    ('q3', '0'): ('q2', '0', 'R'),
    ('q3', '1'): ('q1', '1', 'R'),
    ('q3', ' '): ('q_rejeitar', ' ', 'R')
}

# Criação e execução da máquina de Turing
mt = TuringMachine(fita, estado_inicial, estados_finais, transicoes)
resultado = mt.executar()
print(f"Resultado: {fita}-", resultado)
