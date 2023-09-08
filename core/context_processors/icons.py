from typing import Dict


def icons(_request) -> Dict:
    return {
        "ICON_COMMENT": "bi bi-chat-dots-fill",
        "ICON_UPLOAD": "bi bi-cloud-arrow-up-fill",
        "ICON_POST": "bi bi-send-fill",
        "ICON_UPVOTE": "bi bi-hand-thumbs-up-fill",
        "ICON_DOWNVOTE": "bi bi-hand-thumbs-down-fill",
    }
