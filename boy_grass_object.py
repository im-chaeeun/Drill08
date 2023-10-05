from pico2d import *


# Game object class here
class Grass:    # 클래스의 이름은 대문자로 시작하는 명사로 지음
    def __init__(self):     # 생성자 함수, 모든 클래스에 사용, 객체의 초기 상태 설정, self - 생성된 객체를 가리킴. 정의 할 때만
        self.image = load_image('grass.png')        # shift + enter

    def draw(self):     # 첫 번째 파라미터는 self
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
def reset_world():
    global running
    global grass
    global boy

    running = True
    grass = Grass()     # 클래스를 이용해 객체를 찍어냄
    boy = Boy()

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    boy.update()
    pass
def render_world():
    clear_canvas()
    grass.draw()        #  그리는 순서 중요, 먼저 그린게 뒤에 온다!
    boy.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
