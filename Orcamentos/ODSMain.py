from ADD import AdicionarCelular
from Variaveis import dict_problemas

#Dando Entrada no Celular
nome_cliente = input('Nome do cliente: ')

modelo_celular = input('\nModelo do Celular: ')

senha_celular = input('\nSenha Do Cliente: ')

#laço para adicionar problemas
cliente_teste = AdicionarCelular()
prob_adicionais = cliente_teste.adiciona_problemas()
cliente_teste = cliente_teste.procurar_problemas(prob_adicionais)

#variavel que contem todas as info
resumo = [nome_cliente, modelo_celular, senha_celular, cliente_teste]
