"""Скрипт для работы со списком заметок.

Возможности:
- добавить заметку (строку текста) в список;
- вывести все заметки на экран;
- удалить заметку по номеру.
"""

NOTES = []


def add_note():
    """Добавляет новую заметку в список."""
    text = input("Введите текст заметки: ").strip()
    if not text:
        print("Заметка не может быть пустой.")
        return
    NOTES.append(text)
    print(f"Заметка №{len(NOTES)} добавлена.")


def show_notes():
    """Выводит все заметки на экран."""
    if not NOTES:
        print("Список заметок пуст.")
        return
    print("Все заметки:")
    for number, note in enumerate(NOTES, start=1):
        print(f"{number}. {note}")


def delete_note():
    """Удаляет заметку по её номеру."""
    if not NOTES:
        print("Список заметок пуст, удалять нечего.")
        return
    show_notes()
    try:
        number = int(input("Введите номер заметки для удаления: "))
    except ValueError:
        print("Нужно ввести целое число.")
        return
    if 1 <= number <= len(NOTES):
        removed = NOTES.pop(number - 1)
        print(f"Заметка №{number} удалена: {removed}")
    else:
        print(f"Нет заметки с номером {number}. "
              f"Допустимый диапазон: 1–{len(NOTES)}.")


def print_menu():
    """Выводит меню программы."""
    print("\n--- Меню ---")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Удалить заметку по номеру")
    print("0. Выход")


def main():
    """Основной цикл программы."""
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            delete_note()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()
