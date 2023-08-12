import fitz  # PyMuPDF
from PIL import Image
import io


pdf_file = fitz.open('test_.pdf')

for page_number in range(pdf_file.page_count):
    page = pdf_file[page_number]
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)

        image_data = base_image["image"]
        image = Image.open(io.BytesIO(image_data))
        image.save(f'image_page_{page_number + 1}_img_{img_index + 1}.png', format='PNG')

pdf_file.close()
