from temp import cliente

class Tratamento:
    def __init__(self) -> None:
           self.nome_cliente = cliente[0]
           self.modelo_celular = cliente[1]
           self.senha_do_celular = cliente[2]
           self.problemas_adicionais = cliente[3]
           self.numero = 0
         
    def dados_cliente(numero):
        if numero == 0:
             return cliente[0]
        elif numero == 1:
             return cliente[1]
        elif numero == 2: 
             return cliente[2]
        
a = Tratamento
a.dados_cliente(1)
