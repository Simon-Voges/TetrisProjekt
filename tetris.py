import pygame
import random 
import time 

#Constants
WIDTH, HEIGHT = 200, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 60

SHAPES = [
    [
        '.....',
        '.....',
        '..o..',
        '.ooo.',
        '.....',
           
    ],
    [
        '.....',
        '.....',
        '..oo.',
        '..oo.',
        '.....',
    ],
    [
        '.....',
        '..o..',
        '..o..',
        '..oo.',
        '.....',
    ],
    [
        '.....',
        '...o.',
        '...o.',
        '..oo.',
        '.....',
    ],
    [
        '.....',
        '...o.',
        '...o.',
        '...o.',
        '...o.',
    ],
    [
        '.....',
        '..o..',
        '..oo.',
        '...o.',
        '.....',
    ],
    [
        '.....',
        '...o.',
        '..oo..',
        '..o..',
        '.....',
    ]
    
    ]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0
           
    def rotate(self, grid):
        new_rotation = (self.rotation +1) % len(self.shape)
        test_piece = Tetromino(self.x, self.y, self.shape)
        test_piece.rotation = new_rotation
        
        if not grid.valid_move(test_piece):
            return
        self.rotation = new_rotation
         
    def move(self, grid, dx, dy):
        test_piece = Tetromino(self.x + dx, self.y + dy, self.shape)
        test_piece.rotation = self.rotation
        
        if not grid.valid_move(test_piece):
            return
        self.x += dx
        self.y += dy
        

class Tetris:
    def __init__(self): 
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)] 
        self.current_piece = self.new_piece()
        
    def new_piece (self):
        shape = random.choice(SHAPES)
        x = GRID_WIDTH // 2 - len(shape[0] // 2)
        y = 0
        
        return Tetromino(x,y,shape)
    
    def valid_move(self, piece):
        for y, row in enumerate(piece.shape[piece.rotation]):
            for x, cell in enumerate(row): 
                if cell =='o':
                    grid_x = piece.x + x
                    grid_y = piece.y + y
                    
                    if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT:
                        return False
                    if grid_y >= 0 and self.grid[grid_y][grid_x]: 
                        return False 
        return True
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT-1,-1,-1):
            if all (self.grid[y][x] for x in range (GRID_WIDTH)):
                lines_cleared+=1 
                self.grid.pop(y)
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        return lines_cleared
            
        
        
    
    def update_grid (self):
        for y, row in enumerate(self.current_piece.shape[self.current_piece.rotation]):
            for x, cell in enumerate(row):
                if cell == 'o': 
                    self.grid[self.current_piece.y + y][self.currrent_piece.x + x] = 1
        
    def game_over (self): 
        return not self.valid_move(self.current_piece)
        
        

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock
    game = Tetris()
        #main game loop
        
        
        
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if event.type == pygame.KEYDOWN():
            if event.key == pygame.K_LEFT:
                game.current_piece.move(game.grid, -1,0)
            elif event.key == pygame.K_RIGHT:
                game.current_piece.move(game.grid,-1,0)
            elif event.key == pygame.K_DOWN:
                game.current_piece.move(game.grid,0,-1)
            elif event.key == pygame.K_UP:
                game.current_piece.rotate(game.grid)
                    
                    

            
    
