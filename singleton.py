class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__.update(self._shared_state)


class Singleton(Borg):
    def __init__(self, **kwargs):
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_state)


singleton = Singleton(HTTP="HypterText Transfer Protocol")
print(f"current singleton setup: {singleton}")

singleton = Singleton(SNMP="Simple Network Management Protocol")
print(f"current singleton setup: {singleton}")


class NewSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(NewSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=NewSingleton):
    def log(self, msg):
        print(msg)


logger = Logger()
logger2 = Logger()

print(logger == logger2)
