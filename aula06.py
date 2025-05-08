import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (mach case) escolha caso (a partir da versão 3.10)
#match valor:
#   case valor:


# linguagem= input("DIGITE A LINGUAGEM:")
# match linguagem:

#     case "python":
#         print("é facil")
#     case "java":
#         print("é dificil")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauã não dorme")
#     case 10:
#         print("entrou aqui")
#     case _: 
#         print("outro caso")

# print("*"*10)
# print("DIA DA SEMANA")
# print("1-segunda")
# print("2-terça")
# print("3-quarta")
# print("4-quinta")
# print("5-sexta")
# print("6-sabado")
# print("7-domingo")

# dia= int(input("DIGITE O Nº DO DIA DA SEMANA : "))
# match dia:
#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")

#ATIV CELULAR
# print("*"*10,"celulares","*"*10)
# print("""
# 1- sansung - r$ 4000.00
# 2- iphone -  r$ 15000.00
# 3- motorola- r$ 2000.00   
# FRETE : SP -> 10.00
#         MG -> 15.00
#         RS -> 20.00""")
# modelo= input("digite o nº do produto :") 
# lugar= input("digite seu estado : ")
# match modelo:
#     case "sansung":
#         match lugar: 
#             case "SP":
#                 print("valor do produto: R$ 4000.00")
#                 print("valor do frete: R$ 10.00")
#                 print("valor total: R$ 4010.00")
#             case "MG":
#                 print("valor do produto: R$ 4000.00")
#                 print("valor do frete: R$ 15.00")
#                 print("valor total: R$ 4015.00")
#             case "RS":
#                 print("valor do produto: R$ 4000.00")
#                 print("valor do frete: R$ 20.00")
#                 print("valor total: R$ 4020.00")
#     case "iphone":
#         match lugar: 
#             case "SP":
#                 print("valor do produto: R$ 15000.00")
#                 print("valor do frete: R$ 10.00")
#                 print("valor total: R$ 15010")
#             case "MG":
#                 print("valor do produto: R$15000.00")
#                 print("valor do frete:R$ 15.00")
#                 print("valor total: R$ 15015.00")
#             case "RS":
#                 print("valor do produto: R$15000.00")
#                 print("valor do frete:R$ 20.00")
#                 print("valor total:R$ 15020.00")
#     case "motorola":
#         match lugar: 
#             case "SP":
#                 print("valor do produto:R$ 2000.00")
#                 print("valor do frete: R$ 10")
#                 print("valor total: R$ 2010.00")
#             case "MG":
#                 print("valor do produto: R$2000.00")
#                 print("valor do frete: R$ 15.00")
#                 print("valor total: R$ 2015.00")
#             case "RS":
#                 print("valor do produto: R$2000.00")
#                 print("valor do frete: R$ 20.00")
#                 print("valor total: R$ 2020.00")

#correção
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

#ati pedra, papel, tesoura

você= input("Escolha entre pedra, papel e tesoura : ")
import random
maquina= random.randint(1,3)

match maquina:
    case _ if maquina==1:
        print("MAQUINA:pedra")
    case _ if maquina==2:
        print("MAQUINA:papel")
    case _ if maquina==3:
        print("MAQUINA:tesoura")

match você:
    case _ if você=="pedra":
        print("VOCÊ:pedra")
        tec=1
    case _ if você=="papel":
        print("VOCÊ:papel")
        tec=2
    case _ if você=="tesoura":
        print("VOCÊ:tesoura")
        tec=3

match tec:
    case _ if tec==1 and maquina==1:
        print("emapate")
    case _ if tec==1 and maquina==2:
        print("venceu")
    case _ if tec==1 and maquina==3:
        print("venceu")
    case _ if tec==2 and maquina==1:
        print("venceu")
    case _ if tec==2 and maquina==2:
        print("empate")
    case _ if tec==2 and maquina==3:
        print("perdeu")
    case _ if tec==3 and maquina==1:
        print("perdeu")
    case _ if tec==3 and maquina==2:
        print("venceu")
    case _ if tec==3 and maquina==3:
        print("empate")
