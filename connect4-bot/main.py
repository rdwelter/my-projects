import pygame

CELL_SIZE = 100
WIDTH = CELL_SIZE * 7
HEIGHT = CELL_SIZE * 6

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect Four')
    
    screen.fill((255,255,255))
    pygame.display.flip()
    
    # yellow_pos = red_pos = 0b000000000000000000000000000000000000000000
    yellow_pos = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
    red_pos = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
    
    running = True
    red_turn = True
    winner = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif winner:
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // (CELL_SIZE)
                i = 5
                while i >= 0:
                    if yellow_pos[i][col] == 0 and red_pos[i][col] == 0:
                        break
                    i -= 1
                if i >= 0:
                    if red_turn:
                        red_pos[i][col] = 1
                        winner = check_winner(yellow_pos, red_pos, 'red')
                        red_turn = False
                    else:
                        yellow_pos[i][col] = 1
                        winner = check_winner(yellow_pos, red_pos, 'yellow')
                        red_turn = True
            draw_board(screen, yellow_pos, red_pos)
    
    print(f'Ended program')

def draw_board(screen, yellow_pos, red_pos):
    screen.fill((255,255,255))
    yellow_chip = pygame.image.load('images/yellow.jpeg')
    red_chip = pygame.image.load('images/red.jpeg')
    for row in range(6):
        for col in range(7):
            pygame.draw.rect(screen, (255,255,255), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if yellow_pos[row][col] == 1:
                screen.blit(yellow_chip, (col * CELL_SIZE, row * CELL_SIZE))
            elif red_pos[row][col] == 1:
                screen.blit(red_chip, (col * CELL_SIZE, row * CELL_SIZE))
    pygame.display.flip()
    
def check_winner(yellow_pos, red_pos, turn):
    for row in range(6):
        for col in range(7):
            if turn == 'red' and red_pos[row][col] == 1:
                temp_col = col+1
                while temp_col < 7 and red_pos[row][temp_col] == 1:
                    temp_col += 1
                if temp_col - col >= 4:
                    return True
                temp_row = row+1
                while temp_row < 6 and red_pos[temp_row][col] == 1:
                    temp_row += 1
                if temp_row - row >= 4:
                    return True
                temp_row, temp_col = row+1, col-1
                chips_in_diag = 1
                while temp_row < 6 and temp_col >= 0 and red_pos[temp_row][temp_col] == 1:
                    chips_in_diag += 1
                    temp_row += 1
                    temp_col -= 1
                if chips_in_diag >= 4:
                    return True
                temp_row, temp_col = row+1, col+1
                chips_in_diag = 1
                while temp_row < 6 and temp_col < 7 and red_pos[temp_row][temp_col] == 1:
                    chips_in_diag += 1
                    temp_row += 1
                    temp_col += 1
                if chips_in_diag >= 4:
                    return True
            elif turn == 'yellow' and yellow_pos[row][col] == 1:
                temp_col = col+1
                while temp_col < 7 and yellow_pos[row][temp_col] == 1:
                    temp_col += 1
                if temp_col - col >= 4:
                    return True
                temp_row = row+1
                while temp_row < 6 and yellow_pos[temp_row][col] == 1:
                    temp_row += 1
                if temp_row - row >= 4:
                    return True
                temp_row, temp_col = row+1, col-1
                chips_in_diag = 1
                while temp_row < 6 and temp_col >= 0 and yellow_pos[temp_row][temp_col] == 1:
                    chips_in_diag += 1
                    temp_row += 1
                    temp_col -= 1
                if chips_in_diag >= 4:
                    return True
                temp_row, temp_col = row+1, col+1
                chips_in_diag = 1
                while temp_row < 6 and temp_col < 7 and yellow_pos[temp_row][temp_col] == 1:
                    chips_in_diag += 1
                    temp_row += 1
                    temp_col += 1
                if chips_in_diag >= 4:
                    return True
    return False

if __name__ == "__main__":
    main()
