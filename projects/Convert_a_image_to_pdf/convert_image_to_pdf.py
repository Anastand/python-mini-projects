import os
import img2pdf

def convert_images_to_pdf(folder_path, output_pdf_path):
    # Collect all image files in the specified folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]

    if not image_files:
        print("No images found in the folder.")
        return

    # Convert images to PDF
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_files))

    print(f"PDF saved as: {output_pdf_path}")

if __name__ == "__main__":
    # Specify the folder containing images and the output PDF file path
    folder_path = "/Users/aryan/cillege/python-mini-projects/projects/Convert_a_image_to_pdf/images"  # Change this to your folder path
    output_pdf_path = "output.pdf"  # Change this to your desired output PDF path

    convert_images_to_pdf(folder_path, output_pdf_path)

# it works