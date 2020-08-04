import pygame
from Environment import *

DISPLAY = pygame.display.set_mode((800, 500))
ENV = None

def setup():
    global DISPLAY, ENV

    # Window
    pygame.init()
    pygame.display.set_caption("Genetic Snake")
    DISPLAY.fill(pygame.Color("WHITE"))
    pygame.display.update()

    # Classes
    ENV = Environment(1, 2000)


def draw():
    show_info()


def show_info():
    global DISPLAY, ENV

    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 20)
    text_surf = my_font.render("Generation: " + str(ENV.no_generations), False, pygame.Color("Black"))
    DISPLAY.blit(text_surf, (600, 100))
    pygame.draw.line(DISPLAY, pygame.Color("BLACK"), (500, 0), (500, 500))
    pygame.display.update()


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