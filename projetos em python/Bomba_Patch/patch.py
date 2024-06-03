import customtkinter as ctkn
import os 

janela = ctkn.CTk()
janela.geometry('650x400')
janela.title('Bomba Patch V1.0')

texto = ctkn.CTkLabel(janela,text_color='white',font=('verdana',20,'bold'))
texto.pack(padx=10,pady=10)

desligar = ctkn.CTkLabel(janela,text_color='yellow',font=('verdana',20,'bold'))
desligar.pack(padx=10,pady=10)

reiniciar = ctkn.CTkLabel(janela,text_color='red',font=('verdana',20,'bold'))
reiniciar.pack(padx=10,pady=10)

bloquear = ctkn.CTkLabel(janela,text_color='blue',font=('verdana',20,'bold'))
bloquear.pack(padx=10,pady=10)




