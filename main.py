import colorsys
import random 
import sys
import time

import pygame

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

BLACK = (0, 0, 0)
HUE_VALUE = 0.0

clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Falling Sand')

class Grid:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # Initialize cell size
        self.CELL_SIZE = 2

        # Set initial hue value
        self.HUE_VALUE = 0.0

        self.rows = SCREEN_HEIGHT // self.CELL_SIZE
        self.columns = SCREEN_WIDTH // self.CELL_SIZE

        # Create grid
        self.previous_grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw_cell(self, screen):
        color = self.hue_to_color(self.HUE_VALUE)

        for i in range(self.rows):
            for j in range(self.columns):
                # Calculate the position of the cell
                x = j * self.CELL_SIZE
                y = i * self.CELL_SIZE

                # Draw the cell
                if self.current_grid[i][j] == 1:
                    pygame.draw.rect(screen, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))

    def add_cell(self, xpos, ypos):
        # Calculate the cell coordinates from the mouse position
        cell_x = xpos // self.CELL_SIZE
        cell_y = ypos // self.CELL_SIZE
        
        # Update grid value
        self.current_grid[cell_y][cell_x] = 1

    def update_grid(self):
        # Store current grid state in self.previous_grid
        self.previous_grid = self.current_grid

        # Create a new grid with a state of all O's
        self.current_grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

        # Keeps the last row constant
        self.current_grid[self.rows - 1] = self.previous_grid[self.rows - 1][:]

        # Iterate through each cell in the previous grid state and update its position in the new grid
        for i in range(self.rows - 1):
            for j in range(self.columns):

                if self.previous_grid[i][j] == 1:

                    # Check if the cell can move down
                    if self.previous_grid[i + 1][j] == 0:
                        self.current_grid[i + 1][j] = 1

                    # Both left and right are available
                    elif (j > 0 and self.previous_grid[i + 1][j - 1] == 0 and
                          j < self.columns - 1 and self.previous_grid[i + 1][j + 1] == 0):
                        self.current_grid[i + 1][j + random.choice([-1, 1])] = 1

                    # Only left is available
                    elif j > 0 and self.previous_grid[i + 1][j - 1] == 0:
                        self.current_grid[i + 1][j - 1] = 1

                    # Only right is available
                    elif j < self.columns - 1 and self.previous_grid[i + 1][j + 1] == 0:
                        self.current_grid[i + 1][j + 1] = 1

                    # If no adjacent cells are available, stay in the current position
                    else:
                        self.current_grid[i][j] = 1

    def hue_to_color(self, hue):
        # Convert hue value (0-1) to HSV
        hsv = (hue, 1.0, 1.0)

        # Convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        
        # Scale the RGB values to the range [0, 255]
        color_param = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

        return color_param

def main():
    grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create a timer that expires after 3 seconds
    timer = time.time() + 3

    # Start the main loop
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            # Get the mouse position
            mouse_x, mouse_y = event.pos

            if 0 <= mouse_x < SCREEN_WIDTH and 0 <= mouse_y < SCREEN_HEIGHT:
                grid.add_cell(mouse_x, mouse_y)

            if time.time() >= timer:
                # Wrap around to 0.0 when hue value reaches 1.0
                grid.HUE_VALUE = (grid.HUE_VALUE + 0.1) % 1.0

                # Reset the timer
                timer = time.time() + 3

        # Update the grid state
        grid.update_grid()

        # Redraw the screen during each pass through the loop
        screen.fill(BLACK)

        # Draw the grid
        grid.draw_cell(screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
