import pygame
from Environment import *
from constants import *

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
ENV = None
CLOCK = None

class Window:
    def __init__(self):
        self.is_running = True

    def setup(self):
        pygame.init()
        pygame.display.set_caption("Genetic Snake")
        DISPLAY.fill(pygame.Color("WHITE"))
        pygame.display.update()

        ENV = Environment(POPS_NUMBER, POP_SIZE)
        CLOCK = pygame.time.Clock()


    def draw(self):
        self.show_info()

    def clear_text(self, x: int, y: int, diff: int):
        pygame.draw.rect(DISPLAY, pygame.Color("White"), (x, y, 10, 15))
        pygame.draw.rect(DISPLAY, pygame.Color("White"), (x + diff, y, 10, 15))
        pygame.draw.rect(DISPLAY, pygame.Color("White"), (x + 2 * diff, y, 10, 15))
        pygame.draw.rect(DISPLAY, pygame.Color("White"), (x + 3 * diff, y, 10, 15))

    def show_info(self):
        self.clear_text(590, 105, 5)
        self.clear_text(550, 135, 10)

        my_font = pygame.font.SysFont('Arial', 20)
        text_surf_gen = my_font.render("Generation: " + str(ENV.no_generations), False, pygame.Color("Black"))
        DISPLAY.blit(text_surf_gen, (500, 100))
        text_surf_len = my_font.render("Score: " + str(ENV.best_snake_len), False, pygame.Color("Black"))
        DISPLAY.blit(text_surf_len, (500, 130))

        pygame.draw.line(DISPLAY, pygame.Color("BLACK"), (PLAYABLE_AREA_WIDTH, 0), (PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT))
        pygame.display.update(PLAYABLE_AREA_WIDTH, 0, WINDOW_WIDTH - PLAYABLE_AREA_WIDTH, WINDOW_HEIGHT)


def main():
    clock = pygame.time.Clock()

    win = Window()
    win.setup()

    while win.is_running:
        win.draw()
        if not ENV.is_pop_extinct(): # if any snake is alive
            ENV.update()
        else: # none snake is alive
            ENV.run_genetic()

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win.is_running = False


if __name__ == "__main__":
    main()
