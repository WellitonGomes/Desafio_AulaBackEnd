def verifica_pariedade(): #criamos uma função para verificar se os nbumeros são pares ou impares
    Var = int(input("Digite um numero: ")) #estamos pedindo ao usuario para inserir um valor numerico para iniciarmos a comparação
    par = 0 #definimos que par é zero para que o valor que o usuario definir seja colocado no lugar do zero
    impar = 0  #definimos que impar é zero para que o valor que o usuario definir seja colocado no lugar do zero
    for aux in range(Var): #esta linha cria um loop dos numeros para que o codigo possa conta-lo
        if aux % 2 == 0: #estamos definindo que se o valor inserido pelo usuario se quando dividido por 2 o resto da divisão for 0 este numero sera par
            par = par + aux # estamos definindo que a variavel par é igual a par mais a variavel aux assim par recebera o resultado da divisão presente na variavel aux
            print(aux, "é par")#aqui estamos mostrando na tela do usuario que o numero inserido por ele é par, se todos os fatores acima forem validados
        else: #se os fatores acima nao forem validados entao os comandos a baixo serao executados
            impar = impar + aux #impar sera igual a impar mais aux recebendo entao os valores do resto da divisao acima
            print(aux, "é ímpar")#mostraremos na tela do usuario que o numero inserido por ele é impar


def calcula_soma():#criamos uma funcao para realizarmos uma operacao
    Valor1 = int(input("Digite o primeiro numero para uma soma: "))#estamos definindo uma variavel para receber o primeiro valor que sera inserido pelo usuario
    Valor2 = int(input("Digite o segundo numero para uma soma: "))#estamos definindo uma variavel para receber o segundo valor que sera inserido pelo usuario
    Soma = Valor1 + Valor2#estamos definindo uma variavel para receber o resultado da soma dos outros dois valores inseridos a cima pelo usuario
    print("A soma destes dois numeros é:", Soma)#aqui estamos mostrando na tela do usuario o resultado da soma dos dois valores inseridos por ele

def is_prime(numero):#criamos uma funcao que ira verificar se um numero inserido pelo usuario e primo
    if numero < 2:#aqui estamos comparando se o numero que foi inserido pelo usuario é menor que 2
        return False#esta funcao retorna falsa pois por definicao os numeros menores que 2 nao soa primos
    for i in range(2, int(numero ** 0.5) + 1):#nesta linhas iniciamos um loop que vai do numero 2 ate a raiz quadrada do valor inserido pelo usuario e fazendo uma soma de mais 1
        if numero % i == 0:#esta linha de codigo verifica se o numero inserido pelo usuario e divisivel por i que representa todos os numeros de 2 ate a raiz quadrada do numero inserido pelo usuario
            return False#este false indica que o numero nao e primo
    return True#se o numero inserido pelo usuario nao for divisivel por nenhum numero do entre 2 e sua raiz quadrada a funcao retorna verdadeira dizemdo que este e um numero primo

def verifica_primo():#criamos uma funcao para pedir ao usuario um valor para vermos se ele é realmente primo
    numero = int(input("Digite um numero primo: "))#aqui pedimos diretamente ao usuario para que ele digite um valor para coferirmos se ele é primo
    if is_prime(numero):#aqui chamamos a funcao acima desta que e a qual realizara a comparacao para sabermos se o numero e realmente primo
        print("Este numero é primo")#se apos a revisao o numero for realmente primo esta mensagem sera printada mostrando ao usuario que o numero e realmente primo
    else:#se o numero nao passar nos testes de verificacao
        print("Este numero não é primo")#mostramos na tela do usuario que este numero nao é primo

def conta_vogais():#uma funcao que utilizaremos para contarmos as vogais de uma palavra inserida pelo usuario
    palavra = input("Digite uma palavra para contarmos suas vogais: ")#aqui estamos definindo um input para salvarmos a palavra digitada pelo usuario na variavel palavra
    vogais = 'aeiou'  # Define uma string contendo todas as vogais
    palavra = palavra.lower()  # Converte a string para minúsculas para que a comparação não seja sensível a letras maiúsculas e minúsculas dando erro no codigo
    total_vogais = sum(palavra.count(i) for i in vogais)  # Conta o número de vezes que cada vogal aparece na palavra de cada vogal na string e retorna salvando na soma total
    print("Total de vogais:", total_vogais)#se apos todo o processamento acima mostraremos na tela do usuario a quantidade de vogais presentes na palavra digitada por ele


def geral():#aqui temos a funcao geral que rodara todas as outras funcoes
    verifica_pariedade()#uma função para verificar se os nbumeros são pares ou impares
    calcula_soma()#uma funcao para realizarmos uma operacao
    verifica_primo()#uma funcao para pedir ao usuario um valor para vermos se ele é realmente primo
    conta_vogais()#funcao que utilizaremos para contarmos as vogais de uma palavra inserida pelo usuario

geral()#chama varias outras funcoes que realizam todas as funcoes do codigo
