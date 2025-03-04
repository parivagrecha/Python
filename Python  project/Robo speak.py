# Project of robo speak
import os
print("Welcome to Robospeak by Pari")
while True:
    x = input("Enter what you want to speak: ")
    if x == "q":
        break
    # Command to use PowerShell to speak the text using Windows Speech API
    command = f"powershell {x}"
    os.system(command)
