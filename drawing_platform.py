import pygame
import sys

# Initializing pygame
pygame.init()

# Defining pygame appearance
size = (width, height) = (600, 400)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Handwriting Recognition')

# Other important variables
offset = 10
pixel_size = (width / 2 - 2 * offset) / 28
handwriting = [[0] * 28 for _ in range(28)]

# Fonts
button_font = pygame.font.Font(pygame.font.get_default_font(), 12)

while True:
    window.fill((0, 0, 0))
    # To exit from the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Checking if mouse is pressed
    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
    else:
        mouse = None

    # Draw area
    draw_area = pygame.Rect(offset, offset, width / 2 - 2 * offset, width / 2 -
                            2 * offset)
    pygame.draw.rect(window, (255, 255, 255), draw_area)

    # Pixels
    for i in range(28):
        for j in range(28):
            pixel = pygame.Rect(offset + i * pixel_size, offset + j *
                                pixel_size, pixel_size, pixel_size)

            if handwriting[i][j]:
                dark = handwriting[i][j]
                pygame.draw.rect(window, (dark, dark, dark), pixel)
            else:
                pygame.draw.rect(window, (0, 0, 0), pixel, 1)

            if mouse and pixel.collidepoint(mouse):
                handwriting[i][j] = 10
                if i + 1 < 28:
                    handwriting[i + 1][j] = 20
                if j + 1 < 28:
                    handwriting[i][j + 1] = 20
                if i + 1 < 28 and j + 1 < 28:
                    handwriting[i + 1][j + 1] = 20

    # Reset button
    reset_rect = pygame.Rect(70, offset + 28 * pixel_size + 10, 60, 20)
    pygame.draw.rect(window, (200, 200, 200), reset_rect)
    reset = button_font.render('Reset', True, (0, 0, 0))
    reset_get_rect = reset.get_rect()
    reset_get_rect.center = reset_rect.center
    window.blit(reset, reset_get_rect)

    # Classify button
    classify_rect = pygame.Rect(170, offset + 28 * pixel_size + 10, 60, 20)
    pygame.draw.rect(window, (200, 200, 200), classify_rect)
    classify = button_font.render('Classify', True, (0, 0, 0))
    classify_get_rect = classify.get_rect()
    classify_get_rect.center = classify_rect.center
    window.blit(classify, classify_get_rect)

    # If mouse comes in contact with reset button
    if mouse and reset_rect.collidepoint(mouse):
        handwriting = [[0] * 28 for _ in range(28)]

    # Updating display
    pygame.display.update()