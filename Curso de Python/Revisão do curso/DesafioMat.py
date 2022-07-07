Numero pares
for variavel in range(100):
    if variavel % 2 == 0:
        print(variavel, "é par")

Numeros primos
num=int(input("Digite um numero:"))
contador=1
while contador <= num:
    if num%2==1:
        contador=contador+1
        print("primo")
        break
    else:
        print("não primo")
        break
 Divisibilidade
nun=int(input("Digite um numero:"))
nun2=int(input("Digite o numero para divisão:"))
contador=1
while contador <= 1:
    if nun % nun2 ==0:
        print(f"O {nun} é divisível por{nun2}")
        break
    else:
        print("Não é divisível")
        break

Somar de vetores - não sei faz ainda no python e a criação de função estou aprendendo
# include <iostream>

using
namespace
std;

int
vetor[100], i = 0, soma = 0;

int
main()
{
while (i < 6)
    {
        cout << "Digite o valor da posição: " << endl;
    cin >> vetor[i];
    cout << i << ": " << vetor[i] << endl;
    soma = soma + vetor[i];

    i + +;
    }

    cout << "A soma do vetor é de: " << soma << endl;

    return 0;
}