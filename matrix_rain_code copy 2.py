import pygame
from random import choice, randrange

# Initialize pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)
FONT_SIZE = 30
alpha_value = 150  # For the trail effect

# Expanded character list
chars = (
    'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓ'
    'ﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    '!@#$%^&*()_+-=[]{}|;:\'",.<>?/`~'
)

# Load a font that supports various character types
font_path = "/Users/ericquezada/Downloads/Noto_Sans_JP/NotoSansJP-VariableFont_wght.ttf"  # Replace with the actual path
font = pygame.font.Font(font_path, FONT_SIZE)

# Pre-rendered characters
green = (0, 255, 0)
bright_green = (200, 255, 200)
pre_rendered_chars = [font.render(char, True, green) for char in chars]
bright_char = [font.render(char, True, bright_green) for char in chars]

# Setup screen
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Matrix Code Rain")
display_surface = pygame.Surface(RES, pygame.SRCALPHA)
display_surface.set_alpha(alpha_value)
clock = pygame.time.Clock()

# Symbol class
class Symbol:
    def __init__(self, x, char_set):
        self.x = x
        self.y = randrange(-HEIGHT, 0)
        self.speed = randrange(2, 10)  # Varying speeds for each stream
        self.char_set = char_set

    def draw(self):
        global FONT_SIZE
        char_index = randrange(len(self.char_set))
        # Bright leading character
        screen.blit(bright_char[char_index], (self.x, self.y))
        # Trailing characters
        for i in range(1, randrange(5, 20)):
            trail_y = self.y - i * FONT_SIZE
            if trail_y < 0:
                break
            screen.blit(pre_rendered_chars[char_index], (self.x, trail_y))

        # Move the stream down, reset if off-screen
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -randrange(10, 100)
            self.speed = randrange(2, 10)  # Reset speed

# Generate symbols for the screen width
symbols = [Symbol(x, pre_rendered_chars) for x in range(0, WIDTH, FONT_SIZE)]

# Main loop
run = True
while run:
    screen.fill((0, 0, 0))  # Black background
    display_surface.fill((0, 0, 0, alpha_value))  # Trail effect

    # Draw symbols
    for symbol in symbols:
        symbol.draw()

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
