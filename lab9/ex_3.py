# import pygame
# import math
#
# pygame.init()
#
# fps = 60
# timer = pygame.time.Clock()
# WIDTH = 800
# HEIGHT = 600
# active_figure = 0
# active_color = 'white'
#
# screen = pygame.display.set_mode([WIDTH, HEIGHT])
# pygame.display.set_caption("Paint")
# painting = []
#
#
# def draw_menu(color):
#     pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
#     pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
#     circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
#     # Draw the circle
#     pygame.draw.circle(screen, 'white', (35, 35), 20)
#     pygame.draw.circle(screen, 'black', (35, 35), 18)
#     rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
#     # Draw the square
#     pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)
#     square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
#     # Draw the square
#     pygame.draw.rect(screen, 'white', [135, 15, 40, 40], 2)
#     # Draw the right triangle
#     right_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
#     pygame.draw.polygon(screen, 'white', [(195, 15), (195, 55), (235, 15)], 2)
#
#     equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
#     side_length = 50  # Side length of the square
#     center_x = 250 + side_length / 2  # x-coordinate of the center of the square
#     center_y = 10 + side_length / 2  # y-coordinate of the center of the square
#     triangle_height = side_length * math.sqrt(3) / 2  # Height of the equilateral triangle
#
#     # Reduce the triangle height slightly to make the triangle fit inside the square
#     triangle_height *= 1
#
#     # Vertices of the equilateral triangle
#     vertex1 = (center_x, center_y - triangle_height / 2)
#     vertex2 = (center_x - side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
#     vertex3 = (center_x + side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
#
#     # Draw the equilateral triangle
#     pygame.draw.polygon(screen, 'white', [vertex1, vertex2, vertex3], 2)
#
#     rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
#
#     top_left = (310, 10)
#     top_right = (360, 10)
#     bottom_left = (310, 60)
#     bottom_right = (360, 60)
#
#     # Adjust the positions of the midpoints to decrease the size of the rhombus
#     mid_top = ((top_left[0] + top_right[0]) // 2, (top_left[1] + top_right[1]) // 2 + 4)
#     mid_left = ((top_left[0] + bottom_left[0]) // 2 + 4, (top_left[1] + bottom_left[1]) // 2)
#     mid_bottom = ((bottom_left[0] + bottom_right[0]) // 2, (bottom_left[1] + bottom_right[1]) // 2 - 4)
#     mid_right = ((top_right[0] + bottom_right[0]) // 2 - 4, (top_right[1] + bottom_right[1]) // 2)
#
#     # Draw the rhombus
#     pygame.draw.polygon(screen, 'white', [mid_top, mid_left, mid_bottom, mid_right], 2)
#
#     brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush,
#                   rhombus_brush]
#
#     pygame.draw.circle(screen, color, (400, 35), 30)
#     pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)
#
#     eraser = pygame.image.load("media/eraser-square-svgrepo-com.svg")
#     eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
#     eraser_rect.width = eraser_rect.height = 25
#     screen.blit(eraser, [WIDTH - 150, 7, 25, 25])
#
#     blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
#     red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
#     green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
#     yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
#     teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
#     purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
#     black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
#     # black = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])
#     color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
#     rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
#                 (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
#
#     return brush_list, color_rect, rgb_list
#
#
# def draw_painting(paints):
#     for color, pos, figure in paints:
#         if color == (255, 255, 255):
#             pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
#         else:
#             if figure == 0:
#                 pygame.draw.circle(screen, color, pos, 20, 2)
#             elif figure == 1:
#                 pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)
#             elif figure == 2:
#                 pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 35, 35], 2)
#             elif figure == 3:
#                 pygame.draw.polygon(screen, color, [(pos[0] - 15, pos[1] - 15),
#                                                     (pos[0] - 15, pos[1] + 35),
#                                                     (pos[0] + 35, pos[1] - 15)], 2)
#             elif figure == 4:
#                 size = 50
#                 triangle_height = size * math.sqrt(3) / 2
#
#                 # Calculate vertices of the equilateral triangle
#                 vertex1 = (pos[0], pos[1] - triangle_height / 2)
#                 vertex2 = (pos[0] - size / 2, pos[1] + triangle_height / 2)
#                 vertex3 = (pos[0] + size / 2, pos[1] + triangle_height / 2)
#
#                 # Draw the equilateral triangle
#                 pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3], 2)
#             elif figure == 5:
#                 # Draw the rhombus
#                 pygame.draw.polygon(screen, color, [(pos[0] - 25, pos[1]),
#                                                     (pos[0], pos[1] - 25),
#                                                     (pos[0] + 25, pos[1]),
#                                                     (pos[0], pos[1] + 25)], 2)
#
#
# run = True
# while run:
#     timer.tick(fps)
#     screen.fill("white")
#     mouse = pygame.mouse.get_pos()
#     left_click = pygame.mouse.get_pressed()[0]
#
#     brushes, colors, rgbs = draw_menu(active_color)
#
#     if left_click and mouse[1] > 85:
#         painting.append((active_color, mouse, active_figure))
#     draw_painting(painting)
#
#     if mouse[1] > 85:
#         if active_color == (255, 255, 255):
#             pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20])
#         else:
#             if active_figure == 0:
#                 pygame.draw.circle(screen, active_color, mouse, 20, 2)
#             elif active_figure == 1:
#                 pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
#             elif active_figure == 2:
#                 pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 35, 35], 2)
#             elif active_figure == 3:
#                 pygame.draw.polygon(screen, active_color, [(mouse[0] - 15, mouse[1] - 15),
#                                                            (mouse[0] - 15, mouse[1] + 35),
#                                                            (mouse[0] + 35, mouse[1] - 15)], 2)
#             elif active_figure == 4:
#                 size = 50
#                 triangle_height = size * math.sqrt(3) / 2
#                 vertex1 = (mouse[0], mouse[1] - triangle_height / 2)
#                 vertex2 = (mouse[0] - size / 2, mouse[1] + triangle_height / 2)
#                 vertex3 = (mouse[0] + size / 2, mouse[1] + triangle_height / 2)
#                 pygame.draw.polygon(screen, active_color, [vertex1, vertex2, vertex3], 2)
#             elif active_figure == 5:
#                 pygame.draw.polygon(screen, active_color, [(mouse[0] - 25, mouse[1]),
#                                                            (mouse[0], mouse[1] - 25),
#                                                            (mouse[0] + 25, mouse[1]),
#                                                            (mouse[0], mouse[1] + 25)], 2)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             for i in range(len(colors)):
#                 if colors[i].collidepoint(event.pos):
#                     active_color = rgbs[i]
#
#             for i in brushes:
#                 if i[0].collidepoint(event.pos):
#                     active_figure = i[1]
#
#     pygame.display.flip()
#
# pygame.quit()
import pygame  # Import the pygame library for graphics handling
import math  # Import the math library for mathematical operations

