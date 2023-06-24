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
message_3 = "Pressione S para salvar os pontos"
