from src.extraction import PdfText
from src.ia_robot import Robot
from config import config
from src.to_write_pdf import text_to_pdf
from src.utils.rename import name_file


def main():
    class_pdf = PdfText(config.PATH_FILE)
    pdf_txt = class_pdf.extract()
    if not pdf_txt['status']:
        print(pdf_txt['msg_status'])
        return

    class_robot = Robot(pdf_txt['txt'])
    result = class_robot.response_ia()
    if not result['status']:
        print(result['msg_status'])
        return

    file_name = name_file()
    response_convert = text_to_pdf(result['message'][0].message.content, f"output_{file_name}.pdf")
    if not response_convert['status']:
        print(response_convert['msg_status'])
        return

    print('end')


if __name__ == '__main__':
    main()