# Initialize pygame
pygame.init()

# Set frames per second
fps = 60

# Create a clock object to control the frame rate
timer = pygame.time.Clock()

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600

# Initialize variables for active figure and color
active_figure = 0
active_color = 'white'

# Create the screen with specified dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Set the caption of the window
pygame.display.set_caption("Paint")

# Initialize the list to store painting data
painting = []


# Function to draw the menu
def draw_menu(color):
    # Draw the background rectangle of the menu
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])

    # Draw a horizontal line to separate menu from canvas
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Draw the circle brush icon
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)

    # Draw the rectangle brush icon
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    # Draw the square brush icon
    square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
    pygame.draw.rect(screen, 'white', [135, 15, 40, 40], 2)

    # Draw the right triangle brush icon
    right_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
    pygame.draw.polygon(screen, 'white', [(195, 15), (195, 55), (235, 15)], 2)

    # Draw the equilateral triangle brush icon
    equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
    side_length = 50  # Side length of the square
    center_x = 250 + side_length / 2  # x-coordinate of the center of the square
    center_y = 10 + side_length / 2  # y-coordinate of the center of the square
    triangle_height = side_length * math.sqrt(3) / 2  # Height of the equilateral triangle

    # Reduce the triangle height slightly to make the triangle fit inside the square
    triangle_height *= 1

    # Vertices of the equilateral triangle
    vertex1 = (center_x, center_y - triangle_height / 2)
    vertex2 = (center_x - side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
    vertex3 = (center_x + side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)

    # Draw the equilateral triangle
    pygame.draw.polygon(screen, 'white', [vertex1, vertex2, vertex3], 2)

    # Draw the rhombus brush icon
    rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
    top_left = (310, 10)
    top_right = (360, 10)
    bottom_left = (310, 60)
    bottom_right = (360, 60)

    # Adjust the positions of the midpoints to decrease the size of the rhombus
    mid_top = ((top_left[0] + top_right[0]) // 2, (top_left[1] + top_right[1]) // 2 + 4)
    mid_left = ((top_left[0] + bottom_left[0]) // 2 + 4, (top_left[1] + bottom_left[1]) // 2)
    mid_bottom = ((bottom_left[0] + bottom_right[0]) // 2, (bottom_left[1] + bottom_right[1]) // 2 - 4)
    mid_right = ((top_right[0] + bottom_right[0]) // 2 - 4, (top_right[1] + bottom_right[1]) // 2)

    # Draw the rhombus
    pygame.draw.polygon(screen, 'white', [mid_top, mid_left, mid_bottom, mid_right], 2)

    # Create a list of brush icons
    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush,
                  rhombus_brush]

    # Draw the color palette
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Load the eraser icon and draw it
    eraser = pygame.image.load("media/eraser-square-svgrepo-com.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [WIDTH - 150, 7, 25, 25])

    # Draw color rectangles
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


# Function to draw the painting
def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):  # If the color is white
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 50])  # Draw a white rectangle
        else:
            if figure == 0:  # If the figure is a circle
                pygame.draw.circle(screen, color, pos, 20, 2)  # Draw a circle
            elif figure == 1:  # If the figure is a rectangle
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)  # Draw a rectangle
            elif figure == 2:  # If the figure is a square
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 35, 35], 2)  # Draw a square
            elif figure == 3:  # If the figure is a right triangle
                pygame.draw.polygon(screen, color, [(pos[0] - 15, pos[1] - 15),
                                                    (pos[0] - 15, pos[1] + 35),
                                                    (pos[0] + 35, pos[1] - 15)], 2)  # Draw a right triangle
            elif figure == 4:  # If the figure is an equilateral triangle
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (pos[0], pos[1] - triangle_height / 2)
                vertex2 = (pos[0] - size / 2, pos[1] + triangle_height / 2)
                vertex3 = (pos[0] + size / 2, pos[1] + triangle_height / 2)
                pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3], 2)  # Draw an equilateral triangle
            elif figure == 5:  # If the figure is a rhombus
                pygame.draw.polygon(screen, color, [(pos[0] - 25, pos[1]),
                                                    (pos[0], pos[1] - 25),
                                                    (pos[0] + 25, pos[1]),
                                                    (pos[0], pos[1] + 25)], 2)  # Draw a rhombus


