import sys
import os
import PyPDF2


def encrypt(password):

    for folder, subfolder, files in os.walk('.'):
        files = [f for f in files if f.endswith('.pdf')]
        for file in files:
            with open(os.path.join(folder, file), 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                pdf_writer = PyPDF2.PdfFileWriter()

                for npage in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(npage))

                pdf_writer.encrypt(password)
                filename = file.split('.pdf')[0] + '_encrypted.pdf'
                with open(os.path.join(folder, filename), 'wb') as encrypt_pdf:
                    pdf_writer.write(encrypt_pdf)

            os.remove(os.path.join(folder, file))


def decrypt(password):

    for folder, subfolder, files in os.walk('.'):
        for file in files:
            with open(os.path.join(folder, file), 'rb') as encrypted_file:
                try:
                    pdf_reader = PyPDF2.PdfFileReader(encrypted_file)
                except PyPDF2.utils.PdfReadError as e:
                    print(e)

                if not pdf_reader.isEncrypted:
                    continue

                pdf_reader.decrypt(password)
                pdf_writer = PyPDF2.PdfFileWriter()

                try:
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage((page_num)))
                except PyPDF2.utils.PdfReadError as e:
                    print(e)

                filename = file.split('_')[0] + '_decrypted.pdf'
                with open(os.path.join(folder, filename), 'wb') as encrypt_pdf:
                    pdf_writer.write(encrypt_pdf)


def main():
    password = str(sys.argv[1])
    encrypt(password)
    decrypt(password)


if __name__ == "__main__":
    main()