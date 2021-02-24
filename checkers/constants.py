from pygame import display, image, transform

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

GREY = (127, 127, 127)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)
WIN = display.set_mode((WIDTH, HEIGHT))

CROWN = transform.scale(image.load('assets/crown.png'), (45, 25))
