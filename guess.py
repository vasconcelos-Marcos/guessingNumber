from random import randint

def guess(limite):
  n = randint(1, limite)
  palpite = -10
  count = 0
  
  while(palpite != n):
    count += 1
    palpite = int(input(f"Advinhe o valor de 1 a {limite}: "))
    if palpite>n:
      print("Tente um número menor!")
    elif palpite<n:
      print("Tente um número maior!")
      
  print(f"Parabéns! Você acertou o número {n} em {count} tentativas!")

def computer_guess(limite):
  min = 1
  max = limite
  resposta = ''
  count = 0

  while resposta != 'c':
    count += 1
    if min != max:
      guess = randint(min, max)
    else:
      guess = min
    resposta = input(f"A máquina chutou {guess}, o palpite é alto(A), baixo(B) ou correto(C): ").lower()
    if resposta == 'a':
      max = guess - 1
    elif resposta == 'b':
      min = guess + 1
  print(f"Fim de jogo! A máquina acertou em {count} tentativas!")
      
while True:
  limite = int(input("Defina o número máximo : "))
  select = int(input("[1]Deseja advinhar o número da máquina \n[2]ou que a máquina advinhe seu número: "))
  if select == 1:
    guess(limite)
  elif select == 2:
    computer_guess(limite)
  again = input("Deseja jogar novamente? [S/N]: ").lower()
  if again == 'n':
    break