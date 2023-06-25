import tkinter as tk
import pyautogui

def take_screenshot():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot as an image file
    screenshot.save('screenshot.png')

    print("Screenshot saved as screenshot.png")

# Create the Tkinter window
window = tk.Tk()
window.title("Screenshot App")

# Create the button
button = tk.Button(window, text="Take Screenshot", command=take_screenshot)
button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
