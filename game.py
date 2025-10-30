
import pygame
import sim_ver_3 as gamesim
from buttons import ImageButton, TextButton

global_font = "Raster Forge Regular"

def main_menu():
    pygame.display.set_caption("Main Menu") # set menu caption

    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # put logo on screen
        logo = pygame.image.load("assets/Dream Leagues Large Logo.png")
        logo = pygame.transform.scale_by(logo, 720 / screen_y)
        logo_rect = logo.get_rect(x=screen.get_width() / 85, y=screen.get_height() / 6)
        screen.blit(logo, logo_rect)

        # create gui elements
        single_sim = TextButton(screen.get_width() / 25, screen.get_height() / 2, "Single Sim", int(45 * screen.get_height() / 720),
                                centered=False, font=global_font)
        exit = TextButton(single_sim.x, single_sim.y * 1.2, "Exit", int(45 * screen.get_height() / 720), centered=False, font=global_font)

        buttons = [single_sim, exit]

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

    # NOTE: this dict of team names MUST correspond to the names found in teams.json, maybe add a function to load this
    team_dict = {
        "Cavs": pygame.image.load("assets/team_logos/cavs.png"),
        "Knicks": pygame.image.load("assets/team_logos/knicks.png")
    }

    current_team = "Cavs"
    team_lst = list(team_dict.keys())
    team_index = 0
    
    team_one = None
    team_two = None

    screenx = screen.get_width()
    screeny = screen.get_height()

    # create ui elements:

    # ui for selected teams
    team_one_rect = pygame.rect.Rect((0, 0), (310 * screeny / 720, 310 * screeny / 720))
    team_one_rect.center = (screenx / 5, screeny / 4)
    team_two_rect = pygame.rect.Rect((0, 0), (310 * screeny / 720, 310 * screeny / 720))
    team_two_rect.center = (screenx * 4 / 5, screeny / 4)
    current_team_rect = pygame.rect.Rect((0, 0), (310 * screeny / 720, 310 * screeny / 720))
    current_team_rect.center = (screenx / 2, screeny / 4)
    main_rect = pygame.rect.Rect((0, 0), (team_two_rect.right - team_one_rect.left, 300 * screeny / 720))
    main_rect.center = (screenx / 2, screeny * 5.3 / 7)

    # create buttons
    cycle_r = ImageButton("assets/arrow.png", current_team_rect.right, 
                          current_team_rect.bottom + ((main_rect.top - current_team_rect.bottom) / 2),
                          screeny / 720, screeny / 720, centered=True)
    cycle_r.scale_img(0.15)
    cycle_l = ImageButton("assets/arrow.png", current_team_rect.left,
                          current_team_rect.bottom + ((main_rect.top - current_team_rect.bottom) / 2),
                          screeny / 720, screeny / 720, centered=True)
    cycle_l.rotate_img(180)
    cycle_l.scale_img(0.15)
    select = TextButton(main_rect.centerx, main_rect.centery, "Select", int(55 * (screeny / 720)), text_color="orange", font=global_font)
    sim_button = TextButton(main_rect.centerx, main_rect.centery, "Sim", int(55 * (screeny / 720)), text_color="orange", font=global_font)
    exit = ImageButton("assets/arrow.png", main_rect.left / 2, main_rect.bottom,
                          screeny / 720, screeny / 720, centered=True)
    exit.rotate_img(180)
    exit.scale_img(0.15)

    select_enabled = True

    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # ui that changes
        current_team_font = pygame.font.SysFont(name=global_font, size=int(45 * screeny / 720))
        current_team = team_lst[team_index]
        current_team_render = current_team_font.render(text=current_team, antialias=False, color="black")
        current_team_text_rect = current_team_render.get_rect()
        current_team_text_rect.center = (screenx / 2, current_team_rect.bottom * 1.1)

        
        # render ui
        pygame.draw.rect(screen, "black", main_rect, width=5, border_radius=2)
        pygame.draw.rect(screen, "black", team_one_rect, width=5, border_radius=2)
        pygame.draw.rect(screen, "black", team_two_rect, width=5, border_radius=2)
        pygame.draw.rect(screen, "black", current_team_rect, width=5, border_radius=2)

        current_team_img = pygame.transform.scale_by(team_dict[current_team], factor= (screeny / 720))
        screen.blit(current_team_render, current_team_text_rect)
        screen.blit(current_team_img, (current_team_rect.x + 5, current_team_rect.y + 5))
        

        if team_one is None:
            team_one_img = None
            pass
        else:
            team_one_img = pygame.transform.scale_by(team_dict[team_one], factor= (screeny / 720))
            screen.blit(team_one_img, (team_one_rect.x + 5, team_one_rect.y + 5))
        if team_two is None:
            team_two_img = None
        else:
            team_two_img = pygame.transform.scale_by(team_dict[team_two], factor= (screeny / 720))
            screen.blit(team_two_img, (team_two_rect.x + 5, team_two_rect.y + 5))

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
                    sim_screen((team_one, team_one_img), (team_two, team_two_img),
                               (current_team_rect.right, current_team_rect.bottom + ((main_rect.top - current_team_rect.bottom) / 2)),
                               (current_team_rect.left, current_team_rect.bottom + ((main_rect.top - current_team_rect.bottom) / 2)),
                               (screenx / 2, current_team_rect.bottom * 1.1))
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

