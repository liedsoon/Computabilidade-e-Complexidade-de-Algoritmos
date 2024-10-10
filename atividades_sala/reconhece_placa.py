def reconhece_placa(string):
    estado = 'q0'

    for char in string:

        if estado == 'q0':
            if char.isalpha():
                estado = 'q1'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q1':
            if char.isalpha():
                estado = 'q2'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q2':
            if char.isalpha():
                estado = 'q3'
            else:
                estado = 'q_rejeita'
                break

        elif estado == ('q3'):

            if char == '-':
                estado = 'q4'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q4':
            if char.isdigit():
                estado = 'q5'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q5':
            if char.isdigit():
                estado = 'q6'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q6':
            if char.isdigit():
                estado = 'q7'
            else:
                estado = 'q_rejeita'
                break

        elif estado == 'q7':
            if char.isdigit():
                estado = 'q8'
            else:
                estado = 'q_rejeita'
                break

    if estado == 'q8' and len(string) == 8:
        return "Placa Valida"
    else:
        return "Placa Invalida"

print(reconhece_placa("mma-1845"))
print(reconhece_placa("mma-aaa"))
print(reconhece_placa("mma-18475"))
print(reconhece_placa("mama-aaa"))
print(reconhece_placa("mma-1447"))
