"""
METACLEAN uses exiftool and qpdf to remove metadata permanently and unrecoverable.
"""

import argparse
import subprocess
import os


def remove_pdf_metadata(input_output_pdf: str):
    try:
        # step 1: remove metadata and create temporary workcopy of input pdf file with exiftool
        temp_pdf = "temp.pdf"
        print(f"Remove metadate from {input_output_pdf} with exiftool...")
        exiftool_command = ["exiftool", "-all=", input_output_pdf, "-o", temp_pdf]
        subprocess.run(exiftool_command, check=True)
        print("Metadata removed sucessfully.")

        # step 2: restructure data and save pdf with originally name
        print(f"Restructure {input_output_pdf} with qpdf...")
        qpdf_command = ["qpdf", "--linearize", temp_pdf, input_output_pdf]
        subprocess.run(qpdf_command, check=True)
        print(f"PDF sucessfully reconstructured.")

        # step 3: remove temporary file
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
            print(f"Temporary file {temp_pdf} removed.")

    except subprocess.CalledProcessError as e:
        print(f"An error has occured: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Remove metadata from pdf files permanently and unrecoverable.")
    
    parser.add_argument("input_output_pdf", help="path to input-pdf")
    
    args = parser.parse_args()

    remove_pdf_metadata(args.input_output_pdf)

if __name__ == "__main__":
    main()