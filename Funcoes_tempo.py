import time

class temporizador:
    def __init__(self, hora=0, minuto=0):

        #delimitar valores no construtor (ValueError)
        if not (0 <= hora <= 24):
            raise ValueError('As horas devem estar entre 0 e 24')
        if not (1 <= minuto <= 60):
            raise ValueError('Os minutos devem estar entre 0 e 60')
        self.hora = hora
        self.minuto = minuto

    def contar_minutos(self):
        segundos = (self.minuto * 60)
        while segundos > 0:
            print(f'tempo restante do total de {self.minuto} minutos é: {segundos}')
            time.sleep(1) #espera por 1 segundo
            segundos -= 1
        print('tempo esgotado')

    def contar_horas_minutos(self):
        while self.hora > 0 or self.minuto > 0:
            if self.minuto == 0 and self.hora > 0:
                self.hora -= 1
                self.minuto = 59

            print(f'Hora: {self.hora}, Minuto: {self.minuto}')
            time.sleep(1) # passar para 60 segundos = 1 min
            self.minuto -= 1

        print('tempo esgotado')

try:
    #cria temporizador
    tempo = temporizador(0, 10)
    #tempo.contar_minutos()
    tempo.contar_horas_minutos() #chama função para fazer contagem

    tempo2 = temporizador(0, 10) # vai gerar erro
    tempo2.contar_horas_minutos()
except ValueError as e:
    print('ERRO: ', e)
