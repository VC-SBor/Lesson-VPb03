"""Модуль хранения заметок (слой данных).

Отвечает ТОЛЬКО за данные: список заметок и их сохранение в JSON-файле.
Здесь нет ввода/вывода для пользователя — если что-то не так с данными,
ошибку ищем в этом модуле (локализация ошибок).
"""

import json
from pathlib import Path

# Файл лежит рядом с модулем, независимо от текущей рабочей директории
DB_FILE = Path(__file__).with_name("notes.json")

# Внутреннее состояние модуля — список заметок
_notes: list[str] = []


def load_notes() -> None:
    """Загружает заметки из JSON-файла (если файла ещё нет — начинаем с пустого списка)."""
    global _notes
    if not DB_FILE.exists():
        _notes = []
        return
    try:
        with DB_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # Если файл повреждён или формат не тот — не роняем программу
        _notes = [str(item) for item in data] if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        _notes = []


def save_notes() -> None:
    """Сохраняет текущий список заметок в JSON-файл."""
    with DB_FILE.open("w", encoding="utf-8") as f:
        json.dump(_notes, f, ensure_ascii=False, indent=2)


def get_notes() -> list[str]:
    """Возвращает текущий список заметок (только чтение)."""
    return _notes


def add_note(text: str) -> int:
    """Добавляет заметку в конец списка, возвращает её номер."""
    _notes.append(text)
    save_notes()
    return len(_notes)


def delete_note(number: int) -> str:
    """Удаляет заметку по номеру (1-based), возвращает текст удалённой заметки."""
    removed = _notes.pop(number - 1)
    save_notes()
    return removed
