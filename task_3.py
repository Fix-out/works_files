with open("resource/file1.txt", "w", encoding='utf-8') as file:
    file.write("Фантазии нет,")
with open("resource/file2.txt", "w", encoding='utf-8') as file:
    file.write("чтобы составлять предложения.")
with open("resource/file3.txt", "w", encoding='utf-8') as file:
    file.write("Или что-то")

def combine_files():
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    with open("resource/combined.txt", "w", encoding='utf-8') as combine_file:
        for file_name in file_names:
            try:
                with open(file_name, "r", encoding='utf-8') as file_content:
                    content = file_content.read()

                    combine_file.write(f"=== Содержимое {file_name} ===\n")

                    combine_file.write(content + '\n\n')

            except FileNotFoundError:
                print(f"Файл {file_name} не найден")
combine_files()