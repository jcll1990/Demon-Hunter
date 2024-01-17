import pygame as pg



class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.bow = pg.mixer.Sound(self.path + 'bow.wav')
        self.melee = pg.mixer.Sound(self.path + 'melee.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'demonhuntertheme.wav')
        pg.mixer.music.set_volume(0.3)

        self.reddemonattack = pg.mixer.Sound('resources/sound/NPC/reddemon/attack.wav')
        self.reddemondeath = pg.mixer.Sound('resources/sound/NPC/reddemon/death.wav')
        self.reddemonpain = pg.mixer.Sound('resources/sound/NPC/reddemon/pain.wav')
        self.bigdemonattack = pg.mixer.Sound('resources/sound/NPC/bigdemon/attack.wav')
        self.bigdemondeath = pg.mixer.Sound('resources/sound/NPC/bigdemon/death.wav')
        self.bigdemonpain = pg.mixer.Sound('resources/sound/NPC/bigdemon/pain.wav')
        self.meleedemonattack = pg.mixer.Sound('resources/sound/NPC/meleedemon/attack.wav')
        self.meleedemondeath = pg.mixer.Sound('resources/sound/NPC/meleedemon/death.wav')
        self.meleedemonpain = pg.mixer.Sound('resources/sound/NPC/meleedemon/pain.wav')