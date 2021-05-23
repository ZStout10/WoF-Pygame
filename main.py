

# Wheel of Fortune
# Date started: 3/25/2021
# This is the start of a new adventure. :)

# Creators: Will Robinson, Mark Poplawski, Laura Remeika and Zach Stout

# 5/12/2021


from pygame.locals import *

import pygame, sys, random, time, random

mainClock = pygame.time.Clock()

pygame.init()
# Screen resolution
screenWidth, screenHeight = 1920, 1080

gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Wheel of Fortune')

font = pygame.font.SysFont('Constantia', 30)
base_font = pygame.font.Font(None,32)
board_font = pygame.font.Font(None,100)

#define colors
bg = (204, 102, 0)
black = (0, 0, 0)
white = (255,255,255)
blue = (0, 0, 255)
green = (80, 200, 120)
red = (255, 0, 0)
purple = (147, 0, 184)
yellow = (235, 204, 52)
lBlue = (52, 195, 235)

#Phrases for the game
phrases = ["Spongebob", "Southpark", "Runescape", "Shrek"]
phrase_pick = random.randint(1,4)
phrase_pick = phrases[phrase_pick-1]
phrase_copy = []
x = 0
fill_array = '-'
while x < len(phrase_pick):
    phrase_copy.extend(fill_array)
    x += 1

#To put a specific letter to a specific box (only row 2)
board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
board_square_rect1 = board_square_text1.get_rect()
board_square_rect1.center = (195, 210)

board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
board_square_rect2 = board_square_text2.get_rect()
board_square_rect2.center = (313, 210)

board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
board_square_rect3 = board_square_text3.get_rect()
board_square_rect3.center = (433, 210)

board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
board_square_rect4 = board_square_text4.get_rect()
board_square_rect4.center = (552, 210)

board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
board_square_rect5 = board_square_text5.get_rect()
board_square_rect5.center = (672, 210)

if len(phrase_pick) == 9:
    board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
    board_square_rect6 = board_square_text6.get_rect()
    board_square_rect6.center = (791, 210)

    board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
    board_square_rect7 = board_square_text7.get_rect()
    board_square_rect7.center = (909, 210)

    board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
    board_square_rect8 = board_square_text8.get_rect()
    board_square_rect8.center = (1028, 210)

    board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
    board_square_rect9 = board_square_text9.get_rect()
    board_square_rect9.center = (1148, 210)


#Player name boxes
user_text1 = ''
player1_info_rect = pygame.Rect(50,900,140,50)
player1_name = pygame.Rect(60,910,120,32)

#Solve text box
solve_text1 = ''
solve_text_rect = pygame.Rect(1710,1010,200,50)
solve_text = pygame.Rect(1720,1020,200,32)

#Invisible clickable box over the buttons
spin_button = pygame.Rect(1377, 853, 108, 108)
solve_button = pygame.Rect(1695, 930, 139, 75)
vowel_button = pygame.Rect(1695, 805, 139, 75)
a_button = pygame.Rect(1289, 608, 75, 75)
b_button = pygame.Rect(245, 565, 75, 75)
c_button = pygame.Rect(333, 565, 75, 75)
d_button = pygame.Rect(422, 565, 75, 75)
e_button = pygame.Rect(1383, 608, 75, 75)
f_button = pygame.Rect(510, 565, 75, 75)
g_button = pygame.Rect(598, 565, 75, 75)
h_button = pygame.Rect(684, 565, 75, 75)
i_button = pygame.Rect(1477, 608, 75, 75)
j_button = pygame.Rect(771, 565, 75, 75)
k_button = pygame.Rect(858, 565, 75, 75)
l_button = pygame.Rect(946, 565, 75, 75)
m_button = pygame.Rect(1034, 565, 75, 75)
n_button = pygame.Rect(209, 649, 75, 75)
o_button = pygame.Rect(1572, 608, 75, 75)
p_button = pygame.Rect(295, 649, 75, 75)
q_button = pygame.Rect(381, 649, 75, 75)
r_button = pygame.Rect(467, 649, 75, 75)
s_button = pygame.Rect(553, 649, 75, 75)
t_button = pygame.Rect(639, 649, 75, 75)
u_button = pygame.Rect(1667, 608, 75, 75)
v_button = pygame.Rect(725, 649, 75, 75)
w_button = pygame.Rect(811, 649, 75, 75)
x_button = pygame.Rect(897, 649, 75, 75)
y_button = pygame.Rect(984, 649, 75, 75)
z_button = pygame.Rect(1072, 649, 75, 75)

