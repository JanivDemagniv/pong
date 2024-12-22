from setting import *
from sprite import *

class Game():
    def __init__(self):
        #setup
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption('Pong')
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()

        #sprite
        self.player = Player(POS['player'],(self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.all_sprites)

    def start_game(self):
        while self.running:
            dt = self.clock.tick() / 1000

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #update
            self.all_sprites.update(dt)

            #draw
            self.display_surf.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surf)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.start_game()
