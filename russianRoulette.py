from superPrint import Sprint
from TextSection import get_text 
from time import sleep
from os import system
from random import randint
from colorama import Fore
from sys import stdout

PLAYER_NAME = ''
MAX_SHOT = 7
PLAYER_HP , ENEMY_HP = 3, 3
REAL_SHOT, FAKE_SHOT = 0, 0 
SHOTS = []

def intro () :
    Sprint(get_text("intro_p1"))
    Sprint('matne harif range ')
    Sprint('GHERMEZ ', 'red')
    Sprint('va matne computer ')
    Sprint('ABI \n', 'cyan')
    system("pause")
    system("cls")
    Sprint(get_text("intro_p1.5"), 'cyan')
    Sprint("ie aslahe darim va tosh chand ta goloole ", 'cyan')
    Sprint(get_text("intro_p2"), 'cyan')
    Sprint('gozashtam va be nobat aslahe ro barmidarim va \nroie saremon mizarim ', 'cyan')
    Sprint('shelik mikonim har kodomemon ie tedadi jon dare.\n', 'cyan')
    Sprint("agar goloole asli bod az jonet iedone kam mishe va nobat harif mishe.\n", 'cyan')
    Sprint("agar ham mashghi bod ", 'cyan')
    Sprint(get_text("intro_p3"), 'cyan')
    Sprint("va nobat harif mishe.\n", 'cyan')
    Sprint(get_text('continue'), 'cyan')
    system("pause")
    system("cls")
    
def get_value ():
    
    Sprint(get_text('get_value_p1'), 'cyan')
    PLAYER_NAME = input()
    
    if PLAYER_NAME.isdigit():
        Sprint("esmet ie adade!!!\nkhob bashe.\n", 'cyan')
        system('pause')
        return PLAYER_NAME
    
    PLAYER_NAME = PLAYER_NAME.upper()  + ' '
    
    if PLAYER_NAME == 'MORTEZA ':
        Sprint("oh oh oh khodaie ma omad shoma befarma dakhel.\n", 'LIGHTYELLOW')
        system('pause')
        return PLAYER_NAME
    
    Sprint(get_text('get_value_p2'), 'cyan')
    system('pause')
    return PLAYER_NAME
    
def make_shots():
    global SHOTS, FAKE_SHOT, REAL_SHOT
    for _ in range(MAX_SHOT):
        shot = randint(0,1)
        if shot == 1:
            SHOTS.append(True)
            REAL_SHOT += 1 
            continue
        SHOTS.append(False)
        FAKE_SHOT += 1

def print_shots() :
    global SHOTS
    system('cls')
    Sprint(get_text('print_shots_p1'), 'cyan')
    Sprint('range goloole vaghei: ', 'cyan')
    Sprint('0 \t', 'red')
    Sprint('range goloole mashghi: ', 'cyan')
    Sprint('0 \n', 'blue')
    Sprint(get_text('continue'), 'cyan')
    system('pause')
    wahit()
    for _ in range(3):
        all_shot = MAX_SHOT - 1
        in_gun = SHOTS[:]
        for _ in range(len(in_gun)):
            index = randint(0, all_shot)
            shot = in_gun[index]
            
            if shot == True:
                print(Fore.RED, '0', end='')
                in_gun.remove(in_gun[index])
                all_shot -= 1
                continue
            
            print(Fore.BLUE, '0', end='')
            in_gun.remove(in_gun[index])
            all_shot -= 1
        stdout.flush()
        sleep(0.15)
        system('cls')
    print()
    
def true_value(player_choice):
    while True:
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if player_choice == 1 or player_choice == 2:
                return player_choice
        Sprint(get_text('true_value_p1'), 'cyan')
        Sprint('dobare vared kon : \n', 'cyan')
        Sprint('1) harif\n', 'cyan')
        Sprint('2) khodet\n', 'cyan')
        player_choice = input()
    
def end_game(winner):
    system('cls')
    if winner == 'player':
        Sprint(PLAYER_NAME, 'LIGHTYELLOW')
        Sprint('bord !!!\n', 'cyan')
        Sprint(get_text('player_winner_p1'), 'red')
        Sprint(get_text('player_winner_p2'), 'cyan')
        print()
        system('pause')
    elif winner == 'enemy':
        Sprint(PLAYER_NAME, 'LIGHTYELLOW')
        Sprint('bakhti !!!\n', 'cyan')
        Sprint(get_text('enemy_winner_p1'), 'red')
        Sprint(get_text('enemy_winner_p2'), 'cyan')
        print()
        system('pause')
    exit()
    
def live():
    if ENEMY_HP == 0:
        end_game('player')
    elif PLAYER_HP == 0:
        end_game('enemy')
    else:
        pass
   
def reload():
    make_shots()
    print_shots()
    
