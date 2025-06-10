"""
Terminal UI for pycite program

Communicate to the user through the terminal

Author: Sabrina Sandy 
Date: March 7, 2025
"""

#Library imports
import os
import errno

class View:

    """
    Shows a message to our user
    ! static so it can be used everywhere
    
    Args:
        message: whatever we're displaying to the user
    """
    @staticmethod
    def show_message(message):
        print(message)

    """
    Prompt user to provide a filepath to their CSV file
    
        
    Returns:
        input: ask for file path
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    @staticmethod
    def get_file_input():
        print("Left click and copy your .csv file to easily get the filepath! \n")
        return input("Select a CSV file to upload: ")
    

    
    """
    Prompt user to choose which citation they'd like to create
    
        
    Returns:
        input: ask for choice of citation
        
    """
    @property
    def chooseCitation(self):
        return input("Enter your choice: ").strip()
    
    def citationOptions():
        print("What sort of citation would you like to create?: ")
        print()
        print("(1) MLA Citation \n")
        print("(2) APA Citation \n")
        print("(3) Chicago Citation \n")
        print("(4) All Citations \n")





