from setting import *
from sprite import *
from groups import AllSprites
import json

class Game():
    def __init__(self):
        #setup
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption('Pong')
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

        #groups
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()

        #sprite
        self.player = Player('player',(self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.paddle_sprites , self.update_score ,self.all_sprites)
        Opponent('opponent',self.ball,(self.all_sprites,self.paddle_sprites))

        #score
        try:
            with open(join('data','score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player':0,'opponent':0}
        self.font = pygame.font.Font(None,160)

    def display_score(self):
        #player
        player_score_surf = self.font.render(str(self.score['player']),True,COLORS['bg detail'])
        player_score_rect = player_score_surf.get_frect(center = (WINDOW_WIDTH /2 + 100, WINDOW_HEIGHT/2))
        self.display_surf.blit(player_score_surf,player_score_rect)

        #opponent
        opp_score_surf = self.font.render(str(self.score['opponent']),True,COLORS['bg detail'])
        opp_score_rect = opp_score_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surf.blit(opp_score_surf,opp_score_rect)

        #line
        pygame.draw.line(self.display_surf,COLORS['bg detail'],(WINDOW_WIDTH/2,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT),7 )

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def start_game(self):
        while self.running:
            dt = self.clock.tick() / 1000

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data','score.txt'),'w') as score_file:
                        json.dump(self.score,score_file)
            
            #update
            self.all_sprites.update(dt)

            #draw
            self.display_surf.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            #note to self: this group do not need a surface arrgument to draw on becuse of the custome group I created
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.start_game()
