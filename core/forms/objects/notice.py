from typing import List


class Notice:
    def __init__(
        self,
        title: str,
        texts: List[str],
        submit_button_url: str,
        submit_button_text: str,
    ):
        self.title: str = title
        self.texts: str = texts
        self.submit_button_url: str = submit_button_url
        self.submit_button_text: str = submit_button_text
