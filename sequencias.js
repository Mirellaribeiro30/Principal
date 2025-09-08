function contar() {
    // Obtém os campos do HTML usando o ID
    let startNumber = document.getElementById("start"); // campo de início
    let endNumber = document.getElementById("end");     // campo de fim
    let stepNumber = document.getElementById("step");   // campo de passo
    let result = document.getElementById("result");     // área de exibição do resultado

    // Verifica se algum campo está vazio
    if (
        startNumber.value.length === 0 ||
        endNumber.value.length === 0 ||
        stepNumber.value.length === 0
    ) {
        result.innerHTML = "⚠️ Por favor, preencha todos os campos para iniciar a contagem."; // alerta ao usuário
        return; // encerra a função
    }

    // Converte os valores para números inteiros
    let i = Number(startNumber.value); // valor inicial
    let f = Number(endNumber.value);   // valor final
    let p = Number(stepNumber.value);  // passo da contagem

    // Verifica se o passo é zero ou negativo
    if (p <= 0) {
        alert("⚠️ O passo deve ser maior que 0. Considerando passo = 1."); // mostra alerta
        p = 1; // define passo como 1
    }

    result.innerHTML = "Contando: <br>🏠 "; // mensagem inicial e emoji de início

    // Se o valor inicial for menor que o final → contagem crescente
    if (i < f) {
        for (let c = i; c <= f; c += p) {
            result.innerHTML += `${c} ✌🏻 `; // adiciona número + emoji ✌🏻
        }
    }
    // Caso contrário → contagem regressiva
    else {
        for (let c = i; c >= f; c -= p) {
            result.innerHTML += `${c} ✌🏻 `; // adiciona número + emoji ✌🏻
        }
    }

    result.innerHTML += "🏁"; // emoji de bandeira para indicar o fim
}
function contar() {
    // Obtém os elementos de entrada do HTML
    var startNumber = document.getElementById("start"); // campo de início
    var endNumber = document.getElementById("end");     // campo de fim
    var stepNumber = document.getElementById("step");   // campo de passo
    var result = document.getElementById("result");     // div onde o resultado aparece

    // Verifica se algum dos campos está vazio
    if (startNumber.value.length == 0 || endNumber.value.length == 0 || stepNumber.value.length == 0) {
        result.innerHTML = "⚠️ Por favor, preencha todos os campos para iniciar a contagem."; // mensagem de erro
    } else {
        result.innerHTML = "Contando: <br>"; // limpa e inicia o texto
        result.innerHTML += "🏠 "; // emoji de início

        // Converte os valores para números
        let i = Number(startNumber.value); // valor de início
        let f = Number(endNumber.value);   // valor de fim
        let p = Number(stepNumber.value);  // valor de passo

        // Verifica se o passo é zero ou negativo
        if (p <= 0) {
            window.alert("⚠️ O valor do passo deve ser maior que zero. Considerando passo 1."); // alerta
            p = 1; // define passo como 1
        }

        // Se o início for menor que o fim, faz contagem crescente
        if (i < f) {
            for (let c = i; c <= f; c += p) {
                result.innerHTML += `${c} ✌🏻 `; // exibe os números com emoji ✌🏻
            }
        } else {
            // Se início for maior, faz contagem regressiva
            for (let c = i; c >= f; c -= p) {
                result.innerHTML += `${c} ✌🏻 `; // exibe os números com emoji ✌🏻
            }
        }

        result.innerHTML += `🏁`; // finaliza com bandeira quadriculada
    }
}
