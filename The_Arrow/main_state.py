from pico2d import *
import game_world, game_framework
import pause_state, gameover_state
import m_bow, m_arrow, m_monster1, m_monster2, m_monster3, m_ui, m_skill

name = "MainState"

bow = None
arrows = None
monster1 = None
monster2 = None
monster3 = None
ui = None

MAX = 20
MONSTER1_APPEAR_TIMER = 500
MONSTER2_APPEAR_TIMER = 3000
MONSTER3_APPEAR_TIMER = 6000


def enter():
    global bow, arrows, monsters1, monsters2, monsters3, ui, skill
    global bgm
    if bow == None:
        bow = m_bow.Bow()
        arrows = [m_arrow.Arrow() for i in range(MAX)]
        monsters1 = [m_monster1.Monster() for i in range(MAX)]
        monsters2 = [m_monster2.Monster() for i in range(MAX)]
        monsters3 = [m_monster3.Monster() for i in range(MAX)]
        skill = m_skill.Skill()
        ui = m_ui.Ui()
        bgm = load_music('./resource/main.mp3')
    bgm.repeat_play()


def exit():
    global bow, arrows, monsters1, monsters2, monsters3, ui, skill
    global bgm
    del(bow)
    del(arrows)
    del(monsters1)
    del(monsters2)
    del(monsters3)
    del(skill)
    del(ui)
    bgm.stop()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.push_state(pause_state)
        if event.type == SDL_MOUSEMOTION and event.x > 0:   # 활 회전
            bow.mx, bow.my = event.x, game_framework.HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and \
                event.button == SDL_BUTTON_LEFT:    # 화살 생성
            for arrow in arrows:
                arrow.sound.play(1)
                if not arrow.show:
                    arrow.cx, arrow.cy = event.x, game_framework.HEIGHT - 1 - event.y
                    arrow.show = True
                    break
            for arrow in arrows:
                if not arrow.show2 and arrow.increase_quantity:
                    arrow.cx2, arrow.cy2 = event.x, game_framework.HEIGHT - 1 - event.y
                    arrow.show2 = True
                    break;
            for arrow in arrows:
                if not arrow.show3 and arrow.increase_quantity:
                    arrow.cx3, arrow.cy3 = event.x, game_framework.HEIGHT - 1 - event.y
                    arrow.show3 = True
                    break;
        elif event.type == SDL_MOUSEBUTTONDOWN and \
             event.button == SDL_BUTTON_RIGHT:  # Ui 선택
                if not skill.show and ui.gold >= 5000 \
                        and 470 < event.x < 530 \
                        and 30 < 600 - event.y < 90:    # 스킬사용
                    ui.sound.play(1)
                    skill.sound.play(1)
                    ui.gold -= 5000
                    skill.show = True
                    skill.damage_on = True
                if ui.gold >= 3000 \
                        and 800 < event.x < 860 \
                        and 30 < 600 - event.y < 90:    # 화살 데미지 강화
                    ui.sound.play(1)
                    ui.gold -= 3000
                    for arrow in arrows:
                        arrow.damage += 0.25
                if ui.gold >= 15000 \
                        and 880 < event.x < 940 \
                        and 30 < 600 - event.y < 90:    # 화살 개수 증가
                    for arrow in arrows:
                        if not arrow.increase_quantity:
                            ui.sound.play(1)
                            ui.gold -= 750
                            arrow.increase_quantity = True

def update():
    global MONSTER1_APPEAR_TIMER, MONSTER2_APPEAR_TIMER, MONSTER3_APPEAR_TIMER
    bow.update()
    skill.update()
    for arrow in arrows:
        arrow.update()
    for monster1 in monsters1:
        monster1.update()
    for monster2 in monsters2:
        monster2.update()
    for monster3 in monsters3:
        monster3.update()
    # 몬스터1 등장 주기
    MONSTER1_APPEAR_TIMER -= game_framework.frame_time * 100
    if MONSTER1_APPEAR_TIMER < 0:
        for monster1 in monsters1:
            if not monster1.show:
                monster1.__init__()
                monster1.show = True
                break
        MONSTER1_APPEAR_TIMER = 200 / ui.difficulty_count
    # 몬스터2 등장 주기
    MONSTER2_APPEAR_TIMER -= game_framework.frame_time * 100
    if MONSTER2_APPEAR_TIMER < 0:
        for monster2 in monsters2:
            if not monster2.show:
                monster2.__init__()
                monster2.show = True
                break
        MONSTER2_APPEAR_TIMER = 500 / ui.difficulty_count
    # 몬스터3 등장 주기
    MONSTER3_APPEAR_TIMER -= game_framework.frame_time * 100
    if MONSTER3_APPEAR_TIMER < 0:
        ui.difficulty_count += 0.1
        for monster3 in monsters3:
            if not monster3.show:
                monster3.__init__()
                monster3.show = True
                break
        MONSTER3_APPEAR_TIMER = 2000 / ui.difficulty_count
    # 스킬 사용 시 몬스터 hp 감소
    if skill.damage_on:
        for monster1 in monsters1:
            monster1.hp = 0
        for monster2 in monsters2:
            monster2.hp -= 5
        for monster3 in monsters3:
            monster3.hp -= 15
        skill.damage_on = False

    if ui.player_hp <= 0:
        game_framework.change_state(gameover_state)


def draw():
    hide_cursor()
    clear_canvas()
    ui.draw()
    bow.draw()
    for arrow in arrows:
        arrow.draw()
    for monster1 in monsters1:
        monster1.draw()
    for monster2 in monsters2:
        monster2.draw()
    for monster3 in monsters3:
        monster3.draw()
    skill.draw()
    update_canvas()




