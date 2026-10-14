"""Модуль функций работы с пользователем (слой логики/интерфейса).

Отвечает за добавление, вывод и удаление заметок, а также за меню.
Вся работа с данными делегируется модулю database — здесь мы только
спрашиваем пользователя и показываем результат.
"""

import database


def add_note() -> None:
    """Запрашивает текст заметки и добавляет её через database."""
    text = input("Введите текст заметки: ").strip()
    if not text:
        print("Заметка не может быть пустой.")
        return
    number = database.add_note(text)
    print(f"Заметка №{number} добавлена.")


def show_notes() -> None:
    """Выводит все заметки на экран."""
    notes = database.get_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    print("Все заметки:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


def delete_note() -> None:
    """Запрашивает номер заметки и удаляет её через database."""
    notes = database.get_notes()
    if not notes:
        print("Список заметок пуст, удалять нечего.")
        return
    show_notes()
    try:
        number = int(input("Введите номер заметки для удаления: "))
    except ValueError:
        print("Нужно ввести целое число.")
        return
    if 1 <= number <= len(notes):
        removed = database.delete_note(number)
        print(f"Заметка №{number} удалена: {removed}")
    else:
        print(f"Нет заметки с номером {number}. "
              f"Допустимый диапазон: 1–{len(notes)}.")


def print_menu() -> None:
    """Выводит меню программы."""
    print("\n--- Меню ---")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Удалить заметку по номеру")
    print("0. Выход")
