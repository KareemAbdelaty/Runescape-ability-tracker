from pynput import keyboard
from AbilityTracker import *
from SaveManager import *
from WindowManager import *


def execute():
    print('hotkey')
    

def on_press(key):
    print(key)
    if any([key in COMBO for COMBO in COMBINATIONS]) and not key in current:
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
    try:
        if key.char in bar.getKeys():
            app.showImg("abilityImages\Corruption_Shot.png")
        else:
            app.showImg("abilityImages/noImg.png")
    except AttributeError as e:
        if key == keyboard.Key.f1:
            app.showImg("abilityImages\Onslaught.png")
        else:
            app.showImg("abilityImages/noImg.png")
def on_release(key):
    if key == keyboard.Key.esc:
    # Stop listener
        return False
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.discard(key)
bar = actionbar()
bar.addKeybind("k" , "onslought")
bar.addKeybind("F1" , "corruption")
keybar = {}
current = set()
COMBINATIONS =[{keyboard.Key.ctrl_l, keyboard.KeyCode(char ='r')}, {keyboard.Key.alt_l, keyboard.KeyCode(char ='r')},{keyboard.Key.alt_r, keyboard.KeyCode(char ='r')},{keyboard.Key.shift, keyboard.KeyCode(char ='r')}]
app2 = WindowManager()
#app2.overrideredirect(1)
app = app2.frames[AbilityTracker]
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
app.mainloop()
