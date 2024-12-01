from window import *
from statemachine import *
from initialmenu import *

run=True
while run:
    screen.fill(BACKGROUND_COLOR)
            
    match program.state:
        case 0:
            run = False
        case 1:
            initialmenu()

    pygame.display.update()

pygame.quit()