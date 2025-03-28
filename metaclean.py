"""
METACLEAN - a program that removes metadata permanently and unrecoverable using ExifTool and QPDF.
"""

import argparse
import subprocess
import os


def remove_pdf_metadata(target_file: str) -> None:
    """
    1) Removes all metadata from a PDF file and creates a temporary workcopy of it with `ExifTool`
    2) Restructures the data of the workcopy with the process of Linearization, so the data cannot be restored, and saves it under the original name with `QPDF`.
    3) Removes the temporary workcopy.

    Args:
        target_file (str): The file path to the input PDF file, which will be overwritten
                                with the metadata-free version.

    Raises:
        subprocess.CalledProcessError: If an error occurs while running `ExifTool` or `QPDF`.
        Exception: For other unexpected errors during the process.
    """
    try:
        temp_pdf = "temp.pdf"
        print(f"Remove metadate from {target_file} with ExifTool...")
        exiftool_command = ["exiftool", "-all=", target_file, "-o", temp_pdf]
        subprocess.run(exiftool_command, check=True)
        print("Metadata removed sucessfully.")
        #consideration: write temporary files to /tmp/<filename> (directory that exists in all linux/*nix based OSes) since this directory will be cleaned when powercycling a machine, e.g. server, laptop, etc.

        print(f"Restructure {target_file} with QPDF...")
        qpdf_command = ["qpdf", "--linearize", temp_pdf, target_file]
        subprocess.run(qpdf_command, check=True)
        print(f"PDF sucessfully reconstructured.")

        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
            print(f"Temporary file {temp_pdf} removed.")

    except subprocess.CalledProcessError as e:
        print(f"An error has occured: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """
    The main function of the script. It handles command-line input, validates arguments,
    and initiates the process to remove metadata from a specified PDF file.

    This function uses the argparse library to parse a single command-line argument,
    which specifies the path to the input/output PDF file. The specified file is
    processed by the `remove_pdf_metadata` function, which ensures that all metadata
    is irreversibly removed and the file is reconstructed in a secure and compact format.

    Steps:
        1. Parses the command-line argument to retrieve the file path.
        2. Passes the file path to the `remove_pdf_metadata` function.
        3. Handles any exceptions or errors that occur during execution and displays
           relevant messages to the user.

    Usage:
        Run this script from the command line with the file path as an argument.
        Example: `python metaclean.py example.pdf`

    Raises:
        SystemExit: If invalid arguments are provided (e.g., missing or incorrect path)
                    or if the script encounters critical issues that prevent execution.
    """
    parser = argparse.ArgumentParser(description="Remove metadata from pdf files permanently and unrecoverable.")
    
    parser.add_argument("target_file", help="Path to input PDF file")
    
    args = parser.parse_args()

    remove_pdf_metadata(args.target_file)

if __name__ == "__main__":
    main()