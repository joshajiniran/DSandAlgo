class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello folks"


class Spanish:
    def __init__(self):
        self.name = "Spanish"

    def speak_spanish(self):
        return "Hola munda"


class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "Ichu wina im"


class Adapter:
    def __init__(self, object, **adapter_method):
        self._object = object

        self.__dict__.update(adapter_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []

spanish = Spanish()
english = British()
korean = Korean()

objects.append(Adapter(spanish, speak=spanish.speak_spanish))
objects.append(Adapter(english, speak=english.speak_english))
objects.append(Adapter(korean, speak=korean.speak_korean))

for obj in objects:
    print(f"{obj.name} says {obj.speak()}")
