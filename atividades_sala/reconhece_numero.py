def reconhece_numero(string):
    estado = 'q0'

    for char in string:

        if estado == 'q0':
            if char.isdigit():
                estado = 'q1'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q1':
            if char.isdigit():
                estado = 'q1'
            elif char == '.':
                estado = 'q2'
            else:
                estado = 'q_rejeita'
                break


        elif estado == 'q2':
            if char.isdigit():
                estado = 'q3'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q3':
            if char.isdigit():
                estado = 'q3'
            else:
                estado = 'q_rejeita'
                break

    if estado in ['q1', 'q3']:
        return "Número válido"
    else:
        return "Número invalido!"


print(reconhece_numero("123"))
print(reconhece_numero("123.123"))
print(reconhece_numero("12.12.12"))
print(reconhece_numero("abc"))