def placaMercosul(digitos):
    estado = 'q0'

    for char in digitos:
        if estado == 'q0':
            if digitos[0].isalpha():
                estado = 'q1'
            else:
                estado = 'q_rejeita'
        elif estado == 'q1':
            if digitos[1].isalpha():
                estado = 'q2'
            else:
                estado = 'q_rejeita'
        elif estado == 'q2':
            if digitos[2].isalpha():
                estado = 'q3'
            else:
                estado = 'q_rejeita'
        elif estado == 'q3':
            if digitos[3].isdigit():
                estado = 'q4'
            else:
                estado = 'q_rejeita'
        elif estado == 'q4':
            if digitos[4].isalpha():
                estado = 'q5'
            else:
                estado = 'q_rejeita'

        elif estado == 'q5':
            if digitos[5].isdigit():
                estado = 'q6'
            else:
                estado = 'q_rejeita'
        elif estado == 'q6':
            if digitos[6].isdigit():
                estado = 'q_aceita'
            else:
                estado = 'q_rejeita'

        if estado == 'q_aceita':
            return "Placa " + digitos + " valida."

        if estado == 'q_rejeita':
            return "Placa " + digitos + " invalida."


print(placaMercosul('ABC1D23'))
