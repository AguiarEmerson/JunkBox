from button import *
from statemachine import *

start_button = Button(125, 120, 150, 50, "Iniciar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

def initialmenu():
    
    mouse_pos = pygame.mouse.get_pos()

    # Atualiza e desenha o botão
    start_button.update(mouse_pos)
    start_button.draw(screen)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif start_button.is_clicked(event):
            print("Botão Iniciar clicado!")