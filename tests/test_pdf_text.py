import unittest
from src.extraction import PdfText


class TestPdfText(unittest.TestCase):
    def test_pdf_text(self):
        class_pdf_test = PdfText('../debug/mock_test/test_file.pdf')

        pdf_txt_test = class_pdf_test.extract()
        txt_test = 'Test File Python.'

        self.assertEqual(pdf_txt_test['txt'].rstrip(), txt_test.rstrip(),
                         "Texto extraído do PDF não corresponde ao esperado.")


class TestPdfTextError(unittest.TestCase):
    def test_pdf_text(self):
        class_pdf_test = PdfText('')
        pdf_txt_test = class_pdf_test.extract()
        self.assertEqual(pdf_txt_test['status'], False)


if __name__ == '__main__':
    unittest.main()
