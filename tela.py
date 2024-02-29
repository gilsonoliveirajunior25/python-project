# import tkinter

# def  ola():
#     print('oi tudo bem !!!')
    
# janela = tkinter.Tk()
# janela.geometry('500x300')

# titulo = tkinter.Label(janela,text='Bem vindo ao APP !')
# titulo.pack(padx=10,pady=10)

# botao = tkinter.Button(janela,text='calcular',command=ola)
# botao.pack(padx=10,pady=10)


# janela.mainloop()

#----------------------------------------

import customtkinter as ctkn

ctkn.set_appearance_mode('dark')

janela = ctkn.CTk('yellow')
janela.geometry('500x300')

def clique():
    print('eu nao acredito cara!!')
   

titulo = ctkn.CTkLabel(janela, text='Bem vindo ao APP !!!', text_color='blue', font=('verdana',28))
titulo.pack(padx=10,pady=10)

login = ctkn.CTkEntry(janela,placeholder_text='Digite o seu login',width=250)
login.pack(padx=10,pady=10)

senha = ctkn.CTkEntry(janela,placeholder_text='Digite a sua senha',width=250,show='*')
senha.pack(padx=10,pady=10)

button = ctkn.CTkButton(janela,text='Entrar',command=clique)
button.pack(padx=10,pady=10)

janela.mainloop()