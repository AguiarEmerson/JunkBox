from button import *
from TextInput import *
from statemachine import *
from search import criando_playlist

button1 = Button(SCREEN_WIDTH // 2 - button_width*3 // 2, SCREEN_HEIGHT // 2 - button_height - spacing,
                      button_width, button_height, "Criar Playlist", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button2 = Button(SCREEN_WIDTH // 2 + button_width // 2, SCREEN_HEIGHT // 2 - button_height - spacing,
                      button_width, button_height, "Acessar Playlist", font_size=20, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button3 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing*5,
                     button_width, button_height, "Voltar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

def playlists():
    global criando_playlist

    mouse_pos = pygame.mouse.get_pos()

    button1.update(mouse_pos)
    button1.draw(screen)

    button2.update(mouse_pos)
    button2.draw(screen)

    button3.update(mouse_pos)
    button3.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            criando_playlist.go_to(1)
            program.go_to(5)
        elif button2.is_clicked(event):
            print("Nenhuma playlist criada")
        elif button3.is_clicked(event):
            program.go_to(4)