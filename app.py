### 1 - Crie um programa para efetuar a leitura de um número real e apresentar o resultado do cubo deste número.
numero = float(input("Digite um numero: "))

cubo = numero ** 3

print("O cubo do numero é:", cubo)


### 2 - Crie 3 variáveis para armazenar nomes de frutas. Em seguida, concatene-as .
fruta1 = input("Digite uma fruta: ")
fruta2 = input("Digite outra fruta: ")
fruta3 = input("Digite mais uma fruta: ")

resultado = fruta1 + " , " + fruta2 + " e " + fruta3

print("As frutas escolhidas foram: ", resultado)


### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números.
numero1 = input("Digite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")

resultado = numero1 + numero2

print(" resultado da concatenacao:", resultado)


### 4 - Crie uma variável para armazenar a palavra "Python é show". Em seguida, adicione um dado boleano ao final da palavra usando a concatenação e exiba o resultado.
frase= " Python é show "
valor= True
resultado = frase , (valor)
print(resultado)

