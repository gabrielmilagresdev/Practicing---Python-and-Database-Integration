import tkinter as tk
from tkinter import messagebox
import random
import sqlite3 as db
import re

root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry = ("600x600")

canvas = tk.Canvas(root, width=600, height=600, bg="#FFFFFF", highlightthickness=2)
canvas.pack()

circle = canvas.create_oval(200, 200, 400, 400, fill="#778899", outline="#000000", width=4)
circle_shadow = canvas.create_oval(210,210,410,410,fill="#000000")
canvas.tag_lower(circle_shadow, None) 
text = canvas.create_text(300, 300, text="Gerar Senha", fill="white", font=("Arial", 14, "bold"))

password = []

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
     'w', 'x', 'y', 'z', 
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
     'W', 'X', 'Y', 'Z', 
     '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', 
     ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 
     '[', '\\', ']', '^', '_', '{', '|', '}', '~', '`']


def generate(event):
    x, y = event.x, event.y
    if 200 <= x <= 400 and 200 <= y <= 400: 
        for i in range (7):
            x = random.choice(a)
            password.append(x)
        p = password[0]+password[1]+password[2]+password[3]+password[4]+password[5]+password[6]
    canvas.coords(circle,210,210,410,410)
    canvas.coords(text,310,310)
    root.after(100, lambda: canvas.coords(circle,200,200,400,400))
    root.after(100, lambda: canvas.coords(text,300,300))
    messagebox.showinfo("Senha",f"Senha: {p}")
    link = db.connect("bank.db")
    insert = link.cursor()
    insert.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pass TEXT NOT NULL
    )
    """)
    insert.execute("""INSERT INTO CADASTRO (pass) 
                      VALUES (?)""", (p))
    link.commit()
    link.close()

canvas.bind("<Button-1>", generate)

root.mainloop()

