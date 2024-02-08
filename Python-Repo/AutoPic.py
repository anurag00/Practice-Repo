from pynput import keyboard, mouse

# Flag to keep the loop running
running = True

def on_key_release(key):
    global running
    if key == keyboard.KeyCode.from_char('x'):
        # Stop the loop if 'X' is pressed
        running = False
    elif key == keyboard.KeyCode.from_char('d'):
        # Double-click the mouse and type 'D' followed by Enter if 'D' is pressed
        mouse.Controller().click(mouse.Button.left, 2)
        keyboard.Controller().type('\n')

# Start listening for key releases
with keyboard.Listener(on_release=on_key_release) as listener:
    # Run the loop until 'X' is pressed
    while running:
        pass

# Stop listening for key releases when the loop ends
listener.stop()
