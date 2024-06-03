import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox

#--------funções---------

# def adicionar_tarefa():
#     tarefa = tarefa_entrada.get()
#     if tarefa:
#          liste_tarefas.insert(0,tarefa)
#          tarefa_entrada.delete(0,END)
#          salve_tarefas()
#     else:
#         messagebox.showerror('erro','Digite uma Tarefa !')
        
# def apagar_tarefa():
#     selecionada = liste_tarefas.curselection()
#     if selecionada:
#         liste_tarefas.delete(selecionada[0])
#         salve_tarefas()
#     else:
#         messagebox.showerror('Erro','Escolha uma tarefa para deletar')
        
# def salve_tarefas():
#      with open('tarefas.txt','w') as f:
#          tarefas = liste_tarefas.get(0,END)
#          for x in tarefas:
#             f.write(x +'\n') 

# def carregar_tarefas():
#      with open('tarefas.txt','r') as f:
#          tarefas=f.readlines()
#          for x in tarefas:
#              liste_tarefas.insert(0,x.strip())  
         
        
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

ctk.CTkLabel(janela,text='Sistema de Orçamento',font=font1,text_color='white',).pack(pady=10)




texto = ctk.CTkLabel(janela, text='APP calcular consumo em Viagem',text_color='red',font=('verdana',20,'bold'))
texto.pack(padx=10,pady=10)

distancia = ctk.CTkLabel(janela, text='distancia da Viagem:',text_color='red',font=('verdana',20,'bold'))
distancia.pack(padx=10,pady=10)
distancia = ctk.CTkEntry(janela,placeholder_text='Digite a distancia da Viagem ',width=300,height=40,fg_color='white',text_color='black',placeholder_text_color='gray')

distancia.pack(padx=10,pady=10)
consumo = ctk.CTkLabel(janela, text='Consumo da Viagem:',text_color='red',font=('verdana',20,'bold'))
consumo.pack(padx=10,pady=10)
consumo = ctk.CTkEntry(janela,placeholder_text='Digite a consumo da Viagem ',width=300,height=40,fg_color='white',text_color='black',placeholder_text_color='gray')

consumo.pack(padx=10,pady=10)

preco = ctk.CTkLabel(janela, text='Preco da Viagem:',text_color='red',font=('verdana',20,'bold'))
preco.pack(padx=10,pady=10)
preco = ctk.CTkEntry(janela,placeholder_text='Digite a preco da Viagem (R$) ',width=300,height=40,fg_color='white',text_color='black',placeholder_text_color='gray')

preco.pack(padx=10,pady=10)

botao = ctk.CTkButton(janela,text='Calcular Viagem',font=('verdana',20,'bold'),fg_color='gray',hover_color='darkred',height=50)
botao.pack(padx=10,pady=10)

resultado = ctk.CTkLabel(janela,text='',text_color='yellow',font=('verdana',18,'bold'))
resultado.pack(padx=10,pady=10)


    
    
    

janela.mainloop()