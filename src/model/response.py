from typing import TypedDict


class ResponseJsonExtraction(TypedDict):
    status: bool
    msg_status: str
    txt: str


class ResponseJsonIA(TypedDict):
    status: bool
    msg_status: str
    id: str
    model: str
    message: list


class ResponseJsonWritePDF(TypedDict):
    status: bool
    msg_status: str
