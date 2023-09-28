from temp import cliente
class CriaServicos:

    def organiza() -> str:
        display = (f"Cliente: {cliente[0]}\n"
            f"Celular: {cliente[1]}\n"
            f"Senha: {cliente[2]}\n"
            f"Servico requisitado:\n {cliente[3]}")
        return print(display)
        



        