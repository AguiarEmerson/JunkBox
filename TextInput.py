import pygame

class TextInput:
    def __init__(self, x, y, width, height, font_size=25, text_color=(255, 255, 255), box_color=(0, 200, 0), active_color=(0, 255, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, font_size)
        self.text = ""
        self.text_color = text_color
        self.box_color = box_color
        self.active_color = active_color
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ativa/desativa o campo de entrada com base na posição do clique
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Remove o último caractere
            else:
                self.text += event.unicode  # Adiciona o caractere digitado

    def draw(self, screen):
        # Cor da caixa: ativa ou inativa
        box_color = self.active_color if self.active else self.box_color
        pygame.draw.rect(screen, box_color, self.rect, 2)
        
        # Renderiza o texto
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Ajusta o tamanho do texto na caixa
        self.rect.w = max(200, text_surface.get_width() + 10)
