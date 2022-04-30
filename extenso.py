unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove']

dezenas1 = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
            'setenta', 'oitenta', 'noventa']

centenas = ['cem', 'cento', 'duzentos', 'trezentos', 'quatrocentros',
            'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

def extenso(valor):

    numero = str(valor)
    numero = numero.zfill(3)

    a = int(numero[0])
    b = int(numero[1])
    c = int(numero[2])
    
    if a == 0:
        if b == 0:
            resultado = unidades[c]
            return resultado
        
        elif b == 1:
            if c >= 0 and c <= 9:
                resultado = dezenas1[c]
                return resultado

        elif b >= 2 and b <= 9:

            if c == 0:
                resultado = dezenas2[b-2]
                return resultado

            elif c >= 1 and c <= 9:
                resultado = dezenas2[b-2] + ' e ' + unidades[c]
                return resultado

    if a == 1:
        if b == 0:
            if c == 0:
                resultado = centenas[a-1]
                return resultado
            elif c > 0 and c <= 9:
                resultado = centenas[0] + ' e ' + unidades[c]
                return resultado
        elif b == 1:
            if c >= 0 and c <= 9:
                resultado = 'cento e ' + dezenas1[c]
                return resultado
        elif b >= 2 and b <= 9:
            if c == 0:
                resultado = 'cento e ' + dezenas2[b-2]
                return resultado
            elif c > 0 and c <= 9:
                resultado = 'cento e ' + dezenas2[b-2] + ' e ' + unidades[c]
                return resultado

    elif a >= 2 and a <= 9:
        if b == 0 and c == 0:
            resultado = centenas[a]
            return resultado
        elif b == 0 and c >= 1 and c <= 9:
            resultado = centenas[a] + ' e ' + unidades[c]
            return resultado
        elif b == 1 and c >= 0 and c <= 9:
            resultado = centenas[a] + ' e ' + dezenas1[c]
            return resultado        
        elif b >= 2 and b <= 9 and c == 0:
            resultado = centenas[a] + ' e ' + dezenas2[b-2]
            return resultado
        elif b >= 2 and b <= 9 and c >= 1 and c <= 9:
            resultado = centenas[a] + ' e ' + dezenas2[b-2] + ' e ' + unidades[c]
            return resultado

def main(num):
    result = ''
    numero = str(num)
    numero = numero.zfill(9) + numero

    for i in [0,3,6]:
        var=numero[i]+numero[i+1]+numero[i+2]
        if int(var) != 0:
            res = extenso(var)
            if i == 0:
                result = res + ' milhões '
            elif i == 3:
                result = result + res + ' mil '
            elif i == 6:
                result = result + res
                
    return result
   
print(main(9999999))
