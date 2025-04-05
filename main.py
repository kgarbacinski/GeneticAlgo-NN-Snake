import pygame
from genetic_algorithm.environment import Environment
from config.constants import WINDOW_WIDTH, WINDOW_HEIGHT, POPS_NUMBER, POP_SIZE

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Window:
    def __init__(self):
        self.is_running = True
        self.env = Environment(POPS_NUMBER, POP_SIZE)
        self.clock = pygame.time.Clock()

    def setup(self):
        pygame.init()
        pygame.display.set_caption("Genetic Snake")
        DISPLAY.fill(pygame.Color("WHITE"))
        pygame.display.update()

    def draw(self):
        self.show_info()

    def clear_text(self, x: int, y: int, diff: int):
        for i in range(4):
            pygame.draw.rect(DISPLAY, pygame.Color("White"), (x + i * diff, y, 10, 15))

    def show_info(self):
        self.clear_text(590, 105, 5)
        self.clear_text(550, 135, 10)

        my_font = pygame.font.SysFont('Arial', 20)
        text_surf_gen = my_font.render(f"Generation: {self.env.no_generations}", False, pygame.Color("Black"))
        DISPLAY.blit(text_surf_gen, (500, 100))
        text_surf_len = my_font.render(f"Score: {self.env.best_snake_len}", False, pygame.Color("Black"))
        DISPLAY.blit(text_surf_len, (500, 130))

        pygame.draw.line(DISPLAY, pygame.Color("BLACK"), (PLAYABLE_AREA_WIDTH, 0), (PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT))
        pygame.display.update(PLAYABLE_AREA_WIDTH, 0, WINDOW_WIDTH - PLAYABLE_AREA_WIDTH, WINDOW_HEIGHT)

def main():
    win = Window()
    win.setup()

    while win.is_running:
        win.draw()
        if not win.env.is_pop_extinct():
            win.env.update()
        else:
            win.env.run_genetic()

        win.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win.is_running = False

if __name__ == "__main__":
    main()