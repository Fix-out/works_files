with open ('resource/text.txt', 'w') as file:
    text = [
        "что-то на филосовском",
        "i feel SO sigma",
        "что-то на умном",
        "честно идей нет"
    ]
    for word in text:
        file.write(word + '\n')

words_search = input("Введите слово для поиска:")

cnt = 0
founded = False
encountered = ""
string_num = 1
for i in text:
    if words_search in i.split():
        cnt += 1
        founded = True
        encountered += (str(string_num) + " ")
    string_num += 1

with open('resource/search_results.txt', 'w', encoding='utf-8') as file:
    file.write("Найдено слово\n" if founded else "слово не найдена\n")
    file.write(f"слово {words_search} встречено: {cnt} раз\n")
    file.write(f"слово {words_search} встречается в строках: {encountered}\n")

with open('resource/search_results.txt', 'r', encoding='utf-8') as file:
    result = file.readlines()
    for i in result:
        print(i)