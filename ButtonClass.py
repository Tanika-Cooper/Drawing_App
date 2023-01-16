import pygame

class Button():
    def __init__(self, x, y, width, height, gameScreen, buttonText='Button', onClickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onClickFunction = onClickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.objects = []

        self.gameScreen = gameScreen

        # Options for button state colours
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333'
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('Arial', 40)


        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        self.objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()

        # Initialise button colour
        self.buttonSurface.fill(self.fillColors['normal'])

        # Check if interaction occurs
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if self.onePress:
                self.onClickFunction()
            elif not self.alreadyPressed:
                self.onClickFunction()
                self.alreadyPressed = True
        else:
            self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.gameScreen.blit(self.buttonSurface, self.buttonRect)
