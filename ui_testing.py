import pygame

class Button:

    def __init__(self, coords, fontcolor=None, fontsize=None, text=None, font=None):

        if text != None:
            self.font = pygame.font.Font(size=fontsize)
            self.font.align = pygame.FONT_CENTER
            self.size = self.font.size(text)
            self.render = self.font.render(text, antialias=False, color=fontcolor)
            self.rect = pygame.Rect(coords, self.size)
    
    def render_button(self):

        screen.blit(self.render, self.rect)


def new_menu():
    pygame.display.set_caption("Main Menu")

    running = True
    while running:
        screen.fill((255, 255, 255))

        franchise_button = Button((50, 360), "black", 50, "Franchise Mode")
        exit_button = Button((50, 360 + franchise_button.size[1] + 10), "black", 50, "Exit")

        franchise_button.render_button()
        exit_button.render_button()

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and franchise_button.rect.collidepoint(menu_mouse_pos):
                franchise_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and exit_button.rect.collidepoint(menu_mouse_pos):
                running = False

        pygame.display.flip()


def franchise_menu():
    pygame.display.set_caption("Franchise Menu")

    running = True
    while running:
        screen.fill((255, 255, 255))

        back_button = Button((50, 360), "black", 50, "Back")
        
        back_button.render_button()
      

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.rect.collidepoint(menu_mouse_pos):
                running = False

        pygame.display.flip()



    

        

def main_menu():
    pygame.display.set_caption("Main Menu")
    

    running = True
    while running:
        screen.fill((255, 255, 255))
        
        text = pygame.font.Font(size=50)
        text.align = pygame.FONT_CENTER
        textsize = text.size("To Other Menu")
        rendertext = text.render("To Other Menu", antialias=False, color="black")
        myrect = pygame.Rect((320 - (textsize[0] / 2), 320 - (textsize[1] / 2)), textsize)
        screen.blit(rendertext, myrect)

        exittext = pygame.font.Font(size=30)
        exittext.align = pygame.FONT_CENTER
        exitsize = exittext.size("Exit")
        rendertext2 = exittext.render("Exit", antialias=False, color="black")
        otherrect = pygame.Rect((320 - (exitsize[0] / 2), 320 - (exitsize[1] / 2) + 100), exitsize)
        screen.blit(rendertext2, otherrect)


        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and myrect.collidepoint(menu_mouse_pos):
                other_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and otherrect.collidepoint(menu_mouse_pos):
                running = False

        pygame.display.flip()

def other_menu():
    pygame.display.set_caption("Other Menu")

    running = True
    while running:
        screen.fill((255, 255, 255))
        
        text = pygame.font.Font(size=50)
        text.align = pygame.FONT_CENTER
        textsize = text.size("To Main Menu")
        rendertext = text.render("To Main Menu", antialias=False, color="black")
        myrect = pygame.Rect((320 - (textsize[0] / 2), 320 - (textsize[1] / 2)), textsize)
        other_rect = pygame.Rect((0, 0), (100, 100))
        pygame.draw.rect(screen, color="green", rect=other_rect)

        screen.blit(rendertext, myrect)

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and myrect.collidepoint(menu_mouse_pos):
                running = False
        
        pygame.display.flip()






pygame.quit()


pygame.init()
screen = pygame.display.set_mode((1280, 720))
new_menu()