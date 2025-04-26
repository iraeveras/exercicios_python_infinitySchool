/*
ATIVIDADE PRÁTICA

Atividade 05
Crie um programa que receba um número n e gere um triângulo
numérico invertido no console usando laços de repetição.

O triângulo deve começar com n números na primeira linha,
diminuindo um número a cada linha até chegar a 1.

Por exemplo, se n = 5, o
resultado no console deve ser:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

Objetivo:
Praticar o uso de laços de repetição aninhados e lógica
condicional para gerar padrões complexos no console.

*/

function numeroTrianguloInvertido() {
    let numeros = 5

    for (let i = numeros; i >= 1; i--) {
        let linha = ""
        for (let j = 1; j <= i; j++) {
            linha += j + " ";
        }

        console.log(linha);
        
    }


}

numeroTrianguloInvertido();