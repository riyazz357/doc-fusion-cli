import os
from pypdf import PdfReader, PdfWriter

# --- CONFIGURATION ---
INPUT_FOLDER = "input_pdfs"
OUTPUT_FOLDER = "output_pdfs"

# Ensure folders exist
if not os.path.exists(INPUT_FOLDER):
    os.makedirs(INPUT_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def merge_pdfs():
    """Combines all PDFs in the input folder into one."""
    writer = PdfWriter()
    
    # Get list of all PDF files
    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.pdf')]
    files.sort() # Sort alphabetically (important!)

    if not files:
        print(f"❌ No PDF files found in '{INPUT_FOLDER}' folder.")
        return

    print(f"🔄 Merging {len(files)} files...")
    
    for filename in files:
        filepath = os.path.join(INPUT_FOLDER, filename)
        try:
            reader = PdfReader(filepath)
            # Add all pages from current file to writer
            for page in reader.pages:
                writer.add_page(page)
            print(f"   --> Added: {filename}")
        except Exception as e:
            print(f"   ⚠️ Error reading {filename}: {e}")

    # Save result
    output_path = os.path.join(OUTPUT_FOLDER, "merged_result.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"\n✅ Success! Merged file saved at: {output_path}")

def extract_pages():
    """Extracts specific pages from a target PDF."""
    target_file = input(f"Enter the filename inside '{INPUT_FOLDER}' (e.g., doc.pdf): ")
    input_path = os.path.join(INPUT_FOLDER, target_file)

    if not os.path.exists(input_path):
        print("❌ File not found!")
        return

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        total_pages = len(reader.pages)
        
        print(f"📄 '{target_file}' has {total_pages} pages (Index 0 to {total_pages-1}).")
        user_input = input("Enter page numbers to extract (comma separated, e.g., 0,2,4): ")
        
        # Convert string input "0, 2" into list of integers [0, 2]
        page_indices = [int(p.strip()) for p in user_input.split(',')]

        for index in page_indices:
            if 0 <= index < total_pages:
                writer.add_page(reader.pages[index])
            else:
                print(f"   ⚠️ Skipping invalid page index: {index}")

        # Save result
        output_path = os.path.join(OUTPUT_FOLDER, f"extracted_from_{target_file}")
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"\n✅ Success! Extracted pages saved at: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

# --- MAIN MENU ---
if __name__ == "__main__":
    print("--- 📑 PDF Master Tool ---")
    print(f"1. Merge all PDFs in '{INPUT_FOLDER}'")
    print(f"2. Extract pages from a file")
    
    choice = input("\nSelect option (1 or 2): ")
    
    if choice == "1":
        merge_pdfs()
    elif choice == "2":
        extract_pages()
    else:
        print("Invalid choice.")