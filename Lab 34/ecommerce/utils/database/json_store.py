import json
from pathlib import Path


class JsonStore:
    def __init__(self, filename):
        self.path = Path(filename)

    def save(self, data):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = self.path.with_suffix(self.path.suffix + ".tmp")
        with temporary_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        temporary_path.replace(self.path)

    def load(self, default=None):
        try:
            with self.path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return default
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON data in {self.path}") from error
