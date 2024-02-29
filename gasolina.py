import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')

janela = ctkn.CTk()
janela.geometry('550x400')
janela.iconbitmap('nada.ico')

janela.title('Combustivel APP 2024 do Gilson')

def calcular():
    d = int(distancia.get())
    
    c = int(consumo.get())
    
    p = float(preco.get())
    
    valor = (d/c)*p
    
    resultado.configure(text=f'O Gasto total da Viagem foi R${valor:.2f}')


texto = ctkn.CTkLabel(janela, text='APP calcular consumo em Viagem',text_color='red',font=('verdana',20,'bold'))
texto.pack(padx=10,pady=10)

distancia = ctkn.CTkLabel(janela, text='distancia da Viagem:',text_color='red',font=('verdana',20,'bold'))
distancia.pack(padx=10,pady=10)
distancia = ctkn.CTkEntry(janela,placeholder_text='Digite a distancia da Viagem ',width=300,height=40,fg_color='white',text_color='black'
                          ,placeholder_text_color='gray')

distancia.pack(padx=10,pady=10)
consumo = ctkn.CTkLabel(janela, text='Consumo da Viagem:',text_color='red',font=('verdana',20,'bold'))
consumo.pack(padx=10,pady=10)
consumo = ctkn.CTkEntry(janela,placeholder_text='Digite a consumo da Viagem ',width=300,height=40,fg_color='white',text_color='black'
                          ,placeholder_text_color='gray')

consumo.pack(padx=10,pady=10)

preco = ctkn.CTkLabel(janela, text='Preco da Viagem:',text_color='red',font=('verdana',20,'bold'))
preco.pack(padx=10,pady=10)
preco = ctkn.CTkEntry(janela,placeholder_text='Digite a preco da Viagem (R$) ',width=300,height=40,fg_color='white',text_color='black'
                          ,placeholder_text_color='gray')

preco.pack(padx=10,pady=10)

botao = ctkn.CTkButton(janela,text='Calcular Viagem',font=('verdana',20,'bold'),fg_color='gray',hover_color='darkred',height=50,command=calcular)
botao.pack(padx=10,pady=10)

resultado = ctkn.CTkLabel(janela,text='',text_color='yellow',font=('verdana',18,'bold'))
resultado.pack(padx=10,pady=10)


    
    
    

janela.mainloop()



