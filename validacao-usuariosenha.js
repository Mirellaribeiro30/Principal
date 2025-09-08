// Seleciona o formulário e a mensagem
const form = document.getElementById('loginForm');
const message = document.getElementById('message');

// Adiciona um evento de submissão ao formulário
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtém os valores dos inputs
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Valida o usuário e a senha
    if (username === 'admin' && password === '123@456') {
        message.textContent = 'Login bem-sucedido!'; // Mensagem de sucesso
        message.style.color = 'green'; // Cor verde para sucesso
    } else {
        message.textContent = 'Usuário ou senha incorretos.'; // Mensagem de erro
        message.style.color = 'red'; // Cor vermelha para erro
    }
});