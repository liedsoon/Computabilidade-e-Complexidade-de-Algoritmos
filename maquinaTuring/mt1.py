# Reconhece a linguagem sobre o alfabeto {0, 1}, onde todas as strings terminam com "1"
class TuringMachine:
    def __init__(self, fita, estado_inicial, estados_finais, transicoes):
        # Inicializa os atributos da Máquina de Turing
        self.fita = list(fita)  # A fita da máquina, convertida para uma lista para permitir modificações
        self.cabecote = 0  # Cabeçote começa na posição 0
        self.estado = estado_inicial  # Define o estado inicial da máquina
        self.estados_finais = estados_finais  # Conjunto de estados finais (parada)
        self.transicoes = transicoes  # Dicionário de transições: {(estado_atual, caractere_lido): (novo_estado, caractere_escrito, direção)}

    def passo(self):
        # Executa um único passo da Máquina de Turing
        caractere = self.fita[self.cabecote]  # Lê o caractere na posição atual do cabeçote
        if (self.estado, caractere) in self.transicoes:  # Verifica se existe uma transição válida
            # Obtém a transição correspondente
            novo_estado, escrever_caractere, movimento = self.transicoes[(self.estado, caractere)]
            self.fita[self.cabecote] = escrever_caractere  # Escreve o novo caractere na fita
            self.estado = novo_estado  # Atualiza o estado atual
            # Move o cabeçote de acordo com a direção especificada
            if movimento == 'R':  # Move para a direita
                self.cabecote += 1
            elif movimento == 'L':  # Move para a esquerda
                self.cabecote -= 1
        else:
            # Se não houver transição válida, entra em estado de rejeição
            self.estado = 'rejeitar'

    def executar(self):
        # Executa a máquina até atingir um estado final
        while self.estado not in self.estados_finais:  # Continua enquanto o estado atual não for final
            self.passo()  # Executa um passo
        return self.estado  # Retorna o estado final (aceitar ou rejeitar)


# Definição da fita, estados e transições
fita = "0110111 "  # Adicione um espaço em branco no final
estado_inicial = 'q0'
estados_finais = {'q_aceitar', 'q_rejeitar'}
transicoes = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q1', '1', 'R'),
    ('q0', ' '): ('q_rejeitar', ' ', 'R'),
    ('q1', '0'): ('q0', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', ' '): ('q_aceitar', ' ', 'R')
}

# Criação da Máquina de Turing e execução
mt = TuringMachine(fita, estado_inicial, estados_finais, transicoes)
resultado = mt.executar()
print(f"Resultado: {fita}-", resultado)
