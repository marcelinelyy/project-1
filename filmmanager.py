films = []

def main():
    while True:
        print("\n1. Добавить фильм")
        print("2. Показать список")
        print("3. Отметить просмотренным")
        print("4. Отметить непросмотренным")
        print("5. Удалить фильм")
        print("6. Выйти")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            film = input("Название фильма: ")
            films.append({"title": film, "seen": False})
            print(f"Фильм '{film}' добавлен")
            
        elif choice == "2":
            if not films:
                print("Список фильмов пуст")
            else:
                print("\n Ваш список фильмов:")
                for i, film in enumerate(films, 1):
                    status = "П" if film["seen"] else "НП"
                    print(f"{i}. {film['title']} [{status}]")
                    
        elif choice == "3":
            if not films:
                print("Список фильмов пуст")
            else:
                print("\n Какой фильм отметить просмотренным?")
                for i, film in enumerate(films, 1):
                    status = "П" if film["seen"] else "НП"
                    print(f"{i}. {film['title']} [{status}]")
                
                try:
                    film_num = int(input("Номер фильма: ")) - 1
                    if 0 <= film_num < len(films):
                        films[film_num]["seen"] = True
                        print(f"Фильм '{films[film_num]['title']}' отмечен просмотренным")
                    else:
                        print("Неверный номер фильма")
                except ValueError:
                    print("Пожалуйста, введите число")
                    
        elif choice == "4":
            if not films:
                print("Список фильмов пуст")
            else:
                print("\n Какой фильм отметить непросмотренным?")
                for i, film in enumerate(films, 1):
                    status = "П" if film["seen"] else "НП"
                    print(f"{i}. {film['title']} [{status}]")
                
                try:
                    film_num = int(input("Номер фильма: ")) - 1
                    if 0 <= film_num < len(films):
                        films[film_num]["seen"] = False
                        print(f"Фильм '{films[film_num]['title']}' отмечен непросмотренным")
                    else:
                        print("Неверный номер фильма")
                except ValueError:
                    print("Пожалуйста, введите число")
                    
        elif choice == "5":
            if not films:
                print("Список фильмов пуст")
            else:
                print("\n Какой фильм удалить?")
                for i, film in enumerate(films, 1):
                    status = "П" if film["seen"] else "НП"
                    print(f"{i}. {film['title']} [{status}]")
                
                try:
                    film_num = int(input("Номер фильма: ")) - 1
                    if 0 <= film_num < len(films):
                        removed_film = films.pop(film_num)
                        print(f"Фильм '{removed_film['title']}' удален")
                    else:
                        print("Неверный номер фильма")
                except ValueError:
                    print("Пожалуйста, введите число")
                    
        elif choice == "6":
            print("До свидания")
            break
            
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
