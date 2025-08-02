import random
import string

def senha_aleatoria(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = senha_aleatoria(tamanho_senha)
print(f"Sua nova senha é: {nova_senha}")