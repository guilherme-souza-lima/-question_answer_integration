from openai import OpenAI
from config import config
from src.constants.default_text import create_question_txt
from src.model.response import ResponseJsonIA


class Robot:
    def __init__(self, txt: str):
        self.msg_question = create_question_txt(txt)
        self.api_key = config.IA_API_KEY
        self.model = config.IA_MODEL

    def _response_message_ia(self) -> ResponseJsonIA:
        response: ResponseJsonIA = {
            'status': False,
            'id': '',
            'model': '',
            'message': []
        }
        try:
            client = OpenAI(
                api_key=self.api_key
            )
            chat_completion = client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": self.msg_question
                }]
            )
            response = {
                'status': True,
                'msg_status': '',
                'id': chat_completion.id,
                'model': chat_completion.model,
                'message': chat_completion.choices
            }
        except Exception as e:
            response['msg_status'] = f"Error openIA: ${str(e)}"
        return response

    def response_ia(self) -> ResponseJsonIA:
        msg = self._response_message_ia()
        return msg
