import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.ogg')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.ogg')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.ogg')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.ogg')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.ogg')
        self.theme = pg.mixer.music.load(self.path + 'theme.ogg')
        pg.mixer.music.set_volume(1.0)