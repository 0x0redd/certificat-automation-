import os
from tkinter import Tk, Label, Button, filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import white

def generate_certificate(name, code, background_image, output_path, name_font_path, code_font_path):
    img = Image.open(background_image)
    pdf = canvas.Canvas(output_path, pagesize=img.size)

    # Draw background image
    pdf.drawInlineImage(background_image, 0, 0, width=img.width, height=img.height)

    # Register fonts
    pdfmetrics.registerFont(TTFont('NameFont', name_font_path))
    pdfmetrics.registerFont(TTFont('CodeFont', code_font_path))

    # Set text color to white
    pdf.setFillColorRGB(1, 1, 1)

    # Calculate center positions for the name and code
    x_position = img.width // 2
    y_position = img.height // 2

    # Draw name
    pdf.setFont("NameFont", 24)  # Adjust the size as needed
    pdf.drawCentredString(x_position, y_position + 50, name)  # Adjust y_position + offset as needed

    # Draw code
    pdf.setFont("CodeFont", 18)  # Adjust the size for the code as needed
    pdf.drawCentredString(x_position, y_position - 20, code)  # Adjust y_position - offset as needed

    pdf.save()

def generate_certificates(names_file, background_image, output_folder, name_font_path, code_font_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(names_file, 'r') as file:
        entries = json.load(file)

    for entry in entries:
        name, code = entry.split(', ')
        output_path = f"{output_folder}/{name}_certificate.pdf"
        generate_certificate(name, code, background_image, output_path, name_font_path, code_font_path)

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

        self.name_font_label = Label(root, text="Select Name Font (TTF):")
        self.name_font_label.pack()

        self.name_font_button = Button(root, text="Browse", command=self.browse_name_font)
        self.name_font_button.pack()

        self.code_font_label = Label(root, text="Select Code Font (TTF):")
        self.code_font_label.pack()

        self.code_font_button = Button(root, text="Browse", command=self.browse_code_font)
        self.code_font_button.pack()

        self.generate_button = Button(root, text="Generate Certificates", command=self.generate_certificates)
        self.generate_button.pack()

    def browse_names_file(self):
        self.names_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])

    def browse_background_image(self):
        self.background_image = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])

    def browse_name_font(self):
        self.name_font_path = filedialog.askopenfilename(filetypes=[("TTF Files", "*.ttf")])

    def browse_code_font(self):
        self.code_font_path = filedialog.askopenfilename(filetypes=[("TTF Files", "*.ttf")])

    def generate_certificates(self):
        if hasattr(self, 'names_file') and hasattr(self, 'background_image') and hasattr(self, 'name_font_path') and hasattr(self, 'code_font_path'):
            output_folder = generate_certificates(self.names_file, self.background_image, 'certificates', self.name_font_path, self.code_font_path)
            os.startfile(output_folder)

if __name__ == "__main__":
    root = Tk()
    app = CertificateGeneratorApp(root)
    root.mainloop()
