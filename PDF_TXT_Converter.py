# PDF to TXT Converter for Multiple Files #

import os
import glob

try:
    import PyPDF2
except:
    os.system("pip install PyPDF2")
    import PyPDF2


def PDF_TXT(in_path):
    if not os.path.isfile(in_path):
        print(f"{in_path} does Not Exist!\n")
        return

    with open(in_path, 'rb') as in_file:
        try:
            reader = PyPDF2.PdfReader(in_file)
        except:
            print(f"{in_path} is Not A PDF File!\n")
            return
            
        out_path = in_path[:in_path.rfind(".")] + ".txt"    # Save as ".txt"
        with open(out_path, 'w', encoding="utf-8") as out_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                content = page.extract_text()
                out_file.write(content)
        
    # Printing Process Information
    print(f"Source File: {in_path}")
    print(f"Saved File : {out_path}\n")
    

def main():
    exit_main = False
    while True:
        inputMode = input("File Name(s): 1\nFolder Name : 2\nExit Program: *\nSelect Input Mode: ")
        if inputMode == "*":
            exit_main = True
            break
        
        try:
            inputMode = int(inputMode.strip())
            if inputMode != 1 and inputMode != 2:
                print("Enter 1 or 2!\n")
                continue
        except:
            print("Enter 1 or 2!\n")
            continue
        
        break
    
    
    if not exit_main:
        if inputMode == 1:
            # Example: file1.pdf, file2.pdf
            inputString = input("\nExample: file1.pdf, file2.pdf\nEnter PDF File Name(s): ")
            splitString = [x.strip() for x in inputString.split(',')]
            filenames = [f for f in splitString]

        else:
            # Example: pdf
            inputString = input("\nExample: pdf\nEnter PDF Folder Name: ")
            splitString = inputString.strip()
            if not os.path.isdir(splitString):
                print("\nFolder does Not Exist!")
            filenames = glob.glob(splitString+'/*.*')

        if len(filenames) > 0:
            print()
            for file in filenames:
                PDF_TXT(file)


if __name__ == '__main__':
    
    main()