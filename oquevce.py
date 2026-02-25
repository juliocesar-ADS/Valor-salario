import os 
Nome = input("Digite seu nome:");
salario = int(input("digite seu salario:"));
print("seu salario é: ", salario);
if salario <= 3000:
    print(Nome,"voce e clt")
elif salario > 3000 and  salario <= 10000:
    print(Nome,"voce ta na média")
else:
    print(Nome,"voce é rico");