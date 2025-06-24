from djitellopy import Tello
import time

# Initialize and connect
tello = Tello()
tello.connect()

print(f"Battery: {tello.get_battery()}%")

# Takeoff
tello.takeoff()
time.sleep(2)

# Fly in a square
for _ in range(4):
    tello.move_forward(50)
    tello.rotate_clockwise(90)
    time.sleep(1)

# Land
tello.land()
