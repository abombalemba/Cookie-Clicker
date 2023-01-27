# blocks of code
# 1 - import
# 2 - TODO
# 3 - colors
# 4 - variables
# 5 - shop
# 6 - pygame
# 7 - import data
# 8 - classes
# 9 - defines
# 10 - objects
# 11 - main cycle
# 12 - save data

# import
import pygame
import time
from random import randint
import tkinter

# TODO:
#  [ + ] __main__;
#  [ + ] bugs!;
#  [ ? ] economic;
#  [ + ] (delete object: use sp_left with all objects, update sp_left every {FPS} times, when open object - add it to
#  sp_left, when close object - del it from sp_left);
#  [ + ] info, rewards, achievement, settings (saving, restart, volume, sound);
#  [ - ] fix full / not full screen;
#  [ ? ] echo;
#  [ + ] main window.


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BROWN = (210, 105, 30)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 123, 0)
PINK = (255, 182, 193)
LIME = (51, 255, 0)
LIGHT_BLUE = (48, 213, 200)
LIGHT_BLUE1 = (72, 209, 204)
LIGHT_BLUE2 = (100, 200, 200)
LIGHT_BLUE3 = (140, 210, 255)
LIGHT_BLUE4 = (156, 180, 253)
LIGHT_BLUE5 = (40, 200, 180)
LIGHT_BLUE6 = (25, 180, 160)
LIGHT_BLUE7 = (25, 125, 200)
LIGHT_PINK = (255, 190, 255)
LIGHT_RED = (250, 128, 114)
LIGHT_GREEN = (200, 255, 200)
LIGHT_BLACK = (40, 40, 40)
DARK_BLUE = (0, 0, 100)
DARK_GRAY1 = (90, 90, 90)
DARK_GRAY2 = (73, 66, 61)
SADDLE_BROWN = (139, 69, 19)

COLORS = [BROWN, WHITE, GRAY, BROWN, RED, GREEN, BLUE, YELLOW, ORANGE, PINK, LIME, LIGHT_BLUE, LIGHT_BLUE1, LIGHT_BLUE2,
          LIGHT_BLUE3, LIGHT_BLUE4, LIGHT_BLUE5, LIGHT_BLUE6, LIGHT_BLUE7, LIGHT_PINK, LIGHT_RED, LIGHT_GREEN,
          LIGHT_BLACK, DARK_BLUE, DARK_GRAY1, DARK_GRAY2, SADDLE_BROWN]


# create pygame
pygame.init()
clock = pygame.time.Clock()
root = tkinter.Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
mw = pygame.display.set_mode((X, Y))
surf = pygame.Surface((X, Y))
mw.fill(LIGHT_BLUE)

# open file with data
file = open('progress_v_1.2.txt', 'r')
data2 = file.readline().split(' ')
file.close()

# fix data
data = []
for i in data2:
    if type(i) is str:
        i = int(i)
        data.append(i)
del data2

# variables
display_x, display_y = 0, 0
bonus_coord_x, bonus_coord_y = 0, 0  # coord of bonus
full_screen, running, flag_for_bonus = True, True, True
FPS = 40

# cheats
cheat_cheat, cheat_bonus = 1, 1

# lvl upgrades
count_autoclicker, count_farm, count_fabric, count_mine = 0, 0, 0, 0

# shop
shop_auto_clicker = True

price_of_autoclicker = [10, 20, 35, 50, 75, 100, 150, 200, 300, 460, 720, 880, 1100, 1470, 1600, 2000]
salary_of_autoclicker = [2, 5, 8, 12, 18, 25, 40, 75, 120, 160, 200, 280, 350, 500, 670, 900]

price_of_farm = [50, 100, 175, 250, 400, 600, 1000, 1350, 1600, 1890, 2200, 2700, 3400, 4100, 5000, 5800]
salary_of_farm = [15, 20, 28, 37, 50, 70, 95, 120, 155, 200, 280, 350, 490, 600, 750, 1000]

price_of_fabric = [300, 400, 530, 700, 950, 1300, 1900, 3000, 4500, 7300, 10000, 13000, 16600, 19800, 24000, 30000]
salary_of_fabric = [60, 85, 110, 150, 220, 300, 420, 600, 800, 1050, 1200, 1300, 1450, 1670, 1890, 2100]

