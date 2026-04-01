import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
janela = tk.Tk()
janela.title = ("Formulário")
janela.geometry ("300x300")
janela.configure(background="light pink")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def enviar():
    nome = entrada_nome.get()
    idd = combo.get()
    escolaridade = combo2.get()
    area = opcao.get

    if sexo == 1:
        sexo_texto: 'Feminino'
    elif sexo == == 2:
        area = 'consultoria'
    elif opcao.get() == 3:
        area = 'Tecnico em informática'
    elif opcao.get() == 4:
       area = 'Telecomunicação'

    msg = f"Nome: {nome}\n Idade: {idd}\n Escolaridade: {escolaridade}\n Área: {area}"
    messagebox.showinfo("Dados enviados", msg)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tk.Label(janela, text="Formulário", font=("Arial", 14, "bold"), bg="light pink").grid(row=1, column=1, padx= 100, pady= 10)
tk.Label(janela, text="Nome: ", font=("Arial", 14), bg="light pink").grid(row=2, column=1)
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=3, column=1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tk.Label(janela, text="Idade: ", font=("Arial", 14), bg="light pink").grid(row=4, column=1, pady=5)
combo = ttk.Combobox(janela, width=27, values=["18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"])
combo.set("Selecione sua idade")
combo.grid(row=5, column=1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tk.Label(janela, text="Escolaridade: ", font=("Arial", 14), bg="light pink").grid(row=6, column=1, pady=5)
combo2 = ttk.Combobox(janela, width=27, values=["Ensino Fundamental Incompleto", "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo", "Ensino Técnico Incompleto", "Ensino Técnico Completo", "Ensino Superior Incompleto", "Ensino Superior Completo", "Pós-graduação Incompleta", "Pós-graduação Completa", "Mestrado Incompleto", "Mestrado Completo", "Doutorado Incompleto", "Doutorado Completo", "Pós-doutorado"])
combo2.set("Selecione sua escolaridade")
combo2.grid(row=7, column=1,)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tk.Label(janela, text="Area de Atuação: ", font=("Arial", 14), bg="light pink").grid(row=8, column=1, pady=5)
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text="Administração", bg=("light pink"), variable=opcao, value = 1)
opc2 = tk.Radiobutton(janela, text="Consultoria", bg=("light pink"), variable=opcao, value = 2)
opc3 = tk.Radiobutton(janela, text="Técnico em Informática", bg=("light pink"), variable=opcao, value = 3)
opc4 = tk.Radiobutton(janela, text="Telecomunicações", bg=("light pink"), variable=opcao, value=4)
opc1.grid(row=9, column=1)
opc2.grid(row=10, column=1)
opc3.grid(row=11, column=1)
opc4.grid(row=12, column=1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tk.Button(janela, text="Enviar", command=enviar).grid(row=14, column=1)

janela.mainloop()