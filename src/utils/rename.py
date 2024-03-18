from datetime import datetime


def name_file() -> str:
    now = datetime.now()
    data = now.strftime("%Y_%m_%d")
    hora = now.hour
    minutos = now.minute
    segundos = now.second
    hora_str = str(hora).zfill(2)
    minutos_str = str(minutos).zfill(2)
    segundos_str = str(segundos).zfill(2)

    return f"{data}_{hora_str}_{minutos_str}_{segundos_str}"