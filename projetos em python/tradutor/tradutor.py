import customtkinter as ctk
from deep_translator import GoogleTranslator

#funçôes------------

def traduzir():
    texto_para_traduzir = user_text.get() 
    idioma = lang_to_var.get()
    resultado = GoogleTranslator(source='auto',target=idioma).translate(texto_para_traduzir)
    user_text_sub.configure(state='normal')
    user_text_sub.delete(0,'end')
    user_text_sub.insert(0,resultado)
#-------------------
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
    
    
janela = ctk.CTk()
janela.minsize(500,600)
janela.maxsize(600,600)
janela.title('Tradutor Universal V1.0')
    
    
ctk.CTkLabel(janela,text='Tradutor Universal V1.0',font=('Arial',25,'bold'),text_color='green').pack(anchor=ctk.CENTER,pady=5)

app_flame = ctk.CTkFrame(janela,width=500,height=500,fg_color='#7fffd4')
app_flame.pack(fill=ctk.X,padx=20,pady=10)

ctk.CTkLabel(app_flame,text='Texto para Traduzir',font=('Arial',25,'bold'),text_color='green').pack(fill=ctk.X,padx=20,pady=10)

user_text = ctk.CTkEntry(app_flame,placeholder_text='Digite o texto para traduzir',height=50)
user_text.pack(fill=ctk.X,padx=20,pady=10)

ctk.CTkLabel(app_flame,text='Escolha o idioma a traduzir',text_color='green').pack(padx=5)

lang_to_var = ctk.StringVar(value='english')
lang_list = GoogleTranslator().get_supported_languages()
lang_to = ctk.CTkOptionMenu(app_flame,values=lang_list,variable=lang_to_var,dropdown_hover_color='green')
lang_to.set('english')
lang_to.pack(pady=5)

ctk.CTkLabel(app_flame,text='Texto Traduzido',font=('Arial',25,'bold'),text_color='green').pack(fill=ctk.X,padx=20,pady=10)

user_text_sub = ctk.CTkEntry(app_flame,placeholder_text='O texto traduzido será mostrado aqui',height=60,placeholder_text_color='gray')
user_text_sub.pack(fill=ctk.X)

translate_text = ctk.CTkButton(app_flame,text='Traduza',font=('Arial',18,'bold'),command=traduzir)
translate_text.pack(fill=ctk.X,pady=10)


janela.mainloop()



 

