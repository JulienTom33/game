import pygame
pygame.init()

# crérer la fenêtre du jeu
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygamon Aventure")

# boucle du jeu qui va mainteniren activité la fenêtre
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()            