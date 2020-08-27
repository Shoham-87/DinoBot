import pyautogui
import PIL
import time
# Typing from Keyboard
def typing(keyvalue):
    pyautogui.keyDown(keyvalue)
#jumping of obstacle detection
def obstacle(data):
    for i in range(340,520):
        for j in range(670,720):
            if data[i,j] > 157:
                return "up"
    for i in range(530,580):
        for j in range(580,610):
            if data[i,j] > 157:
                return "down"
    return False

if __name__ == "__main__":
    time.sleep(2)
    # Bot LOOP
    while True:
        image=PIL.ImageGrab.grab().convert('L')
        data=image.load()
        if obstacle(data) == "up":
            typing("up")
        elif obstacle(data) == "down":
            typing("down")
            