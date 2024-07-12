def exercicio1():
    a1 = 2
    a2 = 2
    a3 = a1 + a2
    print(f"texto concatenado com a soma {a3}")

def exercicio2():
    n1 = int(input("coloque o primeiro número: "))
    n2 = int(input("coloque o segundo número: "))
    soma = n1 + n2
    multi = n1 * n2
    divi = n1 / n2
    sub = n1 - n2
    print(f"A soma é igual a {soma}\n a multiplicação é {multi}\n a divisão é {divi}\n e a subtração é {sub}\n")

def exercicio3():
    nome = input("nome: ")
    idade = int(input("idade: "))
    print(f"seu nome é {nome}, sua idade é {idade}")

    n1 = int(input("coloque o primeiro número: "))
    n2 = int(input("coloque o segundo número: "))
    r = n1 + n2
    print(f"o usuário {nome} fez a soma de {n1} e {n2} e obteve o resultado de {r}")

def exercicio4():
    nome = input("digite o nome: ")
    mat = float(input("coloque a nota de matemática: "))
    port = float(input("coloque a nota de português: "))
    geo = float(input("coloque a nota de geografia: "))
    hist = float(input("coloque a nota de história: "))
    fis = float(input("coloque a nota de física: "))

    media = (mat + port + geo + hist + fis) / 5
    print(f"o aluno {nome} obteve a média {media:.2f}")

    if media > 5:
        print("aprovado! Aproveite as férias")
    else:
        print("reprovado :(")

    print(f"notas\n Matemática: {mat}\n{14*'-'}\nPortuguês: {port}\n{14*'-'}\nGeografia: {geo}\n{14*'-'}\nHistória: {hist}\n{14*'-'}\nFísica: {fis}\n{14*'-'}\nMédia: {media:.2f}")
def exercicio5():
    num=int(input("digite o número"))

    if num % 2 == 0:
        print(f"o número {num} é par")
    else:
        print(f"o número {num} é impar")

def exercicio6():
    max=200
    usu=float(input("digite o seu peso"))
    carga=float(input("digite o peso da carga"))
    PTotal= usu+carga

    if PTotal>max:
        print("peso excedente")
    else:
        print("autorizado")

def exercicio7():
    nome=str(input("digite seu nome").upper())
    idade=int(input("digite sua idade"))
    cpf=str(input("digite seu CPF"))
    n1=float(input("nota do primeiro bimestre"))
    n2=float(input("nota do segundo bimestre"))
    n3=float(input("nota do terceiro bimestre"))
    n4=float(input("nota do quarto bimestre"))
    media=(n1+n2+n3+n4)/4


    if idade<18:
        print("somente para os responsáveis")
    else:
        if media>=7:
            print(f"o aluno {nome} foi aprovado com a média de {media:.2f}")
        elif media>=5:
            print(f"o aluno {nome} está de recuperação com a média de {media:.2f}")
        else:
            print(f"o aluno {nome} está reprovado com a média de {media:.2f}")

def exercicio8():
    idade=(input("qual sua idade?"))
    idade = int(idade) 

    altura=(input("qual sua altura?")).replace(',','.')
    altura=float(altura)

    if idade<12 or altura<1.20:
        print("não pode ir :(")
    else:
        print("pode ir :D")

def exercicio9():
    print('Responda o seguinte questionario apenas com "sim" ou "não"')
    humor = input("Você acordou de bom humor? ")
    pai = input("Seu pai chegou em casa?")


    # if humor == "sim" || "Sim" || "s" and pai == "sim":
    if humor == "sim" or humor == "Sim" or humor == "s" or humor=="S" and pai == "sim" or pai == "Sim" or pai == "s" or pai == "S":
        print("Você pode ir a praia")
    else:
        print("Você não pode ir a praia")

def exercicio10():
    peso = str(input('Informe o seu peso em kg: ')).replace(',','.')
    altura = str(input('Informe a sua altura em metros: ')).replace(',','.')

    imc = float(peso) / float(altura)**2

    peso_ideal = 20

    if peso > peso_ideal:
        print("Acima do peso")
    elif peso == peso_ideal:
        print("Peso ideal!")
    else:
        print("Abaixo do peso")

def exercicio11():
    nome = input('Informe o seu nome: ')
    peso = str(input('Informe o seu peso em kg: ')).replace(',','.')
    altura = str(input('Informe a sua altura em metros: ')).replace(',','.')

    imc = float(peso) / float(altura)**2


    print(f'Valor do IMC: {imc:,.2f}.')

    # verifica o imc e retorna o diagnóstico
    if imc < 17:
        print(f'{nome} está com anorexia.')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso.')
    elif imc < 25:
        print(f'{nome} está no peso ideal.')
    elif imc < 30:
        print(f'{nome} está acima do peso.')
    elif imc < 35:
        print(f'{nome} está com grau de obesidade I.')
    elif imc < 40:
        print(f'{nome} está com grau de obesidade II.')
    else:
        print(f'{nome} está com grau de obesidade mórbida.')

