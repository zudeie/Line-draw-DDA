import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's/ Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0, 00)

# Function to draw a line using DDA algorithm
def draw_line_DDA(x1, y1, x2, y2):
    dx=abs(int(x2-x1))
    dy=abs(int(y2-y1))
    if dx>dy:
        step=dx
    else:
        step=dy
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    for a in range (int(step)+1):
        screen.set_at((round(x), round(y)), WHITE)    
        x+=xinc
        y+=yinc   

    
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_DDA(200,50,400,300)
        pygame.display.flip()

if __name__ == "__main__":
    main()
   
   
   
   
   
   