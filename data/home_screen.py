from typing import AnyStr
from dataclasses import dataclass

@dataclass
class HomeScreen:
    connect_team_logo_class_name: AnyStr = "logo"
    careers_button_reg_ex: AnyStr = "//*[contains(text(), 'Careers')]"