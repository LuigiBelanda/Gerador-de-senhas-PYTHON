import random
import time

def analisando(num_caract):
    if (num_caract < 0):
        print("Erro: número negativo")
        exit()
    elif (num_caract == 0):
        print("Erro: Tem que ter pelo menos 1 caracter.")
        exit()

def gerandoSenha(senha):
    while len(senha) != num_caract:
        if (escolha_de_tipo == 1):
            senha = senha + random.choice(char_letras)
        elif (escolha_de_tipo == 2):
            senha = senha + random.choice(char_letras_numeros)
        else:
            senha = senha + random.choice(char_completa)
    if len(senha) == num_caract:
        print("Senha: {}".format(senha))

char_letras = "abcdefghijklmnopqrstuvwxyz"
char_letras_numeros = "abcdefghijklmnopqrstuvwxyz1234567890"
char_completa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print ('Temos tres estilos de senhas, veja a seguir:')
time.sleep(1.5)
print ('1 - só letras')
print ('2 - letras e números')
print ('3 - letras maiúsculas/minúsculas e números')
time.sleep(1.5)
print ('Para selecionar o tipo de senha que deseja basta digitar o número correspondente a sua opção')

escolha_de_tipo = int(input('Qual tipo de senha vc quer? 1, 2 ou 3: '))

if (escolha_de_tipo == 1 or escolha_de_tipo == 2 or escolha_de_tipo == 3):
    if (escolha_de_tipo == 1):
        num_caract = int(input("Número de caracteres para sua senha: "))
        analisando(num_caract)
        senha = ''
        print('PROCESSANDO...')
        time.sleep(2)
        gerandoSenha(senha)

    if (escolha_de_tipo == 2):
        num_caract = int(input("Número de caracteres para sua senha: "))
        analisando(num_caract)
        senha = ''
        print('PROCESSANDO...')
        time.sleep(2)
        gerandoSenha(senha)

    if (escolha_de_tipo == 3):
        num_caract = int(input("Número de caracteres para sua senha: "))
        analisando(num_caract)
        senha = ''
        print('PROCESSANDO...')
        time.sleep(2)
        gerandoSenha(senha)

else:
    print('escolha inválida')