# latex_to_word

This repository contains a Python script for converting LaTeX files (.tex) into Word documents (.docx) using [Pandoc](https://pandoc.org/). The script allows users to easily convert LaTeX files into a format compatible with word processing software, making it easier to share and collaborate.

## Requirements

- [Python 3.x](https://www.python.org/)
- [Pandoc](https://pandoc.org/installing.html) (must be installed and accessible from the command line)

## Installation

1. **Install Pandoc**:  
   If you don’t have Pandoc installed, follow the instructions on the official website [Pandoc Installation Guide](https://pandoc.org/installing.html).

2. **Clone the Repository**:  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/latex_to_word.git
   
3. **Install Python Dependencies**:
   You can install the required Python libraries using pip:
   ```bash
   pip install subprocess shutil
 

**Usage**
Prepare your LaTeX file:
Make sure the LaTeX file you want to convert is available and contains valid LaTeX syntax.

**Run the Script**:
In the script, specify the path to your LaTeX file and the desired output path for the Word document.
Example:

   
    latex_file = "path/to/your/file.tex"
    output_file = "path/to/your/output.docx"
    latex_to_word(latex_file, output_file)

**Conversion Process**:
The script will run the Pandoc command to convert the LaTeX file into a Word document and save it to the specified output location.

Example
Here’s an example of using the script:

    
    latex_file = "C:/Users/User/Desktop/example.tex"
    output_file = "C:/Users/User/Desktop/example.docx"
    latex_to_word(latex_file, output_file)

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
