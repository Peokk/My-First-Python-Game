import pygame,sys,math,random


def pokrywaja_sie(box1,box2):

    srodek_1_x = box1.x + box1.width/2
    srodek_2_x = box2.x + box2.width / 2
    srodek_1_y = box1.y + box1.height / 2
    srodek_2_y = box2.y + box2.height / 2

    r_1 = box1.width/2
    r_2 = box2.width/2

    odleglos = math.sqrt((srodek_2_x - srodek_1_x)**2 + (srodek_1_y - srodek_2_y)**2)

    if odleglos > r_1 + r_2:
        return False
    return True

# Karma
def rand_karma():
    x = random.randint(0, 2500)
    y = random.randint(0, 2500)
    r = random.randint(50, 200)
    g = random.randint(50, 200)
    b = random.randint(50, 200)
    return [x, y ,r ,g ,b]

pygame.init()
delta = 0.0
max_tps = 80.0
clock = pygame.time.Clock()
window = pygame.display.set_mode((1500,1000))

obt = []
obt_green = []

x_o = 0
y_o = 0
l1 = 0
l2 = 0
x_p = 700
y_p = 450

score = 50
pasywka = 0
skill = 0
ult = 0
mana = 100

pokrywa_green = 0

stamina_load = 1
full_stamina = 2000
stamina = full_stamina
stamina_box_width = 1000
s_box = pygame.Rect(200,970,stamina_box_width,20)
s_ramka_box = pygame.Rect(200,970,stamina_box_width,20)
pulap = 0
sprint = 3
#---------------------------
zdrowie = 10
max_zdrowie = 100
#-----------------------------------

show_hp = 0
full_hp = 2000
hp = full_hp
hp_box_width = 1000
hp_box = pygame.Rect(200,950,hp_box_width,20)
hp_ramka_box = pygame.Rect(200,950,hp_box_width,20)

skill_delay = [0,0,0,0,0,0,0]
#---------------------------------------------------------------------------------------------------------------------
full_hunter = 2000
hunter = full_hunter
hunter_box_width = 1000
hunter_box = pygame.Rect(200,960,hunter_box_width,10)
hunter_ramka_box = pygame.Rect(200,960,hunter_box_width,10)
hunter_start = 0
#----------------------------------------------------------------------------------------------------------------------
mana_mana = 100

full_mana = 200
mana = full_mana
mana_box_height = 200
mana_box = pygame.Rect(10,10,20,mana_box_height)
mana_ramka_box = pygame.Rect(10,10,20,mana_box_height)
#-----------------------------------------------------------------------------------------------------------------------
#Jedznie
for i in range(0, 100):
     obt.append(rand_karma())

#Krzaki
for j in range(0, 5):
     x = random.randint(0, 2300)
     y = random.randint(0, 2300)
     obt_green.append([x, y])

#-----------------------------------------------------------------------------------------------------------------------
# Pętla
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit(0)
    # Fps
    delta += clock.tick() / 1000.0
    while delta > 1 / max_tps:
        delta -= 1 / max_tps

#-----------------------------------------------------------------------------------------------------------------------
        # Ruchy
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y_o -= sprint
            if hunter_start == 1:
                hunter_box_width -= 2
                sprint = 6

        if keys[pygame.K_s]:
            y_o += sprint
            if hunter_start == 1:
                hunter_box_width -= 2
                sprint = 6

        if keys[pygame.K_a]:
            x_o -= sprint
            if hunter_start == 1:
                hunter_box_width -= 2
                sprint = 6

        if keys[pygame.K_d]:
            x_o += sprint
            if hunter_start == 1:
                hunter_box_width -= 2
                sprint = 6

        # Pasywka 2
        if pasywka == 2:
            if keys[pygame.K_SPACE] and stamina > pulap:
                sprint = 5
                stamina -= 10

            else:
                sprint = 3
                if stamina < full_stamina:
                    stamina += stamina_load


