from multiprocessing import Value


class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet_type, and star must be non-empty strings")
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name: str = name
        self.planet_type: str = planet_type
        self.star: str = star

        def orbit(self):
            return f"{self.name} is orbiting around {self.star}..."

        def __str__(self):
            return f"Planet: {self.name} | Type: {self.planet_type} | Start: {self.star}"
