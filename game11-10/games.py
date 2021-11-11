import pygame
import os




# Create our Main Surface
WIDTH, HEIGHT = 600, 400  # Define Width and Height as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the surface
pygame.display.set_caption("Play Tag!")  # Label the window with game name


# Color Pallette
GRASS_GREEN = (80, 200, 80)

# Sprites
SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50
SPRITE_WIDTHBUN = 75
SPRITE_HEIGHTBUN = 75
DEER_SPRITE = pygame.image.load(os.path.join('', 'carrot.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

WOLF_SPRITE = pygame.image.load(os.path.join('', 'bunny3.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTHBUN, SPRITE_HEIGHTBUN))

GAME_TEXT = pygame.image.load(os.path.join('', 'CARROT HUNTER.png'))


# Define
FPS = 60

# User Events
CAUGHT = pygame.USEREVENT + 1

# Game Parameters
SPEED = 5

background_image = pygame.image.load("grass.jpg").convert()

# Define a main function that runs the game
def main():
    # Create hit boxes
    deer = pygame.Rect(150, 100, SPRITE_WIDTH, SPRITE_HEIGHT)
    wolf = pygame.Rect(450, 300, SPRITE_WIDTHBUN, SPRITE_HEIGHTBUN)



    clock = pygame.time.Clock()
    run = True  # set run to True
    # While loop that runs the game
    while run:  # Game Loop

        clock.tick(FPS)
        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                run = False  # change run to False to break loop

            if event.type == CAUGHT:
                run = False
                print('GOTCHA')

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 0:  # Deer Left
            deer.x -= SPEED
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 600:  # Deer Right
            deer.x += SPEED
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 0:  # Deer Up
            deer.y -= SPEED
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 400:  # Deer Down
            deer.y += SPEED

        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED > 0:  # Wolf Left
            wolf.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED + SPRITE_WIDTHBUN < 600:  # Wolf Right
            wolf.x += SPEED
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED > 0:  # Wolf Up
            wolf.y -= SPEED
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED + SPRITE_HEIGHTBUN < 400:  # Wolf Down
            wolf.y += SPEED
        draw_window(deer, wolf)  # This function draws the screen
        deer_tagged(deer, wolf)  # Check if tagged

    pygame.quit()  # will close game


# Draw Window Function
def draw_window(deer, wolf):

    WIN.fill(GRASS_GREEN)  # Draw the Grass
    WIN.blit(background_image, [0, 0])
    WIN.blit(DEER, (deer.x, deer.y))  # Sprites
    WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites
    WIN.blit(GAME_TEXT,[-40,-10])
    pygame.display.update()  # Update the screen


# Create a function to determine if tagged
def deer_tagged(deer, wolf):
    if deer.colliderect(wolf):
        pygame.event.post(pygame.event.Event(CAUGHT))



if __name__ == "__main__":
    main()