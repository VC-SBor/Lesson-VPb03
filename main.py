"""Точка входа приложения «Заметки».

Здесь только главный цикл и выбор действия по номеру пункта меню.
Логика разделена между модулями:
- database.py — данные (список + JSON-файл);
- utils.py    — работа с пользователем (добавить/показать/удалить).
"""

from database import load_notes
from utils import add_note, delete_note, print_menu, show_notes

ACTIONS = {
    "1": add_note,
    "2": show_notes,
    "3": delete_note,
}


def main() -> None:
    """Основной цикл приложения."""
    load_notes()  # восстанавливаем заметки из JSON-файла при старте
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        if choice == "0":
            print("Выход из программы.")
            break
        action = ACTIONS.get(choice)
        if action is not None:
            action()
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()
