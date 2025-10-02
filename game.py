
import pygame
import sim_ver_3 as gamesim
from buttons import ImageButton, TextButton

def main_menu():
    pygame.display.set_caption("Main Menu") # set menu caption

    # create gui elements
    single_sim = TextButton(screen_x / 25, screen_y / 2, "Single Sim", 70, centered=False)
    exit = TextButton(single_sim.x, single_sim.y * 1.2, "Exit", 70, centered=False)

    buttons = [single_sim, exit]

    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # render gui elements
        for button in buttons:
            button.render_button(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and single_sim.rect.collidepoint(mouse_pos):
                single_sim_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(mouse_pos):
                running = False

        pygame.display.flip()

def single_sim_menu():
    pygame.display.set_caption("Single Sim") # set menu caption

    # NOTE: this dict of team names MUST correspond to the names found in teams.json
    team_dict = {
        "Cavs": pygame.image.load("assets/team_logos/cavs.png"),
        "Knicks": pygame.image.load("assets/team_logos/knicks.png")
    }

    current_team = "Cavs"
    team_lst = list(team_dict.keys())
    team_index = 0
    
    team_one = None
    team_two = None

    # create ui elements:

    # ui for selected teams
    team_one_rect = pygame.rect.Rect((0, 0), (310 * scale_x, 310 * scale_y))
    team_one_rect.center = (screen_x / 5, screen_y / 4)
    team_two_rect = pygame.rect.Rect((0, 0), (310 * scale_x, 310 * scale_y))
    team_two_rect.center = (screen_x * 4 / 5, screen_y / 4)
    current_team_rect = pygame.rect.Rect((0, 0), (310 * scale_x, 310 * scale_y))
    current_team_rect.center = (screen_x / 2, screen_y / 4)
    main_rect = pygame.rect.Rect((0, 0), (team_two_rect.right - team_one_rect.left, 300 * scale_y))
    main_rect.center = (screen_x / 2, screen_y * 5.3 / 7)

    # create buttons
    cycle_r = ImageButton("assets/arrow.png", current_team_rect.right * 0.98, current_team_rect.bottom * 0.98,
                          scale_x, scale_y, centered=False)
    cycle_r.scale_img(0.15)
    cycle_l = ImageButton("assets/arrow.png", (current_team_rect.right - cycle_r.rect.left) + current_team_rect.left,
                          current_team_rect.bottom * 0.98, scale_x, scale_y, centered=False, right=True)
    cycle_l.rotate_img(180)
    cycle_l.scale_img(0.15)
    select = TextButton(main_rect.centerx, main_rect.centery, "Select", 80, text_color="green")
    sim_button = TextButton(main_rect.centerx, main_rect.centery, "Sim", 80, text_color="green")
    exit = ImageButton("assets/arrow.png", screen_x * 0.01, screen_y * 4.3 / 5,
                          scale_x, scale_y, centered=False)
    exit.rotate_img(180)
    exit.scale_img(0.15)

    select_enabled = True

    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # ui that changes
        current_team_font = pygame.font.Font(size=70)
        current_team = team_lst[team_index]
        current_team_render = current_team_font.render(text=current_team, antialias=False, color="black")
        current_team_text_rect = current_team_render.get_rect().scale_by(scale_x, scale_y)
        current_team_text_rect.center = (screen_x / 2, current_team_rect.bottom * 1.1)

        
        # render ui
        pygame.draw.rect(screen, "black", main_rect, width=5)
        pygame.draw.rect(screen, "black", team_one_rect, width=5)
        pygame.draw.rect(screen, "black", team_two_rect, width=5)
        pygame.draw.rect(screen, "black", current_team_rect, width=5)
        screen.blit(current_team_render, current_team_text_rect)
        screen.blit(team_dict[current_team], (current_team_rect.x + 5, current_team_rect.y + 5))
        

        if team_one is None:
            pass
        else:
            screen.blit(team_dict[team_one], (team_one_rect.x + 5, team_one_rect.y + 5))
        if team_two is None:
            pass
        else:
            screen.blit(team_dict[team_two], (team_two_rect.x + 5, team_two_rect.y + 5))

        # render buttons
        cycle_l.render_button(screen)
        cycle_r.render_button(screen)
        exit.render_button(screen)
        
        if team_one is None or team_two is None:
            select.render_button(screen)
        else:
            select_enabled = False
            sim_button.render_button(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_r.rect.collidepoint(mouse_pos):
                team_index = cycle_list(team_lst, team_index, "forward") # cycles index up by one
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_l.rect.collidepoint(mouse_pos):
                team_index = cycle_list(team_lst, team_index, "backward") # cycles index down by one
            elif event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(mouse_pos):
                running = False

            if select_enabled:
                if event.type == pygame.MOUSEBUTTONDOWN and select.rect.collidepoint(mouse_pos):
                    if team_one is None:
                        team_one = current_team
                    else:
                        team_two = current_team
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and sim_button.rect.collidepoint(mouse_pos):
                    sim((team_one, team_dict[team_one]), (team_two, team_dict[team_two]))
                    running = False
        
        if running is False:
            break

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

def sim(team_one_vals, team_two_vals):
    pygame.display.set_caption("Sim Menu") # set menu caption
    
    # create ui elements:

    # ui for selected teams
    team_one_rect = pygame.rect.Rect((0, 0), (310 * scale_x, 310 * scale_y))
    team_one_rect.center = (screen_x / 5, screen_y / 4)
    team_two_rect = pygame.rect.Rect((0, 0), (310 * scale_x, 310 * scale_y))
    team_two_rect.center = (screen_x * 4 / 5, screen_y / 4)

    main_rect = pygame.rect.Rect((0, 0), (team_two_rect.right - team_one_rect.left, 300 * scale_y))
    main_rect.center = (screen_x / 2, screen_y * 5.3 / 7)

    # create buttons
    exit = ImageButton("assets/arrow.png", screen_x * 0.01, screen_y * 4.3 / 5,
                          scale_x, scale_y, centered=False)
    exit.rotate_img(180)
    exit.scale_img(0.15)

    # run actual sim and get final scores
    team_dict = gamesim.load_teams("gamedata/testteams.json")
    team_one = gamesim.dict_to_team(team_dict[team_one_vals[0]])
    team_two = gamesim.dict_to_team(team_dict[team_two_vals[0]])
    game = gamesim.Match(team_one, team_two)
    game.play()


    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # ui that changes
        team_one_score = pygame.font.Font(size=100)
        team_one_score_render = team_one_score.render(f"{game.scores["t1"]}", antialias=False, color="black")
        team_one_score_rect = team_one_score_render.get_rect(left=(team_one_rect.right + 30),
                                                             centery=team_one_rect.centery)

        team_two_score = pygame.font.Font(size=100)
        team_two_score_render = team_two_score.render(f"{game.scores["t2"]}", antialias=False, color="black")
        team_two_score_rect = team_two_score_render.get_rect(right=(team_two_rect.left - 30),
                                                             centery=team_one_rect.centery)

        # render ui
        pygame.draw.rect(screen, "black", main_rect, width=5)
        pygame.draw.rect(screen, "black", team_one_rect, width=5)
        pygame.draw.rect(screen, "black", team_two_rect, width=5)
        screen.blit(team_one_score_render, team_one_score_rect)
        screen.blit(team_two_score_render, team_two_score_rect)
        screen.blit(team_one_vals[1], (team_one_rect.x + 5, team_one_rect.y + 5))
        screen.blit(team_two_vals[1], (team_two_rect.x + 5, team_two_rect.y + 5))

        # render buttons
        exit.render_button(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(mouse_pos):
                running = False
            
            
        
        if running is False:
            break

        pygame.display.flip()


pygame.init()
screen_x = 1280
screen_y = 720
scale_x = screen_x / 1280
scale_y = screen_y / 720
screen = pygame.display.set_mode((screen_x, screen_y))

main_menu()