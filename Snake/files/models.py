import constants, pygame, texturs_loader
from pygame.math import Vector2
from random import randint


class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * constants.cell_size), int(self.pos.y * constants.cell_size), constants.cell_size, constants.cell_size)
        constants.screen.blit(texturs_loader.apple, fruit_rect)

    # Randomization of fruit appearance
    def randomize(self):
        self.x = self.generate_random_x()
        self.y = self.generate_random_y()
        self.pos = Vector2(self.x, self.y)

    def generate_random_x(self):
        return randint(0, constants.cell_number - 1)

    def generate_random_y(self):
        return randint(0, constants.cell_number - 1)


class Snake:
    def __init__(self):
        self.body = [Vector2(3, 7), Vector2(2, 7), Vector2(1, 7)]
        self.direction = Vector2(0, 0)
        self.new_block = False

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        # One block rect of the snake
        for i, block in enumerate(self.body):
            x_pos = int(block.x * constants.cell_size)
            y_pos = int(block.y * constants.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, constants.cell_size, constants.cell_size)

            # Head or tail texture selection
            if i == 0:
                constants.screen.blit(self.head, block_rect)
            elif i == len(self.body) - 1:
                constants.screen.blit(self.tail, block_rect)

            # Body texture selection
            else:
                previous_block = self.body[i + 1] - block
                next_block = self.body[i - 1] - block
                if previous_block.x == next_block.x:
                    constants.screen.blit(texturs_loader.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    constants.screen.blit(texturs_loader.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        constants.screen.blit(texturs_loader.body_tl, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        constants.screen.blit(texturs_loader.bodt_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        constants.screen.blit(texturs_loader.body_tr, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        constants.screen.blit(texturs_loader.body_br, block_rect)

    #  Choosing a specific head texture
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1, 0):
            self.head = texturs_loader.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = texturs_loader.head_right
        elif head_relation == Vector2(0, 1):
            self.head = texturs_loader.head_up
        elif head_relation == Vector2(0, -1):
            self.head = texturs_loader.head_down

    #  Choosing a specific tail texture
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]

        if tail_relation == Vector2(1, 0):
            self.tail = texturs_loader.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = texturs_loader.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = texturs_loader.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = texturs_loader.tail_down

    # Snake movement illusion
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    # Flag for adding a new element to the snake
    def add_block(self):
        self.new_block = True

    # Eating sound
    def play_crunch_sound(self):
        constants.crunch_sound.play()

    # Put the snake back to the starting position
    def reset(self):
        self.body = [Vector2(3, 7), Vector2(2, 7), Vector2(1, 7)]
        self.direction = Vector2(0, 0)

# General game class
class MAIN:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    # Move Snake, check collision with apple, check fail
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    # draws all textures
    def draw_elements(self):
        self.draw_chess_desk()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    # The moment of eating
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        # checking if the apple was generated inside the snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    # If the snake fucked up
    def check_fail(self):
        # Out of bounds checking
        if not 0 <= self.snake.body[0].x < constants.cell_number or not 0 <= self.snake.body[0].y < constants.cell_number:
            self.game_over()

        # if the snake sucked herself off
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    # Score bar
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = constants.game_font.render(score_text, True, (176,196,222))
        score_rect = score_surface.get_rect(center=(constants.score_x, constants.score_y))
        apple_rect = texturs_loader.apple.get_rect(midright=(score_rect.left, score_rect.centery - 3))

        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height + 3)

        pygame.draw.rect(constants.screen, (123,104,238), bg_rect)
        constants.screen.blit(score_surface, score_rect)
        constants.screen.blit(texturs_loader.apple, apple_rect)

        pygame.draw.rect(constants.screen, (56, 74, 12), bg_rect, 2)

    def game_over(self):
        if self.snake.direction != (0,0):
            constants.game_over_sound.play()
            if self.snake.direction != (-1,0):
                self.fruit.randomize()

        self.snake.reset()




    # Background chess style desk creation and her color
    def draw_chess_desk(self):
        desk_color = ((240,248,255))
        for row in range(constants.cell_number):
            if row % 2 == 0:
                for col in range(constants.cell_number):
                    if col % 2 == 0:
                        desk_rect = pygame.Rect(col * constants.cell_size, row * constants.cell_size,
                                                constants.cell_size, constants.cell_size)
                        pygame.draw.rect(constants.screen, desk_color, desk_rect)
            else:
                for col in range(constants.cell_number):
                    if col % 2 != 0:
                        desk_rect = pygame.Rect(col * constants.cell_size, row * constants.cell_size,
                                                constants.cell_size, constants.cell_size)
                        pygame.draw.rect(constants.screen, desk_color, desk_rect)


main_game = MAIN()
