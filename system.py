import random as rnd  # Alias module name for convenience
from datetime import datetime  # Import specific class from module

global task_counter  # Track task IDs globally
task_counter = 0

class Task:
    """Represents a task in the system."""
    def __init__(self, title: str):
        global task_counter  # Modify global counter
        self.id = task_counter
        task_counter += 1
        self.title = title
        self.completed = False
        self.timestamp = datetime.now()  # Store creation timestamp
    
    def mark_completed(self):
        """Marks task as completed."""
        self.completed = True

    def __str__(self):
        """String representation of the task."""
        return f"[{self.id}] {self.title} | Done: {self.completed} | Created: {self.timestamp}" 


def task_manager():
    """Menu-driven task manager."""
    tasks = []
    
    while True:  # Loop until exit
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Task title: ")
            tasks.append(Task(title))  # Add task
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue  # Skip rest of loop
            
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            
            try:
                index = int(input("Task number to complete: ")) - 1
                assert 0 <= index < len(tasks), "Invalid choice!"
                tasks[index].mark_completed()
            except (ValueError, AssertionError) as e:
                print(f"Error: {e}")
        elif choice == "3":
            if not tasks:
                print("No tasks available.")
            else:
                for task in tasks:
                    print(task)
        elif choice == "4":
            if not tasks:
                print("No tasks to delete.")
                pass  # Placeholder
            else:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
                
                try:
                    index = int(input("Task number to delete: ")) - 1
                    assert 0 <= index < len(tasks), "Invalid choice!"
                    del tasks[index]  # Delete task
                    print("Task deleted.")
                except (ValueError, AssertionError) as e:
                    print(f"Error: {e}")
        elif choice == "5":
            print("Exiting...")
            break  # Exit loop
        else:
            print("Invalid input! Try again.")


def check_none(value):
    """Check if value is None."""
    return "None detected" if value is None else "Value exists"


def divide(a, b):
    """Safe division with error handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        raise ValueError("Division by zero!")  # Raise exception
    else:
        return result or None  # Return None if result is 0


def generator_example():
    """Generate numbers using yield."""
    for i in range(3):
        yield i  # Generator function


def use_lambda():
    """Lambda function for squaring numbers."""
    square = lambda x: x * x  # Define lambda function
    return square(5)


if __name__ == "__main__":
    try:
        with open("log.txt", "w") as file:  # Auto-handle file
            file.write("Task Manager Log\n")
        
        task_manager()
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Goodbye!")  # Always executes
