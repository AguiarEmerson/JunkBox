from button import *
from TextInput import *
from statemachine import *


button1 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing,
                button_width, button_height, "registrar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))


button2 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing*4,
                button_width, button_height, "Voltar", font_size=25, button_color=(0, 200, 0), hover_color=(0, 255, 0))

button3 = Button(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + button_height + spacing,
                button_width, button_height, "Verificar email", font_size=20, button_color=(0, 200, 0), hover_color=(0, 255, 0))

text1 = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 50, 200, 30)

text2 = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2, 200, 30)

email_input = TextInput(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 30)

password_input = TextInput(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 30)

verificou_email= False

def cadastro():
    global verificou_email 
    
    mouse_pos = pygame.mouse.get_pos()

    draw_text("email:",text1,25,(255,255,255))
    draw_text("senha:",text2,25,(255,255,255))


    email_input.draw(screen)
    password_input.draw(screen)

    if verificou_email:
        button1.update(mouse_pos)
        button1.draw(screen)
    else:
        button3.update(mouse_pos)
        button3.draw(screen)
        
    
    
    button2.update(mouse_pos)
    button2.draw(screen)

        
    for event in pygame.event.get():
        email_input.handle_event(event)
        password_input.handle_event(event)
        if event.type == pygame.QUIT:
            program.go_to(0)
        elif button1.is_clicked(event):
            program.go_to(4)
        elif button2.is_clicked(event):
            program.go_to(1)
        elif button3.is_clicked(event):
            verificou_email=True
            print("email verificado")