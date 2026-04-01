import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
from datetime import datetime

DB_FILE = 'estoque.db'

#função de segurança

def hash_senha(senha):
    return senha

#janela de login

class Janelalogin:
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('400x300')
        self.janela.title('LOGIN')
        self.janela.resizable(False,False)
        self.janela.eval('tk::PlaceWindow . center')

 #criação do frame

        frame_principal = ttk.Frame(self.janela , padding='30 40')
        frame_principal.pack(fill="both",expand=True)

        ttk.Label(frame_principal, text='Login Controle de Estoque', font= ('Arial', 14,'bold'))\
           .grid(row=0, column=1, columnspan=2, pady=(0,25),sticky='ew')
        ttk.Label(frame_principal, text='USUÁRIO: ').grid(row=1, column=0, sticky='e', pady=8)
        self.usuario_var = tk.StringVar(value='admin')
        entrada_usuario = ttk.Entry(frame_principal, textvariable=self.usuario_var, width=25)
        entrada_usuario.grid(row=1, column=1, pady=8, sticky='w')

        ttk.Label(frame_principal, text="SENHA: ").grid(row=2, column=0, sticky='e', pady=8)
        self.senha_var = tk.StringVar()
        self.entrada_senha = ttk.Entry(frame_principal, textvariable=self.senha_var, width=25, show='*')
        self.entrada_senha.grid(row=2, column=1, pady=8, sticky='w')

#botões

        btn_frame = ttk.Frame(frame_principal)
        btn_frame.grid(row=4, column= 0, columnspan=2, pady=8 , sticky='ew')
        ttk.Button(btn_frame, text='ENTRAR').pack(side='left')
        ttk.Button(btn_frame, text='SAIR').pack(side='left', padx=10)