#Allows the user to type their name and use the solve text box
active_1 = False
active_2 = False

#Allows the wheel to spin
angle = 0

#variables to keep track of how many times the spin button has been clicked
spinClickCount = 0
letterClickCount = 0
nextClickCount = spinClickCount + 1

#The Wheel
wheelImage = pygame.image.load("WoFwheel.png").convert_alpha()
wheel_rect = wheelImage.get_rect(center= (960,1158))

#Initial Wheel Hider
hiderImage = pygame.image.load("images/Hider.png").convert_alpha()
hider_rect = hiderImage.get_rect(center= (960,1158))

#Wheel pointer
pointerImage = pygame.image.load("images/pointer.png").convert_alpha()
pointer_rect = pointerImage.get_rect(center= (966,775))

#Player info box
money_amount = 0
total_money = 0
game_info_rect = pygame.Rect(50, 960, 200, 100)
money_text = font.render('$', True, white, black)
money_amount_text = font.render(str(total_money), True, white, black)
money_amount_rect = money_amount_text.get_rect()
money_rect = money_text.get_rect()
money_rect.center = (60, 980)
money_amount_rect.center = (80, 980)

#User message box
message = 'Spin the wheel!'
message_box = font.render(message, True, black, blue)
message_rect = message_box.get_rect()
message_rect.center = (500, 800)

#Vowel message box
vowel_message = 'Vowels cost $250'
vowel_message_box = font.render(vowel_message, True, black, blue)
vowel_message_rect = vowel_message_box.get_rect()
vowel_message_rect.center = (1477, 570)

#Displaying the round number
round_num = 1
round_text = font.render(str(round_num), True, white, black)
round_rect = round_text.get_rect()
round_rect.center = (170, 1009)
round_word = font.render('Round:', True, white, black)
round_word_rect = round_word.get_rect()
round_word_rect.center = (100, 1010)

# rotate function for wheel rotation (REWRITTEN)
def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center = (960, 1158))
    return rotated_surface, rotated_rect

# button function
def button(art, x, y, w, h, action=None):
    # Checks for mouse click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Loads images into variable
    buttonImage = pygame.image.load(f"images/{art}.png").convert_alpha()
    # Create the clicking boundaries for image button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # pygame.draw.rect(gameDisplay, (x, y, w, h))
        gameDisplay.blit(buttonImage, (x, y))
           
    else:
        # pygame.draw.rect(gameDisplay, (x, y, w, h))
        gameDisplay.blit(buttonImage, (x, y))


#   Gameboard function for square drawing and data
def gamesquare(x, y, w, h):
    green = (80, 200, 120)
    pygame.draw.rect(gameDisplay, green, (x, y, w, h))

# function for determining award based on wheel spin
def determineScore(angle, money_amount):
    if((angle == 7 or angle < 7) and (angle == 0 or angle > 0)):
        money_amount += 5000
    elif(angle == 353 or angle > 353):
        money_amount += 5000
    elif((angle == 8 or angle > 8) and (angle == 21 or angle < 21)):
        money_amount += 600
    elif((angle == 22 or angle > 22) and (angle == 36 or angle < 36)):
        money_amount += 500
    elif((angle == 37 or angle > 37) and (angle == 51 or angle < 51)):
        money_amount += 300
    elif((angle == 52 or angle > 52) and (angle == 66 or angle < 66)):
        money_amount += 500
    elif((angle == 67 or angle > 67) and (angle == 81 or angle < 81)):
        money_amount += 800
    elif((angle == 82 or angle > 82) and (angle == 96 or angle < 96)):
        money_amount += 550
    elif((angle == 97 or angle > 97) and (angle == 111 or angle < 111)):
        money_amount += 400
    elif((angle == 112 or angle > 112) and (angle == 127 or angle < 127)):
        money_amount += 300
    elif((angle == 128 or angle > 128) and (angle == 141 or angle < 141)):
        money_amount += 900
    elif((angle == 142 or angle > 142) and (angle == 157 or angle < 157)):
        money_amount += 500
    elif((angle == 158 or angle > 158) and (angle == 172 or angle < 172)):
        money_amount += 300
    elif((angle == 173 or angle > 173) and (angle == 187 or angle < 187)):
        money_amount += 900
    elif((angle == 188 or angle > 188) and (angle == 202 or angle < 202)):
        money_amount = 0
        print("Bankrupt!")
    elif((angle == 203 or angle > 203) and (angle == 217 or angle < 217)):
        money_amount += 600
    elif((angle == 218 or angle > 218) and (angle == 232 or angle < 232)):
        money_amount += 400
    elif((angle == 233 or angle > 233) and (angle == 247 or angle < 247)):
        money_amount += 300
    elif((angle == 248 or angle > 248) and (angle == 262 or angle < 262)):
        print("Lost a turn! [UNIMPLEMENTED]")
    elif((angle == 263 or angle > 263) and (angle == 277 or angle < 277)):
        money_amount += 800
    elif((angle == 278 or angle > 278) and (angle == 292 or angle < 292)):
        money_amount += 350
    elif((angle == 293 or angle > 293) and (angle == 307 or angle < 307)):
        money_amount += 450
    elif((angle == 308 or angle > 308) and (angle == 322 or angle < 322)):
        money_amount += 700
    elif((angle == 323 or angle > 323) and (angle == 337 or angle < 337)):
        money_amount += 300
    elif((angle == 338 or angle > 338) and (angle == 352 or angle < 352)):
        money_amount += 600
    
    return money_amount
        
        
    

