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