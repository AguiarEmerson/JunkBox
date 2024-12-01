from text import *

class Button:
    def __init__(self, x, y, width, height, text, font_size=30, text_color=(255, 255, 255), button_color=(0, 0, 255), hover_color=(0, 100, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen):
        # Desenha o botão
        color = self.hover_color if self.is_hovered else self.button_color
        pygame.draw.rect(screen, color, self.rect)

        # Desenha o texto no botão
        draw_text(self.text,self.rect,self.font_size,self.text_color)

    def update(self, mouse_pos):
        # Atualiza estado de hover
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        # Verifica se o botão foi clicado
        return self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
