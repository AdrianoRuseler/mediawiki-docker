import requests
import os

import random
import string
import secrets

def custom_password(length=16):
    #allowed_chars = string.ascii_letters + string.digits + "!@#%^&*()-_=+[]{}<>?"
    allowed_chars = string.ascii_letters + string.digits + "@#%&?"
    return ''.join(random.choices(allowed_chars, k=length))
def generate_env_file(filename='.env'):
    """Generate a .env file with random credentials using custom_password."""
    # Generate random values
    mariadb_password = custom_password()  # Custom password function
    mariadb_root_password = custom_password() 

    # Content for .env file
    env_content = f"""MARIADB_PASSWORD={mariadb_password}
MARIADB_ROOT_PASSWORD={mariadb_root_password}
"""

    # Write to .env file
    try:
        with open(filename, 'w', newline='\n') as f:
            f.write(env_content)
        print(f"Successfully created {filename} with random credentials:")
        print("-" * 50)
        print(env_content)
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
 
def display_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print("\nCurrent file contents:")
            print(file.read())
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

def read_env_file_manual(filename='.env'):
    """Manually read and parse the .env file without dependencies."""
    env_vars = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Skip empty lines or comments
                line = line.strip()
                if line and not line.startswith('#'):
                    # Split on the first '=' only
                    if '=' in line:
                        key, value = line.split('=', 1)
                        env_vars[key] = value
        
        # Print the variables
        print(f"Successfully read {filename}:")
        print("-" * 50)
        for key, value in env_vars.items():
            print(f"{key}={value}")
        
        return env_vars
    
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None
        
if __name__ == "__main__":    
    generate_env_file()
    env_vars = read_env_file_manual()
    if env_vars:
        # Example: Access a specific variable
        print("\nExample usage:")
        print(f"Moodle admin password: {env_vars['MOODLE_PASSWORD']}")
              
        # Display the final file contents
        display_file_contents(output_filename)
    