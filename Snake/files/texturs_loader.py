import pygame

# Apple
app = pygame.image.load("../texturs/apple_minecraft.png").convert_alpha()
apple = pygame.transform.scale(app,(38,38))

# Head
head_up = pygame.image.load("../texturs/head_up.png").convert_alpha()
head_down = pygame.image.load("../texturs/head_down.png").convert_alpha()
head_right = pygame.image.load("../texturs/head_right.png").convert_alpha()
head_left = pygame.image.load("../texturs/head_left.png").convert_alpha()

# Tail
tail_up = pygame.image.load("../texturs/tail_up.png").convert_alpha()
tail_down = pygame.image.load("../texturs/tail_down.png").convert_alpha()
tail_right = pygame.image.load("../texturs/tail_right.png").convert_alpha()
tail_left = pygame.image.load("../texturs/tail_left.png").convert_alpha()

# Body
body_vertical = pygame.image.load("../texturs/body_vertical.png").convert_alpha()
body_horizontal = pygame.image.load("../texturs/body_horizontal.png").convert_alpha()

body_tr = pygame.image.load("../texturs/body_topright.png").convert_alpha()
body_tl = pygame.image.load("../texturs/body_topleft.png").convert_alpha()
body_br = pygame.image.load("../texturs/body_bottomright.png").convert_alpha()
bodt_bl = pygame.image.load("../texturs/body_bottomleft.png").convert_alpha()
