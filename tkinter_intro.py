import tkinter as tk

janela_main = tk.Tk()

janela_main.title('minha janela')
janela_main.configure(background='light pink')
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry('300x300')
#obj em janelas 
tk.Label(janela_main, 
         text= 'hello! \n oie maria >.<',
         bg= 'light pink',
         font=('arial', 16)
         ).pack(expand=True)
#imagens
imagem = tk.PhotoImage(file='cute.png')
imagem = imagem.subsample(5,5)
tk.Label(janela_main, image=imagem).pack()


janela_main.mainloop()