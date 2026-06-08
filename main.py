class ConfigManager:
    _instance = None

    def __new__(cls):
        # Jeśli obiekt jeszcze nie istnieje, tworzymy go
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}

        # Zawsze zwracamy ten sam obiekt
        return cls._instance

    def set_setting(self, key, value):
        # Zapis ustawienia do wspólnego słownika
        self.settings[key] = value

    def get_setting(self, key):
        # Odczyt ustawienia ze wspólnego słownika
        return self.settings.get(key)

    def show_settings(self):
        # Wyświetlenie wszystkich ustawień
        print("Aktualne ustawienia:", self.settings)


# Program główny
config1 = ConfigManager()
config2 = ConfigManager()

config1.set_setting("nazwa_aplikacji", "Moja aplikacja")
config1.set_setting("debug", True)
config1.set_setting("wersja", "1.0")

print("Odczyt z config2:")
print("Nazwa aplikacji:", config2.get_setting("nazwa_aplikacji"))
print("Debug:", config2.get_setting("debug"))
print("Wersja:", config2.get_setting("wersja"))

print()
config2.show_settings()

print()
print("Czy config1 i config2 to ten sam obiekt?")
print(config1 is config2)