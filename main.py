import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
import asyncio


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 100)
        self.game_state = 'playing' # 🔑 NEW: Game state flag
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        self.game_state = 'playing' # 🔑 NEW: Game state flag
        pg.mixer.music.play(-1)

    def update(self):
        # 🔑 FIX: Only run game logic if state is 'playing'
        if self.game_state == 'playing': 
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
        pg.display.flip()
        
        # 🔑 FIX: Remove the FPS argument (set in settings.py as 100)
        # This allows the browser to run the game as fast as possible (up to 60 FPS).
        self.delta_time = self.clock.tick() 
        
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # 🔑 FIX: Draw ONLY the scene or the end screen, based on state
        if self.game_state == 'playing':
            self.object_renderer.draw() 
            self.weapon.draw()
        elif self.game_state == 'game_over':
            self.object_renderer.game_over()
        elif self.game_state == 'win':
            self.object_renderer.win()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                # sys.exit() is generally problematic on the web, though Pygbag handles it.
                sys.exit() 
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    async def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            # This yields control to the browser, allowing it to redraw the screen.
            await asyncio.sleep(0)


if __name__ == '__main__':
    game = Game()
    # This runs the asynchronous loop correctly.
    asyncio.run(game.run())
