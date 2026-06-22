from pathlib import Path
import yaml

# Create config file path
config_path = Path("config.yml")

# Read file as text
config_str = config_path.read_text(encoding="utf-8")

# TODO: Распарсить текст в dict, используя safe_load из yaml


# TODO: Вывести на экран полученный словарь

