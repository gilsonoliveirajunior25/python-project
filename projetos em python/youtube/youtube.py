import customtkinter as ctk
import tkinter
from tkinter import *
from pytube import YouTube

#funções --------------

def Downloader():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink,on_progress_callback=em_progresso)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        textofinal.configure(text='Download Completo !')
    except:
        textofinal.configure(text='erro no Download - Link')
        
def em_progresso(stream,x,bytes_restantes):
    tamanho_total = stream.filesize
    bytes_baixados = tamanho_total - bytes_restantes
    porcentagem_completa = (bytes_baixados/tamanho_total)*100
    por = str(int(porcentagem_completa))
    progresso.update()
    progresso.configure(text=f'{por}%')
    #barra de progresso
    barraprogresso.update()
    barraprogresso.set(float(porcentagem_completa)/100)



#-----------------------


ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('800x400')
janela.title('Youtube Downloader V1.1 - by Artur Brasil')

ctk.CTkLabel(janela, text='Youtube Downloader V1.1 - by Artur Brasil',font=('arial',30,'bold')).pack(pady=5)

link = ctk.CTkEntry(janela,placeholder_text='Digite a url do Youtube',width=600,height=50)
link.pack(pady=20)

btn = ctk.CTkButton(janela,text='Downloader Video',font=('arial',25,'bold'),command=Downloader)
btn.pack(pady=5)

titulo = ctk.CTkLabel(janela,text='',font=('arial',18,'bold'),text_color='white')
titulo.pack(pady=5)

progresso = ctk.CTkLabel(janela,text='0%',font=('arial',25,'bold'),text_color='blue')
progresso.pack(pady=3)

barraprogresso = ctk.CTkProgressBar(janela,width=600,height=20,fg_color='white',progress_color='blue')
barraprogresso.set(0)
barraprogresso.pack(pady=5)

textofinal = ctk.CTkLabel(janela,text='',font=('Arial',18,'bold'))
textofinal.pack(pady=5)


janela.mainloop()