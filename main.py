import pygame
from tetris import Tetris
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, SPEED
from ai import AI
import time

def draw_switch(screen, ai_control):
    switch_color = WHITE if ai_control else BLACK
    pygame.draw.rect(screen, switch_color, pygame.Rect(10, 10, 80, 30))
    font = pygame.font.Font(None, 24)
    text = font.render("AI" if ai_control else "Manual", True, BLACK if ai_control else WHITE)
    screen.blit(text, (20, 15))

def draw_score(screen, score):
    pygame.draw.rect(screen, WHITE, pygame.Rect(SCREEN_WIDTH - 190, 10, SCREEN_WIDTH - 30, 30))
    font = pygame.font.Font(None, 24)
    text = font.render("Lines Cleared: " + str(score), True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - 180, 20))

def calculate_aspect_ratio_size(base_width, base_height, screen_width, screen_height):
    target_aspect = base_width / base_height
    screen_aspect = screen_width / screen_height

    if screen_aspect > target_aspect: 
        height = screen_height
        width = int(height * target_aspect)
    else:
        width = screen_width
        height = int(width / target_aspect)
    
    return width, height

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Tetris AI")
    pygame.display.set_icon(pygame.image.load("./TetrisIcon.png"))

    ai = AI(-0.510066, 0.760666, -0.35663, -0.184483)

    clock = pygame.time.Clock()
    game = Tetris()
    drop_time = 500
    last_move_down_time = pygame.time.get_ticks()
    ai_control = True
    ai_speed = 0.01
    fullscreen = False

    ai_speed = SPEED

    base_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11: 
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                if not ai_control:
                    if event.key == pygame.K_LEFT:
                        game.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        game.move(1, 0)
                    if event.key == pygame.K_DOWN:
                        game.move(0, 1)
                    if event.key == pygame.K_UP:
                        game.rotate()
                    if event.key == pygame.K_SPACE:
                        game.drop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 10 <= mouse_x <= 90 and 10 <= mouse_y <= 40:
                    ai_control = not ai_control

        if ai_control:
            best_move = ai.best_move(game)
            if best_move:
                rotation, target_x = best_move
                for _ in range(rotation):
                    game.rotate()
                while game.current_tetrimino.x != target_x:
                    if game.current_tetrimino.x < target_x:
                        game.move(1, 0)
                    else:
                        game.move(-1, 0)
                game.drop()
            time.sleep(ai_speed)

        if pygame.time.get_ticks() - last_move_down_time > drop_time:
            game.move(0, 1)
            last_move_down_time = pygame.time.get_ticks()

        base_surface.fill(BLACK)
        game.draw(base_surface)
        draw_switch(base_surface, ai_control)
        draw_score(base_surface, game.score)

        screen_size = screen.get_size()
        scaled_width, scaled_height = calculate_aspect_ratio_size(SCREEN_WIDTH, SCREEN_HEIGHT, *screen_size)
        scaled_surface = pygame.transform.scale(base_surface, (scaled_width, scaled_height))

        x_offset = (screen_size[0] - scaled_width) // 2
        y_offset = (screen_size[1] - scaled_height) // 2
        screen.fill(BLACK)  
        screen.blit(scaled_surface, (x_offset, y_offset))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
