a=int(input('primeiro valor '))
b=int(input('segundo valor '))
while True:
  print("""[1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa""")

  x = int(input('qual a sua opção ?'))

  if x == 1:
    print(a+b)
  elif x == 2:
    print(a*b)
  elif x == 3:
    if a>b:
      print(a)
    else:
      print(b)
  elif x == 4:
    print('informe novos numeros :')
    a=int(input( 'primeiro valor : '))
    b=int(input('segundo valor : '))

    print(a,b)
  elif x == 5:
    break