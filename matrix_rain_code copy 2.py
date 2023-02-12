import pygame
from random import choice, randrange

pygame.init()

WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

FONT_SIZE = 35
alpha_value = randrange(30, 40, 5)

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','w','y',
'0','1','2','3','4','5','6','7','8','9','日','ﾊ','ﾐ','ﾋ','ｰ','ｳ','ｼ','ﾅ','ﾓ','ﾆ','ｻ','ﾜ','ﾂ','ｵ','ﾘ','ｱ','ﾎ','ﾃ','ﾏ',
'ｹ','ﾒ','ｴ','ｶ','ｷ','ﾑ','ﾕ','ﾗ','ｾ','ﾈ','ｽ','ﾀ','ﾇ','ﾍ','ｦ','ｲ','ｸ','ｺ','ｿ','ﾁ','ﾄ','ﾉ','ﾌ','ﾔ','ﾖ','ﾙ','ﾚ','ﾛ','ﾝ',
'0','1','2','3','4','5','6','7','8','9','α','β','γ','Δ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','Σ',
'σ','ς','τ','υ','φ','χ','ψ','Ω','ω','Ա','ա','Բ','Գ','Դ','դ','դ','δ','Ե','ե','Զ','զ','Է','է','Ը','ը','թ','Թ','թ','t',
'Ժ','Ի','ի','Ι','ι','Լ','լ','Խ','խ','Ծ','ծ','Կ','կ','Κ','Ձ','ձ','Ղ','ղ','Ճ','ճ','Մ','մ','Μ','μ','Յ','յ','Ն','ն'
'Շ','շ','Ո','Չ','չ','Պ','պ','Ջ','ջ','Ռ','ռ','Ս','ս','Վ','վ','Տ','տ','Τ','τ','Ր','ր','Ց','ց','Ւ','ւ','Փ','փ','Ք','ք',
'Օ','օ','Ֆ','ֆ','ո','ւ','և','!','@','#','$','%','^','*','`','~','_',';','?','|','{','A','B','C','D','E','F','G','H','I',
'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','}']

font = pygame.font.SysFont('MS Mincho', FONT_SIZE)
font_2 = pygame.font.SysFont('MS Mincho', FONT_SIZE - FONT_SIZE // 6)
font_3 = pygame.font.SysFont('Ms Mincho', FONT_SIZE - FONT_SIZE // 3)

green_chars = [font.render(char, True, (randrange(0, 100), 255, randrange(0, 100))) for char in chars]
green_chars_2 = [font_2.render(char, True, (40, randrange(100, 175), 40)) for char in chars]
green_chars_3 = [font_3.render(char, True, (40, randrange(50, 100), 40)) for char in chars]

screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(alpha_value)

clock = pygame.time.Clock()


class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 40
        self.value = choice(green_chars)

    def draw(self):
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))

    def draw_2(self):
        self.value_2 = choice(green_chars_2)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_2, (self.x, self.y))

    def draw_3(self):
        self.value_3 = choice(green_chars_3)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_3, (self.x, self.y))


symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 3)]
symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 3)]

run = True
while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw() for symbol in symbols]
    [symbol_2.draw_2() for symbol_2 in symbols_2]
    [symbol_3.draw_3() for symbol_3 in symbols_3]

    pygame.time.delay(140)

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False