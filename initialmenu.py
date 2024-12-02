from button import *
from statemachine import *

button1 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height - spacing,
                      button_width, button_height, "Login", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button2 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2,
                      button_width, button_height, "Cadastrar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button3 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing,
                     button_width, button_height, "Sair", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))


def initialmenu():
    
    mouse_pos = pygame.mouse.get_pos()

    button1.update(mouse_pos)
    button2.update(mouse_pos)
    button3.update(mouse_pos)

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            program.go_to(2)
        elif button2.is_clicked(event):
            program.go_to(3)
        elif button3.is_clicked(event):
            program.go_to(0)