from window import *
from statemachine import *
from initialmenu import initialmenu
from login import login
from cadastro import cadastro
from mainmenu import mainmenu

run=True
while run:
    screen.fill(BACKGROUND_COLOR)
            
    match program.state:
        case 0:
            run = False
        case 1:
            initialmenu()
        case 2:
            login()
        case 3:
            cadastro()
        case 4:
            mainmenu()

    pygame.display.update()

pygame.quit()