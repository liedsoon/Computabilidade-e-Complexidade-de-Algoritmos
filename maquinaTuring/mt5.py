# Máquina de Turing que substitui todos os 0s por 1s e todos os 1s por 0s
class TuringMachine:
    def __init__(self, fita, estado_inicial, estados_finais, transicoes):
        # Inicializa os atributos da Máquina de Turing
        self.fita = list(fita)  # Converte a fita em uma lista para facilitar alterações
        self.cabecote = 0  # Define a posição inicial do cabeçote
        self.estado = estado_inicial  # Define o estado inicial da máquina
        self.estados_finais = estados_finais  # Conjunto de estados finais (aceitação)
        self.transicoes = transicoes  # Dicionário com as transições

    def passo(self):
        # Executa um único passo da Máquina de Turing
        caractere = self.fita[self.cabecote]  # Lê o caractere na posição atual do cabeçote
        if (self.estado, caractere) in self.transicoes:  # Verifica se há transição válida
            novo_estado, escrever_caractere, movimento = self.transicoes[(self.estado, caractere)]
            self.fita[self.cabecote] = escrever_caractere  # Escreve o novo caractere na fita
            self.estado = novo_estado  # Atualiza o estado atual
            # Move o cabeçote para a direita ou esquerda
            if movimento == 'R':  # Direita
                self.cabecote += 1
            elif movimento == 'L':  # Esquerda
                self.cabecote -= 1
        else:
            # Vai para o estado de aceitação se não houver transição válida
            self.estado = 'q_aceitar'

    def executar(self):
        # Executa a máquina até atingir um estado final
        while self.estado not in self.estados_finais:  # Continua enquanto o estado atual não for final
            self.passo()  # Executa um passo
        return self.estado  # Retorna o estado final (aceitação)

# Definição da fita, estados e transições
fita = "10010100000 "  # Exemplo de entrada (a fita termina com um espaço em branco)
estado_inicial = 'q0'  # Estado inicial
estados_finais = {'q_aceitar'}  # Estado final de aceitação
transicoes = {
    # Substituição de '0' por '1'
    ('q0', '0'): ('q0', '1', 'R'),  # Substitui '0' por '1' e move para a direita
    # Substituição de '1' por '0'
    ('q0', '1'): ('q0', '0', 'R'),  # Substitui '1' por '0' e move para a direita
    # Final da fita
    ('q0', ' '): ('q_aceitar', ' ', 'R')  # Quando encontra espaço, aceita
}

# Criação e execução da máquina de Turing
mt = TuringMachine(fita, estado_inicial, estados_finais, transicoes)
resultado = mt.executar()

# Exibição do resultado
print(f"Resultado: {fita}-", ''.join(mt.fita).strip())
