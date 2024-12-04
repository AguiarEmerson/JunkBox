from button import *
from TextInput import *
from statemachine import *

button1 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2,
                      button_width, button_height, "carregar arquivo", font_size=20, button_color=(0, 200, 0), hover_color=(0, 255, 0))
button2 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing*5,
                     button_width, button_height, "Voltar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

def upload():
    mouse_pos = pygame.mouse.get_pos()

    button1.update(mouse_pos)
    button1.draw(screen)

    button2.update(mouse_pos)
    button2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            print("Carrega arquivo")
        elif button2.is_clicked(event):
            program.go_to(4)