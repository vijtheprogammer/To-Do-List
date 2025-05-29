import time
import os
import platform

# Constants
SLEEP_TIME_SHORT = 0.75
SLEEP_TIME_LONG = 1

def loading_animation(duration=SLEEP_TIME_SHORT, dots=3):
    for _ in range(dots):
        print(".", end='', flush=True)
        time.sleep(SLEEP_TIME_LONG)

def view_tasks():
    flag = 0
    bad_counter = 0

    while True:
        try:
            time.sleep(0.8)
            filename = input("\nPlease specify a filename (or type exit to cancel). \nFile: ")

            last_four = filename[-4:]

            if (filename.lower() == "exit"):
                print("\n   Exiting the viewing screen.\n")
                loading_animation(SLEEP_TIME_SHORT, 3)
                break
            if not filename.lower().endswith(".txt"):
                print("\n   Please specify .txt files only.")
                
                bad_counter += 1
                print(f"   Invalid attempts: {bad_counter}/3")

                if (bad_counter == 3):
                    loading_animation(SLEEP_TIME_LONG, 3)
                    print("\n   Too many invalid attempts. \nExiting the View Task screen effective immediately.\n")
                    break
                
                continue

            else: 
                with open(filename, 'r') as file:
                    print("\nTasks")
                    print("-----\n")
                    # i is the line number and line is the content
                    for i, line in enumerate(file, start=1):
                        print(f"{i}. {line.strip()}")
                        time.sleep(0.8)
                    print()
                break
                    
        except FileNotFoundError:
            loading_animation(SLEEP_TIME_SHORT, 3)
            print("   \rError: File was not found or does not exist.\n")
            print("     Please add tasks first.\n")

def add_tasks():
    bad_counter = 0

    while True:
        output_file = input("\nPlease specify the .txt file below\nFile name: ")
        last_four = output_file[-4:]

        try:

            if not output_file.lower().endswith(".txt"):
                print("\n   Please specify .txt files only.")

                bad_counter += 1
                print(f"    Invalid attempts: {bad_counter}/3")

                if (bad_counter == 3):
                    loading_animation(SLEEP_TIME_LONG, 3)
                    print("\r")
                    print("\n   Too many invalid attempts. \nExiting the Add Task screen effective immediately.\n")
                    break
                continue
            with open(output_file, 'a') as file:
                loading_animation(SLEEP_TIME_SHORT, 3)
                print()
                print("\rPlease enter one task per line. Press 'q' to quit.")

                while True:
                    task = input("Task: ")
                    if (task.lower() == 'q'):
                        time.sleep(0.8)
                        print("\nAll tasks have been written successfully!\n")
                        return
                    
                    file.write(task + "\n")
                    
        except FileNotFoundError:
            loading_animation(SLEEP_TIME_SHORT, 3)
            print("\r   Error: File was not found or does not exist.\n")

def delete_tasks():
    bad_counter = 0

    while True:
        filename = input("\nPlease specify the .txt file to delete from (or type exit to cancel).\nFile: ").strip()

        if filename.lower() == "exit":
            print("\n   Exiting the Delete Task screen.\n")
            loading_animation(SLEEP_TIME_SHORT, 3)
            return
        
        if not filename.endswith(".txt"):
            bad_counter += 1
            print("\n   Please specify .txt files only.")
            print(f"   Invalid attempts: {bad_counter}/3")

            if bad_counter == 3:
                loading_animation(SLEEP_TIME_LONG, 3)
                print("\n   Too many invalid attempts. Exiting Delete Task screen.\n")
                return
            continue

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            if not lines:
                print("\n   The file is empty. Nothing to delete.\n")
                return

            print("\nTasks")
            print("-----\n")
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")

            try:
                task_to_delete = int(input("\nEnter the number of the task you want to delete: "))
            except ValueError:
                print("\n   Invalid input. Task number must be an integer.\n")
                return

            if task_to_delete < 1 or task_to_delete > len(lines):
                print("\n   Task number is out of range.\n")
                return

            del lines[task_to_delete - 1]

            with open(filename, 'w') as file:
                file.writelines(lines)

            print(f"\nTask {task_to_delete} has been deleted.\n")
            return

        except FileNotFoundError:
            print("\n   File not found. Please try again.\n")


def exit_tasks():
    print("\nShutting down")
    print("---------------\n")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1.2)
    print("1")
    time.sleep(1.5)
    print("\nThank you for using the To-Do List!")
    clear_terminal()


def decision(choice):
    if (choice == 1):
        view_tasks()
    elif (choice == 2):
        add_tasks()
    elif (choice == 3):
        delete_tasks()
    else:
        print("\n   Invalid choice. Please enter a number between 1 and 4.\n")

def clear_terminal():
    input("\nPress Enter to clear the terminal")

    # Check the operating system and clear accordingly
    current_os = platform.system().lower()
    
    if current_os == "windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux or macOS


def main():
    bad_counter = 0

    print("\nWelcome to your To-Do List!")
    print("---------------------------\n")
    loading_animation(SLEEP_TIME_SHORT, 3)

    while True:    
        print("\rPlease select an option:\n")
        try: 
            choice = int(input("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit\n\n"))

            if choice == 4:
                exit_tasks()
                break

            decision(choice)
            bad_counter = 0
        except ValueError:
            loading_animation(SLEEP_TIME_SHORT, 3)
            bad_counter += 1

            print("    \n\n")
            print("    Please only enter integer values.")
            print(f"    Invalid attempts: {bad_counter}/3")

            if bad_counter == 3:
                loading_animation(0.5, 3)
                print("\nToo many invalid attempts. Exiting program.\n")
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting gracefully.\n")
        time.sleep(1)
