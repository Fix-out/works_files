with open('resource/input.txt', 'w', encoding='utf-8') as file:
    file.write("I feel so sigma\n")
    file.write("Здесь могла быть ваша реклама\n")
    file.write("Это третья строка\n")
    file.write("Это последняя строка\n")

with open('resource/input.txt', 'r') as file:
    content = file.readlines()
    num_lines = len(content)
    words = sum(len(line.split()) for line in content)

with open("resource/statistics.txt", "w", encoding='utf-8') as file:
    file.write(str(f"количество строк: {num_lines}"))
    file.write("\n")
    file.write(str(f"количество слов: {words}"))