var idade = 67 //Essa linha está criando uma variável chamada idade e atribuindo o valor 67 a ela. Ou seja, a variável idade agora guarda o valor 67, que pode ser usado em outras partes do código.
console.log(`Você tem ${idade} anos.`) //Ela exibe uma mensagem no console que informa a idade da pessoa, usando o valor da variável idade.
if (idade < 16) {
    console.log("Não vota.") //Esse código verifica se a variável idade é menor que 16 e, se for verdadeira a condição, ele executa o código dentro do bloco {} — que, no caso, exibe uma mensagem no console.
} else if (idade < 18 || idade > 65) { //Esse código verifica se a variável idade é menor que 16 e, se for verdadeira a condição, ele executa o código dentro do bloco {} — que, no caso, exibe uma mensagem no console.
        console.log("Voto opcional.") //Ela exibe uma mensagem no console do navegador (ou do ambiente de execução JavaScript, como o Node.js) com o texto "Voto opcional.".
    } else {
        console.log("Voto obrigatório.") //Essa parte é o bloco final de uma estrutura condicional if-else, e sua função é executar o código dentro das chaves {} quando todas as condições anteriores (do if ou else if) não forem verdadeiras.
    }