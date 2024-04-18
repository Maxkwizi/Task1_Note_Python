import csv
import os
import datetime

# Метод для чтения всех заметок из файла
def read_notes():
    if not os.path.exists('notes.csv'):
        print()
        print("Файл не найден или удалён")
        return []
   
    with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        notes = list(reader)
        return notes
    

# Метод для сохранения заметок в файл
def save_notes(notes):
    with open('notes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)


# Метод для добавления новой заметки
def add_note():
    print()
    note_id = input("Введите идентификатор заметки: ")
    print()
    title = input("Введите заголовок заметки: ")
    print()
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = [note_id, title, body, timestamp]
    notes = read_notes()
    notes.append(note)
    save_notes(notes)
    print()
    print("Заметка " + note_id + " успешно сохранена.")


# Метод для чтения одной заметки
def read_selected_note():
    print()
    note_id = input("Введите идентификатор заметки для чтения: ")
    print()
    notes = read_notes()
    for note in notes:
        if note[0] == note_id:
            print()
            print(f"Идентификатор: {note[0]}")
            print(f"Заголовок: {note[1]}")
            print(f"Текст: {note[2]}")
            print(f"Дата/время: {note[3]}")
            print()
            return
    print()
    print("Заметка с таким идентификатором не найдена.")


# Метод для чтения всех заметок
def read_all_notes():
    notes = read_notes()
    for note in notes:
        print()
        print(f"Идентификатор: {note[0]}")
        print(f"Заголовок: {note[1]}")
        print(f"Текст: {note[2]}")
        print(f"Дата/время: {note[3]}")
        print()
    
    
# Метод для редактирования заметки
def edit_note():
    print()
    note_id = input("Введите идентификатор заметки для редактирования: ")
    notes = read_notes()
    for note in notes:
        if note[0] == note_id:
            print()
            note[1] = input("Введите новый заголовок: ")
            print()
            note[2] = input("Введите новый текст: ")
            print()
            note[3] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print()
            save_notes(notes)
            print("Заметка " + note_id + " успешно отредактирована.")
            return
    print()
    print("Заметка с таким идентификатором не найдена.")


# Метод для удаления заметки
def delete_note():
    print()
    note_id = input("Введите идентификатор заметки для удаления: ")
    notes = read_notes()
    for note in notes:
        if note[0] == note_id:
            notes.remove(note)
            save_notes(notes)
            print()
            print("Заметка " + note_id +" успешно удалена.")
            return
    print()
    print("Заметка с таким идентификатором не найдена.")


# Основной метод для взаимодействия с пользователем через консоль
def main():
    while True:
        print()
        print("1. Добавить заметку")
        print("2. Показать одну заметку")
        print("3. Показать все заметки")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выход")
        print()

        choice = input("Выберите действие: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_selected_note() 
        elif choice == "3":
            read_all_notes()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()