def render_stat_column(stat, player_list, x_cord, y_cord, diff, max_w):

    factor = 0
    for player in player_list:
        stat_font = pygame.font.SysFont(global_font, 50)
        stat_render = stat_font.render(str(player.game_stats[stat]), False, "black")
        stat_rect = stat_render.get_rect(center=((x_cord), (y_cord + (factor * diff))))
        amt = 1
        while stat_rect.width > (max_w - 10):
            stat_font = pygame.font.SysFont(global_font, 50 - amt)
            stat_render = stat_font.render(str(player.game_stats[stat]), False, "black")
            stat_rect = stat_render.get_rect(center=((x_cord), (y_cord + (factor * diff))))
            amt += 1
        screen.blit(stat_render, stat_rect)
        factor += 1
    

def sim_screen(team_one_vals, team_two_vals, right_button_cords, left_button_cords, team_label_cords):
    pygame.display.set_caption("Sim Menu") # set menu caption

    screenx = screen.get_width()
    screeny = screen.get_height()
    
    team_list = [team_one_vals[0], team_two_vals[0]]
    team_index = 0

    page = 0

    # create ui elements:

    # ui for selected teams
    team_one_rect = pygame.rect.Rect((0, 0), (310 * screeny / 720, 310 * screeny / 720))
    team_one_rect.center = (screenx / 5, screeny / 4)
    team_two_rect = pygame.rect.Rect((0, 0), (310 * screeny / 720, 310 * screeny / 720))
    team_two_rect.center = (screenx * 4 / 5, screeny / 4)

    main_rect = pygame.rect.Rect((0, 0), (team_two_rect.right - team_one_rect.left, 300 * screeny / 720))
    main_rect.center = (screenx / 2, screeny * 5.3 / 7)

    # create buttons
    cycle_r = ImageButton("assets/arrow.png", right_button_cords[0], 
                          right_button_cords[1],
                          screeny / 720, screeny / 720, centered=True)
    cycle_r.scale_img(0.15)
    cycle_l = ImageButton("assets/arrow.png", left_button_cords[0],
                          left_button_cords[1],
                          screeny / 720, screeny / 720, centered=True)
    cycle_l.rotate_img(180)
    cycle_l.scale_img(0.15)
    cycle_u = ImageButton("assets/arrow.png", 0, 
                          int(main_rect.centery - (main_rect.height / 4)),
                          screeny / 720, screeny / 720, centered=True)
    cycle_u.scale_img(0.15)
    cycle_u.x = int(cycle_u.x + (main_rect.left / 2))
    cycle_u.rotate_img(90)
    cycle_d = ImageButton("assets/arrow.png", 0, 
                          int(main_rect.centery + (main_rect.height / 4)),
                          screeny / 720, screeny / 720, centered=True)
    cycle_d.scale_img(0.15)
    cycle_d.x = int(cycle_d.x + (main_rect.left / 2))
    cycle_d.rotate_img(-90)
    exit = ImageButton("assets/arrow.png", main_rect.left / 2, main_rect.bottom,
                          screeny / 720, screeny / 720, centered=True)
    exit.rotate_img(180)
    exit.scale_img(0.15)

    dash = pygame.font.Font(size=int(100 * screeny / 720))
    dash_render = dash.render("-", antialias=False, color="black")
    dash_rect = dash_render.get_rect(centerx = screenx / 2, centery=team_one_rect.centery)

    # run actual sim and get final scores
    team_dict = gamesim.load_teams("gamedata/testteams.json")
    team_one = gamesim.dict_to_team(team_dict[team_one_vals[0]])
    team_two = gamesim.dict_to_team(team_dict[team_two_vals[0]])
    game = gamesim.Match(team_one, team_two)
    game.play()

    rost_size = max([len(game.teams["t1"].roster), len(game.teams["t2"].roster)])
    page_count = rost_size // 4
    if rost_size % 4 != 0:
        page_count += 1


    team_one_pages = {}
    team_two_pages = {}
    for x in range(0, page_count):
        slice_one = game.teams["t1"].roster[(x * 4):(x + 1) * 4]
        slice_two = game.teams["t2"].roster[(x * 4):(x + 1) * 4]
        team_one_pages[x] = slice_one
        team_two_pages[x] = slice_two


    running = True
    while running:
        screen.fill("white")
        mouse_pos = pygame.mouse.get_pos()

        # ui that changes
        team_one_score = pygame.font.SysFont(name=global_font, size=int(60 * screeny / 720))
        team_one_score_render = team_one_score.render(f"{game.scores["t1"]}", antialias=False, color="black")
        team_one_score_rect = team_one_score_render.get_rect(left=(team_one_rect.right + 30),
                                                             centery=team_one_rect.centery)

        team_two_score = pygame.font.SysFont(name=global_font, size=int(60 * screeny / 720))
        team_two_score_render = team_two_score.render(f"{game.scores["t2"]}", antialias=False, color="black")
        team_two_score_rect = team_two_score_render.get_rect(right=(team_two_rect.left - 30),
                                                             centery=team_one_rect.centery)
        

        # render ui
        pygame.draw.rect(screen, "black", main_rect, width=5, border_radius=2)
        pygame.draw.rect(screen, "black", team_one_rect, width=5, border_radius=2)
        pygame.draw.rect(screen, "black", team_two_rect, width=5, border_radius=2)
        screen.blit(team_one_score_render, team_one_score_rect)
        screen.blit(team_two_score_render, team_two_score_rect)
        screen.blit(team_one_vals[1], (team_one_rect.x + 5, team_one_rect.y + 5))
        screen.blit(team_two_vals[1], (team_two_rect.x + 5, team_two_rect.y + 5))
        screen.blit(dash_render, dash_rect)
        
        current_team_font = pygame.font.SysFont(name=global_font, size=int(45 * screeny / 720))
        current_team = team_list[team_index]
        current_team_render = current_team_font.render(text=current_team, antialias=False, color="black")
        current_team_text_rect = current_team_render.get_rect()
        current_team_text_rect.center = team_label_cords
        screen.blit(current_team_render, current_team_text_rect)
        
        for x in range(4):
            pygame.draw.line(screen, "black", (main_rect.left + ((x + 1) * main_rect.width / 5), main_rect.top),
                             (main_rect.left + ((x + 1 )* main_rect.width / 5), main_rect.bottom), 5)

            pygame.draw.line(screen, "black", (main_rect.left, (main_rect.top + ((x + 1) * (main_rect.height / 5)))),
                             (main_rect.right, (main_rect.top + ((x + 1) * (main_rect.height / 5)))), 5)
            
        # insert columns into table
        player_font = pygame.font.SysFont(global_font, 50)
        player_font_render = player_font.render("Player", False, "orange")
        player_font_rect = player_font_render.get_rect(center=(main_rect.left + (main_rect.width / 5) / 2,
                                                               main_rect.top + (main_rect.height / 5) / 2))
        pts_font = pygame.font.SysFont(global_font, 50)
        pts_font_render = pts_font.render("PTS", False, "orange")
        pts_font_rect = pts_font_render.get_rect(center=((main_rect.left + (3 * main_rect.width / 5) / 2) ,
                                                               main_rect.top + (main_rect.height / 5) / 2))
        
        ast_font = pygame.font.SysFont(global_font, 50)
        ast_font_render = ast_font.render("AST", False, "orange")
        ast_font_rect = ast_font_render.get_rect(center=((main_rect.left + (5 * main_rect.width / 5) / 2) ,
                                                               main_rect.top + (main_rect.height / 5) / 2))
        
        three_font = pygame.font.SysFont(global_font, 50)
        three_font_render = three_font.render("3PM", False, "orange")
        three_font_rect = three_font_render.get_rect(center=((main_rect.left + (7 * main_rect.width / 5) / 2) ,
                                                               main_rect.top + (main_rect.height / 5) / 2))
        
        fg_font = pygame.font.SysFont(global_font, 50)
        fg_font_render = fg_font.render("FG%", False, "orange")
        fg_font_rect = fg_font_render.get_rect(center=((main_rect.left + (9 * main_rect.width / 5) / 2) ,
                                                               main_rect.top + (main_rect.height / 5) / 2))
        
        '''
        need to be able to view the whole team
        pages contain 4 players
        pages = rostersize // 4
        if rostersize % 4:
            pages += 1
        start index : start index + 4
        page must determine start index
        page# * 4 - 4: page# * 4

        '''

        

        team_one_players = team_one_pages[page]
        team_two_players = team_two_pages[page]

        if team_index == 0:
            render_table_values(team_one_players, main_rect)
        elif team_index == 1:
            render_table_values(team_two_players, main_rect)
        
        # render table values
        screen.blit(player_font_render, player_font_rect)
        screen.blit(pts_font_render, pts_font_rect)
        screen.blit(ast_font_render, ast_font_rect)
        screen.blit(three_font_render, three_font_rect)
        screen.blit(fg_font_render, fg_font_rect)

        # render buttons
        cycle_r.render_button(screen)
        cycle_l.render_button(screen)
        cycle_d.render_button(screen)
        cycle_u.render_button(screen)
        exit.render_button(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_r.rect.collidepoint(mouse_pos):
                team_index = cycle_list(team_list, team_index, "forward") # cycles index up by one
                page = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_l.rect.collidepoint(mouse_pos):
                team_index = cycle_list(team_list, team_index, "backward") # cycles index down by one
                page = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_u.rect.collidepoint(mouse_pos):
                page = cycle_list(range(page_count), page, "backward") # cycles index down by one
            elif event.type == pygame.MOUSEBUTTONDOWN and cycle_d.rect.collidepoint(mouse_pos):
                page = cycle_list(range(page_count), page, "forward") # cycles index down by one
            elif event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(mouse_pos):
                running = False
            
            
        
        if running is False:
            break

        pygame.display.flip()

def render_table_values(players, main_rect):

    render_stat_column("name", players, main_rect.left + (main_rect.width / 5) / 2,
                           (main_rect.top + (3 * main_rect.height / 5) / 2), main_rect.height / 5,
                           main_rect.width / 5)
    render_stat_column("pts", players, main_rect.left + (3 * main_rect.width / 5) / 2,
                           (main_rect.top + (3 * main_rect.height / 5) / 2), main_rect.height / 5,
                           main_rect.width / 5)
    render_stat_column("ast", players, main_rect.left + (5 * main_rect.width / 5) / 2,
                           (main_rect.top + (3 * main_rect.height / 5) / 2), main_rect.height / 5,
                           main_rect.width / 5)
    render_stat_column("threes", players, main_rect.left + (7 * main_rect.width / 5) / 2,
                           (main_rect.top + (3 * main_rect.height / 5) / 2), main_rect.height / 5,
                           main_rect.width / 5)
    render_stat_column("fg%", players, main_rect.left + (9 * main_rect.width / 5) / 2,
                           (main_rect.top + (3 * main_rect.height / 5) / 2), main_rect.height / 5,
                           main_rect.width / 5)
    

pygame.init()
screen_x = 2256
screen_y = 1504
screen = pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)

main_menu()

# TODO: function documentation
# TODO: clean up logic and make code more readable
# TODO: implement pages for stat viewing
# TODO: implement stat viewing for whole team, not just starting lineup (possibly involves cleaning up the "rosterize" function)