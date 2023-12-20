import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 64)
        self.menu_items = ["Play", "Quit"]
        self.selected_item = 0
        self.background = pygame.image.load("../graphics/background.png").convert()

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))

        title_text = self.title_font.render("Space Invaders", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen.get_width() / 2, 100))
        self.screen.blit(title_text, title_rect)

        for index, item in enumerate(self.menu_items):
            text = self.font.render(item, True, (255, 255, 255) if index != self.selected_item else (255, 0, 0))
            text_rect = text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + index * 50))
            self.screen.blit(text, text_rect)

    def run_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                    elif event.key == pygame.K_UP:
                        self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                    elif event.key == pygame.K_RETURN:
                        return self.selected_item 

            self.draw_menu()
            pygame.display.flip()

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.replay_button = pygame.Rect(250, 350, 100, 50)
        self.replay_text = self.font.render("Replay", True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.game_over_text, (200, 250))  # Vẽ chữ Game Over ở vị trí mới
        pygame.draw.rect(screen, (0, 255, 0), self.replay_button)
        screen.blit(self.replay_text, (260, 360))  # Vẽ nút Replay ở vị trí mới

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.replay_button.collidepoint(event.pos):
                return True
        return False
