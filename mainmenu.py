from button import *
from statemachine import *

button1 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height - spacing,
                      button_width, button_height, "pesquisar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button2 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2,
                      button_width, button_height, "playlists", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button3 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing,
                     button_width, button_height, "AAAAAAA", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button4 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing*4,
                     button_width, button_height, "Logout", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))


def mainmenu():
    
    mouse_pos = pygame.mouse.get_pos()

    button1.update(mouse_pos)
    button2.update(mouse_pos)
    button3.update(mouse_pos)
    button4.update(mouse_pos)

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            print("Apertou!")
        elif button2.is_clicked(event):
            print("Apertou!")
        elif button3.is_clicked(event):
            print("Apertou!")
        elif button4.is_clicked(event):
            program.go_to(1)