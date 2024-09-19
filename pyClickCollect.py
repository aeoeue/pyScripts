import json
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

clicks = []
stop_flag = False

def on_click(x, y, button, pressed):
    global stop_flag
    if pressed and not stop_flag:
        # Record the click's position and button
        clicks.append({'x': x, 'y': y, 'button': str(button)})
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def on_press(key):
    global stop_flag
    if key == Key.esc:
        stop_flag = True
        return False  # Stop the keyboard listener

def save_clicks(filename='clicks.json'):
    with open(filename, 'w') as file:
        json.dump(clicks, file, indent=4)
        print(f"Clicks saved to {filename}")

def start_tracking():
    global stop_flag

    # Start the mouse and keyboard listeners
    with MouseListener(on_click=on_click) as mouse_listener, \
         KeyboardListener(on_press=on_press) as keyboard_listener:
        print("Tracking mouse clicks. Press 'Esc' to stop.")
        keyboard_listener.join()  # Wait for Esc key press to stop the listener
        stop_flag = True  # Stop the mouse listener after the Esc key is pressed
        mouse_listener.stop()  # Manually stop the mouse listener

if __name__ == "__main__":
    start_tracking()
    save_clicks()
