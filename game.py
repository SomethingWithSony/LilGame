import pygame

pygame.init() # Initialize pygame

pygame.display.set_caption("Platformer")
screen = pygame.display.set_mode((640,480)) # Tuple with resolution in px

clock = pygame.time.Clock()  
running = True

# Game Loop
while running: 
  
  pygame.display.update()
  clock.tick(60) # Force the game to run at 60fps
  
  for event in pygame.event.get(): # Get inputs
    if event.type == pygame.QUIT:
      running = False
      
pygame.quit() # Closes pygame
      