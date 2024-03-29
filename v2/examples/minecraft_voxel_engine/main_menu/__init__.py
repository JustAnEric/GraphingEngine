import pygame, sys
from .button import Button

from voxel_engine import VoxelEngine
from threading import Thread

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/MinecraftRegular.otf", size)

def launch_minecraft():
    global SCREEN
    SCREEN = pygame.Surface((1280, 720))
    app = VoxelEngine(play_loading_game)
    app.run()
    pygame.display.set_caption("Minecraft Kinda")
    while app.is_running == True: pass
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Launch Minecraft?", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 460), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Red")
    
        PLAY_LAUNCH = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 340), 
                            text_input="LAUNCH", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        PLAY_LAUNCH.changeColor(PLAY_MOUSE_POS)
        PLAY_LAUNCH.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_LAUNCH.checkForInput(PLAY_MOUSE_POS):
                    launch_minecraft()

        pygame.display.update()

def play_loading_game(wl):
    #while True:
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    SCREEN.fill("black")
    PLAY_TEXT = get_font(45).render(wl, True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
    SCREEN.blit(PLAY_TEXT, PLAY_RECT)

    PLAY_BACK = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 460), 
                            text_input="CANCEL", font=get_font(55), base_color="White", hovering_color="Red")

    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_BACK.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

    #pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 460), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="White")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MINECRAFT", True, "#444444" #"#b68f40"
                                         )
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/ButtonRect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def start():
    main_menu()