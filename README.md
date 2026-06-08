# Singleton w Pythonie - Menedżer konfiguracji

Projekt przedstawia prostą implementację wzorca projektowego **Singleton** w języku Python.  
 
## Opis wzorca Singleton

Singleton to wzorzec kreacyjny, którego celem jest zapewnienie, że z danej klasy powstanie tylko jeden obiekt.  
Oznacza to, że nawet jeśli programista kilka razy spróbuje utworzyć nową instancję klasy, program zawsze zwróci ten sam obiekt.

W tym projekcie Singleton został użyty do klasy `ConfigManager`, która przechowuje ustawienia aplikacji w jednym wspólnym słowniku.

## Implementacja

Główna klasa programu to:

```python
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}

        return cls._instance
```

### Jak działa implementacja?

1. W klasie znajduje się pole klasowe `_instance`.
2. Na początku `_instance` ma wartość `None`, czyli obiekt jeszcze nie istnieje.
3. Metoda `__new__()` kontroluje tworzenie obiektu.
4. Jeśli obiekt jeszcze nie istnieje, zostaje utworzony za pomocą `super().__new__(cls)`.
5. Utworzony obiekt zostaje zapisany w `cls._instance`.
6. Przy każdym kolejnym wywołaniu `ConfigManager()` zwracany jest ten sam obiekt.
7. Ustawienia aplikacji są przechowywane w słowniku `settings`.

Dzięki temu poniższe zmienne:

```python
config1 = ConfigManager()
config2 = ConfigManager()
```

nie są dwoma różnymi obiektami. Obie wskazują na tę samą instancję klasy.

Można to sprawdzić za pomocą operatora `is`:

```python
print(config1 is config2)
```

Jeżeli program działa poprawnie, wynikiem będzie:

```text
True
```

## Funkcje programu

Program umożliwia:

- utworzenie jednej wspólnej instancji klasy `ConfigManager`,
- zapis ustawień aplikacji,
- odczyt ustawień aplikacji,
- sprawdzenie, czy dwa obiekty są tak naprawdę tą samą instancją.

Przykładowe ustawienia:

```python
config1.set_setting("nazwa_aplikacji", "Moja aplikacja")
config1.set_setting("debug", True)
config1.set_setting("wersja", "1.0")
```

Odczyt ustawień może odbywać się przez inną zmienną:

```python
print(config2.get_setting("debug"))
```

Ponieważ `config1` i `config2` wskazują na ten sam obiekt, dane zapisane przez `config1` są widoczne również przez `config2`.

## Struktura projektu

Przykładowa struktura plików:

```text
.
├── main.py
└── README.md
```

Plik `main.py` zawiera kod programu z implementacją wzorca Singleton.

## Uruchomienie na Linux/macOS

1. Otwórz terminal.
2. Przejdź do folderu z projektem:

```bash
cd sciezka/do/projektu
```

3. Uruchom program poleceniem:

```bash
python3 main.py
```


## Uruchomienie na Windows

1. Otwórz terminal.
2. Przejdź do folderu z projektem:

```powershell
cd C:\sciezka\do\projektu
```

3. Uruchom program poleceniem:

```powershell
python main.py
```

## Wynik działania programu

Po uruchomieniu programu można otrzymać wynik podobny do poniższego:

```text
Odczyt z config2:
Nazwa aplikacji: Moja aplikacja
Debug: True
Wersja: 1.0

Aktualne ustawienia: {'nazwa_aplikacji': 'Moja aplikacja', 'debug': True, 'wersja': '1.0'}

Czy config1 i config2 to ten sam obiekt?
True
```

