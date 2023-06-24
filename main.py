import pygame

pygame.init()

# Configurações da janela
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Marker Eduardo e Anderson")

icon_image = pygame.image.load("space.png")
pygame.display.set_icon(icon_image)

# Carregar imagem de fundo
background_image = pygame.image.load("spacemarker.jpg")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Configurações do círculo e das marcações
circle_radius = 5
marks = []  # Lista para armazenar as marcações (nome e coordenadas)
unknown_point = None  # Coordenadas do ponto "desconhecido"

font = pygame.font.Font(None, 20)
text_color = (255, 255, 255)
message_1 = "Pressione C para carregar os pontos"
message_2 = "Pressione E para excluir os pontos"
message_3 = "Pressione S para salvar os pontos"import pygame
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

import pygame
import tkinter as tk
from tkinter import messagebox, simpledialog

# Loop principal e interação do usuário
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_marks()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_marks()
                running = False
            elif event.key == pygame.K_c:
                load_marks()
            elif event.key == pygame.K_e:
                clear_marks()
            elif event.key == pygame.K_s:
                save_marks()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            root = tk.Tk()
            root.withdraw()
            name = simpledialog.askstring("Nome da estrela", "Digite o nome da estrela:")
            root.destroy()
            if name:
                current_point = (x, y)
                if name.lower() == "desconhecido":
                    unknown_point = current_point
                    messagebox.showinfo("Mensagem", f"Nome: {name}\nCoordenadas: {current_point}")
                else:
                    marks.append((name, current_point))
                    messagebox.showinfo("Mensagem", f"Nome: {name}\nCoordenadas: {current_point}")


# Desenho dos elementos na tela
# Desenhar imagem de fundo
window.blit(background_image, (0, 0))

# Desenhar as marcações no círculo e traçar linhas
for i in range(len(marks)):
    name, pos = marks[i]
    pygame.draw.circle(window, (255, 255, 255), pos, circle_radius)
    text_surface = font.render(name, True, (255, 255, 255))
    window.blit(text_surface, (pos[0] + 10, pos[1]))
    if i > 0:
        prev_name, prev_pos = marks[i - 1]
        pygame.draw.line(window, (255, 255, 255), prev_pos, pos, 1)
        distance = calculate_distance(prev_pos, pos)
        text_surface = font.render(str(distance), True, (255, 255, 255))
        line_center = ((prev_pos[0] + pos[0]) // 2, (prev_pos[1] + pos[1]) // 2)
        window.blit(text_surface, (line_center[0] + 10, line_center[1] + 10))
if unknown_point is not None:
    if len(marks) > 0:
        prev_pos = marks[-1][1]
        pygame.draw.line(window, (255, 255, 255), prev_pos, unknown_point, 1)
        distance = calculate_distance(prev_pos, unknown_point)
        text_surface = font.render(str(distance), True, (255, 255, 255))
        line_center = ((prev_pos[0] + unknown_point[0]) // 2, (prev_pos[1] + unknown_point[1]) // 2)
        window.blit(text_surface, (line_center[0] + 10, line_center[1] + 10))
    pygame.draw.circle(window, (255, 255, 255), unknown_point, circle_radius)
    text_surface = font.render(f"Desconhecido: {unknown_point[0]}, {unknown_point[1]}", True, (255, 255, 255))
    window.blit(text_surface, (unknown_point[0] + 10, unknown_point[1]))


