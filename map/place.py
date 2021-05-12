from node import *

INF: float = float('inf')


class Place:
    def __init__(self) -> None:
        self._name: str = ""
        self._icon: str = ""
        self._cost_for_role_P: int = 0
        self.top_place: Place = None
        self.bottom_place: Place = None
        self.left_place: Place = None
        self.right_place: Place = None
        self.top_left_node: Node = None
        self.top_right_node: Node = None
        self.bottom_left_node: Node = None
        self.bottom_left_node: Node = None

    def get_cost(self) -> int:
        return self._cost_for_role_P

    def get_icon(self) -> str:
        return self._icon


class QuarantinePlace(Place):
    def __init__(self) -> None:
        self._name: str = "Quarantine Place"
        self._icon: str = "*"
        self._cost_for_role_P: float = INF


class VaccineSpot(Place):
    def __init__(self) -> None:
        self._name: str = "Vaccine Spot"
        self._icon: str = "%"
        self._cost_for_role_P: int = 2


class PlayingGround(Place):
    def __init__(self) -> None:
        self._name: str = "Playing Ground"
        self._icon: str = "@"
        self._cost_for_role_P: int = 0


class EmptyPlace(Place):
    def __init__(self) -> None:
        self._name: str = "Empty Place"
        self._icon: str = "#"
        self._cost_for_role_P: int = 1
