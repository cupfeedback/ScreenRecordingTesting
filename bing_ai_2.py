import tkinter as tk
from pynput import mouse, keyboard
import json

# Initialize the lists to store the recorded events
mouse_events = []
keyboard_events = []

# Define the functions to handle mouse events
def on_move(x, y):
    mouse_events.append(('move', x, y))

def on_click(x, y, button, pressed):
    mouse_events.append(('click', x, y, str(button), pressed))

def on_scroll(x, y, dx, dy):
    mouse_events.append(('scroll', x, y, dx, dy))

# Define the function to handle keyboard events
def on_press(key):
    keyboard_events.append(('press', str(key)))

def on_release(key):
    keyboard_events.append(('release', str(key)))

# Create the main window
root = tk.Tk()
root.geometry('400x200')

# Create a button to start/stop recording
recording = False
def toggle_recording():
    global recording
    recording = not recording
    if recording:
        record_button.config(text="Stop Recording")
        # Start the mouse and keyboard listeners
        mouse_listener.start()
        keyboard_listener.start()
    else:
        record_button.config(text="Start Recording")
        # Stop the mouse and keyboard listeners
        mouse_listener.stop()
        keyboard_listener.stop()

record_button = tk.Button(root, text="Start Recording", command=toggle_recording)
record_button.pack()

# Create a button to save the recorded events to a file
def save_events():
    with open('events.json', 'w') as f:
        json.dump({'mouse': mouse_events, 'keyboard': keyboard_events}, f)

save_button = tk.Button(root, text="Save Events", command=save_events)
save_button.pack()

# Create the mouse and keyboard listeners
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Run the main loop
root.mainloop()