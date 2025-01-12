import pygame



class Game:
  def __init__(self):
    pygame.init() # Initialize pygame
    pygame.display.set_caption("Platformer")
    
    self.screen = pygame.display.set_mode((640,480)) # Tuple with resolution in px
    self.clock = pygame.time.Clock()  
    self.running = True
    
    self.img = pygame.image.load('data/images/clouds/cloud_1.png')
    self.img.set_colorkey((0,0,0)) # Remove bg color 
    
    self.img_pos = [160,260]
    self.movement = [False,False]
    
    self.collision_area = pygame.Rect(50,50,300,50)
    
  def run(self):
    # Game Loop
    while self.running: 
      self.screen.fill((14, 219, 248))
      self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
      self.screen.blit(self.img,self.img_pos)
      
      
      img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
      if img_r.colliderect(self.collision_area):
        pygame.draw.rect(self.screen,(255,0,0), self.collision_area)
      else:
        pygame.draw.rect(self.screen,(0,100,255), self.collision_area)
        
      
        
      pygame.display.update()
      self.clock.tick(60) # Force the game to run at 60fps
      
      for event in pygame.event.get(): # Get inputs
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            self.movement[0] = True
          if event.key == pygame.K_DOWN:
            self.movement[1] = True
        
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            self.movement[0] = False
          if event.key == pygame.K_DOWN:
            self.movement[1] = False
          
        if event.type == pygame.QUIT:
          self.running = False
        
          
    pygame.quit() # Closes pygame
    
Game().run()




      