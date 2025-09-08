let salario = 3300;
let result = 0;
if (salario >= 3500) {
    (result=salario-500) }
else
if (salario >= 3100) {
    result = salario-300}
else
if (salario >= 2500) {
    result = salario-150}
else 
if (salario <= 2499){
    result = "ISENTO"}
console.log("O valor final do salário com descontos é de: " + result)