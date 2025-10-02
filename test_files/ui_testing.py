import pygame

class Button:

    def __init__(self, coords=None, fontcolor=None, fontsize=None, text=None, font=None, shape=None, dimensions=None, color=None):
        self.shape = shape

        if text != None:
            self.font = pygame.font.Font(size=fontsize) # type: ignore
            self.font.align = pygame.FONT_CENTER
            self.size = self.font.size(text)
            self.render = self.font.render(text, antialias=False, color=fontcolor) # type: ignore
            self.rect = pygame.Rect(coords, self.size) # type: ignore
            self.coords = coords
        else:
            match shape:
                case "rect":
                    self.rect = pygame.Rect(coords, dimensions) # type: ignore
                case "tri":
                    self.rect = dimensions
            self.color = color

    def render_button(self):

        if self.shape == None:
            screen.blit(self.render, self.rect) # type: ignore
        elif self.shape == "rect":
            pygame.draw.rect(screen, self.color, self.rect) # type: ignore
        elif self.shape == "tri":
            pygame.draw.polygon(screen, self.color, self.rect) # type: ignore




def new_menu():
    pygame.display.set_caption("Main Menu")

    running = True
    while running:
        screen.fill((255, 255, 255))

        single_button = Button((50, 360), "black", 50, "Single Sim")
        franchise_button = Button((50, single_button.coords[1] + single_button.size[1] + 10), "black", 50, "Franchise Mode") # type: ignore
        exit_button = Button((50, franchise_button.coords[1] + franchise_button.size[1] + 10), "black", 50, "Exit") # type: ignore

        single_button.render_button()
        franchise_button.render_button()
        exit_button.render_button()

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and single_button.rect.collidepoint(menu_mouse_pos): # type: ignore
                single_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and franchise_button.rect.collidepoint(menu_mouse_pos): # type: ignore
                franchise_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and exit_button.rect.collidepoint(menu_mouse_pos): # type: ignore
                running = False

        pygame.display.flip()


def single_menu():
    pygame.display.set_caption("Single Sim")

    teamdict = {
        "cavs": pygame.image.load("cavs.png"),
        "knicks": pygame.image.load("knicks.png")
    }

    current_team = "cavs"
    team_lst = list(teamdict.keys())
    team_index = 0
    
    team_one = None
    team_two = None

    running = True
    while running:
        screen.fill((255, 255, 255))

        # putting teams on screen
        current_team = team_lst[team_index]
        teamrect = pygame.Rect(((1280/2) - 150, 50), (300, 300))
        pygame.draw.rect(screen, "black", ((485, 45), (310, 310)))
        screen.blit(teamdict[current_team], teamrect)

        # TODO: modernize GUI -> im sick of manually calculating gui coordinates

        # putting text on screen
        team_label = pygame.font.Font(size=35)
        team_label.align = pygame.FONT_CENTER
        team_label_size = team_label.size(current_team)
        team_label_rect = pygame.Rect(((1280/2)  - (team_label_size[0] / 2), (720 / 2) + 15 - (team_label_size[1]/2)),(team_label_size))
        team_label_render = team_label.render(current_team, False, "black")
        screen.blit(team_label_render, team_label_rect)

        # putting selected teams on screen
        team_one_rect = pygame.Rect((((screen_x / 4) - 150 - 70), 50), (300, 300))
        pygame.draw.rect(screen, "black", ((((screen_x / 4) - 150 - 5 - 70), 50 - 5), (310, 310)))
        if team_one is None:
            pass
        else:
            screen.blit(teamdict[team_one], team_one_rect)

        team_two_rect = pygame.Rect((((screen_x / 4) - 150 + 70), 50), (300, 300))
        pygame.draw.rect(screen, "black", (((((screen_x * 3) / 4  - 5 + 70) - 150), 50 - 5), (310, 310)))
        if team_two is None:
            pass
        else:
            screen.blit(teamdict[team_two], team_two_rect)


        # adding buttons
        right_tri = ((800, 155), (800, 245), (850, 200))
        right_button = Button(dimensions=right_tri, color="black", shape="tri")
        left_tri = ((480, 155), (480, 245), (430, 200))
        left_button = Button(dimensions=left_tri, color="black", shape="tri")
        back_button = Button((50, 650), "black", 50, "Back")
        select_button = Button(coords=((1280 / 2), (650)), fontcolor="green", fontsize=30, text="Select")
        
        right_button.render_button()
        left_button.render_button()
        back_button.render_button()
        select_button.render_button()
      

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.rect.collidepoint(menu_mouse_pos): # type: ignore
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and check_in_triangle(menu_mouse_pos, right_button.rect): # type: ignore
                team_index = cycle_list(team_lst, team_index, "forward")
            elif event.type == pygame.MOUSEBUTTONDOWN and check_in_triangle(menu_mouse_pos, left_button.rect): # type: ignore
                team_index = cycle_list(team_lst, team_index, "backward")

        pygame.display.flip()

def cycle_list(lst, index, dir):
    '''used for cycling UI elements'''

    match dir:
        case "forward":

            if index + 1 > (len(lst) - 1):
                return 0
            else:
                return index + 1
    
        case "backward":
        
            if index - 1 < 0:
                return (len(lst) - 1)
            else:
                return index - 1

def franchise_menu():
    pygame.display.set_caption("Franchise Menu")

    running = True
    while running:
        screen.fill((255, 255, 255))

        back_button = Button((50, 360), "black", 50, "Coming Soon")
        
        back_button.render_button()
      

        menu_mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.rect.collidepoint(menu_mouse_pos): # type: ignore
                running = False

        pygame.display.flip()

def check_in_triangle(coords, triangle_coords): # TODO: implement triangle collision detection
    
    y_vals = []
    x_vals = []
    for tup in triangle_coords:
        x_vals.append(tup[0])
        y_vals.append(tup[1])


    x_max = max(x_vals)
    x_min = min(x_vals)
    y_max = max(y_vals)
    y_min = min(y_vals)

    if (coords[0] >= x_min and coords[0] <= x_max) and (coords[1] >= y_min and coords[1] <= y_max):
        return True
    
    return False
    


        

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
screen_x = 1280
screen_y = 720
new_menu()