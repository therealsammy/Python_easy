def find_max(list):
    max_num = list[0]

    for number in list:
        if number > max_num:
            max_num = number
    return max_num


def emojis_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😄",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
