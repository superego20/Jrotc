from djitellopy import Tello
import pygame
import time

# Initialize Pygame and the Tello drone
pygame.init()
pygame.display.set_mode((400, 300))  # Required for key detection

tello = Tello()
tello.connect()

print(f"Battery: {tello.get_battery()}%")

# Take off flag
is_flying = False

# Set speed in cm
SPEED = 50

# Control loop
running = True
print("Press T to take off, L to land, ESC to quit.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press events
        elif event.type == pygame.KEYDOWN:
            key = event.key

            if key == pygame.K_ESCAPE:
                running = False

            elif key == pygame.K_t:  # Takeoff
                tello.takeoff()
                is_flying = True

            elif key == pygame.K_l:  # Land
                tello.land()
                is_flying = False

            elif is_flying:
                if key == pygame.K_UP:
                    tello.move_forward(SPEED)
                elif key == pygame.K_DOWN:
                    tello.move_back(SPEED)
                elif key == pygame.K_LEFT:
                    tello.move_left(SPEED)
                elif key == pygame.K_RIGHT:
                    tello.move_right(SPEED)
                elif key == pygame.K_w:
                    tello.move_up(SPEED)
                elif key == pygame.K_s:
                    tello.move_down(SPEED)
                elif key == pygame.K_a:
                    tello.rotate_counter_clockwise(45)
                elif key == pygame.K_d:
                    tello.rotate_clockwise(45)

pygame.quit()
