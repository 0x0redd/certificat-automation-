import os
from tkinter import Tk, Label, Button, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_certificate(name, background_image, output_path, font_path):
    img = Image.open(background_image)
    pdf = canvas.Canvas(output_path, pagesize=img.size)

    # Draw background image
    pdf.drawInlineImage(background_image, 0, 0, width=img.width, height=img.height)

    # Register Montserrat thin font
    pdfmetrics.registerFont(TTFont('Montserrat-Thin', font_path))

    # Set the font to Montserrat thin
    pdf.setFont("Montserrat-Thin", 100)  # Adjust the size as needed

    # Position to place the name on the certificate
    x_position = img.width // 1.9
    y_position = img.height // 2

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
            output_path = f"{output_folder}/{name}_certificate.pdf"
            generate_certificate(name, background_image, output_path, font_path)
        elif isinstance(name, dict) and 'name' in name:
            output_path = f"{output_folder}/{name['name']}_certificate.pdf"
            generate_certificate(name['name'], background_image, output_path, font_path)

    return output_folder

class CertificateGeneratorApp:
    def __init__(self, root):
        self.root = root
        root.title("Certificate Generator")

        self.names_file_label = Label(root, text="Select Names JSON File:")
        self.names_file_label.pack()

        self.names_file_button = Button(root, text="Browse", command=self.browse_names_file)
        self.names_file_button.pack()

        self.background_image_label = Label(root, text="Select Background Image (PNG):")
        self.background_image_label.pack()

        self.background_image_button = Button(root, text="Browse", command=self.browse_background_image)
        self.background_image_button.pack()

        self.font_label = Label(root, text="Select Montserrat Thin Font (TTF):")
        self.font_label.pack()

        self.font_button = Button(root, text="Browse", command=self.browse_font)
        self.font_button.pack()

        self.generate_button = Button(root, text="Generate Certificates", command=self.generate_certificates)
        self.generate_button.pack()

    def browse_names_file(self):
        self.names_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])

    def browse_background_image(self):
        self.background_image = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])

    def browse_font(self):
        self.font_path = filedialog.askopenfilename(filetypes=[("TTF Files", "*.ttf")])

    def generate_certificates(self):
        if hasattr(self, 'names_file') and hasattr(self, 'background_image') and hasattr(self, 'font_path'):
            output_folder = generate_certificates(self.names_file, self.background_image, 'certificates', self.font_path)
            os.startfile(output_folder)

if __name__ == "__main__":
    root = Tk()
    app = CertificateGeneratorApp(root)
    root.mainloop()
