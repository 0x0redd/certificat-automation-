Certificate Generator App

This application is a desktop tool for generating personalized certificates using a background image and custom fonts for the name and code fields. It utilizes the Tkinter library for the GUI, PIL for image handling, and ReportLab for PDF generation.
Features

    Select Names JSON File: Choose a JSON file containing names and codes.
    Select Background Image: Choose a background image in PNG format.
    Select Fonts: Choose custom fonts for the name and code.
    Generate Certificates: Automatically generates PDF certificates and saves them to a specified folder.
    Progress Bar: Visual feedback of the generation process.

Requirements

    Python 3.x
    Tkinter
    PIL (Pillow)
    ReportLab

Installation

    Clone the repository:

    sh

git clone https://github.com/yourusername/certificate-generator-app.git
cd certificate-generator-app

Install dependencies:

sh

    pip install pillow reportlab

Usage

    Run the application:

    sh

    python main.py

    Select Files:
        Names JSON File: Click "Browse" and select a JSON file containing names and codes in the format ["Name1, Code1", "Name2, Code2", ...].
        Background Image: Click "Browse" and select a PNG file to be used as the background for the certificates.
        Name Font: Click "Browse" and select a TTF file for the name font.
        Code Font: Click "Browse" and select a TTF file for the code font.

    Generate Certificates:
        Click "Generate Certificates" to start the generation process.
        The progress bar will update, showing the progress of certificate generation.
        Generated certificates will be saved in a folder named certificates.

File Structure

bash

certificate-generator-app/
│
├── main.py                # Main application script
├── README.md              # This README file
└── requirements.txt       # Dependencies list

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Tkinter for the GUI.
    Pillow for image handling.
    ReportLab for PDF generation.

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
