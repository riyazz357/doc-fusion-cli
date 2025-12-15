# 📑 PDF Master Tool (Day 8)

A Python CLI utility for manipulating PDF documents. It allows users to **Merge** multiple PDF files into a single document or **Extract** specific pages from a file.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Merge Mode:** Combines all PDFs in a specific folder into one `merged_output.pdf`.
* **Extract Mode:** Pulls specific pages (or a range) from a PDF and saves them as a new file.
* **Metadata Preservation:** Keeps the original quality and formatting of the pages.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Library:** `pypdf` (The modern replacement for PyPDF2).
* **Interface:** Command Line Interface (CLI).

## ⚙️ Installation

### 1. Install Dependencies
```bash
pip install pypdf
2. Setup Folders
Create two folders in the project directory to keep things organized:

input_pdfs/ (Put your files here)

output_pdfs/ (Results appear here)

python main.py