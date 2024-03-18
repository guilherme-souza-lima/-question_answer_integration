import PyPDF2
from src.model.response import ResponseJsonExtraction


class PdfText:
    def __init__(self, file_pdf):
        self.file_pdf = file_pdf

    def _extract_txt(self) -> ResponseJsonExtraction:
        response: ResponseJsonExtraction = {
            'status': False,
            'msg_status': '',
            'txt': ''
        }
        try:
            with open(self.file_pdf, 'rb') as file:
                read_pdf = PyPDF2.PdfReader(file)
                for page in range(len(read_pdf.pages)):
                    response['txt'] += read_pdf.pages[page].extract_text()
            response['status'] = True
        except Exception as e:
            response['msg_status'] = f"Error PyPDF: ${str(e)}"
        finally:
            return response

    def extract(self) -> ResponseJsonExtraction:
        list_txt = self._extract_txt()
        return list_txt
