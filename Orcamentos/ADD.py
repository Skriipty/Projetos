class AdicionarCelular:
    def __init__(self, nome_cliente, modelo_celular, senha):
        self.nome_cliente = nome_cliente
        self.modelo_celular = modelo_celular
        self.senha = senha
    
    def select_prob() -> int:
        problema = int(input('\n\nQual o problema do dispositivo?\n\n'
                '(01)Dispositivo Apagado (02)Bateria   (03)Tela\n' 
                '(04)Camera Trazeira     (05)Placa     (06)Áudio\n' 
                '(07)Camera Frontal      (08)Microfone (09)Carcaça\n'
                '(10)Conector de Carga   (11)Botões    (12)Touch\n'
                '(13)Conector de Fone    (14)Chip      (15)Wi-Fi\n'
                '(16)Marcas de Mal Uso   (17)Molhado\n\n'
                'Escolha uma opção: '))
        
        return problema
    
    def adiciona_problemas(self):
        problemas = 0
        prob_adicionais = []
        while(problemas != 1):
    
            tem = int(input('(1)Sim (2)Não\n'
                'Problemas Adicionais?\n'))

            if tem == 1:

                prob_adicionais.append(AdicionarCelular.select_prob())
    
            else:
                problemas += 1
                print(prob_adicionais)


