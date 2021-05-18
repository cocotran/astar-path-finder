from map.node import *

INF: float = float('inf')


class Place:
    def __init__(self) -> None:
        self._type: str = ""
        self._icon: str = ""
        self._cost_for_role_C: int = 0

    def get_cost(self) -> int:
        return self._cost_for_role_C

    def get_icon(self) -> str:
        return self._icon


class QuarantinePlace(Place):
    def __init__(self) -> None:
        super().__init__()
        self._type: str = "Quarantine Place"
        self._icon: str = "*"
        self._cost_for_role_C: float = 0


class VaccineSpot(Place):
    def __init__(self) -> None:
        super().__init__()
        self._type: str = "Vaccine Spot"
        self._icon: str = "%"
        self._cost_for_role_C: int = 2


class PlayingGround(Place):
    def __init__(self) -> None:
        super().__init__()
        self._type: str = "Playing Ground"
        self._icon: str = "@"
        self._cost_for_role_C: int = 3


class EmptyPlace(Place):
    def __init__(self) -> None:
        super().__init__()
        self._type: str = "Empty Place"
        self._icon: str = "#"
        self._cost_for_role_C: int = 1
