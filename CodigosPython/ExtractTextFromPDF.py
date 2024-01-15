"""
Created Date: 08/01/2024
Last Update: 08/01/2024
Description: Extract text from PDF
Observation: You may have to install the package PyPDF2: pip install PyPDF2.
"""

# pip install PyPDF2
import PyPDF2 as pdf

# Function to read a PDF using the definition of 
# which page start to read and how many
#PDF in the same folder as the code
def read_pdf(first_page, qtd_pages, pdf_name):
    try:
        # Open the PDF and initiate the process of reading it
        with open(pdf_name, 'rb') as pdf_arc:
            # Initialize the variable to be used with the PDF
            read_pdf = pdf.PdfReader(pdf_arc)
            if first_page > 0 and len(read_pdf.pages) < first_page:
                print('First page is beyond the last page of the PDF!')
            elif first_page > 0 and len(read_pdf.pages) < first_page + qtd_pages:
                print('First page + quantity of pages to read is beyond the last page of the PDF!')
            elif len(read_pdf.pages) > 0:
                extract_text = ''
                actual_page = 0
                if first_page > 0 and qtd_pages == 0:
                    # Read the single page
                    page = read_pdf.pages[first_page -1]
                    # Get the text of the single page
                    extract_text += page.extract_text()
                elif first_page > 0 and qtd_pages > 0:
                    # Loop to be used in the search with +1 to reach the last indicated page
                    for num_page in range(qtd_pages+1):
                        # Read the page
                        page = read_pdf.pages[(first_page + actual_page) -1]
                        # Increments the variable to advance through the pages
                        actual_page += 1
                        # Get the text
                        extract_text += page.extract_text()
                else:
                    # Loop to be used in the search
                    for num_page in range(len(read_pdf.pages)):
                        # Read the page
                        page = read_pdf.pages[num_page]
                        # Get the text
                        extract_text += page.extract_text()
                # Print the data of the page
                print(extract_text)
            else:
                print('The PDF is empty!')
    except FileNotFoundError:
        print('PDF file not found!')
    except Exception as ex:
        print(f'An error has ocurred: {str(ex)}')

def option_menu():
    print('\nMenu for the PDF Extractor!')
    pdf_name = input('What is the name of the PDF: ')
    print('Choose an option: ')
    print('1. Extract all the text from the PDF')
    print('2. Extract the text from one page of the PDF')
    print('3. Extract the text from a rage of pages of the PDF')
    print('4. Exit')
    option = int(input())
    if option == 1: 
        read_pdf(0, 0, pdf_name)
        print('--------------------------------------------------')
        return True
    elif option == 2:
        selected_page = int(input('Type the number of the page: '))
        read_pdf(selected_page, 0, pdf_name)
        print('--------------------------------------------------')
        return True
    elif option == 3:
        selected_page = int(input('Type the number of the page: '))
        total_pages = int(input('Type the number of pages to be read: '))
        read_pdf(selected_page, total_pages, pdf_name)
        print('--------------------------------------------------')
        return True
    elif option == 4:
        return False
    else:
        print('Invalid selection. Try again!')
        return True


# Call the functions
if __name__ == '__main__':
    while True: 
        ret = option_menu()
        if not ret:
            print('Bye!')
            break
    