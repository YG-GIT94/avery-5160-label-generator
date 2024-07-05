import fitz  # PyMuPDF
from PIL import Image
import io
import os
from tkinter import Tk, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Function to draw a single label with the barcode image centered within the label dimensions
def draw_label_final_corrected(c, x, y, image_path):
    image_width = label_width - 0.3 * inch  # Leave some margin
    image_height = label_height - 0.3 * inch  # Leave some margin
    image_x = x + (label_width - image_width) / 2
    image_y = y + (label_height - image_height) / 2
    c.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

# Function to draw title
def draw_title(c, title_text):
    c.setFont("Helvetica-Bold", 14)
    title_width = c.stringWidth(title_text, "Helvetica-Bold", 14)
    title_x = (page_width - title_width) / 2
    title_y = page_height - top_margin + 0.1 * inch  # Move down further from the top margin
    c.drawString(title_x, title_y, title_text)

# Define the exact label positions and sizes for Avery 5160
label_width = 2.625 * inch  # 2 5/8 inches
label_height = 1.0 * inch  # 1 inch
horizontal_spacing = 0.125 * inch  # Approximate spacing between labels horizontally
vertical_spacing = 0.0 * inch  # No vertical spacing between labels
page_width, page_height = letter

# Calculate margins
top_margin = 0.5 * inch
bottom_margin = 0.5 * inch
left_margin = 0.19 * inch  # Approximate left margin based on visual inspection
right_margin = 0.19 * inch  # Approximate right margin based on visual inspection

# Function to show file dialog and select files
def select_files():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Prevents the window from hanging
    root.attributes('-topmost', True)  # Bring the window to the front
    file_paths = filedialog.askopenfilenames(title="Select Barcode Files", filetypes=[("PDF Files", "*.pdf")])
    root.destroy()
    return file_paths

# Function to show directory dialog and select folder
def select_output_directory():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Prevents the window from hanging
    root.attributes('-topmost', True)  # Bring the window to the front
    output_dir = filedialog.askdirectory(title="Select Output Folder")
    root.destroy()
    return output_dir

# Ask the user to select barcode files
barcode_files = select_files()

if not barcode_files:
    print("No files selected. Exiting...")
    exit()

# Ask the user to select output directory
output_dir = select_output_directory()

if not output_dir:
    print("No output directory selected. Exiting...")
    exit()

for barcode_file_path in barcode_files:
    # Extract the barcode image from the PDF file
    barcode_pdf_document = fitz.open(barcode_file_path)
    barcode_page = barcode_pdf_document[0]
    barcode_image_full = barcode_page.get_pixmap(dpi=300)
    barcode_image_full_path = os.path.join(output_dir, "barcode_image_full.png")
    barcode_image_full.save(barcode_image_full_path)
    
    # Determine the output PDF file name
    file_name = os.path.basename(barcode_file_path)
    name_without_ext = os.path.splitext(file_name)[0]
    output_pdf_path_final = os.path.join(output_dir, f"{name_without_ext}_label.pdf")
    
    # Create a new PDF for the Avery 5160 labels using the correct dimensions and layout
    c = canvas.Canvas(output_pdf_path_final, pagesize=letter)
    
    # Populate the template with the labels
    for row in range(10):  # 10 rows
        for col in range(3):  # 3 columns
            x = left_margin + col * (label_width + horizontal_spacing)
            y = page_height - top_margin - (row + 1) * label_height
            draw_label_final_corrected(c, x, y, barcode_image_full_path)
    
    # Draw title after populating the barcodes
    draw_title(c, name_without_ext)
    
    # Save the final PDF with the correct layout
    c.save()
    
    # Delete the barcode image file
    os.remove(barcode_image_full_path)

    print(f"PDF saved at: {output_pdf_path_final}")

print("All files processed successfully!")
