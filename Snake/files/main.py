import pygame, sys, constants, models

# Game init
pygame.mixer.pre_init(44100, -16,2,512)
pygame.init()
pygame.display.set_caption("mc_slime")

clock = pygame.time.Clock()

# The main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Snake's move timer
        if event.type == constants.SCREEN_UPDATE:
            models.main_game.update()

        # Snake control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if models.main_game.snake.direction.y != 1:
                    constants.move_sound.play()
                    models.main_game.snake.direction = models.Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if models.main_game.snake.direction.y != -1:
                    constants.move_sound.play()
                    models.main_game.snake.direction = models.Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if models.main_game.snake.direction.x != 1  and models.main_game.snake.direction != (0,0):
                    constants.move_sound.play()
                    models.main_game.snake.direction = models.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if models.main_game.snake.direction.x != -1:
                    constants.move_sound.play()
                    models.main_game.snake.direction = models.Vector2(1, 0)

        # Move Snake, check collision, check fail
        models.main_game.update()

    # Background color
    constants.screen.fill((176,196,222))

    #draws all textures
    models.main_game.draw_elements()


    # FPS
    pygame.display.update()
    clock.tick(constants.framerate)