import pyautogui
import time
import random
import win32gui
import win32con

def move_windows():
    """Move random windows around."""
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            # Get the window title
            title = win32gui.GetWindowText(hwnd)
            if title:
                # Move the window to a random position
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                win32gui.MoveWindow(hwnd, x, y, 400, 300, True)

    win32gui.EnumWindows(callback, None)

def random_mouse_movement():
    """Move the mouse to random locations."""
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=0.2)

def annoying_message_box():
    """Display random annoying message boxes."""
    import ctypes
    messages = [
        "Something went wrong!",
        "Oops! Try again!",
        "Your system is haunted!",
        "Random Error 404!"
    ]
    ctypes.windll.user32.MessageBoxW(0, random.choice(messages), "Annoying Message", 0)

# Main function to run the chaos
def create_chaos():
    try:
        while True:
            move_windows()
            random_mouse_movement()
            if random.randint(0, 5) == 0:  # Occasionally show a message box
                annoying_message_box()
            time.sleep(0.5)  # Add a small delay
    except KeyboardInterrupt:
        print("Chaos stopped. You're welcome!")

if __name__ == "__main__":
    create_chaos()