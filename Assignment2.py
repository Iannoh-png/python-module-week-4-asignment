def read_file_safely(filename):
    """
    Reads a file and handles potential errors.

    Args:
        filename (str): The name of the file to read.
    """
    try:
        # Attempt to open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read the entire contents of the file
            content = file.read()
            # Print the file content
            print(f"Content of '{filename}':\n{content}")
    # Handle the specific error when the file is not found
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    # Handle general input/output errors (e.g., file cannot be read)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
    # Handle any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to get filename from user and read the file safely.
    """
    # Get the filename from the user
    filename = input("Enter the name of the file to read: ")
    # Call the function to read the file and handle errors
    read_file_safely(filename)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
