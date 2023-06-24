
import pygame
import tkinter as tk
from tkinter import messagebox, simpledialog

# Funções de manipulação de marcações
def save_marks():
    try:
        with open("marks.txt", "w") as file:
            for name, pos in marks:
                file.write(f"{name},{pos[0]},{pos[1]}\n")
            if unknown_point is not None:
                file.write(f"desconhecido,{unknown_point[0]},{unknown_point[1]}\n")
        messagebox.showinfo("Mensagem", "As marcações foram salvas com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar as marcações:\n{str(e)}")

def load_marks():
    global unknown_point
    try:
        with open("marks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, x, y = line.strip().split(",")
                if name.lower() == "desconhecido":
                    unknown_point = (int(x), int(y))
                else:
                    marks.append((name, (int(x), int(y))))
        messagebox.showinfo("Mensagem", "As marcações foram carregadas com sucesso.")
    except FileNotFoundError:
        messagebox.showinfo("Mensagem", "Arquivo de marcações não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar as marcações:\n{str(e)}")

def clear_marks():
    global unknown_point
    marks.clear()
    unknown_point = None
    messagebox.showinfo("Mensagem", "Todas as marcações foram removidas.")

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance
