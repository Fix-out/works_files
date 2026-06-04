with open("resource/words.txt", "w", encoding="utf-8") as file:
    text = [
        "Aboba",
        "Bag",
        "Squirrel",
        "Back",
        "Cloudy",
        "Amogus",
        "City",
        "Tree",
        "Needle",
        "Bread",
        "Umbrella",
        "Giraffe",
        "Book ",
        "Laboratory",
        "Shop",
        "Fork"
    ]
    for word in text:
        file.write(word + '\n')

with open('resource/words.txt', 'r', encoding="utf-8") as file:
    txt = file.readlines()
    sorted_alphabetically = sorted(txt)

    sorted_by_length = sorted(txt,key = len)

    sorted_reverse = sorted(txt,reverse = True)

with open('resource/sorted_alphabetically.txt', 'w', encoding="utf-8") as file:
    for word in sorted_alphabetically:
        file.write(word + '\n')

with open('resource/sorted_by_length.txt', 'w', encoding="utf-8") as file:
    for word in sorted_by_length:
        file.write(word + '\n')

with open('resource/sorted_reverse.txt', 'w', encoding="utf-8") as file:
    for word in sorted_reverse:
        file.write(word + '\n')


