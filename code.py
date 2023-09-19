import board
import time
import neopixel

# Define the RGB LED parameters
pixel_pin = board.NEOPIXEL  # Use the built-in RGB LED
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False)

# Define the colors and their durations
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

blink_duration = 0.5  # Duration of each blink in seconds
pause_duration = 0.2  # Duration between sets of blinks in seconds

num_blinks_red = 17
num_blinks_green = 17
num_blinks_yellow = 17
num_blinks_blue = 17

# Main animation loop
while True:
    for _ in range(num_blinks_red):
        pixels.fill(RED)
        pixels.show()
        time.sleep(blink_duration)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(blink_duration)

    time.sleep(pause_duration)

    for _ in range(num_blinks_green):
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(blink_duration)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(blink_duration)

    time.sleep(pause_duration)

    for _ in range(num_blinks_yellow):
        pixels.fill(YELLOW)
        pixels.show()
        time.sleep(blink_duration)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(blink_duration)

    time.sleep(pause_duration)

    for _ in range(num_blinks_blue):
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(blink_duration)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(blink_duration)

    time.sleep(pause_duration)

# The animation will loop indefinitely


