s1 = float(input('primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos PODEM FORMAR um triângulo ', end='')
    if s1 == s2 and s2 == s3: # s1 == s2 == s3
        print('EQUILÁTERO')
    elif s1 != s2 or s2 != s3 or s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('os segmentos NÃO PODEM FORMAR um triângulo')


