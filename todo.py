todos=[]
while True:
    print("\n1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("\nВыбор: ")

    if choice == "1":
        if not todos:
            print("Список пуст.")
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

    elif choice == "2":
        task = input("Введите задачу: ")
        todos.append(task)
        print("Добавлено!")

    elif choice == "3":
        if not todos:
            print("Список пуст.")
        else:
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
            n = int(input("Номер для удаления: "))
            todos.pop(n - 1)
            print("Удалено!")

    elif choice == "4":
        break