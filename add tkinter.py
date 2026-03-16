import tkinter as tk

janela_main = tk.Tk()

janela_main.title('<3')
janela_main.configure(background='#FFB6C1')
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry('300x300')

#obj em janelas 
tk.Label(janela_main, 
         text= 'hello (kitty)!',
         bg= '#FFC0CB',
         font=('arial', 16, 'bold')
         ).pack(expand=True)
#imagens
imagem = tk.PhotoImage(file='cute - Copia.png')
imagem = imagem.zoom(1,1)
tk.Label(janela_main, image=imagem).pack()

janela_main.mainloop()