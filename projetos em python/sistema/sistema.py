import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox

#--------funções---------

def adicionar_tarefa():
    tarefa = tarefa_entrada.get()
    if tarefa:
         liste_tarefas.insert(0,tarefa)
         tarefa_entrada.delete(0,END)
         salve_tarefas()
    else:
        messagebox.showerror('erro','Digite uma Tarefa !')
        
def apagar_tarefa():
    selecionada = liste_tarefas.curselection()
    if selecionada:
        liste_tarefas.delete(selecionada[0])
        salve_tarefas()
    else:
        messagebox.showerror('Erro','Escolha uma tarefa para deletar')
        
def salve_tarefas():
     with open('sistema.txt','w') as f:
         tarefas = liste_tarefas.get(0,END)
         for x in tarefas:
            f.write(x +'\n') 

def carregar_sistema():
     with open('sistema.txt','r') as f:
         tarefas = f.readlines()
         for x in tarefas:
             liste_tarefas.insert(0,x.strip())  
         
        
#interface---------------

janela = ctk.CTk('#4287f5')
janela.minsize(350,450)
janela.maxsize(350,500)
janela.title('Lista de Tarefas V1.0')

#-------- Reserva de Fontes -----

font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')

#-------------------------

ctk.CTkLabel(janela,text='Lista de Tarefas V1.0',font=font1,text_color='white',).pack(pady=10)

add_botao = ctk.CTkButton(janela,text='Adicionar Tarefas',font=font2, text_color='white', fg_color='green',cursor='pirate',corner_radius=5,width=120,command=adicionar_tarefa)
add_botao.place(x=10,y=80)

remove_botao = ctk.CTkButton(janela,text='Remover Tarefas',font=font2,text_color='white',fg_color='#900C3F',cursor='pirate',corner_radius=5,width=120,command=apagar_tarefa)
remove_botao.place(x=185,y=80)

tarefa_entrada = ctk.CTkEntry(janela,font=font2,text_color='black',fg_color='white',border_color='white',width=250,
                              placeholder_text='Digite a sua Tarefa')
tarefa_entrada.place(x=70,y=130)

liste_tarefas = Listbox(janela,width=45,height=10,font=font3)
liste_tarefas.place(x=18,y=180)

carregar_sistema()
janela.mainloop()