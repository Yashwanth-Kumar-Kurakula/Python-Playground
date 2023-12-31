'''
Thanks to Clear code for the tutorial.
Tutorial Reference -  https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=3221s
'''

import pygame
from sys import exit
import random

def display_score():
    """
    Displays the current score on the screen.
    """
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"Score: {round(current_time/1000)}", False, (64,64,64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return round(current_time/1000)

def obstacle_movement(obstacle_list):
    """
    Moves obstacles to the left and removes those that are off-screen.
    """
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def player_animation():
    """
    Animates the player character based on its position.
    """
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

def collisions(player, obstacles):
    """
    Checks for collisions between the player and obstacles.
    """
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect):
                return False
    return True

def start_screen():
    """
    Displays the start screen with game title and instructions.
    """
    screen.fill((94, 129, 162))
    player_stand_surf = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
    player_stand_surf = pygame.transform.scale2x(player_stand_surf)
    player_stand_rect = player_stand_surf.get_rect(center=(400, 200))

    runner_text_surf = test_font.render("Runner", False, "white")
    runner_text_rect = runner_text_surf.get_rect(center=(400, 50))

    screen.blit(player_stand_surf, player_stand_rect)
    screen.blit(runner_text_surf, runner_text_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Load graphics and audio resources
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

snail_frames = [pygame.image.load(f"graphics/snail/snail{i}.png").convert_alpha() for i in range(1, 3)]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frames = [pygame.image.load(f"graphics/fly/Fly{i}.png").convert_alpha() for i in range(1, 3)]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk = [pygame.image.load(f"graphics/Player/player_walk_{i}.png").convert_alpha() for i in range(1, 3)]
player_jump = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()

player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(bottomleft=(80, 300))

player_stand_surf = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand_surf = pygame.transform.scale2x(player_stand_surf)
player_stand_rect = player_stand_surf.get_rect(center=(400, 200))

jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.5)

bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.6)
bg_music.play(-1)

player_gravity = -20

game_active = False
start_time = 0
score = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Handle mouse click for jumping
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 300:
                        player_gravity = -20

            # Handle space key for jumping
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
                        jump_sound.play()

            # Generate obstacles at regular intervals
            if event.type == obstacle_timer:
                if random.randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(random.randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(random.randint(900, 1100), 210)))

            # Animate snail frames
            if event.type == snail_animation_timer:
                snail_frame_index = 1 - snail_frame_index  # Toggle between 0 and 1
                snail_surf = snail_frames[snail_frame_index]

            # Animate fly frames
            if event.type == fly_animation_timer:
                fly_frame_index = 1 - fly_frame_index  # Toggle between 0 and 1
                fly_surf = fly_frames[fly_frame_index]

        else:
            # Handle space key to start the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        # Game active logic
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Display and update score
        score = display_score()

        # Move obstacles, check collisions, and update player position
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        # Animate player
        player_animation()
        screen.blit(player_surf, player_rect)

    else:
        # Game inactive logic (start screen or game over screen)
        start_screen()
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        if score == 0:
            instructions_text_surf = test_font.render("Press SPACE to run", False, "white")
            instructions_text_rect = instructions_text_surf.get_rect(center=(400, 350))
            screen.blit(instructions_text_surf, instructions_text_rect)
        else:
            score_message_surf = test_font.render(f"Your score is {score}", False, "white")
            score_message_rect = score_message_surf.get_rect(center=(400, 350))
            screen.blit(score_message_surf, score_message_rect)

    pygame.display.update()
    clock.tick(60)
    
