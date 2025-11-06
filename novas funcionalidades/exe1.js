const notas = [10,9,8,7,6,5,4,3,2,1]
media = 0
soma = 0
quant = 0
notas.forEach(function(notas,indice){
    soma += notas
    if(notas >= 7){
        quant++
    }
    if(indice %2 == 0){
        console.log(`As notas nas posições pares são ${notas}`)
    }
})

media = soma/notas
console.log(`As notas são: ${notas}`)
console.log(`A soma das notas é ${soma}`)
console.log(`A quantidade de alunos aprovados é ${quant}`)
