import logging  # Import the logging module to log errors
import os  # Import the os module to interact with the operating system

# Step 1: Get the path to the user's desktop dynamically
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Step 2: Define the full path for the log file (saved as error_log.txt on the desktop)
log_file_path = os.path.join(desktop_path, "error_log.txt")

# Step 3: Configure the logging system
logging.basicConfig(
    filename=log_file_path,  # Save logs in the specified file
    level=logging.ERROR,  # Log only ERROR level messages and above
    format="%(asctime)s - %(levelname)s - %(message)s"  # Define log message format
)

def divide_numbers(a, b):
    """
    Function to perform division and handle ZeroDivisionError.

    Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float: The result of division if successful, None if an error occurs.
    """
    try:
        result = a / b  # Attempt division
        return result  # Return result if no exception occurs
    except ZeroDivisionError as e:
        # Step 4: Log the error with details
        logging.error(f"ZeroDivisionError: Attempted to divide {a} by zero.")

        # Step 5: Provide user-friendly feedback
        print("An error occurred! Check the log file on your desktop.")

        return None  # Return None to indicate failure

# Step 6: Test the function by intentionally triggering a ZeroDivisionError
divide_numbers(10, 7)

# Step 7: Inform the user where the log file is saved
print(f"Error log saved at: {log_file_path}")
