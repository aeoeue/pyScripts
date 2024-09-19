import json
import time
from pynput.mouse import Button, Controller

mouse = Controller()

def load_clicks(filename='clicks.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def replay_clicks(clicks, repeat=5, delay=0.1):
    for _ in range(repeat):
        for click in clicks:
            x, y = click['x'], click['y']
            button = Button.left if 'Button.left' in click['button'] else Button.right
            mouse.position = (x, y)
            mouse.click(button)
            time.sleep(delay)  # Add a delay between clicks if needed

if __name__ == "__main__":
    clicks = load_clicks()
    repeat_count = int(input("How many times should the clicks be repeated? "))
    replay_clicks(clicks, repeat=repeat_count)
