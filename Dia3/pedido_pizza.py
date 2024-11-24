print("Bem-vindo à Python Pizza Deliveries!")
tamanho = input("Qual o tamanho da pizza que o(a) senhor(a) deseja? P, M ou G:\n")
pepperoni = input("O(a) senhor(a) gostaria de adicionar pepperoni à sua pizza? S ou N :\n")
extra_queijo = input("Gostaria o(a) senhor(a) de adicionar queijo extra? S ou N:\n")

conta = 0

# Verificando o tamanho da pizza
if tamanho == "P" or tamanho == "p":
    conta += 15
    if pepperoni == "S" or pepperoni == "s":
        conta += 2
    if extra_queijo == "S" or extra_queijo == "s":
        conta += 1

elif tamanho == "M" or tamanho == "m":
    conta += 20
    if pepperoni == "S" or pepperoni == "s":
        conta += 3
    if extra_queijo == "S" or extra_queijo == "s":
        conta += 1

elif tamanho == "G" or tamanho == "g":
    conta += 25
    if pepperoni == "S" or pepperoni == "s":
        conta += 3
    if extra_queijo == "S" or extra_queijo == "s":
        conta += 1

print(f"O valor da sua conta é: R${conta}")