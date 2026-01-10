import pygame as pg
from resource_manager import resource_path


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(resource_path(self.path + 'shotgun.wav'))
        self.npc_pain = pg.mixer.Sound(resource_path(self.path + 'npc_pain.wav'))
        self.npc_death = pg.mixer.Sound(resource_path(self.path + 'npc_death.wav'))
        self.npc_shot = pg.mixer.Sound(resource_path(self.path + 'npc_attack.wav'))
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(resource_path(self.path + 'player_pain.wav'))
        self.theme = pg.mixer.music.load(resource_path(self.path + 'theme.mp3'))
        pg.mixer.music.set_volume(0.7)
