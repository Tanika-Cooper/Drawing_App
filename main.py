import sys
import pygame
import ctypes
from ButtonClass import Button

# Config
ctypes.windll.shcore.SetProcessDpiAwareness(True)

pygame.init()
fps = 300
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
font = pygame.font.SysFont('Arial', 20)

# Variable Declarations
buttonsList = []
drawColour = [0, 0, 0]
brushSize = 30
brushSizeSteps = 3
canvasSize = [800, 800]

# ---------------------------------------------------------------------
# Handler Functions
def changeColour(colour):
    global drawColour
    drawColour = colour

def changeBrushSize(dir):
    global brushSize
    if dir == 'greater':
        brushSize += brushSizeSteps
    else:
        brushSize -= brushSizeSteps

def save():
    pygame.image.save(canvas, "canvas.png")
# ---------------------------------------------------------------------


# Button Variables
buttonWidth = 120
buttonHeight = 35

buttonDetails = [
    ['Black', lambda: changeColour([0, 0, 0])],
    ['White', lambda: changeColour([255, 255, 255])],
    ['Blue', lambda: changeColour([0, 0, 255])],
    ['Green', lambda: changeColour([0, 255, 0])],
    ['Brush Larger', lambda: changeBrushSize('greater')],
    ['Brush Smaller', lambda: changeBrushSize('smaller')],
    ['Save', save],
]

# Generate the buttons
for index, buttonName in enumerate(buttonDetails):
    Button(index * (buttonWidth + 10) + 10, 10, buttonWidth, buttonHeight, font, screen, buttonsList, buttonName[0], buttonName[1])

# Canvas
canvas = pygame.Surface(canvasSize)
canvas.fill((255, 255, 255))

# ---------------------------------------------------------------------
# Game Loop
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Render Buttons
    for button in buttonsList:
        button.process()

    # Draw Canvas in centre
    x, y = screen.get_size()
    screen.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])

    # Check for button press
    if  pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()

        # Calculate relative canvas position
        dx = mx - x/2 + canvasSize[0]/2
        dy = my - y/2 + canvasSize[1]/2
        pygame.draw.circle(
            canvas,
            drawColour,
            [dx, dy],
            brushSize
        )

    pygame.display.flip()
    fpsClock.tick(fps)
