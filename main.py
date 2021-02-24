import pygame

from checkers import minimax
from checkers.button import Button
from checkers.constants import *
from checkers.game import Game

pygame.display.set_caption('Checkers')

BUTTON_STYLE = {"hover_color": BLUE,
                "clicked_color": GREEN,
                "clicked_font_color": BLACK,
                "hover_font_color": ORANGE,
                }


class Control(object):
    def __init__(self):
        self.screen = WIN
        self.AI = True
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60
        self.game = Game(WIN)
        self.color = WHITE
        self.button = Button((0, 0, 200, 50), RED, self.change_opponent,
                             text='vs Player', **BUTTON_STYLE)
        self.button2 = Button((0, 0, 200, 50), RED, self.main_loop,
                              text='vs AI', **BUTTON_STYLE)
        self.button.rect.center = (self.screen_rect.centerx, 200)
        self.button2.rect.center = (self.screen_rect.centerx, 400)

    def ai(self):
        if self.game.turn == WHITE:
            value, new_board = minimax.algorithm(position=self.game.get_board(),
                                                 depth=4,
                                                 max_player=WHITE,
                                                 game=self.game)
            self.game.ai_move(new_board)

    def change_opponent(self):
        self.AI = False
        self.main_loop()

    @staticmethod
    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.button.check_event(event)
            self.button2.check_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = Control.get_row_col_from_mouse(pos)
                self.game.select(row, col)

    def menu(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            self.button.update(self.screen)
            self.button2.update(self.screen)
            pygame.display.update()

    def main_loop(self):
        while not self.done:
            self.clock.tick(self.fps)

            if self.AI:
                self.ai()

            if self.game.winner():
                print(self.game.winner())
                self.done = True

            self.event_loop()
            self.game.update()


if __name__ == '__main__':
    pygame.init()
    run_it = Control()
    run_it.menu()
    pygame.quit()

