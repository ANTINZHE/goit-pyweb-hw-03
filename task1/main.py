import shutil
from pathlib import Path
import concurrent.futures


def check_folders():
    while True:
        trash_input = input("Введіть шлях до директорії зі 'сміттям': ")
        trash_folder = Path(trash_input)

        if trash_folder.is_dir():
            break
        else:
            print("Не вірно вказаний шлях")

    while True:
        finish_input = input("Введіть шлях до директорії сортування: ")

        if not finish_input:
            finish_folder = Path("C:\\py_hw_web_3\\dist")
        else:
            finish_folder = Path(finish_input)

        if finish_folder.is_dir():
            break
        else:
            print("Не вірно вказаний шлях")

    return trash_folder, finish_folder


def sorted_files(trash_folder: Path, finish_folder: Path, executor):
    try:
        for item in sorted(trash_folder.iterdir()):
            if item.is_dir():
                sorted_files(item, finish_folder, executor)
            else:
                executor.submit(copy_files, item, finish_folder)

    except PermissionError:
        print("Доступ закритий")


def copy_files(item, finish_folder: Path):
    print(f"копіювання файлу {item}")
    suffix = item.suffix.lstrip(".")
    ext_folder = finish_folder / suffix
    ext_folder.mkdir(
        parents=True, exist_ok=True
    )  # Створюється директорія, якщо її немає
    shutil.copy2(
        item, ext_folder / item.name
    )  # Копіюємо файл за допомогою copy2 з усіма даними
    print(f"Завершення копіювання {item}")


def main():
    trash_folder, finish_folder = check_folders()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sorted_files(trash_folder, finish_folder, executor)


if __name__ == "__main__":
    main()
