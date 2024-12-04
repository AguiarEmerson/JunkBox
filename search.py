from button import *
from TextInput import *
from statemachine import *

button1 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing*5,
                     button_width, button_height, "Voltar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button2 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height - spacing,
                     button_width, button_height, "Pesquisar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

search_input = TextInput(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 150, 200, 30)

criando_playlist= statemachine()
criando_playlist.go_to(0)

def search():

    mouse_pos = pygame.mouse.get_pos()

    button1.update(mouse_pos)
    button1.draw(screen)

    button2.update(mouse_pos)
    button2.draw(screen)


    search_input.draw(screen)

    for event in pygame.event.get():
        search_input.handle_event(event)
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            if criando_playlist.state:
                criando_playlist.go_to(0)
                program.go_to(7)
            else:
                program.go_to(4)
        elif button2.is_clicked(event):
            print("Apresentar resultados!")