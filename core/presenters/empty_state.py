class EmptyState:
    def __init__(
        self,
        title: str,
        text: str,
        call_to_action_url: str,
        call_to_action_text: str,
    ):
        self._title: str = title
        self._text: str = text
        self._call_to_action_url: str = call_to_action_url
        self._call_to_action_text: str = call_to_action_text

    @property
    def title(self) -> str:
        return self._title

    @property
    def text(self) -> str:
        return self._text

    @property
    def call_to_action_url(self) -> str:
        return self._call_to_action_url

    @property
    def call_to_action_text(self) -> str:
        return self._call_to_action_text
