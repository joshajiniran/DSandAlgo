from dataclasses import dataclass
from turtle import position


class CPU:
    def freeze(self) -> None:
        print("Freezing processor")

    def jump(self, postion: int) -> None:
        print(f"Jumping to {postion}")

    def execute(self) -> None:
        print("Executing...")


class Memory:
    def load(self, position, data) -> None:
        print(f"Loading from {position} data: `{data}`")


class SolidStateDrive:
    def read(self, lba, size) -> None:
        print(f"Some data from sector {lba} with size {size}")


@dataclass
class ComputerFacade:
    cpu: CPU = CPU()
    memory: Memory = Memory()
    ssd: SolidStateDrive = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    computer_facade: ComputerFacade = ComputerFacade()
    computer_facade.start()


if __name__ == "__main__":
    main()