# Main program loop
run = True
while run:
    # Control the frame rate
    timer.tick(fps)

    # Fill the screen with white color
    screen.fill("white")

    # Get the current mouse position
    mouse = pygame.mouse.get_pos()

    # Check if the left mouse button is pressed
    left_click = pygame.mouse.get_pressed()[0]

    # Draw the menu and get brush list, color rectangles, and RGB values
    brushes, colors, rgbs = draw_menu(active_color)

    # If left mouse button is pressed and the mouse is below the menu
    if left_click and mouse[1] > 85:
        # Append the painting data (color, position, figure) to the painting list
        painting.append((active_color, mouse, active_figure))

    # Draw the painting
    draw_painting(painting)

    # If the mouse is below the menu
    if mouse[1] > 85:
        # If the active color is white
        if active_color == (255, 255, 255):
            # Draw a white rectangle at the mouse position
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 50])
        else:
            # Depending on the active figure, draw the corresponding shape at the mouse position
            if active_figure == 0:  # Circle
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:  # Rectangle
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
            elif active_figure == 2:  # Square
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 35, 35], 2)
            elif active_figure == 3:  # Right triangle
                pygame.draw.polygon(screen, active_color, [(mouse[0] - 15, mouse[1] - 15),
                                                           (mouse[0] - 15, mouse[1] + 35),
                                                           (mouse[0] + 35, mouse[1] - 15)], 2)
            elif active_figure == 4:  # Equilateral triangle
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (mouse[0], mouse[1] - triangle_height / 2)
                vertex2 = (mouse[0] - size / 2, mouse[1] + triangle_height / 2)
                vertex3 = (mouse[0] + size / 2, mouse[1] + triangle_height / 2)
                pygame.draw.polygon(screen, active_color, [vertex1, vertex2, vertex3], 2)
            elif active_figure == 5:  # Rhombus
                pygame.draw.polygon(screen, active_color, [(mouse[0] - 25, mouse[1]),
                                                           (mouse[0], mouse[1] - 25),
                                                           (mouse[0] + 25, mouse[1]),
                                                           (mouse[0], mouse[1] + 25)], 2)

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button
            run = False  # Set run to False to exit the loop

        if event.type == pygame.MOUSEBUTTONDOWN:  # If the user presses a mouse button
            for i in range(len(colors)):  # Iterate over the color rectangles
                if colors[i].collidepoint(event.pos):  # If the mouse click is within the color rectangle
                    active_color = rgbs[i]  # Set the active color to the corresponding RGB value

            for i in brushes:  # Iterate over the brush icons
                if i[0].collidepoint(event.pos):  # If the mouse click is within the brush icon
                    active_figure = i[1]  # Set the active figure to the corresponding brush type

        # Update the display
        pygame.display.flip()

# Quit pygame
pygame.quit()


