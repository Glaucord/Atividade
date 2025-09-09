# Atividade Avaliativa Algorítmos e Programação

# Primeiro criamos uma função para calcular os divisores de um número.
def encontrar_divisores(numero):
    '''
    Se o número for primo, retorna o 1 e ele mesmo.
    Caso não seja um número primo, vamos somente até a raiz quadrada do número.
    '''
# Se o número for par e maior que 2, retornamos 2 e o resultado da divisão.
    if numero % 2 == 0 and numero > 2:
        return [2, numero // 2]
# A busca só vai até a raiz quadrada do número. O '+1' é para garantir que a raiz seja incluída.
    limite_de_busca = int(numero**0.5) + 1
# Começamos a busca a partir de 3, e pulamos de 2 em 2. Assim, só testamos números ímpares.
    for i in range(3, limite_de_busca, 2):
# Encontramos o primeiro divisor se o resultado do módulo for 0.
        if numero % i == 0:
# O segundo divisor é o resultado da divisão do primeiro número.
            outro_divisor = numero // i
# Encontrando o par a função termina retornando os dois divisores.
            return [i, outro_divisor]
# Se nenhum divisor for encontrado, o número é primo.
    return [1, numero]
''' Primeiramente precisamos ler os números, validar os números e armazenar em um vetor.'''
vet_Glauco = []
print("~~~~~ Bem-vindo(a) ao algorítmo de chave pública RSA! ~~~~~")
print(''' 
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
print("Por gentileza, digite quantos números inteiros positivos quiser.")
print("Digite -1 para encerrar a entrada de dados.")
while True:
# Aqui tentamos converter a entrada do usuário para um número inteiro.
    entrada_do_usuario = input("Digite um número: ")
    try:
        numero = int(entrada_do_usuario)
# Verificamos a condição de parada do loop.
        if numero == -1:
            print("Sinal de parada recebido (-1). Entrada de dados finalizada.")
            break 
# Verificamos se o número é positivo e maior que 1.
        elif numero <= 1:
            print(f"O número {numero} não é válido. Por favor, insira um número inteiro positivo maior que 1 ou -1 para terminar.")
# Verificamos se o número já foi inserido.
        elif numero in vet_Glauco:
            print(f"O número {numero} já foi inserido anteriormente. Por favor, insira um número diferente ou -1 para terminar.")
# Se todas as validações forem passadas, adicionamos o número ao vetor.
        else: 
            vet_Glauco.append(numero)
            print(f"Número {numero} adicionado com sucesso.")
# Este bloco é executado se o 'int()' falhar.
    except ValueError:
        print(f"Entrada '{entrada_do_usuario}' é inválida. Por favor, tente novamente.")
print("~~~ Leitura de dados concluída. Processando os resultados. ~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("     Resultados Finais")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Se o usuário não inseriu nenhum número, informamos e encerramos o programa.
if not vet_Glauco:
    print("Nenhum número foi inserido para processamento. \n Encerrando o programa.")
# Esse loop é para passar por cada "item" na lista 'vet_Glauco' e encontrar seus divisores.
else:
    for item in vet_Glauco:
        lista_de_divisores = encontrar_divisores(item)
# Convertemos a lista de divisores em uma string formatada para exibição.
        texto_formatado = " e ".join(map(str, lista_de_divisores))
        print(f"{item} tem divisores {texto_formatado}.")
# Agora geramos o arquivo com os resultados com formato CSV.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Gerando arquivo de resultados...")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Se o usuário não inseriu nenhum número, informamos e encerramos o programa.
if not vet_Glauco:
    print("Nenhum número foi inserido para processamento. \n Nenhum arquivo será gerado.")
# Aqui definimos o nome do arquivo.
else:
    nome_arquivo_csv = "relat_glauco.csv"
# Abrimos o arquivo em modo de escrita ("w").
    with open(nome_arquivo_csv, "w") as arquivo:
# Verificamos cada número novamente. 
        for item in vet_Glauco:
# Encontramos os divisores do número atual.
            lista_de_divisores = encontrar_divisores(item)
# Formatamos a lista de divisores para o formato CSV
            divisores_csv = ",".join(map(str, lista_de_divisores))
# Montamos a linha que será escrita no arquivo.
            linha_csv = f"{item},{divisores_csv}\n"
# Escrevemos a linha no arquivo.            
            arquivo.write(linha_csv)
    print(f"Relatório CSV '{nome_arquivo_csv}' gerado com sucesso!")

print("~~~~~ Fim do programa. Obrigado por usar! ~~~~~")
