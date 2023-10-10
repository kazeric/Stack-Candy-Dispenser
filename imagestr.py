import pygame
import random

pygame.init()

# Create a Pygame screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image with Falling Text")

# Load the image
image = pygame.image.load("candy1.png")
image_width, image_height = image.get_rect().size

# Load a font and set its size
font = pygame.font.Font(None, 36)

# Text settings
text = "Hello, Pygame!"
text_color = (255, 255, 255)

# Initialize image and text positions
image_x = random.randint(0, screen_width - image_width)
image_y = 0
text_x = image_x + 10
text_y = image_y + 10
fall_speed = 2  # Adjust this value to control the falling speed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update image and text positions for falling effect
    image_y += fall_speed
    text_y += fall_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the image onto the screen at the updated position
    screen.blit(image, (image_x, image_y))

    # Render the text onto the screen at the updated position
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()

    # Reset the image and text positions when they reach the bottom
    if image_y > screen_height:
        image_x = random.randint(0, screen_width - image_width)
        image_y = -image_height
        text_x = image_x + 10
        text_y = image_y + 10

pygame.quit()

