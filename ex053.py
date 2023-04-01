frase = str(input('insira uma frase: ')).strip().upper() #frase maiúscula e sem espaços desnecessários
palavras = frase.split() #separando a frase em palavras
junto = ''.join(palavras) #juntando as palavras sem espaços
inverso = ''

for letra in range(len(junto) -1, -1, -1): #fazendo o inverso da frase
    inverso += junto[letra] # inverso = junto[::-1]

print('frase normal: {}'.format(junto))
print('frase inversa: {}'.format(inverso))

if inverso == junto:
    print('a frase é um palíndromo')
else:
    print('a frase NÃO É um palíndromo')
