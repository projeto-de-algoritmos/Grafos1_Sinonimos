import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Visualização de Grafo de Palavras")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

palavra_label = ttk.Label(frame, text="Palavra:")
palavra_label.pack()

palavra_entry = ttk.Entry(frame)
palavra_entry.pack()

sinonimos_label = ttk.Label(frame, text="Sinônimos (separados por vírgula):")
sinonimos_label.pack()

sinonimos_entry = ttk.Entry(frame)
sinonimos_entry.pack()

palavra_busca_label = ttk.Label(frame, text="Palavra para busca:")
palavra_busca_label.pack()

palavra_busca_entry = ttk.Entry(frame)
palavra_busca_entry.pack()

resultado_label = ttk.Label(frame, text="")
resultado_label.pack()

root.mainloop()
