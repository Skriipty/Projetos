class Tratamento:
    def __init__(self, nome_cliente, modelo_celular,
                  senha_do_celular, problemas_adicionais) -> None:
           self.nome_cliente = nome_cliente
           self.modelo_celular = modelo_celular
           self.senha_do_celular = senha_do_celular
           self.problemas_adicionais = problemas_adicionais

    def cliente(self, dado) -> str:
        if dado == 0: ((f"{self.nome_cliente}"))
        elif dado == 1: (f"{self.modelo_celular}")    
        elif dado == 2: (f"{self.senha_do_celular}")\
        
        return dado
        
    def problemas(self) -> list:
         pass