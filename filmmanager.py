books = []

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать список")
        print("3. Отметить прочитанной")
        print("4. Отметить непрочитанной")
        print("5. Удалить книгу")
        print("6. Выйти")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            book = input("Название книги: ")
            books.append({"title": book, "read": False})
            print(f"Книга '{book}' добавлена!")
            
        elif choice == "2":
            if not books:
                print("Список книг пуст!")
            else:
                print("\nВаш список книг:")
                for i, book in enumerate(books, 1):
                    status = "✓" if book["read"] else "✗"
                    print(f"{i}. {book['title']} [{status}]")
                    
        elif choice == "3":
            if not books:
                print("Список книг пуст!")
            else:
                print("\nКакую книгу отметить прочитанной?")
                for i, book in enumerate(books, 1):
                    status = "✓" if book["read"] else "✗"
                    print(f"{i}. {book['title']} [{status}]")
                
                try:
                    book_num = int(input("Номер книги: ")) - 1
                    if 0 <= book_num < len(books):
                        books[book_num]["read"] = True
                        print(f"Книга '{books[book_num]['title']}' отмечена как прочитанная!")
                    else:
                        print("Неверный номер книги!")
                except ValueError:
                    print("Пожалуйста, введите число!")
                    
        elif choice == "4":
            if not books:
                print("Список книг пуст!")
            else:
                print("\nКакую книгу отметить непрочитанной?")
                for i, book in enumerate(books, 1):
                    status = "✓" if book["read"] else "✗"
                    print(f"{i}. {book['title']} [{status}]")
                
                try:
                    book_num = int(input("Номер книги: ")) - 1
                    if 0 <= book_num < len(books):
                        books[book_num]["read"] = False
                        print(f"Книга '{books[book_num]['title']}' отмечена как непрочитанная!")
                    else:
                        print("Неверный номер книги!")
                except ValueError:
                    print("Пожалуйста, введите число!")
                    
        elif choice == "5":
            if not books:
                print("Список книг пуст!")
            else:
                print("\nКакую книгу удалить?")
                for i, book in enumerate(books, 1):
                    status = "✓" if book["read"] else "✗"
                    print(f"{i}. {book['title']} [{status}]")
                
                try:
                    book_num = int(input("Номер книги: ")) - 1
                    if 0 <= book_num < len(books):
                        removed_book = books.pop(book_num)
                        print(f"Книга '{removed_book['title']}' удалена!")
                    else:
                        print("Неверный номер книги!")
                except ValueError:
                    print("Пожалуйста, введите число!")
                    
        elif choice == "6":
            print("До свидания!")
            break
            
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
