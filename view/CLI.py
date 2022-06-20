from tkinter import filedialog
from view.UI import UI

class CLI(UI):

    def get_input_file(self):
        input("Find input file (Press 'ENTER' to open file dialog) :: ")
        filename = filedialog.askopenfilename()

        print(f"Filename: { filename }")
        print()

        return filename

    def get_keyword(self):
        keyword = input("Enter keyword :: ")
        print()

        return keyword

    def get_output_file(self):
        input("Find output file (Press 'ENTER' to open file dialog) :: ")
        filename = filedialog.askopenfilename()

        print(f"Filename: { filename }")
        print()

        return filename

    def get_summary(self, input, keyword, output):
        return super().get_summary(input, keyword, output)