#logar com enter

        self.entrada_senha.bind('<Return>', lambda e: self.verificar_login() )
        style = ttk.Style()
        style.configure('Accent.Tbutton', font=(' Arial', 10, 'bold'))
        self.entrada_senha.focus()
    def verificar_login(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()

        if usuario == 'admin' and senha == '123456789':
           messagebox.showinfo('Bem-vindo!', f'Login realizado com sucesso! \n Olá {usuario}')
           self.janela.destroy()
           abrir_sistema_estoque()



        else:
            messagebox.showerror('Erro de login.', 'Usuario ou senha incorretos!')
            self.senha_var.set("")
            self.entrada_senha.focus()

class EstoqueApp:
    def __init__(self, janela_main):
        self.janela_main = janela_main
        self.janela_main.title('Controle de Estoque')
        self.janela_main.geometry('950x650')
        self.janela_main.minsize(800,600)
    

        self.com = sqlite3.connect(DB_FILE)
        self.criar_tabelas()
        self.criar_interface()

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Arial', 10))
        style.configure('Treeview', rowheight=26, font=('Arial', 10))

    def criar_tabelas(self):
        cursor = self.com.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
            )
            ''')
        self.com.commit()
    def criar_interface(self):
        #botões de interações
        frame_botões = ttk.Frame(self.janela_main, padding='10')
        frame_botões.pack(fill='k')

        botoes = [
            ('Novo produto' , self.novo_produto),
            ('Editar produto' , self.editar_produto),
            ('Excluir produto' , self.excluir_produto),
            ('Entrada' , self.entrada_produto),
            ('Saída' , self.saída_produto),
            ('Atualizar' , self.atualizar_produto),
            ('Sair' , self.sair_produto),
        ]
        for texto, cmd in botoes:
            ttk.Button(frame_botões, text=texto, command=cmd).pack(side='left',padx=5 )

            #Tabela

            frame_tabela = ttk.Frame(self.janela_main, padding='10')
            frame_tabela.pack(fill='both', expand=True)

            colunas = ('id', 'nome','quantidade', 'preço')
            self.tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings', selectmode='browse')

            self.tree.heading('id', text= 'codigo')
            self.tree.heading('nome', text= 'nome do produto')
            self.tree.heading('quantidade', text= 'quantidade')
            self.tree.heading('preco', text= 'preço R$')
 
            self.tree.column('id', width=50, anchor='center')
            self.tree.column('nome', width=150)
            self.tree.column('quantidade', width=100, anchor='center')
            self.tree.column('preço', width=50, anchor='center')

            scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)

            self.tree.pack(side='left', fill='both',expand=True)
            scrollbar.pack(side='right', fill='y' )

            self.status_var = tk.StringVar(value='Pronto')
            ttk.Label(self.janela_main, textvariable=self.status_var, relief='sunken', anchor='w')\
           .pack(side='bottom', fill='x')
            
        
        self.atualizar_tabela()


        def atualizar_tabela(self):
            for item in self.tree.get_children():
                self.tree.delete(item)
            cursor = self.conn.cursor()
            cursor.execute('SELECT id, nome, quantidade, preço FROM produtos ORDER BY id')
            for row in cursor.fetchall():
                self.tree.insert("",'end', values=(row[0], row[1], row[2], f'{row[3]: .2f}'))
                cursor.execute('SELECT COUNT(*) FROM produtos')
                total = cursor.fetchone()[0]
                self.status_var.set(f'Total de produtos: {total}  |  Base de dados {DB_FILE}')

        def get_produtos_selecionados(self):
            sel = self.tree.selection()
            if not sel:
                messagebox.showwarning('ATENÇÃO:' , 'Selecionou um produto na tabela!')
                return None
            id = self.tree.item(sel[0])['values'][0]
            cursor = self.conn.cursor()
            cursor.execute('SELECT nome, quantidade, preço FROM produtos WHERE ID=?,' (id))
            row = cursor.fetchone()
            return (id, {'nome': row[0], 'quantidade': row[1], 'preco': row[2]}) if row else None 
        
        def novo_produto(self):
            janela_add = tk.Toplevel(self.janela_main)
            janela_add.title('Adicionar Produto')
            janela_add.geometry('450x350')
            janela_add.transient(self.janela_main)
            janela_add.grab_set()

            ttk.Label(janela_add, text='ID: ').pack(pady=(20,5))
            entrada_id = ttk.Entry(janela, width=25)
            entrada_id.pack

            ttk.Label(janela_add, text='Nome: ').pack(pady=(20,5))
            entrada_nome = ttk.Entry(janela, width=25)
            entrada_nome.pack

            ttk.Label(janela_add, text='Qantidade: ').pack(pady=(20,5))
            entrada_quantidade = ttk.Entry(janela, width=25)
            entrada_quantidade.pack

            ttk.Label(janela_add, text='Preço: ').pack(pady=(20,5))
            entrada_preço = ttk.Entry(janela, width=25)
            entrada_preço.pack

            def salvar():
                id = entrada_id.get().trip().upper()
                nome = entrada_nome.get().stip()
                try:
                    qtd = int(entrada_quantidade.get())
                    preco = float(entrada_preço.get().replace(','',''.'))
                except:
                    messagebox.showerror('ERRO', 'Valores Inválidos.')
                    return
                if not id or not nome:
                    messagebox.showwarning('Atenção', 'Código e Nome são obrigatórios')
                    return
                try:
                    cursor = self.conn.cursor()
                    cursor.execute('INSERT  INTO  produtos (id, nome, quantidade, preco) VALUES (?, ?, ?, ?)' 
                                   (id, nome, qtd, preco))
                    self.conn.commit()
                    self.atualizar_tabela()
                    janela_add.destroy()
                    messagebox.showinfo('Sucesso!', 'f Produto {nome} cadastrado!')
                except sqlite3.IntegrityError:
                    messagebox.showerror('Erro', 'Este ID já existe!')
                    ttk.Button(janela_add, text='Salvar', command=salvar).pack(pady=25)

        def editar_produto(self):
            item = self.get_produto_selecionado()
            if not item:
                return
            id, dados = item

            janela_edit = tk.Toplevel(self.janela_main)
            janela_edit.title('editar produto')
            janela_edit.geometry('450x360')
            janela_edit.transient(self.janela_main)
            janela_edit.grab_set

            ttk.Label(self.janela_edit, text=f'id:{id}').pack(pady=10)

            ttk.Label(self.janela_edit)



            def editar_produto(self):messagebox.showinfo('Em desenvolvimento... Já termino')
            def excluir_produto(self):messagebox.showinfo('Em desenvolvimento... Já termino')
            def entrada_estoque(self):messagebox.showinfo('Em desenvolvimento... Já termino')
            def saida_estoque(self):messagebox.showinfo('Em desenvolvimento... Já termino')
            def sair_produto(self): self.janela_main.quit()
            





def abrir_sistema_estoque():
        janela = tk.Tk()
        EstoqueApp(janela)
        janela.mainloop()


if __name__ == '__main__':
    janela = tk.Tk()
    app = Janelalogin(janela)
    janela.mainloop()
