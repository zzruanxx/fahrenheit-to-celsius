import tkinter as tk
from tkinter import ttk, messagebox

def fahrenheit_para_celsius():
    try:
        f = float(entry_temp.get())
        c = (f - 32) * 5 / 9
        label_resultado.config(text=f"{c:.2f} °C")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

def celsius_para_fahrenheit():
    try:
        c = float(entry_temp.get())
        f = (c * 9 / 5) + 32
        label_resultado.config(text=f"{f:.2f} °F")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("350x200")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

label_instrucao = ttk.Label(frame, text="Digite a temperatura:")
label_instrucao.pack(pady=5)

entry_temp = ttk.Entry(frame, width=20)
entry_temp.pack(pady=5)

frame_botoes = ttk.Frame(frame)
frame_botoes.pack(pady=10)

btn_f_c = ttk.Button(frame_botoes, text="Fahrenheit → Celsius", command=fahrenheit_para_celsius)
btn_f_c.pack(side="left", padx=5)

btn_c_f = ttk.Button(frame_botoes, text="Celsius → Fahrenheit", command=celsius_para_fahrenheit)
btn_c_f.pack(side="left", padx=5)

label_resultado = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
label_resultado.pack(pady=10)

root.mainloop()