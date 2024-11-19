# METACLEAN

A program that removes metadata permanently and unrecoverable using **ExifTool** and **QPDF**.    

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

It was coded on **Windows 10** using **VSCode** as code editor.

## Table of Contents
1. <a href="#technologies">Technologies</a>  
2. <a href="#features">Features</a>  
3. <a href="#getting-started">Getting Started</a>  
4. <a href="#usage">Usage</a>  
5. <a href="#additional-notes">Additional Notes</a>  

## Technologies
* **Python** 3.12.2
    * **argparse, subprocess, os** (modules from standard library)
* **ExifTool** 12.76 (<a href="https://exiftool.org/">More Information</a>)
* **QPDF** 11.9.1 (<a href="https://qpdf.readthedocs.io/en/stable/overview.html">More Information</a>) 

## Features
The following table shows which functions **Metaclean** supports:  

| Flag | Description | Required |
| ---- | ----------- | -------- |
| -h <br> --help | Get a list of the available options | no |
| input_output_pdf | Path to input/output PDF file | positional argument |

**Flow of the Program**
- Removes all metadata from a PDF file and creates a temporary workcopy of it with **ExifTool**.
    - **ExifTool** is a command-line application used for reading, writing and editing metadata in various file formats, including images, videos, PDFs and more.
-  Restructures the data of the workcopy and saves it under the original name with **QPDF**. The feature used here is `Linearization`. While its primary purpose is to optimize for web viewing, it has a beneficial side effect: it removes or overwrites residual or fragmented data in the PDF file, including metadata - so this data cannot be restored. 
    - **QPDF** is a command-line tool and library used for processing and transforming PDF files. It is not a PDF viewer or editor, but rather a utility to perform structural changes and optimizations on PDFs.
- Removes the temporary workcopy.

## Getting Started
0) <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">Fork</a> the project to your namespace, if you want to make changes or open a <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">Pull Request</a>.

1) <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">Clone</a> the project to your platform if you just want to use the program.
    - <ins>Example</ins>: Clone the repo e.g. using an SSH-Key:  
    ```bash
    git clone git@github.com:SarahZimmermann-Schmutzler/metaclean.git
    ```

2) Install the programs **ExifTool** and **QPDF** if you haven't already:
    - Linux/Ubuntu:
        ```bash
        sudo apt update && apt upgrade
        sudo apt install libimage-exiftool-perl qpdf
        ```
    - Windows:
        - Download ExifTool <a href="https://exiftool.org/">Take a look here</a>
        - Download QPDF <a href="https://github.com/qpdf/qpdf/releases/">Take a look here</a>

## Usage
- Make sure you are in the folder where you cloned **Metaclean** into.  

- Help! What options does the program support!?  
    ```bash
    python metaclean.py -h
    # or
    python metaclean.py --help
    ```  

- To remove the metadata of a PDF file unrecoverable use the following command in your terminal:  
    ```bash
    python metaclean.py [path/to/pdf or pdf]
    ```  
    - <ins>Example</ins>: The PDF file is in the current directory:  
        ```bash
        python metaclean.py test.pdf
        ```
    - <ins>Example</ins>: The PDF file is in another directory:  
        ```bash
        python metaclean.py "C:\Users\MyName\DeveloperAkademie\test.pdf"
        ```

- What you see in the terminal, if the removal was succesful:  
    ```
    Remove metadate from test.pdf with ExifTool...
    Metadata removed sucessfully.
    Restructure test.pdf with QPDF...
    PDF sucessfully reconstructured.
    Temporary file temp.pdf removed.
    ```
- The input PDF file is now overwritten. The critical metadata is removed and because of the linearization process it cannot be restored.

## Additional Notes
The **argparse** module is used to parse (read) command line arguments in Python programs. It allows to define arguments and options that can be passed to the program when starting it from the command line. These are then processed and are available in the program as variables.  
  
**Subprocess** is a Python module that allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It is used for interacting with external commands or programs from within your Python script. For example, you can use subprocess to run shell commands or external scripts, capture the output or handle the input of these commands and check the exit status of the executed commands to ensure they ran successfully.
  
The **os** module in Python is part of the standard library and provides functions to interact with the operating system. It allows you to perform tasks like working with files and directories, interacting with the environment, and managing processes. Key features include Functions to create, delete, and navigate files and directories, access and modify environment variables, Work with file paths and execute and manage system processes.  
  
**ChatGPT** was involved in the creation of the program (Debugging, Prompt Engineering etc.).  
  
I use **Google Translate** for translations from German into English.