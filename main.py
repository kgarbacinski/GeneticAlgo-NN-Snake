import pygame
from Environment import *
from constants import *

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
ENV = None


def setup():
    global DISPLAY, ENV

    # Window
    pygame.init()
    pygame.display.set_caption("Genetic Snake")
    DISPLAY.fill(pygame.Color("WHITE"))
    pygame.display.update()

    # Classes
    ENV = Environment(1, 500)


def draw():
    show_info()


def show_info():
    global DISPLAY, ENV

    pygame.draw.rect(DISPLAY, pygame.Color("White"), (690, 105, 10, 15))
    pygame.draw.rect(DISPLAY, pygame.Color("White"), (695, 105, 10, 15))
    pygame.draw.rect(DISPLAY, pygame.Color("White"), (700, 105, 10, 15))

    pygame.draw.rect(DISPLAY, pygame.Color("White"), (690, 205, 10, 15))
    pygame.draw.rect(DISPLAY, pygame.Color("White"), (695, 205, 10, 15))
    pygame.draw.rect(DISPLAY, pygame.Color("White"), (700, 205, 10, 15))

    my_font = pygame.font.SysFont('Arial', 20)
    text_surf_gen = my_font.render("Generation: " + str(ENV.no_generations), False, pygame.Color("Black"))
    DISPLAY.blit(text_surf_gen, (600, 100))
    text_surf_len = my_font.render("Best score: " + str(ENV.best_len), False, pygame.Color("Black"))
    DISPLAY.blit(text_surf_len, (600, 200))

    pygame.draw.line(DISPLAY, pygame.Color("BLACK"), (PLAYABLE_AREA_WIDTH, 0), (PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT))
    pygame.display.update(PLAYABLE_AREA_WIDTH, 0, WINDOW_WIDTH - PLAYABLE_AREA_WIDTH, WINDOW_HEIGHT)


def main():
    setup()
    is_running = True
    while is_running:
        draw()
        if not ENV.is_pop_extinct(): # if any snake is alive
            ENV.update()
        else: # none snake is alive
            ENV.run_genetic()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False


if __name__ == "__main__":
    main()