import pygame, random
pygame.init()

# FPS
framerate = 60

# Cells
cell_size = 40
cell_number = 15

# Screen size
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# Fruit coords
fruit_x = random.randint(0, cell_number -1)
fruit_y = random.randint(0, cell_number -1)

# Screen
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 192)

# Fonts
game_font = pygame.font.Font('../fonts/ProtestRiot-Regular.ttf', 25)

# Score bar coords
score_x = int(cell_size * cell_number - 60)
score_y = int(cell_size * cell_number - 40)

# Sounds
crunch_sound = pygame.mixer.Sound("../Sounds/eat_sound.mp3")
move_sound = pygame.mixer.Sound("../Sounds/move_sound.mp3")
game_over_sound = pygame.mixer.Sound("../Sounds/game_over_sound.mp3")
game_over_sound.set_volume(0.3)
move_sound.set_volume(0.3)