def shot(target, _from):
    global SHOTS, FAKE_SHOT, REAL_SHOT, PLAYER_HP, ENEMY_HP
    shot = SHOTS.pop()
    if shot == True:
        if target == 'enemy':
            Sprint('shelik be samte enemy: \n', 'cyan')
            system('pause')
            wahit()
            ENEMY_HP -= 1
            REAL_SHOT -= 1
            Sprint('goloole asli bod.\n', 'cyan')
            Sprint(f'{PLAYER_NAME} HP: {PLAYER_HP}\n', 'cyan')
            Sprint(f'ENEMY HP: {ENEMY_HP}\n', 'cyan')
            if _from == 'player':
                Sprint(PLAYER_NAME, 'lightyellow')
                Sprint(get_text('after_pTOe_T'), 'red')
            else:
                Sprint(get_text('after_eTOe_T'), 'red') 
            system('pause')
            live()
        else:
            Sprint('shelik be samte ', 'cyan')
            Sprint(PLAYER_NAME, 'LIGHTYELLOW')
            Sprint(': \n', 'cyan')
            system('pause')
            wahit()
            PLAYER_HP -= 1
            REAL_SHOT -= 1 
            Sprint('goloole asli bod.\n', 'cyan')
            Sprint(f'{PLAYER_NAME} HP: {PLAYER_HP}\n', 'cyan')
            Sprint(f'ENEMY HP: {ENEMY_HP}\n', 'cyan')
            if _from == 'player':
                Sprint(get_text('after_pTOp_T'), 'red') 
            else:
                Sprint(get_text('after_eTOp_T'), 'red')
            system('pause')
            live()
    else:
        if target == 'enemy':
            Sprint('shelik be samte enemy: \n', 'cyan')
            system('pause')
            wahit()
            FAKE_SHOT -= 1
            Sprint('goloole masghi bod.\n', 'cyan')
            Sprint(f'{PLAYER_NAME} HP: {PLAYER_HP}\n', 'cyan')
            Sprint(f'ENEMY HP: {ENEMY_HP}\n', 'cyan')
            if _from == 'player':
                Sprint(get_text('after_pTOe_F'), 'red') 
            else:
                Sprint(get_text('after_eTOe_F'), 'red')               
            system('pause')
        else:
            Sprint('shelik be samte ', 'cyan')
            Sprint(PLAYER_NAME, 'LIGHTYELLOW')
            Sprint(': \n', 'cyan')
            system('pause')
            wahit()
            FAKE_SHOT -= 1
            Sprint('goloole masghi bod.\n', 'cyan')
            Sprint(f'{PLAYER_NAME} HP: {PLAYER_HP}\n', 'cyan')
            Sprint(f'ENEMY HP: {ENEMY_HP}\n', 'cyan')
            if _from == 'player':
                Sprint(get_text('after_pTOp_F'), 'red') 
            else:
                Sprint(get_text('after_eTOp_F'), 'red')
            system('pause')
    if REAL_SHOT <= 0 and FAKE_SHOT <= 0:
        reload()
    system('cls')
    
def player_gun():
    
    Sprint(get_text('player_gun_p1'), 'red')
    Sprint('ki ro mikhai bezani: \n', 'cyan')
    Sprint('1) harif\n', 'cyan')
    Sprint('2) khodet\n', 'cyan')
    
    player_choice = input()
    player_choice = true_value(player_choice)
    
    if player_choice == 1:
        Sprint(get_text('before_pTOe'), 'red')
        return 'enemy' 
    else:
        Sprint(get_text('before_pTOp'), 'red')
        return 'player'    
    
def enemy_gun():
    Sprint(get_text('enemy_gun'), 'red') 
    if REAL_SHOT >= FAKE_SHOT:
        Sprint(get_text('before_eTOp'), 'red')
        return 'player'
    else:
        Sprint(get_text('before_eTOe'), 'red')
        return 'enemy'

def wahit():
    system('cls')
    count = 3
    for _ in range(3):
        Sprint(f'{count}', 'cyan')
        sleep(1)
        count -= 1
        system('cls')
    
def player_tern():
    global SHOTS
    target = player_gun()
    if target == 'enemy':
        shot(target, 'player')
        system('cls')
        enemy_tern()
    else:
        shot(target, 'player')
        system('cls')
        player_tern()
        
def enemy_tern():
    global SHOTS
    target = enemy_gun()
    if target == 'enemy':
        shot(target, 'enemy')
        enemy_tern()
    else:
        shot(target, 'enemy')
        player_tern()
    
def game ():
    make_shots()
    print_shots()
    Sprint('nobat aval ba ' , 'cyan')
    Sprint(PLAYER_NAME , 'LIGHTYELLOW')
    Sprint(':\n', 'cyan')
    player_tern()       

if __name__ == "__main__":
    # intro()
    # PLAYER_NAME = get_value()
    game()