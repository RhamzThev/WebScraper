from operator import truediv
from tkinter import filedialog
from view.ui import UI

class CLI(UI):

    def get_input_file(self):
        print("===== INPUT FILE =====")
        input("Find input file (Press 'ENTER' to open file dialog) :: ")
        filename = filedialog.askopenfilename()

        print(f"Filename: { filename }")
        print()

        return filename

    def get_keyword(self):
        print("===== KEYWORD =====")
        keyword = input("Enter keyword :: ")
        print()

        return keyword

    def get_output_file(self):
        print("===== OUTPUT FILE =====")
        input("Find output file (Press 'ENTER' to open file dialog) :: ")
        filename = filedialog.askopenfilename()

        print(f"Filename: { filename }")
        print()

        return filename

    def get_summary(self, input_file, keyword, output_file):
        print("===== SUMMARY =====")
        print(f"Input File: {input_file}")
        print(f"Keyword: {keyword}")
        print(f"Output File: {output_file}")

        confirmation = input("Confirm (Press 'Y' to confirm) :: ")
        print()

        if confirmation.upper() == 'Y':
            return True
        return False
