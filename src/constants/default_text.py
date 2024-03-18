from config import config


def create_question_txt(msg: str) -> str:
    question_txt = f"Ler o contexto do texto e criar ${config.NUMBER_QUESTIONS} perguntas com ${config.NUMBER_QUESTIONS_RESPONSE} multiplas escolhas. Mostrar todas as resposta corretas no final do arquivo:\n\n"
    obs_question_txt = "\nAo montar as perguntas deixa o titulo como atividade 1, atividade 2, atividade 3...\nDar um titulo para cada atividade para saber o tema de cada pergunta sobre.\nDeixar as respostas para o final do arquivo, dar o titulo de respostas das atividades"

    return f"${question_txt} ${msg} ${obs_question_txt}"
