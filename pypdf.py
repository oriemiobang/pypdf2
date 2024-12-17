import os
import re
import PyPDF2 as pdf
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


# file = open("files/torbel.pdf", "rb")
# reader = PdfReader(file)
# data = reader.metadata
# print(reader.pages[0].extract_text())

def getPdfMetadata(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        info = reader.metadata
        return info
    
# function to extract text from pdf file
def extractPDFText(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        result = []
        for i in range(0, len(reader.pages)):
            selectedPage = reader.pages[i]
            text = selectedPage.extract_text()
            result.append(text)
        return ''.join(result)
    
# split pdf into multiple pages
def split_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
       
        for i in range(0, len(reader.pages)):
            selectedPage = reader.pages[i]
            writer = PdfWriter()
            writer.add_page(selectedPage)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_{i+1}.pdf"
        #save to pdf
            with open(output_filename, "wb") as out:
             writer.write(out)
            print("created a pdf: " + output_filename )

def get_pdf_upto(pdf_path, start_page:int = 0, stop_page:int = 0, output_path = "output"):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for i in range(start_page, stop_page):
            selectedPage = reader.pages[i]
            writer.add_page(selectedPage)
            fileName = os.path.splitext(pdf_path[0])
            output_filename = f"{fileName}_from_{start_page}_to_{stop_page}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
        print("created a pdf: " + output_filename )

def get_last_page(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        selectedPage = reader.pages[len(reader.pages) - 1]
        writer.add_page(selectedPage)
        fileName = os.path.splitext(pdf_path[0])
        output_filename = f"{fileName}_last_page.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
        print("created a pdf: " + output_filename )

def fetch_all_pdf_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

def merge_pdf(last_of_pdfs, output_filename = "final_merged_file.pdf"):
    merger = PdfMerger()
    with open(output_filename, "wb") as f:
        for file in last_of_pdfs:
            merger.append_pdf(file)
        merger.writer(f)

def split_text_into_verses(text):
    # Regular expression to match verse numbers (numbers at the beginning of lines)
    verses = re.split(r'(?<=\d)\s', text)
    # Filter out any empty strings and strip leading/trailing whitespace
    verses = [verse.strip() for verse in verses if verse.strip()]
    return verses

# pdf_list = fetch_all_pdf_files("./Out")
# merge_pdf(pdf_list)
# get_last_page("files/torbel2.pdf")
# get_pdf_upto("files/torbel2.pdf", 0 , 2)
# split_pdf("files/torbel.pdf")
# metadata = getPdfMetadata("files/piliman.pdf")
# texts = extractPDFText("files/torbel.pdf")

texts = extractPDFText("files/pili.pdf")
# verses = split_text_into_verses(texts.split("%")[1])
# print(verses)

# print(metadata)

chapterName = texts.split("%")[0].split("\n")[0]
# about = texts.split("%")[1].split("\n")[0]
title = ""
text = ""
# verses = texts.split("%")

print("===============" + chapterName[1:] + "===============")
verseNumber = 0;
for number in range(0, len(texts.split("%")[1].split("*"))):
   myText =  split_text_into_verses(texts.split("%")[1].split("*")[number])
   for index in range(0, len(myText)):
       
       if index == 0:
          splittedTitle = myText[index].split(" ")
        #   print(splittedTitle)
          splittedTitle.remove(splittedTitle[-1])
        #   print(splittedTitle)
          joinedTitle = ' '.join(splittedTitle)
          print(" title: " + joinedTitle)
       else: 
           verseNumber = verseNumber + 1
           splittedVerse = myText[index].split(" ")
           splittedVerse.remove(splittedVerse[-1])
           joinedVerse =' '.join(splittedVerse)
           print(f"{verseNumber} " + joinedVerse)
       
   




# print(te)
# print(texts)

#