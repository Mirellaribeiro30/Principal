function exibirSaudacao() {
    const agora = new Date();
    const hora = agora.getHours();
    const saudacao = document.getElementById('saudacao');
    const imagem = document.getElementById('imagem');

    if (hora >= 6 && hora < 12) {
        saudacao.textContent = "Bom dia!";
        imagem.src = "manhã.png"; 
    } else if (hora >= 12 && hora < 18) {
        saudacao.textContent = "Boa tarde!";
        imagem.src = "tarde.png"; 
    } else {
        saudacao.textContent = "Boa noite!";
        imagem.src = "noite.png"; 
    }
}

window.onload = exibirSaudacao;