import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 75
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 0, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT = "Click Me!"

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Button Example")

# Create a font object for the button text
font = pygame.font.Font(None, 36)

def draw_button(x,y):
    # Create a rectangle for the button
    button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Check if the mouse is over the button
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    # Change button color when hovered
    if is_hovered:
        pygame.draw.rect(window, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(window, BUTTON_COLOR, button_rect)

    # Create button text
    text = font.render(BUTTON_TEXT, True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)

    # Draw button text
    window.blit(text, text_rect)
    button_clicked = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left moue button
                if draw_button(100,500).collidepoint(event.pos):
                    button_clicked = True

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the button
    draw_button(100,500)
    draw_button()
    if button_clicked:
        print("Button Clicked!")
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()