def mascara_cpf(cpf):
    estado = 'q0'
    for char in cpf:
        if estado == 'q0':
            char = 'x'
            estado = 'q1'
        elif estado == 'q1':
            char = 'x'
            estado = 'q2'
        elif estado == 'q2':
            char = 'x'
            estado = 'q3'
        elif estado == 'q3':
            estado = 'q4'
        elif estado == 'q4':
            estado = 'q5'
        elif estado == 'q5':
            estado = 'q6'
        elif estado == 'q6':
            estado = 'q7'
        elif estado == 'q7':
            estado = 'q8'
        elif estado == 'q8':
            estado = 'q9'
        elif estado == 'q9':
            char = 'x'
            estado = 'q10'
        elif estado == 'q10':
            char = 'x'
            estado = 'q_aceita'
        elif estado == 'q_aceita':
            return "CPF mascarado!"
        else:
            estado = 'q_rejeita'
            return "CPF inválido!"
            break

        print(char, end='')

print(mascara_cpf('12345678911'))