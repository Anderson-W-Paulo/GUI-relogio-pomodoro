import tkinter as tk
import ttkbootstrap.constants
import ttkbootstrap as ttkb

class Aplicacao:
    def __init__(self, master=None):
        self.fonte_textos = ('URW Bookman L', '11') #fonte padrão para uso

        self.container1_pratico = tk.Frame(master) #divisão de frame, container para organizar na tela
        self.container1_pratico.place(x=50, y=18)  #.place() trás praticidade de escolher o pixel
        self.container1_tempo = tk.Frame(master)
        self.container1_tempo.place(x=32, y=55)

        #CONTAINER DESCANSO E TEMPO DESCANSO
        self.container2_descanso = tk.Frame(master)
        self.container2_descanso.place(x=223, y=18)
        self.container2_tempo = tk.Frame(master)
        self.container2_tempo.place(x=212, y=55)

        self.container1_butao = tk.Frame(master)
        self.container1_butao.place(x=137, y=146)


        #PRÁTICO
        self.txt_container1_pratico = tk.Label(self.container1_pratico, text='PRÁTICO', font=self.fonte_textos, width=8)
        self.txt_container1_pratico.pack()

        #HORA/MINUTO/SEGUNDO ABAIXO DO CONTAINER PRÁTICO
        self.entrada_hora_pratico = ttkb.Entry(self.container1_tempo, bootstyle='success', font=('', '24'), width=2)
        self.entrada_hora_pratico.pack(side=tk.LEFT)
        self.dois_pontos_pratico = tk.Label(self.container1_tempo, text=':', font=('URW Bookman L', '12', 'bold'))
        self.dois_pontos_pratico.pack(side=tk.LEFT)
        self.entrada_minuto_pratico = ttkb.Entry(self.container1_tempo, bootstyle='success', font=('', '24'), width=2)
        self.entrada_minuto_pratico.pack(side=tk.LEFT)
        #self.dois_pontos_pratico2 = tk.Label(self.container1_tempo, text=':', font=self.fonte_textos)
        #self.dois_pontos_pratico2.pack(side=tk.LEFT)
        #self.entrada_segundo_pratico = ttkb.Entry(self.container1_tempo, bootstyle='success', width=2)
        #self.entrada_segundo_pratico.pack(side=tk.LEFT)

        #DECANSO
        self.txt_container2_descanso = tk.Label(self.container2_descanso, text='DESCANSO', font=self.fonte_textos,width=10)
        self.txt_container2_descanso.pack()

        #HORA/MINUTO/SEGUNDO ABAIXO DO CONTAINER DESCANSO
        self.entrada_hora_descanso = ttkb.Entry(self.container2_tempo, bootstyle='success', font=('', '24'), width=2)
        self.entrada_hora_descanso.pack(side=tk.LEFT)
        self.dois_pontos_descanso = tk.Label(self.container2_tempo, text=':', font=('URW Bookman L', '12', 'bold'))
        self.dois_pontos_descanso.pack(side=tk.LEFT)
        self.entrada_minuto_descanso = ttkb.Entry(self.container2_tempo, bootstyle='success', font=('', '24'), width=2)
        self.entrada_minuto_descanso.pack(side=tk.LEFT)
        #self.dois_pontos2_descanso = tk.Label(self.container2_tempo, text=':', font=self.fonte_textos)
        #self.dois_pontos2_descanso.pack(side=tk.LEFT)
        #self.entrada_segundo_descanso = ttkb.Entry(self.container2_tempo, bootstyle='success', width=2)
        #self.entrada_segundo_descanso.pack(side=tk.LEFT)

        #BUTÃO INICIAR
       # style = ttkb.Style()
        #style.configure('Bold.TButton', font=('URW Bookman L', '11', 'bold'))
        self.botao_iniciar = ttkb.Button(self.container1_butao, text='INICIAR', bootstyle=ttkb.SUCCESS,   width=9)
        self.botao_iniciar.pack(side=tk.TOP)






root = ttkb.Window(themename='darkly') #executar, permite widgets possam ser executados na aplicação
root.title(' POMODORO')
root.geometry('375x190')

# Bloqueia o redimensionamento (horizontal=False, vertical=False)
root.resizable(False, False)

#botao1 = ttkb.Button(text='INICIAR', bootstyle= ttkb.SUCCESS)
#botao1.pack(side=tk.TOP)
Aplicacao(root)
root.mainloop() #event loop
