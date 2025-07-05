import pygame
import sys

# -----------------------
# Pygame Setup
# -----------------------
pygame.init()
WIDTH, HEIGHT = 1024, 768
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gwent - Mini Witcher 3 Clone")
FPS = 60

# Colors
WHITE = (255, 255, 255)
DARK_GREEN = (34, 139, 34)
LIGHT_BROWN = (181, 101, 29)
CARD_COLOR = (240, 240, 240)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont("arial", 24)

# -----------------------
# Card Class
# -----------------------
class Card:
    def __init__(self, name, strength, position):
        self.name = name
        self.strength = strength
        self.rect = pygame.Rect(position[0], position[1], 100, 150)

    def draw(self, surface):
        pygame.draw.rect(surface, CARD_COLOR, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text = FONT.render(f"{self.name} ({self.strength})", True, BLACK)
        surface.blit(text, (self.rect.x + 5, self.rect.y + 60))

# -----------------------
# Sample Player Hand
# -----------------------
player_hand = [
    Card("Geralt", 15, (100, HEIGHT - 200)),
    Card("Triss", 7, (220, HEIGHT - 200)),
    Card("Yennefer", 7, (340, HEIGHT - 200))
]

# -----------------------
# Main Game Loop
# -----------------------
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    WINDOW.fill(LIGHT_BROWN)  # Board background

    # Draw Gwent rows (player/opponent)
    pygame.draw.rect(WINDOW, DARK_GREEN, (0, HEIGHT // 2 - 75, WIDTH, 150))  # Battlefield

    # Draw player hand
    for card in player_hand:
        card.draw(WINDOW)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
