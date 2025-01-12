# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:13:30 2025

@author: Suheda
"""

import subprocess
import shutil

def latex_to_word(latex_file, output_file):
    """
    Converts a LaTeX file into Word format (docx).
    
    Args:
        latex_file (str): Full file path of the LaTeX file to be converted.
        output_file (str): Full file path of the output Word document.
    
    Returns:
        None: The function does not return a value.
    """
    # Check if Pandoc is installed
    if not shutil.which("pandoc"):
        raise EnvironmentError("Pandoc is not installed. Please install Pandoc.")
    
    try:
        # Run the Pandoc command
        subprocess.run(
            ["pandoc", latex_file, "-o", output_file],
            check=True
        )
        print(f"Conversion completed: {output_file}")
    except subprocess.CalledProcessError as e:
        print("An error occurred during conversion:", e)

# Example usage
latex_file = "C:/Users/User/Desktop/simple.tex"  # Full path to the LaTeX file
output_file = "C:/Users/User/Desktop/simple.docx"  # Full path to the output Word file

# Call the function
latex_to_word(latex_file, output_file)
