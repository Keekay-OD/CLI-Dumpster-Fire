import os
import time
import random
import subprocess

def show_code():
    code_lines = [
        "def main():",
        "    print('Hello, World Domination!')",
        "",
        "if __name__ == '__main__':",
        "    main()",
        "",
        "def imdumb():",
        "    raise Exception('Welcome to the end of the world!')",
    ]
    
    print("\nCompiling your World Domination script...\n")
    for line in code_lines:
        print(line)
        time.sleep(0.5)  # simulating slow typing

def show_error_animation():
    # Display some sort of animation or error message
    print("\nCompiling...")
    time.sleep(1)
    
    # Simple animation loop
    for i in range(5):
        print("Compiling" + "." * (i % 3 + 1), end="\r")
        time.sleep(0.5)
    
    print("\n")
    print("Error: Something went wrong while compiling!")
    time.sleep(2)
    print("Error: Something went wrong again!")
    time.sleep(2)
    print("You might be ok...")
    time.sleep(2)
    print("EVERYTHING IS ON FIRE!!!")
    time.sleep(2)
    # Simulate small fire animation
    print("\n🔥🔥🔥🔥🔥")
    for i in range(10):  # Extend the fire animation to last a bit longer
        print("🔥" + "🔥" * random.randint(1, 5) + "💥" * random.randint(0, 2), end="\r")
        time.sleep(0.3)
    
    print("\n🔥🔥🔥🔥🔥")

def main():
    show_code()
    
    # Wait for user to type "compile"
    user_input = input("\nType 'compile' to compile the code: ")
    
    if user_input.lower() == "compile":
        show_error_animation()
        print("\nExecuting aafire for dramatic effect...\n")
        
        # Run `aafire` as a separate process
        subprocess.run(["aafire"])  # Ensure aafire is installed and accessible

if __name__ == "__main__":
    main()


# Run the script