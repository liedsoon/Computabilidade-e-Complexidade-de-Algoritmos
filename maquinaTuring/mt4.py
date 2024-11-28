# Máquina de Turing que aceita strings binárias que
# começam e terminam com o mesmo caractere.
class TuringMachine:
    def __init__(self, fita, estado_inicial, estados_finais, transicoes):
        # Inicializa os atributos da Máquina de Turing
        self.fita = list(fita)  # Converte a fita em uma lista para facilitar alterações
        self.cabecote = 0  # Define a posição inicial do cabeçote
        self.estado = estado_inicial  # Define o estado inicial da máquina
        self.estados_finais = estados_finais  # Conjunto de estados finais (aceitação/rejeição)
        self.transicoes = transicoes  # Dicionário de transições

    def passo(self):
        # Executa um único passo da Máquina de Turing
        caractere = self.fita[self.cabecote]  # Lê o caractere na posição atual do cabeçote
        if (self.estado, caractere) in self.transicoes:  # Verifica se há transição válida
            novo_estado, escrever_caractere, movimento = self.transicoes[(self.estado, caractere)]
            self.fita[self.cabecote] = escrever_caractere  # Escreve o caractere na fita
            self.estado = novo_estado  # Atualiza o estado atual
            # Move o cabeçote na direção especificada
            if movimento == 'R':  # Direita
                self.cabecote += 1
            elif movimento == 'L':  # Esquerda
                self.cabecote -= 1
        else:
            # Vai para o estado de rejeição se não houver transição válida
            self.estado = 'q_rejeitar'

    def executar(self):
        # Executa a máquina até alcançar um estado final
        while self.estado not in self.estados_finais:  # Continua enquanto o estado atual não for final
            self.passo()  # Executa um passo
        return self.estado  # Retorna o estado final (aceitar/rejeitar)


# Definição da fita, estados e transições
fita = "0111100010 "  # Exemplo de entrada

estado_inicial = 'q0'  # Estado inicial
estados_finais = {'q_aceitar', 'q_rejeitar'}  # Estados finais
transicoes = {
    # Estado inicial: identificar o primeiro caractere
    ('q0', '0'): ('q1', '0', 'R'),  # Se o primeiro for '0', prepare para verificar o último
    ('q0', '1'): ('q2', '1', 'R'),  # Se o primeiro for '1', prepare para verificar o último
    ('q0', ' '): ('q_rejeitar', ' ', 'R'),  # String vazia é rejeitada

    # Movendo-se para o final da fita ao começar com '0'
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', ' '): ('q3', ' ', 'L'),  # Quando chegar ao espaço, volta para verificar

    # Movendo-se para o final da fita ao começar com '1'
    ('q2', '0'): ('q2', '0', 'R'),
    ('q2', '1'): ('q2', '1', 'R'),
    ('q2', ' '): ('q4', ' ', 'L'),  # Quando chegar ao espaço, volta para verificar

    # Verificação do último caractere ao começar com '0'
    ('q3', '0'): ('q_aceitar', '0', 'R'),  # Aceita se o último for '0'
    ('q3', '1'): ('q_rejeitar', '1', 'R'),  # Rejeita se o último for '1'

    # Verificação do último caractere ao começar com '1'
    ('q4', '0'): ('q_rejeitar', '0', 'R'),  # Rejeita se o último for '0'
    ('q4', '1'): ('q_aceitar', '1', 'R'),  # Aceita se o último for '1'
}

# Criação e execução da máquina de Turing
mt = TuringMachine(fita, estado_inicial, estados_finais, transicoes)
resultado = mt.executar()
print(f"Resultado: {fita}-", resultado)
