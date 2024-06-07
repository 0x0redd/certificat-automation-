import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QProgressBar
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from PyQt5.QtCore import Qt

class CertificateGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.names_file_label = QLabel("Select Names JSON File:")
        self.names_file_button = QPushButton("Browse", clicked=self.browse_names_file)

        self.background_image_label = QLabel("Select Background Image (PNG):")
        self.background_image_button = QPushButton("Browse", clicked=self.browse_background_image)

        self.font_label = QLabel("Select Font (TTF):")
        self.font_button = QPushButton("Browse", clicked=self.browse_font)

        self.generate_button = QPushButton("Generate Certificates", clicked=self.generate_certificates)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.names_file_label)
        self.layout.addWidget(self.names_file_button)
        self.layout.addWidget(self.background_image_label)
        self.layout.addWidget(self.background_image_button)
        self.layout.addWidget(self.font_label)
        self.layout.addWidget(self.font_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.progress_bar)

        self.names_file = ""
        self.background_image = ""
        self.font_path = ""

    def browse_names_file(self):
        self.names_file, _ = QFileDialog.getOpenFileName(self, "Select Names JSON File", "", "JSON Files (*.json)")

    def browse_background_image(self):
        self.background_image, _ = QFileDialog.getOpenFileName(self, "Select Background Image (PNG)", "", "PNG Files (*.png)")

    def browse_font(self):
        self.font_path, _ = QFileDialog.getOpenFileName(self, "Select Font (TTF)", "", "TTF Files (*.ttf)")

    def generate_certificates(self):
        if self.names_file and self.background_image and self.font_path:
            self.progress_bar.setVisible(True)
            self.generate_button.setEnabled(False)
            output_folder = generate_certificates(self.names_file, self.background_image, 'certificates', self.font_path)
            os.startfile(output_folder)
            self.progress_bar.setVisible(False)
            self.generate_button.setEnabled(True)

def generate_certificate(name, background_image, output_path, font_path):
    img = Image.open(background_image)
    pdf = canvas.Canvas(output_path, pagesize=img.size)

    # Draw background image
    pdf.drawInlineImage(background_image, 0, 0, width=img.width, height=img.height)

    # Register Montserrat thin font
    pdfmetrics.registerFont(TTFont('Montserrat-Thin', font_path))

    # Set the font to Montserrat thin and change text color to white
    # Define your hexadecimal color
    hex_color = "#ffffff"

    # Set the fill color using the HexColor object
    pdf.setFillColor(colors.HexColor(hex_color))

    pdf.setFont("Montserrat-Thin", 120)

    # Position to place the name on the certificate
    x_position = img.width // 2
    y_position = img.height // 2.25 

    # Centering the text on the page
    pdf.drawCentredString(x_position, y_position, name)

    pdf.save()

def generate_certificates(names_file, background_image, output_folder, font_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(names_file, 'r') as file:
        names = json.load(file)

    for i, name in enumerate(names):
        if isinstance(name, str):
            output_path = f"{output_folder}/{name}.pdf"
            generate_certificate(name, background_image, output_path, font_path)
        elif isinstance(name, dict) and 'name' in name:
            output_path = f"{output_folder}/{name['name']}_certificate.pdf"
            generate_certificate(name['name'], background_image, output_path, font_path)
    
        # Update progress bar
        progress = int((i + 1) / len(names) * 100)
        app.processEvents()  # Ensure the GUI updates
        window.progress_bar.setValue(progress)


    return output_folder

if __name__ == "__main__":
    app = QApplication([])
    window = CertificateGeneratorApp()
    window.show()
    app.exec_()
