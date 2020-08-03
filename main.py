import pygame
from Environment import Environment

display = None
env = None


def setup():
    global display, env

    # Window
    pygame.init()
    display = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Genetic Snake")
    display.fill(pygame.Color("WHITE"))
    pygame.display.update()

    # Classes
    env = Environment()


def draw():
    show_info()

def show_info():
    global display, env

    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 20)
    text_surf = my_font.render("Generation: " + str(env.no_generations), False, pygame.Color("Black"))
    display.blit(text_surf, (600, 100))
    pygame.draw.line(display, pygame.Color("BLACK"), (500, 0), (500, 500))
    pygame.display.update()


def main():
    setup()
    is_running = True
    while is_running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

if __name__ == "__main__":
    main()