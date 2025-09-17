print("Digite uma sequência de pares(nome,nota)")
print("Para encerrar, digite um nome vazio")


alunos = []
notas = []
aluno = input("Digite o nome do aluno: ")

while aluno != "":
    nota = float(input("Digite a nota o aluno: "))
    alunos.append(aluno)
    notas.append(nota)
    aluno = input("Digite o nome do aluno: ")

for i  in range(len(alunos)):
    print (alunos[i] + " " + str(notas[i]))

media = 0
for l in range(len(notas)):
    media = media + notas[l]

media = media/len(notas)
print("Media da turma = {media}")

print("Busca por notas")
busca = True
while busca:
    nome = input("Digite o nome de um aluno para receber sua nota:")
    
    l=0
    while i<len(alunos) and alunos[i] !=nome:
        l == 1
    if l<len(alunos):
        print(alunos[i]+ " " + str(notas[l]))
    else:
        print("Aluno inexistente")

    cond = input("Quer continuar? (s/n)")
    if cond == "n":
        busca = False