running = True

while running:

    #   Background color
    blue = (0, 0, 255)
    gameDisplay.fill(blue)
    # First row of keyboard
    button("Bbutton", 245, 565, 75, 75, pygame.QUIT)
    button("Cbutton", 333, 565, 75, 75, pygame.QUIT)
    button("Dbutton", 422, 565, 75, 75, pygame.QUIT)
    button("Fbutton", 510, 565, 75, 75, pygame.QUIT)
    button("Gbutton", 598, 565, 75, 75, pygame.QUIT)
    button("Hbutton", 684, 565, 75, 75, pygame.QUIT)
    button("Jbutton", 771, 565, 75, 75, pygame.QUIT)
    button("Kbutton", 858, 565, 75, 75, pygame.QUIT)
    button("Lbutton", 946, 565, 75, 75, pygame.QUIT)
    button("Mbutton", 1034, 565, 75, 75, pygame.QUIT)
    # Second row of keyboard
    button("Nbutton", 209, 649, 75, 75, pygame.QUIT)
    button("Pbutton", 295, 649, 75, 75, pygame.QUIT)
    button("Qbutton", 381, 649, 75, 75, pygame.QUIT)
    button("Rbutton", 467, 649, 75, 75, pygame.QUIT)
    button("Sbutton", 553, 649, 75, 75, pygame.QUIT)
    button("Tbutton", 639, 649, 75, 75, pygame.QUIT)
    button("Vbutton", 725, 649, 75, 75, pygame.QUIT)
    button("Wbutton", 811, 649, 75, 75, pygame.QUIT)
    button("Xbutton", 897, 649, 75, 75, pygame.QUIT)
    button("Ybutton", 984, 649, 75, 75, pygame.QUIT)
    button("Zbutton", 1072, 649, 75, 75, pygame.QUIT)
    # Vowel row
    button("Abutton", 1289, 608, 75, 75, pygame.QUIT)
    button("Ebutton", 1383, 608, 75, 75, pygame.QUIT)
    button("Ibutton", 1477, 608, 75, 75, pygame.QUIT)
    button("Obutton", 1572, 608, 75, 75, pygame.QUIT)
    button("Ubutton", 1667, 608, 75, 75, pygame.QUIT)
    # Vowel Spin and Solve buttons
    button("Solve", 1695, 930, 139, 75, pygame.QUIT)
    button("Spin", 1377, 853, 108, 108, pygame.QUIT)
    # First row of gameboard
    gamesquare(264, 26, 100, 114)
    gamesquare(383, 26, 100, 114)
    gamesquare(502, 26, 100, 114)
    gamesquare(621, 26, 100, 114)
    gamesquare(740, 26, 100, 114)
    gamesquare(859, 26, 100, 114)
    gamesquare(978, 26, 100, 114)
    gamesquare(1097, 26, 100, 114)
    gamesquare(1216, 26, 100, 114)
    gamesquare(1335, 26, 100, 114)
    gamesquare(1454, 26, 100, 114)
    gamesquare(1573, 26, 100, 114)
    # Second row of gameboard
    gamesquare(145, 152, 100, 114)
    gamesquare(264, 152, 100, 114)
    gamesquare(383, 152, 100, 114)
    gamesquare(502, 152, 100, 114)
    gamesquare(621, 152, 100, 114)
    gamesquare(740, 152, 100, 114)
    gamesquare(859, 152, 100, 114)
    gamesquare(978, 152, 100, 114)
    gamesquare(1097, 152, 100, 114)
    gamesquare(1216, 152, 100, 114)
    gamesquare(1335, 152, 100, 114)
    gamesquare(1454, 152, 100, 114)
    gamesquare(1573, 152, 100, 114)
    gamesquare(1692, 152, 100, 114)
    # Third row of gameboard
    gamesquare(145, 278, 100, 114)
    gamesquare(264, 278, 100, 114)
    gamesquare(383, 278, 100, 114)
    gamesquare(502, 278, 100, 114)
    gamesquare(621, 278, 100, 114)
    gamesquare(740, 278, 100, 114)
    gamesquare(859, 278, 100, 114)
    gamesquare(978, 278, 100, 114)
    gamesquare(1097, 278, 100, 114)
    gamesquare(1216, 278, 100, 114)
    gamesquare(1335, 278, 100, 114)
    gamesquare(1454, 278, 100, 114)
    gamesquare(1573, 278, 100, 114)
    gamesquare(1692, 278, 100, 114)
    # fourth row of gameboard
    gamesquare(264, 404, 100, 114)
    gamesquare(383, 404, 100, 114)
    gamesquare(502, 404, 100, 114)
    gamesquare(621, 404, 100, 114)
    gamesquare(740, 404, 100, 114)
    gamesquare(859, 404, 100, 114)
    gamesquare(978, 404, 100, 114)
    gamesquare(1097, 404, 100, 114)
    gamesquare(1216, 404, 100, 114)
    gamesquare(1335, 404, 100, 114)
    gamesquare(1454, 404, 100, 114)
    gamesquare(1573, 404, 100, 114)
    #player name rectangles
    pygame.draw.rect(gameDisplay, red, player1_info_rect)
    pygame.draw.rect(gameDisplay, white, player1_name, 2)
    #solve box rectangles
    pygame.draw.rect(gameDisplay, red, solve_text_rect)
    pygame.draw.rect(gameDisplay, white, solve_text, 2)

    #Game info rect
    pygame.draw.rect(gameDisplay, black, game_info_rect)
    gameDisplay.blit(money_text, money_rect)
    gameDisplay.blit(money_amount_text, money_amount_rect)
    gameDisplay.blit(round_text, round_rect)
    gameDisplay.blit(round_word, round_word_rect)

    #Displaying the letters to the board
    gameDisplay.blit(board_square_text1, board_square_rect1)
    gameDisplay.blit(board_square_text2, board_square_rect2)
    gameDisplay.blit(board_square_text3, board_square_rect3)
    gameDisplay.blit(board_square_text4, board_square_rect4)
    gameDisplay.blit(board_square_text5, board_square_rect5)
    if len(phrase_pick) == 9:
        gameDisplay.blit(board_square_text6, board_square_rect6)
        gameDisplay.blit(board_square_text7, board_square_rect7)
        gameDisplay.blit(board_square_text8, board_square_rect8)
        gameDisplay.blit(board_square_text9, board_square_rect9)

    #Displaying the message boxes
    gameDisplay.blit(message_box, message_rect)
    gameDisplay.blit(vowel_message_box, vowel_message_rect)

    #This is where the user is able to enter the name of the players
    text_surface1 = base_font.render(user_text1,True,(white))
    gameDisplay.blit(text_surface1, (player1_name.x + 5, player1_name.y + 5))
    player1_name.w = max(100,text_surface1.get_width() + 10)

    #This is where the user is able to guess the word and use the Solve button
    text_surface2 = base_font.render(solve_text1,True,(white))
    gameDisplay.blit(text_surface2, (solve_text.x + 5, solve_text.y + 5))
    solve_text.w = max(100,text_surface2.get_width() + 10)

    gameDisplay.blit(wheelImage, (wheel_rect.x +5, wheel_rect.y+5))
    gameDisplay.blit(pointerImage, (pointer_rect.x, pointer_rect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #button events for player name box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player1_name.collidepoint(event.pos):
                active_1 = True
            else:
                active_1 = False
        if event.type == pygame.KEYDOWN:
            if active_1 == True:
                if event.key == K_BACKSPACE:
                    user_text1 = user_text1[:-1]
                else:
                    user_text1 += event.unicode

        #button events for solve text box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if solve_text.collidepoint(event.pos):
                active_2 = True
            else:
                active_2 = False
        if event.type == pygame.KEYDOWN:
            if active_2 == True:
                if event.key == K_BACKSPACE:
                    solve_text1 = solve_text1[:-1]
                else:
                    solve_text1 += event.unicode
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spin_button.collidepoint(event.pos):
                if(spinClickCount == letterClickCount or spinClickCount < letterClickCount):
                    #keep track of how many times "Spin" has been clicked
                    spinClickCount = spinClickCount + 1
                    #generate random numbers of ticks the wheel will spin
                    tickCount = random.randint(400,600)
                    #counter
                    i = 0
                    #increment counter by 1 and adjust wheel by 1 degree once per tick
                    while(i < tickCount):
                        i = i + 1
                        angle += 1
                        wheel_rotated, wheel_rotated_rect = rotate(wheelImage, angle)
                        gameDisplay.blit(wheel_rotated, wheel_rotated_rect)
                        pygame.display.flip()
                        if (angle == 360):
                            angle = 0
                    #determine score
                    money_amount = determineScore(angle, money_amount)
                else:
                    message = 'Pick a letter'
                    message_box = font.render(message, True, black, blue)
                
            elif solve_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = solve_text1[counter]
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            #ENABLE FOR DEV STUFF
                            # print(choice)
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                            if counter < len(phrase_pick):
                                choice = solve_text1[counter]
                                
                            
                        else:
                            counter = len(phrase_pick)
                            message = 'Incorrect guess.'
                            message_box = font.render(message, True, black, blue)

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                    

            elif a_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    money_amount -= 250
                    choice = 'A'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)
                    
            elif b_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'B'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif c_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'C'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif d_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'D'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif e_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    money_amount -= 250
                    choice = 'E'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif f_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'F'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif g_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'G'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif h_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'H'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif i_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    money_amount -= 250
                    choice = 'I'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif j_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'J'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif k_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'K'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif l_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'L'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif m_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'M'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif n_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'N'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif o_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    money_amount -= 250
                    choice = 'O'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif p_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'P'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif q_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'Q'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif r_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'R'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif s_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'S'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif t_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'T'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif u_button.collidepoint(event.pos):
                if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    money_amount -= 250
                    choice = 'U'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif v_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'V'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif w_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'W'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif x_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'X'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif y_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'Y'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

            elif z_button.collidepoint(event.pos):
                 if(spinClickCount > letterClickCount):
                    counter = 0
                    letter_count = 0
                    choice = 'Z'
                    while counter < len(phrase_pick):
                        if phrase_pick[counter].upper() == choice:
                            phrase_copy[counter] = choice
                            counter += 1
                            letter_count += 1
                            board_square_text1 = board_font.render(phrase_copy[0], True, black, green)
                            board_square_text2 = board_font.render(phrase_copy[1], True, black, green)
                            board_square_text3 = board_font.render(phrase_copy[2], True, black, green)
                            board_square_text4 = board_font.render(phrase_copy[3], True, black, green)
                            board_square_text5 = board_font.render(phrase_copy[4], True, black, green)
                            if len(phrase_pick) == 9:
                                board_square_text6 = board_font.render(phrase_copy[5], True, black, green)
                                board_square_text7 = board_font.render(phrase_copy[6], True, black, green)
                                board_square_text8 = board_font.render(phrase_copy[7], True, black, green)
                                board_square_text9 = board_font.render(phrase_copy[8], True, black, green)
                        else:
                            counter += 1

                    total_money = total_money + (money_amount * letter_count)
                    money_amount_text = font.render(str(total_money), True, white, black)
                    letterClickCount = letterClickCount + 1
                    letter_count = 0
                    round_num += 1
                    round_text = font.render(str(round_num), True, white, black)
                 else:
                    message = 'Please spin again.'
                    message_box = font.render(message, True, black, blue)

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # hide initial blit of wheel after the first click on the "Spin" button          
    if (spinClickCount > 0):
        gameDisplay.blit(hiderImage, (hider_rect.x +5, hider_rect.y+5))
        gameDisplay.blit(pointerImage, (pointer_rect.x, pointer_rect.y))

    # blit final wheel position after spin
    if (spinClickCount == nextClickCount or spinClickCount > nextClickCount):
        gameDisplay.blit(wheel_rotated, (wheel_rotated_rect.x +5, wheel_rotated_rect.y+5))
        
    pygame.display.update()
    pygame.display.flip()
    mainClock.tick(60)
pygame.quit()
