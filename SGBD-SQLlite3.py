import sqlite3 as db
import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Cadastro de Usuários")
root.geometry("400x300")

cpf_label = tk.Label(root, text="CPF (formato: 123.456.789-00):")
cpf_label.pack()
cpf_entry = tk.Entry(root)
cpf_entry.pack()

nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

idade_label = tk.Label(root, text="Idade:")
idade_label.pack()
idade_entry = tk.Entry(root)
idade_entry.pack()

endereco_label = tk.Label(root, text="Endereço:")
endereco_label.pack()
endereco_entry = tk.Entry(root)
endereco_entry.pack()

def inserir_dados():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    idade = idade_entry.get()
    endereco = endereco_entry.get()

    if not cpf or not nome or not idade or not endereco:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    link = db.connect("bank.db")
    insert = link.cursor()

    insert.execute("""INSERT INTO CADASTRO (cpf, nome, idade, endereco) 
                      VALUES (?,?,?,?)""", (cpf, nome, idade, endereco))
    link.commit()

    link.close()

    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    idade_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)

inserir_button = tk.Button(root, text="Cadastrar", command=inserir_dados)
inserir_button.pack()

root.mainloop()