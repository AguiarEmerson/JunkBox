from window import *

def draw_text(text,rect,size,text_color):
    font= pygame.font.SysFont("ComicSans",size)
    text_img = font.render(text, True, text_color)
    text_rect = text_img.get_rect(center=rect.center)
    screen.blit(text_img, text_rect)
