import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 0, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Two Buttons Example")

# Create fonts
font = pygame.font.Font(None, FONT_SIZE)

# Define button properties
button1_text = "Button 1"
button2_text = "Button 2"

# Define button rectangles
button1_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 4, (HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
button2_rect = pygame.Rect((3 * WIDTH - BUTTON_WIDTH) // 4, (HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

# Initialize button click flags
button1_clicked = False
button2_clicked = False

def draw_button(button_rect, text, clicked):
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    if is_hovered:
        pygame.draw.rect(window, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(window, BUTTON_COLOR, button_rect)

    text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    window.blit(text_surface, text_rect)

    if clicked:
        pygame.draw.rect(window, (0, 255, 0), button_rect, 3)  # Draw a green border when clicked

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1_rect.collidepoint(event.pos):
                    button1_clicked = True
                if button2_rect.collidepoint(event.pos):
                    button2_clicked = True

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw buttons
    draw_button(button1_rect, button1_text, button1_clicked)
    draw_button(button2_rect, button2_text, button2_clicked)

    # Handle button actions
    if button1_clicked:
        print("Button 1 Clicked!")
        # Add functionality for Button 1 here
        button1_clicked = False  # Reset the flag

    if button2_clicked:
        print("Button 2 Clicked!")
        # Add functionality for Button 2 here
        button2_clicked = False  # Reset the flag

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
