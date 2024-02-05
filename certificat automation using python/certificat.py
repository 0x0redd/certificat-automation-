import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.names_file_label)
        self.layout.addWidget(self.names_file_button)
        self.layout.addWidget(self.background_image_label)
        self.layout.addWidget(self.background_image_button)
        self.layout.addWidget(self.font_label)
        self.layout.addWidget(self.font_button)
        self.layout.addWidget(self.generate_button)

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
            output_folder = generate_certificates(self.names_file, self.background_image, 'certificates', self.font_path)
            os.startfile(output_folder)

def generate_certificate(name, background_image, output_path, font_path):
    img = Image.open(background_image)
    pdf = canvas.Canvas(output_path, pagesize=img.size)

    # Draw background image
    pdf.drawInlineImage(background_image, 0, 0, width=img.width, height=img.height)

    # Register Montserrat thin font
    pdfmetrics.registerFont(TTFont('Montserrat-Thin', font_path))

    # Set the font to Montserrat thin
    pdf.setFont("Montserrat-Thin", 170)  # Adjust the size as needed

    # Position to place the name on the certificate
    x_position = 3000
    y_position = 2200

    # Centering the text on the page
    pdf.drawCentredString(x_position, y_position, name)

    pdf.save()

def generate_certificates(names_file, background_image, output_folder, font_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(names_file, 'r') as file:
        names = json.load(file)

    for name in names:
        if isinstance(name, str):
            output_path = f"{output_folder}/{name}.pdf"
            generate_certificate(name, background_image, output_path, font_path)
        elif isinstance(name, dict) and 'name' in name:
            output_path = f"{output_folder}/{name['name']}_certificate.pdf"
            generate_certificate(name['name'], background_image, output_path, font_path)

    return output_folder

if __name__ == "__main__":
    app = QApplication([])
    window = CertificateGeneratorApp()
    window.show()
    app.exec_()
