import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox


#interface---------------

janela = ctk.CTk('#4287f5')
janela.minsize(500,550)
janela.maxsize(500,800)
janela.title('Sistema de Orçamento')

#-------- Reserva de Fontes -----

font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')

#-------------------------

ctk.CTkLabel(janela,text='Lista de Tarefas V1.0',font=font1,text_color='white',).pack(pady=10)

sistema_entrada = ctk.CTkEntry(janela,font=font2,text_color='black',fg_color='white',border_color='white',width=250,
                              placeholder_text='Digite a sua ')
sistema_entrada.place(x=70,y=130)