import os
os.system("cls")
#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE
# in (dentro) -> Se o texto estiver dento do in é uma coisa se não é outra

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#exercicio if Else

# #1
# idade= input("digite a sua idade:")
# if idade == 18: 
#     print("maior") 
# else:
#       print("menor")

# #2
# idade= int(input("digite sua idade: "))
# if idade == 0 or idade > 120:
#         print("idade é invalida")
# else:
#     print("idade valida")


# # #3
# email= input("digite seu email:")
# senha= input("digite seua senha")
# if email  == "python@senai.com": 
#      if senha == "12345678":
#           print("usuario autenticado")
# else:
#       print("usuario ou senha invalido")

#atidade4 maças
# macas= int(input("quantas maças voce quer:"))
# if macas < 12:
#     print("R$0.30")
# else:
#     print("0.25")
# print("TOTAL:")
# total= print(macas * 0.30 or 0.25)

#correção
# qtd= int(input("digite a qtd de maças que deseja: "))
# if qtd < 12 :
#     calc= qtd * 0.30
#     print("você vai pagar: R$ ", calc)
# else:
#     calc= qtd * 0.25
#     print("você vai pagar: R$ ", calc)    

# #ativ5
#upper() -> converte para maiusculo
#lower() -> converte para minusculo
# letra=(input("digite uma letra: "))
# if letra == "a" or letra== "e" or letra== "i" or letra== "o" or letra== "u":
#     print("vogal")
# else:
#     print("consoante")

#ativ6
numero= float(input("digite um numero: "))  
numero1= float(input("digite outro numero: ")) 
if numero<numero1:
    print("maior", numero1)
    print("menor", numero)
else:
    print("maior", numero)
    print("menor",numero1 )