#-----------------------------------------------------------------------------------------
        if zdrowie > max_zdrowie:
            zdrowie = 100

        if skill == 3:
            if keys[pygame.K_f]:
                show_hp = 1
                hp_box_width -= 10
                zdrowie += 1
            if zdrowie > 100 or hp_box_width == 0:
                show_hp = 0
        # Ult 1

        if hunter_box_width <= 0:
            hunter_start = 0
            sprint = 3
            hunter_box_width = 1000
            hunter_iv = 50
            hunter_iv_hp = 3


        if ult == 1:
                if keys[pygame.K_r]:
                    if mana_mana >= 60:
                        mana_mana -= 60
                        mana_box_height -=120
                        hunter_start = 1

#Umiejętności ----------------------------------------------------------------------------------------
        if score == 140:
            print("1.Dash - Po zjedzeniu karmy wykonujesz lekki dash")
            print("2.Sprint - Otrzymujesz pasek staminy")
            print("3.Invisible - Stajesz się niewidzialny stojąc w krzaku")
            Pasywka = input("Wybierz Umiejętność Pasywną:")
            score += 2
            if Pasywka == "1":
                pasywka = 1
            if Pasywka == "2":
                pasywka = 2
            if Pasywka == "3":
                pasywka = 3
        if score == 300:
            print("1.Freeze - Zatrzymujesz każdego wroga w pobliżu ciebie zadając mu obrażenia.")
            print("2.Mine - Ustawiasz niewidoczną dla przeciwników mine gdy w nią wejdą zostaną im zadane obrażenia.")
            print("3.Heal - Aktywujesz pasek który pozwala ci się leczyć aż się skończy.")
            Skill = input("Wybierz Umiejętność")
            score += 2
            if Skill == "1":
                skill = 1
            if Skill == "2":
                skill = 2
            if Skill == "3":
                skill = 3
        if score == 400:
            print("1.Hunter - Stajesz się niewidzialny jednocześnie zyskujesz większą prędkość gdy zbliżysz się do przeciwnika skoczysz na niego zadając mu obrażenia jesteś niewidoczny ąż skończy ci się pasek ulta który się zmniejszą za każdym razem gdy się ruszysz")
            print("2.Shoot - Wykonujesz natychmiastowy strzał w przeciwnika który jest w twoim polu widzenia zadając mu obrażenia.")
            print("3.Repulse - Odpychasz przeciwników którzy są w pobliżu ciebię zadajać im obrażenia.")
            Ult = input("Wybierz Umiejętność Główną")
            score += 2
            if Ult == "1":
                ult = 1
            if Ult == "2":
                ult = 2
            if Ult == "3":
                ult = 3

