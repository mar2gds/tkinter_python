import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
#inicio de texto :D
label_entrada = ttk.Label(janela, text="Nome")
label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()
#CheckBox
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os Termos", variable=checkbox)
check.pack()
#Opções
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value = 1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value = 2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value = 3)
opc1.pack()
opc2.pack()
opc3.pack()
#listbox
lista = tk.Listbox(janela)
lista.insert(1, "Python")
lista.insert(2, "JAVA")
lista.insert(3, "PhP")
lista.insert(4, "JavaScript")
lista.pack()
#COMBOBOX
combo = ttk.Combobox(janela, values=["MG", "RJ", "RS", "RN"])
combo.set("Selecione um Estado")
combo.pack()
#BOTÃO
def clicar():
    messagebox.showinfo("AVISO", "Botão Acionado!")
btn = tk.Button(janela, text="Mostrar Mensagem", command=clicar)
btn.pack()






janela.mainloop()