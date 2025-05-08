import os 
os.system("cls")
#IF ENCADEADO -> ESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA

# x = 15 
# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")

# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")

# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO

# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))
# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# idade= int(input("digite sua idade"))
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#ativ classificação boletim
#replace("valor1","valor2") substitui o valor1 pelo valor2
# :.2f -> formata para 2 casa decimais, OBS:APENAS NO fstring
# nota1= float(input("Digite sua nota:"))
# nota2= float(input("Digite sua outra nota:"))
# media= (nota1+nota2)/2
# print(f"MEDIA DO ALUNO: {media:.2f}")
# if media <= 5:
#     print("REPROVADO")
# elif media in (5,6,7):
#     print("EM RECUPERAÇÃO")
# elif media > 7:
#     print("APROVADO")

# #ativ IMC
# print("*"*8,"IMC","*"*8)
# peso= float(input("Digite seu peso:"))
# altura= float(input("Digite sua altura:"))
# imc= round(peso/(altura*altura),2)
# print(f"seu IMC é : {imc} ")
# if imc < 17:
#     print("muito abaixo do peso")
# elif imc >= 17 and  imc<=18.49:
#     print("abaixo do peso")
# elif imc >= 18.5 and imc<=24.9:
#     print("peso normal")
# elif imc >= 25 and imc<=29.99:
#     print("acima do peso")
# elif imc >= 30 and imc<= 34.99:
#     print("obesidade I")
# elif imc >= 35 and imc<= 39.99:
#     print("obesidade II")
# else:
#     print("obesidade III MORBIDA")

#ativ salario
print(r"""     
     /\^/`\   
    | \/   |  
    | |    |  
    \ \    /  
     '\\//'   
       ||     
       ||     
       ||     
       ||  ,  
   |\  ||  |\ 
   | | ||  | |
   | | || / / 
    \ \||/ /  
     `\\//`   
    ^^^^^^^^""")

print("TABELA DE REAJUSTE DE SALARIO")
print("salario até R$2799,99 : aumento 20%")
print("salario entre R$ 2800,00 E R$ 6999,99: aumento 15%")
print("salario entre R$ 7000,00 e R$14999,99: aumento 10% ")
print("salario de R$ 15000,00 em diante: aumento 5%")
print()
salario= float(input("Digite seu salario:"))
valorsal= salario 
aum= valorsal-salario
if salario <= 2799.99:
    valorsal= salario * 1.2
    aum= valorsal - salario 
    print("salario original", salario)
    print("percentual de aumento aplicado 20%")
    print("valor do aumento",aum )
    print("salario atualizado", valorsal)
elif salario <=6999.99:
    valorsal= salario * 1.5
    aum= valorsal - salario 
    print("salario original", salario)
    print("percentual de aumento aplicado 15%")
    print("valor do aumento",aum )
    print("salario atualizado", valorsal)
elif salario <= 14999.99:
    valorsal= salario * 1.1
    aum= valorsal - salario 
    print("salario original", salario)
    print("percentual de aumento aplicado 10%")
    print("valor do aumento",aum )
    print("salario atualizado", valorsal)
else:
    valorsal=salario*1.05
    aum= valorsal - salario 
    print("salario original", salario)
    print("percentual de aumento aplicado 5%")
    print("valor do aumento",aum )
    print("salario atualizado", valorsal)