import psycopg2
import tkinter as tk
from tkinter import messagebox

# CONEXÃO COM BANCO
def conectar():
    return psycopg2.connect(
        host="localhost",
        database="proj_inter_III",
        user="postgres",
        password="1234"
    )

# SALVAR
def salvar():
    if not (entry_marca.get() and entry_modelo.get() and entry_ano.get() and entry_cor.get() and entry_preco.get()):
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO veiculo (marca, modelo, ano, cor, preco)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        entry_marca.get(),
        entry_modelo.get(),
        entry_ano.get(),
        entry_cor.get(),
        entry_preco.get()
    ))

    conn.commit()
    cur.close()
    conn.close()

    # SALVAR EM TXT
    with open("veiculo.txt", "a") as f:
        f.write(f"{entry_marca.get()}, {entry_modelo.get()}, {entry_ano.get()}, {entry_cor.get()}, {entry_preco.get()}\n")

    messagebox.showinfo("Sucesso", "Veículo salvo!")

# PESQUISAR
def pesquisar():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM veiculo")
    dados = cur.fetchall()

    texto_resultado.delete("1.0", tk.END)
    for linha in dados:
        texto_resultado.insert(tk.END, str(linha) + "\n")

    cur.close()
    conn.close()

# EXCLUIR
def excluir():
    id = entry_id.get()

    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM veiculo WHERE id = %s", (id,))
    conn.commit()

    cur.close()
    conn.close()

    messagebox.showinfo("Sucesso", "Veículo excluído!")

# ALTERAR
def alterar():
    id = entry_id.get()

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE veiculo
        SET marca=%s, modelo=%s, ano=%s, cor=%s, preco=%s
        WHERE id=%s
    """, (
        entry_marca.get(),
        entry_modelo.get(),
        entry_ano.get(),
        entry_cor.get(),
        entry_preco.get(),
        id
    ))

    conn.commit()
    cur.close()
    conn.close()

    messagebox.showinfo("Sucesso", "Veículo atualizado!")

# INTERFACE
janela = tk.Tk()
janela.title("Cadastro de Veículos")

# CAMPOS
tk.Label(janela, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(janela)
entry_id.grid(row=0, column=1)

tk.Label(janela, text="Marca").grid(row=1, column=0)
entry_marca = tk.Entry(janela)
entry_marca.grid(row=1, column=1)

tk.Label(janela, text="Modelo").grid(row=2, column=0)
entry_modelo = tk.Entry(janela)
entry_modelo.grid(row=2, column=1)

tk.Label(janela, text="Ano").grid(row=3, column=0)
entry_ano = tk.Entry(janela)
entry_ano.grid(row=3, column=1)

tk.Label(janela, text="Cor").grid(row=4, column=0)
entry_cor = tk.Entry(janela)
entry_cor.grid(row=4, column=1)

tk.Label(janela, text="Preço").grid(row=5, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=5, column=1)

# BOTÕES
tk.Button(janela, text="Salvar", command=salvar).grid(row=6, column=0)
tk.Button(janela, text="Pesquisar", command=pesquisar).grid(row=6, column=1)
tk.Button(janela, text="Excluir", command=excluir).grid(row=7, column=0)
tk.Button(janela, text="Alterar", command=alterar).grid(row=7, column=1)

# RESULTADO
texto_resultado = tk.Text(janela, height=10, width=40)
texto_resultado.grid(row=8, column=0, columnspan=2)

janela.mainloop()