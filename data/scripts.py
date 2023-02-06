from typing import AnyStr
from dataclasses import dataclass


@dataclass
class Commands:
    scroll_to_bottom: AnyStr = "window.scrollTo(0, document.body.scrollHeight);"
