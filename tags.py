import subprocess
import time

# Default tags with their initial state
DEFAULT_TAGS = {
    "Red": False,
    "Orange": False,
    "Blue": False,
    "Green": False,
    "Purple": False,
    "Gray": False,
    "Home": False,
    "Important": False,
    "Work": False,
}

TAG_COMMAND = "tag"  # The command-line tool used for tagging


# Retrieve all tags usage
def get_tags_all():
    # Command to retrieve all tags used in the user's home directory
    command = [TAG_COMMAND, "-u", "~"]

    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, text=True)

        # Split the output into lines
        lines = output.strip().split("\n")

        # Initialize a dictionary with default tags and their initial state
        all_tags = DEFAULT_TAGS.copy()

        # Update the state of each tag based on the command output
        for line in lines:
            _, tag_name = line.split(None, 1)
            all_tags[tag_name.strip()] = False

        return all_tags

    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        return DEFAULT_TAGS


# Get tags associated with a file
def get_tags_file(file_path):
    # Command to retrieve tags associated with a specific file
    command = [TAG_COMMAND, "-l", str(file_path)]

    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, text=True)

        # Split the output into parts
        parts = output.strip().split("\t", 1)

        tags_list = []

        # If there are tags associated with the file, extract and return them
        if len(parts) >= 2:
            tags_part = parts[1]
            tags_list = tags_part.split(",")

        return tags_list

    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        return []


# Run a tagging command for a given tag and file
def run_tag_command(command, tag, file_path):
    full_command = [TAG_COMMAND, command, str(tag), str(file_path)]

    try:
        # Execute the tagging command
        subprocess.run(full_command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


# Add a new tag to a file
def add_tag(tag, file_path):
    run_tag_command("-a", tag, file_path)


# Remove a tag from a file
def remove_tag(tag, file_path):
    run_tag_command("-r", tag, file_path)


# Check for updates on a specific tag associated with a file
def check_update(new_tag, file_path):
    wait = True

    while wait:
        # Get the list of tags associated with the file and all tags in the home directory
        file_tags = get_tags_file(file_path)
        all_tags = get_tags_all()

        # Check if the new tag exists in both the file tags and all tags
        if new_tag in file_tags and new_tag in all_tags:
            wait = False
        else:
            # Wait for a short duration before checking again
            time.sleep(1)
