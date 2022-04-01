from random import randint

n = randint(1, 100)
palpite = -10

while(palpite != n):
  palpite = int(input("Digite um valor de 1 a 100: "))
  if palpite>n:
    print("Tente um número menor!")
  elif palpite<n:
    print("Tente um número maior!")
  else:
    print("Parabéns! Você acertou!")