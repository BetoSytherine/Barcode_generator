from barcode import EAN13
from barcode.writer import ImageWriter # para salvar em png
import random
import string
"""dicio = {'nome': 'Erick'}

# Atualiza o elemento de chave 'nome'
dicio.update({'nome':'Matheus'})
iddd = 18
# Cria os elementos de chave 'idade' e 'tamanho'
dicio.update({'idade':iddd})
dicio.update(tamanho=1.60)

print(dicio)
"""
carrinho=[]
produto= input('Digite o nome de um produto: ')
preco = float(input("Digite o valor desse produto:"))

produto_cadastrado = {'Produto': produto, 'preco1': preco}


print(f' O produto {produto} foi cadastrado com o preço de {preco}')
print()
print("Deseja gerar o codigo de barra para esse produto? ")
resposta = int(input("Digite 1 para sim e 2 para não: "))
if resposta == 1: 
    
    palavra = string.digits

    tamanho = 12
    codigobar = ""
    for i in range(tamanho):
        codigobar+=random.choice(palavra)
        
        
    codigo_barra = EAN13(codigobar, writer=ImageWriter()) # writer para salvar em png
    codigo_barra.save(produto) 
else:
        print("Agradecemos a preferencia!!")