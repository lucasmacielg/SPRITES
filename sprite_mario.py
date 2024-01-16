import pygame 
import spritesheet 

pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Mario")

sprite_sheet_image1 = pygame.image.load("mario.png").convert_alpha()
sprite_sheet1 = spritesheet.SpriteSheet(sprite_sheet_image1)

BLACK = (0, 0, 0)

animation_list = []
animation_steps = [4, 4, 3, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 300
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet1.get_image(step_counter, 35, 60, 5, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:
    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()
    
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
    if frame >= len(animation_list[action]):
        frame = 0

    screen.blit(animation_list[action][frame], (230, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    pygame.display.flip()

pygame.quit()