price_of_mine = [1000, 1200, 1500, 1960, 2400, 3000, 4100, 6500, 8000, 10000, 13400, 17100, 20000, 25000, 29900, 96000]
salary_of_mine = [230, 310, 480, 630, 800, 1000, 1310, 1600, 1950, 2300, 2810, 3200, 3500, 3970, 4400, 4900]

cps_autoclicker, cps_farm, cps_fabric, cps_mine = 0.1, 1, 10, 100
price_autoclicker, price_farm, price_fabric, price_mine = 10, 100, 1000, 10000
lvl_autoclicker, lvl_farm, lvl_fabric, lvl_mine = data[2], data[3], data[4], data[5]
int_COUNT, t = int(data[0]), data[1]


# rectangle
class Area(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color, self.surf = color, pygame.Surface((X, Y))

    def color(self, new_color):
        self.fill_color = new_color

    def draw(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def disappear(self):
        pygame.draw.rect(mw, LIGHT_BLUE, self.rect)

    def rotate(self):
        car2 = pygame.transform.flip(pygame.Surface((X, Y)), True, False)
        car2 = pygame.transform.flip(pygame.Surface((X, Y)), False, True)

    def __del__(self):
        self.kill()


# circle
class Circle(pygame.sprite.Sprite):
    def __init__(self, color, center, radius):
        pygame.sprite.Sprite.__init__(self)
        self.surf, self.center, self.radius, self.fill_color = (500, 500), center, radius, color
        self.circle, self.surf = pygame.draw.circle(mw, color, center, radius), pygame.Surface((X, Y))

    def color(self, new_color):
        self.fill_color = new_color

    def draw(self):
        pygame.draw.circle(mw, self.fill_color, self.center, self.radius)

    def fill(self):
        pygame.draw.circle(mw, self.fill_color, self.center, self.radius)

    def collidepoint(self, x, y):
        return self.circle.collidepoint(x, y)

    def __del__(self):
        return self.kill()


class Label(Area):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = None

    def set_text(self, text, font_size=15, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('microsoft yahei', font_size).render(text, True, text_color)
        # verdana, tahoma, microsoft yahei, georgia

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def move(self, x, y):
        pass

    def __del__(self):
        return self.kill()


# count
def def_count():
    global int_COUNT, cookie, wall7, image
    int_COUNT += 1
    # str_count = fix_number(int_COUNT)
    counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
    counter_clicks.draw(20, 10)


# auto clicker
def auto_clicker():
    global int_COUNT, str_COUNT, counter_clicks
    # str_COUNT = fix_number(int_COUNT)
    int_COUNT += cps_autoclicker * lvl_autoclicker + cps_farm * lvl_farm + cps_fabric * lvl_fabric + cps_mine * lvl_mine
    counter_clicks.set_text('Денег: ' + str(int(int_COUNT)), 40, BLACK)
    counter_clicks.draw(20, 10)


# fix number
def fix_number(int_count):
    if int_count >= 1000000000000:
        str_count = str(int(int_count // 1000000000000)) + ' T'
    elif int_count >= 1000000000:
        str_count = str(int(int_count // 1000000000)) + ' B'
    elif int_count >= 1000000:
        str_count = str(int(int_count // 1000000)) + ' M'  # '.' + str(int_count // 10000 % 100) + ' M'
    # elif int_count >= 1000:
    #    str_count = str(int(int_count // 1000)) + ' K'
    else:
        str_count = str(int_count)
    return str_count


# str_COUNT = fix_number(int_COUNT)


def echo():
    global image
    # big cookie
    # image = pygame.image.load('cookie.png')
    image = pygame.transform.scale(image, (int(X * 0.22), int(X * 0.22)))
    mw.blit(image, (X * 0.14, Y * 0.305))
    time.sleep(0.05)
    # small cookie
    # image = pygame.image.load('cookie.png')
    image = pygame.transform.scale(image, (int(X * 0.2), int(X * 0.2)))
    mw.blit(image, (X * 0.15, Y * 0.325))


# difference per second
def difference_per_sec(old, new):
    global int_COUNT
    if new - old > 0:
        print('>')
    elif new == old:
        print('==')
    elif new - old < 0:
        print('<')


# warning
def def_error():
    error = Area(70, 70, 60, 60, LIGHT_BLUE)
    error1 = Circle(WHITE, (100, 100), 30)
    error2 = Circle(RED, (100, 100), 28)
    error3 = Area(95, 80, 10, 20, WHITE)
    error4 = Area(95, 108, 10, 10, WHITE)
    sp_of_errors = [error1, error2, error3, error4]
    for ii in sp_of_errors:
        ii.draw()
    error.draw()
    for ii in sp_of_errors:
        ii.draw()


# upgrades
def def_upgrades_autoclicker():
    global X, Y, lvl_autoclicker, count_autoclicker, price_of_autoclicker, salary_of_autoclicker, upgrades_autoclicker,\
        upgrades_autoclicker1, upgrades_autoclicker2, upgrades_autoclicker3, upgrades_autoclicker4
    if lvl_autoclicker < 15:
        lvl_autoclicker += 1

    upgrades_autoclicker = Label(X * 0.53, Y * 0.1, X * 0.45, Y * 0.15, GRAY)
    upgrades_autoclicker.set_text('', 30, BLACK)
    upgrades_autoclicker1 = Label(X * 0.615, Y * 0.11, X * 0.355, Y * 0.06, WHITE)
    upgrades_autoclicker1.set_text('автокликер' + f' [ {lvl_autoclicker} ]', 26, BLACK)
    upgrades_autoclicker2 = Label(X * 0.615, Y * 0.18, X * 0.175, Y * 0.06, WHITE)
    upgrades_autoclicker2.set_text('Доход:' + f' {sum([salary_of_autoclicker[x] for x in range(lvl_autoclicker)])}'
                                              f' cl/sec', 26, BLACK)
    upgrades_autoclicker3 = Label(X * 0.795, Y * 0.18, X * 0.175, Y * 0.06, WHITE)
    upgrades_autoclicker3.set_text('Улучшение:' + f' {price_of_autoclicker[lvl_autoclicker]} cl', 26, BLACK)
    upgrades_autoclicker4 = Area(X * 0.535, Y * 0.11, Y * 0.13, Y * 0.13, WHITE)

    if lvl_autoclicker >= 15:
        upgrades_autoclicker1.color(LIME)

    upgrades_autoclicker.draw()
    upgrades_autoclicker1.draw(210, 18)
    upgrades_autoclicker2.draw(60, 18)
    upgrades_autoclicker3.draw(60, 18)
    upgrades_autoclicker4.draw()


def def_upgrades_farm():
    global X, Y, lvl_farm, count_farm, price_of_farm, salary_of_farm, upgrades_farm, upgrades_farm1, upgrades_farm2, \
        upgrades_farm3, upgrades_farm4
    if lvl_farm < 15:
        lvl_farm += 1

    upgrades_farm = Label(X * 0.53, Y * 0.27, X * 0.45, Y * 0.15, GRAY)
    upgrades_farm.set_text('', 30, BLACK)
    upgrades_farm1 = Label(X * 0.615, Y * 0.28, X * 0.355, Y * 0.06, WHITE)
    upgrades_farm1.set_text('ферма' + f' [ {lvl_farm} ]', 26, BLACK)
    upgrades_farm2 = Label(X * 0.615, Y * 0.35, X * 0.175, Y * 0.06, WHITE)
    upgrades_farm2.set_text('Доход:' + f' {sum([salary_of_farm[x] for x in range(lvl_farm)])} cl', 26, BLACK)
    upgrades_farm3 = Label(X * 0.795, Y * 0.35, X * 0.175, Y * 0.06, WHITE)
    upgrades_farm3.set_text('Улучшение:' + f' {price_of_farm[lvl_farm]} cl', 26, BLACK)
    upgrades_farm4 = Area(X * 0.535, Y * 0.28, Y * 0.13, Y * 0.13, WHITE)

    if lvl_farm >= 15:
        upgrades_farm1.color(LIME)

    upgrades_farm.draw()
    upgrades_farm1.draw(225, 18)
    upgrades_farm2.draw(60, 18)
    upgrades_farm3.draw(60, 18)
    upgrades_farm4.draw()


def def_upgrades_fabric():
    global X, Y, lvl_fabric, count_fabric, price_of_fabric, salary_of_fabric, upgrades_fabric, upgrades_fabric1, \
        upgrades_fabric2, upgrades_fabric3, upgrades_fabric4
    if lvl_fabric < 15:
        lvl_fabric += 1

    upgrades_fabric = Label(X * 0.53, Y * 0.44, X * 0.45, Y * 0.15, GRAY)
    upgrades_fabric.set_text('', 30, BLACK)
    upgrades_fabric1 = Label(X * 0.615, Y * 0.45, X * 0.355, Y * 0.06, WHITE)
    upgrades_fabric1.set_text('завод' + f' [ {lvl_fabric} ]', 26, BLACK)
    upgrades_fabric2 = Label(X * 0.615, Y * 0.52, X * 0.175, Y * 0.06, WHITE)
    upgrades_fabric2.set_text('Доход:' + f' {sum([salary_of_fabric[x] for x in range(lvl_fabric)])} cl',
                              26, BLACK)
    upgrades_fabric3 = Label(X * 0.795, Y * 0.52, X * 0.175, Y * 0.06, WHITE)
    upgrades_fabric3.set_text('Улучшение:' + f' {price_of_fabric[lvl_fabric]} cl', 26, BLACK)
    upgrades_fabric4 = Area(X * 0.535, Y * 0.45, Y * 0.13, Y * 0.13, WHITE)

    if lvl_fabric >= 15:
        upgrades_fabric1.color(LIME)

    upgrades_fabric.draw()
    upgrades_fabric1.draw(228, 18)
    upgrades_fabric2.draw(60, 18)
    upgrades_fabric3.draw(60, 18)
    upgrades_fabric4.draw()


def def_upgrades_mine():
    global X, Y, lvl_mine, count_mine, price_of_mine, salary_of_mine, upgrades_mine, upgrades_mine1, upgrades_mine2, \
        upgrades_mine3, upgrades_mine4
    if lvl_mine < 15:
        lvl_mine += 1

    upgrades_mine = Label(X * 0.53, Y * 0.61, X * 0.45, Y * 0.15, GRAY)
    upgrades_mine.set_text('', 30, BLACK)
    upgrades_mine1 = Label(X * 0.615, Y * 0.62, X * 0.355, Y * 0.06, WHITE)
    upgrades_mine1.set_text('шахта' + f' [ {lvl_mine} ]', 26, BLACK)
    upgrades_mine2 = Label(X * 0.615, Y * 0.69, X * 0.175, Y * 0.06, WHITE)
    upgrades_mine2.set_text('Доход:' + f' {sum([salary_of_mine[x] for x in range(lvl_mine)])} cl', 26, BLACK)
    upgrades_mine3 = Label(X * 0.795, Y * 0.69, X * 0.175, Y * 0.06, WHITE)
    upgrades_mine3.set_text('Улучшение:' + f' {price_of_mine[lvl_mine]} cl', 26, BLACK)
    upgrades_mine4 = Area(X * 0.535, Y * 0.62, Y * 0.13, Y * 0.13, WHITE)

    if lvl_mine >= 15:
        upgrades_mine1.color(LIME)

    upgrades_mine.draw()
    upgrades_mine1.draw(225, 18)
    upgrades_mine2.draw(60, 18)
    upgrades_mine3.draw(60, 18)
    upgrades_mine4.draw()


# frames
def def_frame(*objects):
    global frame, frame1, frame2, draw_obj
    '''obj1, obj2, obj3 = objects[0], objects[1], objects[2]
    if obj1 in draw_obj and obj2 in draw_obj and obj3 in draw_obj:
        del frame, frame1, frame2
    else:
        draw_obj.append(frame)
        draw_obj.append(frame1)
        draw_obj.append(frame2)
        draw_obj.append(obj1)
        draw_obj.append(obj2)
        draw_obj.append(obj3)'''
    if frame in draw_obj and frame1 in draw_obj and frame2 in draw_obj:
        frame.kill(), frame1.kill(), frame2.kill()
        print('удолил')
        frame = Area(X * 0.51, Y * 0.8, X * 0.49, Y * 0.2, DARK_GRAY1)
        frame1 = Area(X * 0.51, Y * 0.8, X * 0.49, Y * 0.03, GRAY)
        frame2 = Area(X * 0.95, Y * 0.8, X * 0.05, Y * 0.03, RED)
        print('воссоздал')
        # draw_obj.remove(frame), draw_obj.remove(frame1), draw_obj.remove(frame2)
    else:
        print('отрисовка + забивка')
        frame.draw(), frame1.draw(), frame2.draw()
        draw_obj.append(frame), draw_obj.append(frame1), draw_obj.append(frame2)


def def_frame_info():
    frame_info = Label(X * 0.51, Y * 0.8, X * 0.49, Y * 0.1, DARK_GRAY1)

    def_frame()


def def_frame_rewards():
    def_frame()


def def_frame_achievement():
    def_frame()


def def_frame_settings():
    def_frame()


frame = Area(X * 0.509, Y * 0.801, X * 0.49, Y * 0.2, DARK_GRAY1)
frame1 = Area(X * 0.509, Y * 0.801, X * 0.49, Y * 0.03, GRAY)
frame2 = Area(X * 0.95, Y * 0.8, X * 0.05, Y * 0.03, RED)

# background
wall1 = Area(X * 0.5, 0, X * 0.5, Y, LIGHT_BLUE4)
wall2 = Area(X * 0.49, 0, X * 0.02, Y, LIGHT_BLACK)
wall3 = Area(X * 0.145, Y * 0.195, X * 0.21, Y * 0.06, LIGHT_BLUE7)
wall4 = Area(0, 0, X * 0.49, Y * 0.05, LIGHT_BLUE6)
wall5 = Area(0, Y * 0.05, X * 0.49, Y * 0.125, LIGHT_BLUE5)
wall1.draw(), wall2.draw(), wall3.draw(), wall4.draw(), wall5.draw()

# main object
cookie = Circle(LIGHT_BLUE6, (X * 0.25, Y * 0.5), X * 0.115)
cookie.draw()

# images
cookie_ = pygame.image.load('cookie.png')
cookie_ = pygame.transform.scale(cookie_, (int(X * 0.2), int(X * 0.2)))

cursor = pygame.image.load('cursor.png')
cursor = pygame.transform.scale(cursor, (int(Y * 0.08), int(Y * 0.11)))

farm = pygame.image.load('farm.jpg')
farm = pygame.transform.scale(farm, (int(Y * 0.13), int(Y * 0.13)))

fabric = pygame.image.load('fabric.jpg')
fabric = pygame.transform.scale(fabric, (int(Y * 0.13), int(Y * 0.13)))

mine = pygame.image.load('mine.png')
mine = pygame.transform.scale(mine, (int(Y * 0.13), int(Y * 0.13)))


info = pygame.image.load('info.jpg')
info = pygame.transform.scale(info, (int(X * 0.11), int(Y * 0.11)))

rewards = pygame.image.load('quests.jpg')
rewards = pygame.transform.scale(rewards, (int(X * 0.11), int(Y * 0.11)))

achievement = pygame.image.load('achievement.jpg')
achievement = pygame.transform.scale(achievement, (int(X * 0.11), int(Y * 0.11)))

settings = pygame.image.load('settings.jpg')
settings = pygame.transform.scale(settings, (int(X * 0.11), int(Y * 0.11)))

# name
name = Label(X * 0.1375, Y * 0.1, X * 0.23, Y * 0.075, LIGHT_BLUE5)
name.set_text('Cookie Clicker', 70, BLACK)
name.draw(0, -15)

# counter of clicks
a = sum([salary_of_autoclicker[x] for x in range(lvl_autoclicker)])
b = sum([salary_of_farm[x] for x in range(lvl_farm)])
c = sum([salary_of_fabric[x] for x in range(lvl_fabric)])
d = sum([salary_of_mine[x] for x in range(lvl_mine)])

counter_clicks = Label(X * 0.15, Y * 0.2, X * 0.2, Y * 0.05, LIGHT_BLUE4)
counter_clicks.set_text('loading..', 40, BLACK)
counter_clicks.draw(20, 10)
counter_clicks1 = Area(0, Y * 0.8, X * 0.49, Y * 0.8, DARK_GRAY1)
counter_clicks1.draw()
counter_clicks2 = Label(X * 0.01, Y * 0.81, X * 0.23, Y * 0.05, LIGHT_BLUE4)
counter_clicks2.set_text(f'Доход в секунду: {a}', 26, BLACK)
counter_clicks2.draw(80, 12)
counter_clicks3 = Label(X * 0.25, Y * 0.81, X * 0.23, Y * 0.05, LIGHT_BLUE4)
counter_clicks3.set_text(f'Доход за 1 клик: {b + c + d}', 26, BLACK)
counter_clicks3.draw(80, 12)

# version
version = Label(X * 0.375, 0, X * 0.05, Y * 0.04, LIGHT_BLUE6)
version.set_text('v: 1.2', 30, BLACK)
version.draw(20, 5)

# timer
time_count = Label(X * 0.425, 0, X * 0.065, Y * 0.04, LIGHT_BLUE6)
time_count.set_text(str(t), 30, BLACK)
time_count.draw(25, 5)

# fps
fps_counter = Label(X * 0.325, 0, X * 0.05, Y * 0.04, LIGHT_BLUE6)
fps_counter.set_text(f'fps: {FPS}', 30, BLACK)
fps_counter.draw(0, 7)

# menu
menu = Area(0, Y * 0.87, X * 0.49, Y * 0.13, DARK_GRAY1)
menu1 = Area(X * 0.01, Y * 0.88, X * 0.11, Y * 0.11, WHITE)
menu2 = Area(X * 0.13, Y * 0.88, X * 0.11, Y * 0.11, WHITE)
menu3 = Area(X * 0.25, Y * 0.88, X * 0.11, Y * 0.11, WHITE)
menu4 = Area(X * 0.37, Y * 0.88, X * 0.11, Y * 0.11, WHITE)

# bonus
bonus = Label(bonus_coord_x, bonus_coord_y, 45, 45, ORANGE)
bonus.set_text('bonus!', 20, BLACK)

# stop game
stop_game = Area(X * 0.95, 0, X * 0.05, Y * 0.035, RED)
stop_game1 = Area(X * 0.965, Y * 0.025, X * 0.02, Y * 0.005, WHITE)
stop_game2 = Area(X * 0.965, Y * 0.015, X * 0.02, Y * 0.005, WHITE)
stop_game.draw(), stop_game1.draw(), stop_game2.draw()

# hide game
hide_game = Area(X * 0.925, 0, X * 0.026, Y * 0.035, GRAY)
hide_game1 = Area(X * 0.9325, Y * 0.025, X * 0.01, Y * 0.005, WHITE)
hide_game.draw(), hide_game1.draw()

def_upgrades_autoclicker()
def_upgrades_farm()
def_upgrades_fabric()
def_upgrades_mine()

# all objects
draw_obj = [wall1, wall2, wall3, wall4, wall5, menu, name, version, fps_counter, time_count,
            counter_clicks, counter_clicks1, counter_clicks2, counter_clicks3, menu1, menu2, menu3, menu4,
            upgrades_autoclicker, upgrades_autoclicker1, upgrades_autoclicker2, upgrades_autoclicker3,
            upgrades_autoclicker4, upgrades_farm, upgrades_farm1, upgrades_farm2, upgrades_farm3, upgrades_farm4,
            upgrades_fabric, upgrades_fabric1, upgrades_fabric2, upgrades_fabric3, upgrades_fabric4,
            upgrades_mine, upgrades_mine1, upgrades_mine2, upgrades_mine3, upgrades_mine4,
            stop_game, stop_game1, stop_game2, hide_game, hide_game1]

start_time, cur_time = time.time(), t

while running:
    int_COUNT = int(int_COUNT)
    '''for element in draw_obj:
        if element is version:
            element.draw(20, 5)
        elif element is fps_counter:
            element.draw(0, 7)
        elif element is time_count:
            element.draw(25, 5)
        elif element is name:
            element.draw(0, -15)
        elif element is counter_clicks:
            element.draw(20, 10)
        elif element is counter_clicks2 or element is counter_clicks3:
            element.draw(80, 12)
        elif element is upgrades_autoclicker2 or element is upgrades_autoclicker3 or element is upgrades_farm2 or \
                element is upgrades_farm3 or element is upgrades_fabric2 or element is upgrades_fabric3 or \
                element is upgrades_mine2 or element is upgrades_mine3:
            element.draw(60, 18)
        elif element is upgrades_autoclicker1:
            element.draw(210, 18)
        elif element is upgrades_fabric1:
            element.draw(228, 18)
        elif element is upgrades_farm1 or element is upgrades_mine1:
            element.draw(225, 18)
        else:
            element.draw()'''

    mw.blit(cookie_, (X * 0.15, Y * 0.325))

    mw.blit(cursor, (X * 0.555, Y * 0.12))
    mw.blit(farm, (X * 0.535, Y * 0.28))
    mw.blit(fabric, (X * 0.535, Y * 0.45))
    mw.blit(mine, (X * 0.535, Y * 0.62))

    mw.blit(info, (X * 0.01, Y * 0.88))
    mw.blit(rewards, (X * 0.13, Y * 0.88))
    mw.blit(achievement, (X * 0.25, Y * 0.88))
    mw.blit(settings, (X * 0.37, Y * 0.88))

    # time
    new_time = time.time()
    if new_time - cur_time >= 1:  # 1 sec finished
        if shop_auto_clicker is True:  # autoclicker
            auto_clicker()
        t += 1  # update timer
        time_count.set_text(str(t), 30, BLACK)
        time_count.draw(25, 5)
        cur_time = new_time

    old_int_COUNT = int_COUNT

    # opportunity for upgrade
    if lvl_autoclicker < 15:
        if int_COUNT >= price_of_autoclicker[lvl_autoclicker]:
            upgrades_autoclicker1.color(LIGHT_PINK)
        else:
            upgrades_autoclicker1.color(WHITE)
        upgrades_autoclicker1.draw(210, 18)

    if lvl_farm < 15:
        if int_COUNT >= price_of_farm[lvl_farm] and lvl_farm < 15:
            upgrades_farm1.color(LIGHT_PINK)
        else:
            upgrades_farm1.color(WHITE)
        upgrades_farm.draw()
        upgrades_farm1.draw(225, 18)
        upgrades_farm2.draw(60, 18)
        upgrades_farm3.draw(60, 18)
        upgrades_farm4.draw()
    else:
        def_upgrades_farm()
    mw.blit(farm, (X * 0.535, Y * 0.28))

    if lvl_fabric < 15:
        if int_COUNT >= price_of_fabric[lvl_fabric] and lvl_fabric < 15:
            upgrades_fabric1.color(LIGHT_PINK)
        else:
            upgrades_fabric1.color(WHITE)
        upgrades_fabric1.draw(228, 18)

    if lvl_mine < 15:
        if int_COUNT >= price_of_mine[lvl_mine] and lvl_mine < 15:
            upgrades_mine1.color(LIGHT_PINK)
        else:
            upgrades_mine1.color(WHITE)
        upgrades_mine1.draw(225, 18)

    # event
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # LCM
            xx, yy = event.pos

            # +cl
            if cookie.collidepoint(xx, yy):
                def_count()

            # create bonus
            if randint(0, 1000) == 9 and int_COUNT >= 10000000:
                if flag_for_bonus is False:
                    flag_for_bonus = True
                    bonus_coord_x, bonus_coord_y = randint(350, 450), randint(100, 300)

                    bonus = Label(bonus_coord_x, bonus_coord_y, 45, 45, ORANGE)
                    bonus.set_text('bonus!', 20, BLACK)
                    bonus.draw(0, 15)

            # collidepoint of bonus
            if bonus.collidepoint(xx, yy) and flag_for_bonus is True:
                flag_for_bonus = False
                COUNT = int_COUNT + ((int_COUNT // 100) * 10)  # +10%
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)
                del_block = Area(bonus_coord_x, bonus_coord_y, 45, 45, LIGHT_BLUE)
                del_block.draw()

            # collidepoint of upgrades
            if upgrades_autoclicker.collidepoint(xx, yy) and int_COUNT >= price_of_autoclicker[lvl_autoclicker] \
                    and lvl_autoclicker < 15:
                int_COUNT -= price_of_autoclicker[lvl_autoclicker]
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)
                def_upgrades_autoclicker()

            if upgrades_farm.collidepoint(xx, yy) and int_COUNT >= price_of_farm[lvl_farm] and lvl_farm < 15:
                int_COUNT -= price_of_farm[lvl_farm]
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)
                def_upgrades_farm()

            if upgrades_fabric.collidepoint(xx, yy) and int_COUNT >= price_of_fabric[lvl_fabric] and lvl_fabric < 15:
                int_COUNT -= price_of_fabric[lvl_fabric]
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)
                def_upgrades_fabric()

            if upgrades_mine.collidepoint(xx, yy) and int_COUNT >= price_of_mine[lvl_mine] and lvl_mine < 15:
                int_COUNT -= price_of_mine[lvl_mine]
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)
                def_upgrades_mine()

            if cookie.collidepoint(xx, yy):
                # cl for 1 click
                int_COUNT += sum([salary_of_farm[x] for x in range(lvl_farm)])
                int_COUNT += sum([salary_of_fabric[x] for x in range(lvl_fabric)])
                int_COUNT += sum([salary_of_mine[x] for x in range(lvl_mine)])
                counter_clicks.set_text('Денег: ' + str(int_COUNT), 40, BLACK)
                counter_clicks.draw(20, 10)

            # close frame of settings
            '''if frame_settings in draw_obj and frame_settings1 in draw_obj and frame_settings2 in draw_obj:
                if frame_settings2.collidepoint(xx, yy):
                    def_frame_settings()'''

            # collidepoint of info
            if menu1.collidepoint(xx, yy):
                def_frame_info()

            # collidepoint of rewards
            if menu2.collidepoint(xx, yy):
                def_frame_rewards()

            # collidepoint of achievement
            if menu3.collidepoint(xx, yy):
                def_frame_achievement()

            # collidepoint of settings
            if menu4.collidepoint(xx, yy):
                print('725')
                def_frame_settings()

            # quite
            if stop_game.collidepoint(xx, yy):
                running = False

            # (full / not full) screen
            if hide_game.collidepoint(xx, yy):
                if full_screen is True:
                    full_screen = False
                    X //= 2
                    Y //= 2
                    mw = pygame.display.set_mode((X, Y))
                    surf = pygame.Surface((X, Y))
                    mw.fill(LIGHT_BLUE)
                    image = pygame.transform.scale(cookie_, (int(X * 0.2), int(X * 0.2)))
                    cursor = pygame.transform.scale(cursor, (int(Y * 0.08), int(Y * 0.11)))
                    farm = pygame.transform.scale(farm, (int(Y * 0.13), int(Y * 0.13)))
                    fabric = pygame.transform.scale(fabric, (int(Y * 0.13), int(Y * 0.13)))
                    mine = pygame.transform.scale(mine, (int(Y * 0.13), int(Y * 0.13)))
                    info = pygame.transform.scale(info, (int(X * 0.11), int(Y * 0.11)))
                    rewards = pygame.transform.scale(rewards, (int(X * 0.11), int(Y * 0.11)))
                    achievement = pygame.transform.scale(achievement, (int(X * 0.11), int(Y * 0.11)))
                    settings = pygame.transform.scale(settings, (int(X * 0.11), int(Y * 0.11)))
                else:
                    full_screen = True
                    X = root.winfo_screenwidth()
                    Y = root.winfo_screenheight()
                    surf = pygame.Surface((X, Y))
                    mw = pygame.display.set_mode((X, Y))
                '''for element in draw_obj:
                    print('Элемент отображен')
                    element.draw()'''

        # keyboard
        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and cheat_cheat == 1:
                cheat_cheat = 2
            elif event.key == pygame.K_h and cheat_cheat == 2:
                cheat_cheat = 3
            elif event.key == pygame.K_e and cheat_cheat == 3:
                cheat_cheat = 4
            elif event.key == pygame.K_a and cheat_cheat == 4:
                cheat_cheat = 5
            elif event.key == pygame.K_t and cheat_cheat == 5:
                int_COUNT += 1000000
            else:
                cheat_cheat = 1

            if event.key == pygame.K_b and cheat_bonus == 1:
                cheat_bonus = 2
            elif event.key == pygame.K_o and cheat_bonus == 2:
                cheat_bonus = 3
            elif event.key == pygame.K_n and cheat_bonus == 3:
                cheat_bonus = 4
            elif event.key == pygame.K_u and cheat_bonus == 4:
                cheat_bonus = 5
            elif event.key == pygame.K_s and cheat_bonus == 5:
                int_COUNT += 10000000
            else:
                cheat_bonus = 1'''

        a = sum([salary_of_autoclicker[x] for x in range(lvl_autoclicker)])
        b = sum([salary_of_farm[x] for x in range(lvl_farm)])
        c = sum([salary_of_fabric[x] for x in range(lvl_fabric)])
        d = sum([salary_of_mine[x] for x in range(lvl_mine)])

        counter_clicks2.set_text(f'Доход в секунду: {a}', 26, BLACK)
        counter_clicks2.draw(80, 12)
        counter_clicks3.set_text(f'Доход за 1 клик: {b + c + d}', 26, BLACK)
        counter_clicks3.draw(80, 12)

        # quite
        if event.type == pygame.QUIT:
            running = False

    # difference_per_sec(old_int_COUNT, int_COUNT)

    pygame.display.update()
    clock.tick(FPS)

# save data
file = open('progress_v_1.2.txt', 'w')
file.write(f'{str(int(int_COUNT))} {str(t)} {str(int(lvl_autoclicker) - 1)} {str(int(lvl_farm) - 1)} '
           f'{str(int(lvl_fabric) - 1)} {str(int(lvl_mine) - 1)}')
file.close()
