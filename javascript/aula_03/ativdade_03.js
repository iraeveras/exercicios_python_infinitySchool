let numeroSecreto = 4

alert("Adivinhe o nemuro secreto")

let tentativa
while (true) {
    tentativa = parseInt(prompt("Digite seu palpite: "))
    if (tentativa === numeroSecreto) {
        alert("Parabéns, voce acertou!")
        break
    } else {
        alert("Errado, tente novamente.")
    }
}