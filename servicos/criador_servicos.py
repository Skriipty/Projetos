from tratamento import Tratamento

class CriaServicos:
    def __init__(self) -> None:
        self.nome = 0
        self.modelo = 1
        self.senha = 2
        


    def organiza(self) -> str:
        nome = Tratamento.cliente(0)
        modelo = Tratamento.cliente(1)
        senha = Tratamento.cliente(2)
        problemas = Tratamento.problemas()

        self.display = (f"Cliente: {nome}\n"
                   f"Celular: {modelo} / Senha : {senha}"
                   f"Servico requisitado:\n {problemas}")
        return self.display
        
    def servicos(self) -> str:
        print(self.display)

