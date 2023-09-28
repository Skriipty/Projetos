from Variaveis import dict_problemas

class AdicionarCelular:
    def select_prob() -> int:
        problema = int(input('\n\nQual o problema do dispositivo?\n\n'
                '(01)Dispositivo Apagado (02)Bateria   (03)Tela\n' 
                '(04)Camera Traseira     (05)Placa     (06)Áudio\n' 
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
    
            tem = int(input('Adicionar Problemas? (1)Sim (2)Não\n:'))

            if tem == 1:

                prob_adicionais.append(AdicionarCelular.select_prob())

            else:
                problemas += 1

                return prob_adicionais

    def procurar_problemas(self, prob_adicionais: list):
        
        todos_problemas = []
        for achado_int in prob_adicionais:
            
            if achado_int <= 17:
                achado_str = dict_problemas[achado_int]
                todos_problemas.append(achado_str)
                print('\n', achado_str)
            
            else:
                print('*Opção selecionada não disponivel*')
        
        return todos_problemas