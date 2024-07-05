# Avery 5160 Label Generator

This project generates 3x10 barcode labels (Avery 5160) from PDF barcode files. The application extracts barcode images from PDF files and places them on a label template, which is then saved as a new PDF.

## Features
- Extract barcode images from PDF files
- Generate Avery 5160 label templates
- Save the output as a PDF file

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YG-GIT94/avery-5160-label-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd avery-5160-label-generator
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python src/main.py
    ```
2. Select the barcode PDF files when prompted.
3. Choose the output directory for the generated label PDFs.

## Requirements

- Python 3.x
- PyMuPDF
- Pillow
- reportlab

## License

This project is licensed under the MIT License.