#Drawin-----------------------------------------------------cc------------------------------------------------------------
        #Pasywka 2
        s_box.width = stamina / full_stamina * stamina_box_width
        hp_box.width = stamina / full_hp * hp_box_width
        hunter_box.width = hunter / full_hunter * hunter_box_width
        mana_box.height = mana / full_mana * mana_box_height

        #Siatka
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 2500, 2500))
        #
        x_k = 0
        y_k = 0
        for y in range(0, 25):
            pygame.draw.rect(window, (220, 220, 220), (int(0 - x_o), int(y_k - y_o), 2500,  2))
            y_k += 100

        for x in range(0, 25):
            pygame.draw.rect(window, (220, 220, 220), (int(x_k - x_o), int(0 - y_o), 2, 2500))
            x_k += 100

        #Jedzenie
        for i in range(0,100):
            pygame.draw.rect(window, (obt[i][2], obt[i][3], obt[i][4]), ((obt[i][0]- x_o), (obt[i][1]- y_o), 20, 20))

        for o in obt:
            if pokrywaja_sie(pygame.Rect((o[0]- x_o), (o[1]- y_o), 20, 20),pygame.Rect(700,450,50,50)):
                obt.remove(o)
                score +=1
                obt.append(rand_karma())
                score += 1
                if mana_box_height < 200:
                    mana_box_height += 2
                if mana_mana < 100:
                    mana_mana += 1

                # pasywka 1
                if pasywka == 1:
                    if keys[pygame.K_w]:
                        for w in range(0,2):
                            y_o -= 5
                    if keys[pygame.K_s]:
                        for s in range(0,2):
                            y_o += 5
                    if keys[pygame.K_a]:
                        for a in range(0,2):
                            x_o -= 5
                    if keys[pygame.K_d]:
                        for d in range(0,2):
                            x_o += 5
                    if keys[pygame.K_w] and keys[pygame.K_d]:
                        for wd in range(0,2):
                            y_o -= 5
                            x_o += 5
                    if keys[pygame.K_w] and keys[pygame.K_a]:
                        for wa in range(0,2):
                            y_o -= 5
                            x_o -= 5
                    if keys[pygame.K_s] and keys[pygame.K_d]:
                        for sd in range(0,2):
                            y_o += 5
                            x_o += 5
                    if keys[pygame.K_s] and keys[pygame.K_a]:
                        for sa in range(0,2):
                            y_o += 5
                            x_o -= 5
        # Pasywka 3
        pokrywa_green = 0
        colour = 50

        for j in range(0,5):
            pygame.draw.rect(window, (50, 200, 50), (obt_green[j][0]- x_o, obt_green[j][1]- y_o, 200, 200))

        if pasywka == 3:
            for obg in obt_green:
                if pokrywaja_sie(pygame.Rect((obg[0] - x_o), (obg[1] - y_o), 200, 200),pygame.Rect(700, 450, 50, 50)):
                    colour = 200
                    pokrywa_green = 1

        # Bariery
        pygame.draw.rect(window, (0, 0, 0), (2500 - x_o, 0 - y_o, 10, 2500))
        pygame.draw.rect(window, (0, 0, 0), (0 - x_o, 2500 - y_o, 2500, 10))
        pygame.draw.rect(window, (0, 0, 0), (0 - x_o, 0 - y_o, 10, 2500))
        pygame.draw.rect(window, (0, 0, 0), (0 - x_o, 0 - y_o, 2500, 10))

        # Player Domyslny
        pygame.draw.rect(window, (50, 50, 50), (700, 450, 50, 50))

        # Hp Domyslne
        zdrowie_len = zdrowie / 2
        pygame.draw.rect(window, (50, 50, 50), (700, 510, 50, 3))
        pygame.draw.rect(window, (50, 200, 50), (700, 510, zdrowie_len, 3))

        #Player
        if hunter_start == 1:
            pygame.draw.rect(window, (255, 255, 255), (699, 510, 52, 3))
            pygame.draw.rect(window, (255, 255, 255), (699, 510, 52, 3))
            pygame.draw.rect(window, (255, 255 , 255), (700, 450, 50, 50))

        #Skill 3
        if show_hp == 1:
            pygame.draw.rect(window, (50, 50, 50), hp_ramka_box)
            pygame.draw.rect(window, (150, 10, 10), hp_box)

        # Paswyka 2
        if pasywka == 2:
            pygame.draw.rect(window, (50, 50, 50), s_ramka_box)
            pygame.draw.rect(window, (0, 100, 0), s_box)

        #Ult 1
        if hunter_start == 1:
            pygame.draw.rect(window, (50, 50, 50), hunter_ramka_box)
            pygame.draw.rect(window, (0, 0, 120), hunter_box)
            for obg in obt_green:
                if pokrywaja_sie(pygame.Rect((obg[0] - x_o), (obg[1] - y_o), 200, 200),
                    pygame.Rect(700, 450, 50, 50)):
                    colour = 200
                    pokrywa_green = 1

        if pokrywa_green == 1:
                pygame.draw.rect(window, (50, colour, 50), (700, 450, 50, 50))
                pygame.draw.rect(window, (50, colour, 50), (699, 510, 52, 3))

        #Mana
        pygame.draw.rect(window, (50, 50, 50), mana_ramka_box)
        pygame.draw.rect(window, (0, 0, 200), mana_box)
        pygame.display.flip()

