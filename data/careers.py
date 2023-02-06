from dataclasses import dataclass
from typing import AnyStr


@dataclass
class Careers:
    r_and_d_button: AnyStr = "//*[contains(text(), 'R&D')]"
    careers_selections_class_name: AnyStr = "careers-category__cards-listItem-title"
    generic_position_button: AnyStr = "//*[contains(text(), '{}')]"

