from dataclasses import dataclass
from typing import AnyStr


@dataclass
class Common:
    connect_team_web_page: AnyStr = 'https://connecteam.com/'
    first_name: AnyStr = "Yaron"
    last_name: AnyStr = "Blum"
    email: AnyStr = "yaron@blum.com"
    phone: int = 507776666
    linkedin: AnyStr = "some_linkedin_profile"
