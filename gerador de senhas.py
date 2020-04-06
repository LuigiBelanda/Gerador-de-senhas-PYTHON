import random
import time

char_letras = "abcdefghijklmnopqrstuvwxyz"
char_letras_numeros = "abcdefghijklmnopqrstuvwxyz1234567890"
char_completa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print ('Temos tres estilos de senhas, veja a seguir:')
time.sleep(1)
print ('1 - só letras')
print ('2 - letras e números')
print ('3 - letras maiusculas/minusculas e números')
time.sleep(1)
print ('Para selecionar o tipo de senha que deseja basta digitar o número correspondente a sua opção')

escolha_de_tipo = int(input('Qual tipo de senha vc quer? 1, 2 ou 3: '))

if (escolha_de_tipo == 1):
    num_caract = int(input("Número de caracteres para sua senha: "))
    if (num_caract < 0): 
        print("Erro: número negativo")
        exit()
    elif (num_caract == 0):
        print("Erro: Tem que ter pelo menos 1 caracter.")
        exit()
    else:
        senha = ""

    print('PROCESSANDO...')
    time.sleep(2)

    while len(senha) != num_caract:
        senha = senha + random.choice(char_letras)
    if len(senha) == num_caract:
        print("Senha: {}".format(senha))

if (escolha_de_tipo == 2):
    num_caract = int(input("Número de caracteres para sua senha: "))
    if (num_caract < 0): 
        print("Erro: número negativo")
        exit()
    elif (num_caract == 0):
         print("Erro: Tem que ter pelo menos 1 caracter.")
         exit()
    else:
        senha = ""

    print('PROCESSANDO...')
    time.sleep(2)

    while len(senha) != num_caract:
        senha = senha + random.choice(char_letras_numeros)
    if len(senha) == num_caract:
        print("Senha: {}".format(senha))

if (escolha_de_tipo == 3):
    num_caract = int(input("Número de caracteres para sua senha: "))
    if (num_caract < 0): 
        print("Erro: número negativo")
        exit()
    elif (num_caract == 0):
        print("Erro: Tem que ter pelo menos 1 caracter.")
        exit()
    else:
        senha = ""

    print('PROCESSANDO...')
    time.sleep(2)

    while len(senha) != num_caract:
        senha = senha + random.choice(char_completa)
    if len(senha) == num_caract:
        print("Senha: {}".format(senha))

else:
    print('escolha inválida')