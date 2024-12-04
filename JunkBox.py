from window import *
from statemachine import *
from initialmenu import initialmenu
from login import login
from cadastro import cadastro
from mainmenu import mainmenu
from search import search
from selectrepro import selectrepro
from playlists import playlists
from upload import upload

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
        case 5:
            search()
        case 6:
            selectrepro()
        case 7:
            playlists()
        case 8:
            upload()

    pygame.display.update()

pygame.quit()