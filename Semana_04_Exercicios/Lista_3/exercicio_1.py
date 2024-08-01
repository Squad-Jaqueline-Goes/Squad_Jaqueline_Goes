"""
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
          "Telefonou para a vítima?"
          "Esteve no local do crime:"
          "Mora perto da vítima?"
          "Devia para a vítima?"
          "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões, ela deve ser
classificada como "Suspeita"; entre 3 e 4, como "Cúmplice" e 5, como
"Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

# ista de perguntas
lista_perguntas = ["Telefonou para a vítima? ",  
          "Esteve no local do crime: ",  
          "Mora perto da vítima? ", 
          "Devia para a vítima? ", 
          "Já trabalhou com a vítima? "]

# quantidades de respostas sim/nao
quant_sim = 0
quant_nao = 0

# perguntas para o usuario
for perguntas in lista_perguntas:
          print("\n" + perguntas)
          resp = input("Responda 's', para sim, ou 'n', para não: ")
          
          # contador de respostas
          if resp.lower() == "s":
                    quant_sim = quant_sim + 1
          elif resp.lower() == "n":
                    quant_nao = quant_nao + 1
          else:
                    print("Responda o que foi pedido, por favor!")
      
# classificação     
if (quant_sim < 2):
          classe = "Inocente"
elif(quant_sim == 2):
          classe = "Suspeita" 
elif(quant_sim == 5):
          classe = "Assassino"
else:
          classe = "Cúmplice"

# saida de dados
print(f"\nO usuário foi classificado como {classe}") 