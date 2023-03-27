n1 = float(input('insira 1° nota: '))
n2 = float(input('insira 2° nota: '))

media = (n1+n2)/2

if media >= 7:
    print('com as notas {:;1f} e {:;1f} você tem média {:;1f}'.format(n1,n2,media))
    print('parabéns, você foi APROVADO!!')
elif 5 <= media <=6.9:
    print('com as notas {:;1f} e {:;1f} você tem média {:;1f}'.format(n1, n2, media))
    print('sinto muito, você está de RECUPERAÇÃO!!')
elif media < 5:
    print('com as notas {:;1f} e {:;1f} você tem média {:;1f}'.format(n1, n2, media))
    print('infelizmente você está REPROVADO!!')