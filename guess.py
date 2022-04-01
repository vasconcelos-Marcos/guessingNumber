from random import randint

def guess(limite):
  n = randint(1, limite)
  palpite = -10
  
  while(palpite != n):
    palpite = int(input(f"Advinhe o valor de 1 a {limite}: "))
    if palpite>n:
      print("Tente um número menor!")
    elif palpite<n:
      print("Tente um número maior!")
      
  print(f"Parabéns! Você acertou o número {n}!")

guess(20)