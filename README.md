# METACLEAN

A program that **removes metadata permanently and unrecoverable** using **ExifTool** and **QPDF**.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

## Table of Contents

1. [Technologies](#technologies)
1. [Getting Started](#getting-started)
1. [Usage](#usage)
   * [Program Options](#program-options)
   * [Program Flow](#program-flow)
   * [Example Run](#example-run)  

## Technologies

* **Python** 3.12.2
  * **argparse, subprocess, os**
* **ExifTool** 12.76 [More Information](https://exiftool.org/)
  * It is a command-line application used for reading, writing and editing metadata in various file formats, including images, videos, PDFs and more.
* **QPDF** 11.9.1 [More Information](https://qpdf.readthedocs.io/en/stable/overview.html)
  * It is a command-line tool and library used for processing and transforming PDF files. It is not a PDF viewer or editor, but rather a utility to perform structural changes and optimizations on PDFs.

## Getting Started

0) [Fork](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the project to your namespace, if you want to make changes or open a [Pull Request](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project to your platform if you just want to use it:

    ```bash
    git clone git@github.com:SarahZimmermann-Schmutzler/metaclean.git
    ```

1. Install the programs **ExifTool** and **QPDF** if you haven't already:

    * Linux/Ubuntu:

        ```bash
        sudo apt update && apt upgrade
        sudo apt install libimage-exiftool-perl qpdf
        ```

    * Windows:
      * [Download](https://exiftool.org/) ExifTool
      * [Download](https://github.com/qpdf/qpdf/releases/) QPDF

## Usage

* For the further commands navigate to the directory you cloned **metaclean** into.

### Program Options

* To see all available **program options** have a look in the `help-section`:

    ```bash
    python metaclean.py -h
    # or
    python metaclean.py --help
    ```

  | Option (Long) | Short | Description | Required? |
  | ------------- | ----- | ----------- | --------- |
  | --help | -h | Get a list of the **available options** | no |
  | target_file |  | Path to **input PDF file** | yes |
  
### Program Flow

* Removes all metadata from a PDF file and creates a temporary workcopy of it with **ExifTool**.
* Restructures the data of the workcopy and saves it under the original name with **QPDF**. The feature used here is `Linearization`. While its primary purpose is to optimize for web viewing, it has a beneficial side effect: it removes or overwrites residual or fragmented data in the PDF file, including metadata - so this data cannot be restored.
* Removes the temporary workcopy.
* The input PDF file is now overwritten. The critical metadata is removed and because of the linearization process it cannot be restored.

### Example Run

* To remove the metadata of a PDF file unrecoverable use the following command:  

    ```bash
    python metaclean.py "C:\Users\MyName\DeveloperAkademie\test.pdf"
    ```

- It will yield the following **output**:  

    ```bash
    Remove metadate from test.pdf with ExifTool...
    Metadata removed sucessfully.
    Restructure test.pdf with QPDF...
    PDF sucessfully reconstructured.
    Temporary file temp.pdf removed.
    ```
