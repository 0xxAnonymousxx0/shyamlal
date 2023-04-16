import pygame
pygame.init()

#game window
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode ((screen_width,screen_height))
pygame.display.set_caption("UwU")
clock = pygame.time.Clock()
font = pygame.font.Font('Pixeltype.ttf',40)
fonte = pygame.font.Font(None,30)
game_over = False
collision = False
#clour

white = (255, 255, 255)
red = (255, 0, 0)

black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)


#bg img

bg_img = pygame.image.load('sky.png').convert_alpha()


#score
score = 0
score_message = font.render("sigma score :",False,white)
score_rect = score_message.get_rect(center =(375,50))
score_messageS = fonte.render("sigma score :"+str(score),False,red)
hiscore_messageS = fonte.render("high sigma score :",False,red)




#enemies

snail = pygame.image.load('snail1.png')
snail_x = 600
snail_y = 253
snail_rect = snail.get_rect(bottomright =(500,289))

fly = pygame.image.load('Fly1.png')
fly_x = 600
fly_y = 200
fly_rect = fly.get_rect(bottomright =(600,130))


hand_1 = pygame.image.load('h1.png')
hand_2 = pygame.image.load('h2.png')

h1_rect = hand_1.get_rect(bottomright =(600,130))
h2_rect = hand_2.get_rect(bottomright =(600,130))

#player

player = pygame.image.load('player_stand.png').convert_alpha()
player_rect  = player.get_rect(bottomright =(80,289))
player_posx = 70
player_posy = 205
player_gravity = 0
cycle = 0
jump = 0

#can't touch grass
grass = pygame.image.load('r.png').convert_alpha()
grass_rect  = grass.get_rect(bottomright =(50,350))

#time
def text_screen(text,color, x,y ):
    screen_text = font.render(text,False,color)
    screen.blit(screen_text,[x,y])

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos) and player_rect.y >= 205:player_gravity =  -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.y >= 105:
                player_gravity =  -20
                jump += 1




    player_rect.y += player_gravity
    player_gravity += 1

    if snail_rect.x >= screen_width :
        cycle += 1
    print(cycle)

    if player_rect.y > 205:
        player_rect.y = 205
        player_gravity = 0

    if player_rect.y <= -10 :
        player_rect.y = 205
    snail_rect.x -= 6
    if snail_rect.x <= -100: snail_rect.x = 800
    if fly_rect.x <= -100: fly_rect.x = 800
    fly_rect.x -= 4
    if cycle >= 2:
        snail_rect.x -=4
        cycle += 1/100
    if snail_rect.x >= 800: snail_rect.x = 800

    if fly_rect.x >=screen_width:
        fly_rect.x = 0

    if cycle >= 1:
        score = 1
    if cycle >= 2:
        fly_rect.x -=1.24
        snail_rect.x +=5
    if cycle >= 7:
        fly_rect.x -=1
        snail_rect.x -=2

    if cycle >= 12:
        fly_rect.x += 14
        snail_rect.x += 2
        player_rect.x = 0

    if cycle >= 14:
        fly_rect.x = - 100
        snail_rect.x = - 100



    if collision == True:
        cycle = 0

    if player_rect.y >= 350:
        player_rect.y = 200

    if jump >=0 :
        player_rect.x = 100

    if game_over == True:
        screen.fill(black)
        screen.blit(score_messageS,(10,30))
        screen.blit(hiscore_messageS, (10, 0))

#blit
    if game_over == False:
        screen.blit(bg_img,(0,0))
        screen.blit(player,player_rect)
        screen.blit(snail,snail_rect)
        screen.blit(fly, fly_rect)
        screen.blit(grass,(-10,270))
        screen.blit(score_message,score_rect)

        if player_rect.colliderect(snail_rect):
            game_over = True
            collision = True


        if player_rect.colliderect(fly_rect):
            game_over = True
            collision = True


    clock.tick(60)
    pygame.display.update()

