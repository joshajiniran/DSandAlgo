from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CharacterTrait:
    strength: int = 0
    constitution: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    health: int = 100


@dataclass
class Player:
    name: str
    character: CharacterTrait = field(default_factory=CharacterTrait)
    xp: int = 0
    inventory: list[str] = field(default_factory=list)


def main():
    player = Player(
        name="Arjan Codes",
        strength=10,
        constitution=10,
        dexterity=10,
        wisdom=20,
        charisma=20,
    )
    print(player)


if __name__ == "__main__":
    main()
