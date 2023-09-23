import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

# Carregar o grafo de palavras a partir de um arquivo JSON, se existir.
try:
    with open('grafo_palavras.json', 'r') as file:
        grafo_palavras_data = json.load(file)
        grafo_palavras = nx.node_link_graph(grafo_palavras_data)
except FileNotFoundError:
    grafo_palavras = nx.DiGraph()

palavras_adicionadas = set()

def adicionar_palavra():
    palavra = palavra_entry.get()
    sinonimos = sinonimos_entry.get().split(',')

    if palavra in palavras_adicionadas:
        resultado_label.config(text=f"'{palavra}' já existe no grafo.")
        return

    grafo_palavras.add_node(palavra)
    palavras_adicionadas.add(palavra)

    for sinonimo in sinonimos:
        sinonimo = sinonimo.strip()
        grafo_palavras.add_edge(palavra, sinonimo)

    palavra_entry.delete(0, 'end')
    sinonimos_entry.delete(0, 'end')

    desenhar_grafo()

    # Salvar o grafo atualizado em um arquivo JSON
    with open('grafo_palavras.json', 'w') as file:
        grafo_palavras_data = nx.node_link_data(grafo_palavras)
        json.dump(grafo_palavras_data, file)

def desenhar_grafo():
    pos = nx.spring_layout(grafo_palavras)
    ax.clear()
    nx.draw(grafo_palavras, pos, with_labels=True, node_size=800, node_color='skyblue', ax=ax)
    canvas.draw()

def mostrar_subgrafo():
    palavra = palavra_busca_entry.get()
    if palavra in grafo_palavras:
        subgrafo = nx.bfs_tree(grafo_palavras, source=palavra)
        pos = nx.spring_layout(subgrafo)
        ax.clear()
        nx.draw(subgrafo, pos, with_labels=True, node_size=800, node_color='skyblue', ax=ax)
        canvas.draw()
        resultado_label.config(text=f"Subgrafo a partir de '{palavra}':")
    else:
        resultado_label.config(text=f"'{palavra}' não encontrado no grafo.")

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

adicionar_button = ttk.Button(frame, text="Adicionar Palavra", command=adicionar_palavra)
adicionar_button.pack()

palavra_busca_label = ttk.Label(frame, text="Palavra para busca:")
palavra_busca_label.pack()

palavra_busca_entry = ttk.Entry(frame)
palavra_busca_entry.pack()

buscar_button = ttk.Button(frame, text="Buscar Subgrafo", command=mostrar_subgrafo)
buscar_button.pack()

resultado_label = ttk.Label(frame, text="")
resultado_label.pack()

desenhar_grafo()
root.mainloop()
