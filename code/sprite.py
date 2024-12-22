from setting import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(SIZE['ball'])
        self.image.fill(COLORS['ball'])
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,50))
        self.dir = pygame.Vector2(2,1)
        self.speed = SPEED['ball']

    def move(self,dt):
        self.rect.center += self.dir * self.speed * dt

    def collision_screen(self):
        if self.rect.right >= WINDOW_WIDTH:
            self.dir.x = self.dir.x * -1
            self.rect.right = WINDOW_WIDTH
        if self.rect.top <= 0:
            self.dir.y = self.dir.y * -1
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.dir.y = self.dir.y * -1
        if self.rect.left <= 0:
            self.dir.x = self.dir.x * -1
    def update(self, dt):
        self.move(dt)
        self.collision_screen()