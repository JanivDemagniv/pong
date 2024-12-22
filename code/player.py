from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(SIZE['paddle'])
        self.image.fill(COLORS['paddle'])
        self.rect = self.image.get_frect(center = pos)
        self.dir = 0
        self.speed = SPEED['player']

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.dir = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])

    def move(self,dt):
        self.rect.y += self.dir * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def update(self, dt):
        self.get_direction()
        self.move(dt)
