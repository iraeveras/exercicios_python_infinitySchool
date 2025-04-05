/*
Atividade 03
Crie um código que peça ao usuário para adivinhar um número
entre 1 e 10, repetindo o pedido até que o usuário acerte. Defina
o número a ser adivinhado diretamente no código.

Objetivo:
Aprender a utilizar a estrutura de repetição while (true) para
criar um jogo simples de adivinhação.
*/
export function jogoAdivinheNumero() {    
    let numeroSecreto = 4
    
    alert("Adivinhe o nemuro secreto")
    
    let tentativa = 0
    // while (tentativa >= 0 === 10) {
    //     tentativa = parseInt(prompt("Digite seu palpite: "))
    //     if (tentativa === numeroSecreto) {
    //         alert("Parabéns, voce acertou!")
    //         break
    //     } else {
    //         alert("Errado, tente novamente.")
    //     }
    // }
    
    for (let tentativa = 0; tentativa >= 0 || tentativa === 10; tentativa++) {
        tentativa = parseInt(prompt("Digite seu palpite: "))
        if (tentativa === numeroSecreto) {
            alert("Parabéns, voce acertou!")
            break
        } else {
            alert("Errado, tente novamente.")
        }    
    }
}