def exercicio12():
    while True:
        nome = input('Informe o seu nome ou deixe em branco para sair: ')
        

        if nome != '':
            peso = str(input('Informe o seu peso em kg: ')).replace(',','.')
            altura = str(input('Informe a sua altura em metros: ')).replace(',','.')
            imc = float(peso) / float(altura)**2

            if imc < 17:
                print(f'{nome} está com anorexia.')
            elif imc < 18.5:
                print(f'{nome} está abaixo do peso.')
            elif imc < 25:
                print(f'{nome} está no peso ideal.')
            elif imc < 30:
                print(f'{nome} está acima do peso.')
            elif imc < 35:
                print(f'{nome} está com grau de obesidade I.')
            elif imc < 40:
                print(f'{nome} está com grau de obesidade II.')
            else:
                print(f'{nome} está com grau de obesidade mórbida.')
        else:
            break # encerra o loop

def exercicio13():
    import os

    while True:
        idade = input("Digite sua idade: ")
        idade = int(idade)
        print(f"{25*'-'}cinesenai{25*'-'}\nsala 1: Minecraft: O filme do Jogo (aventura) -10 anos\nsala 2: Especial de natal do podpah (terror) -21 anos\nsala 3: Git push (suspense) -14 anos\nsala 4: Smurfs 7 (infantil) -L\nSala 5: Valorant O filme (adulto) -18\n{25*'-'}cinesenai{25*'-'}")
        e = input("Digite a sala com o filme desejado(deixe em branco para sair):")

        if e != '':
            e = int(e)  

            if e == 1 and idade >= 10:
                print("Filme: Minecraft: O filme do Jogo. Aproveite o filme!")
            elif e == 2 and idade >= 21:
                os.system('cls')
                print("Filme: Especial de natal do podpah. Aproveite o filme!")
            elif e == 3 and idade >= 14:
                os.system('cls')
                print("Filme: Git push. Aproveite o filme!")
            elif e == 4:
                print("Filme: Smurfs 7. Aproveite o filme!")
            elif e == 5 and idade >= 18:
                os.system('cls')
                print("Filme: Valorant O filme. Aproveite o filme!")
            else:
                print("Você não tem idade para assistir esse filme ou sala inválida!")
        else:
            break

def exercicio14():
#arvore de natal
    alt=20
    espacamento=0
    asterisco=1
    simbolo='*'

    for i in range(alt,):
        espacamento=alt-i-1

        for j in range(espacamento):
            print(' ', end='')
        
        for k in range(asterisco):
            print(simbolo, end='')
        print()
        asterisco+=2

def exercicio15():
    from random import random, randint, choice
    import os


    lista=[]
    lista_sorteados=[]
    while True:
        nome = input("Digite os nomes que serão sorteado: ")
        if nome !='':
            lista.append(nome)
        else:
            break

    while True:
        if lista:
            os.system('cls')
            premiado=choice(lista)
            lista_sorteados.append(premiado)
            lista.pop(premiado)

            print(f'o premiado da vez foi {premiado}')
            opcao= input(f'deseja ralizar um novo sorteio? (s/n)').lower()
            os.system('cls')
            

            if opcao !='s':
                break
        else:
            print("não existem nomes para serem sorteados!")
    print("sistema finalizado")
    print(lista)
    print(lista_sorteados)

def exercicio16():
    from random import random, randint, choice
    import os

    ns=randint(1,10000)

    tentativas=0
    max=1000
    acertou=False

    print(f'vc possui {max} tentativas apaa acertar o número secreto entre 1 e 10')

    #lógica de contagem de tentativas
    while tentativas<max:
        palpite=int(input('digite um número: '))
        tentativas+=1

        if palpite==ns:
            acertou=True
            break
        elif palpite<ns:
            print("tente um número maior")
        else:
            print('tente um número menor')
    if acertou:
        print(f'Parabns! vc acertou o número secreto {ns} com {tentativas} tentativas')
    else:
        print(f'que pena, vc não acertou o número secreto {ns}')

def exercicio17():
    nome=["henrique","pedro","matheus","leonardo","henrique"]

    for i in range(len(nome)):
        print(f'{i+1}° nome da lista é: {nome[i]}')

    novon=input('digite o novo nome á adicionar: ')

    p=input("digite a posição que deseja colocar nesse nome: ")
    p=int(p)


    #corrigindo a posição
    p-=1

    if p>=0 and p<=len(nome):
        nome.insert(p, novon)
    else: 
        print("posição invalida")

    #mostra lista atualizada
    print()
    print(30*'=', 'lista atualizada', 30*'=')

    for i in range(len(nome)):
        print(f'{i+1}° nome da lista é: {nome[i]}')

exercicios = {
    1: exercicio1,
    2: exercicio2,
    3: exercicio3,
    4: exercicio4,
    5: exercicio5,
    6: exercicio6,
    7: exercicio7,
    8: exercicio8,
    9: exercicio9,
    10: exercicio10,
    11: exercicio11,
    12: exercicio12,
    13: exercicio13,
    14: exercicio14,
    15: exercicio15,
    16: exercicio16,
    17: exercicio17,
}

def executar_exercicio(numero):
    exercicio = exercicios.get(numero)
    if exercicio:
        exercicio()
    else:
        print("Exercício não encontrado.")

def main():
    while True:
        try:
            numero = int(input("Digite o número do exercício que deseja executar (ou 0 para sair): "))
            if numero == 0:
                break
            executar_exercicio(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()