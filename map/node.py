class Node:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._neighbors: dict = {}