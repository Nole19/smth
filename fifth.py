def task1(map: dict[str, float]) -> float:
    return sum(map.values())


def task2(arr: list[str]) -> list[str]:
    return sorted(arr, key=lambda elem: int("".join([x for x in elem if x.isdigit()])))


def task3(l: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(l, key=lambda elem: elem[1])


def task4(arr: list[int]) -> int:
    arr = [x for x in arr if x > 0]
    result = 1
    while 1:
        if result not in arr:
            return result
        result += 1


def task5() -> int:
    user_input = input("Please enter a sentence or phrase: ")
    result = 0
    for char in user_input:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += 1
    return result


def task6(file_name: str) -> dict[str, int]:
    result = {}
    file = open(file_name, "r")

    file_content = "".join(file.readlines())
    file_content = file_content.replace('\n', ' ')
    file_content = file_content.replace(',', '')
    file_content = file_content.replace('.', '')
    file_content = file_content.replace('!', '')
    file_content = file_content.replace('?', '')
    file_content = file_content.lower()

    for word in file_content.split(" "):
        result[word] = result.get(word, 0) + 1
    return dict(sorted(result.items()))


def xor_cipher(text: str, key: str) -> str:
    result = ""
    i = 0

    for char in text:
        result += chr(ord(char) ^ ord(key[i]))
        i = (i + 1) % len(key)

    return result


def decrypt(input: str, key: str) -> str:
    result = ""
    i = 0

    for char in input:
        result += chr(ord(char) ^ ord(key[i]))
        i = (i + 1) % len(key)

    return result


def main():
    print(task1({'apple': 2.5, 'banana': 1.8, 'orange': 3.0, 'grapes': 4.5}))
    print(task2(["3abc", "10xyz", "1def", "7ghi"]))
    print(task3([('bear', 3), ('tiger', 1), ('elephant', 2)]))
    print(task4([3, 4, -1, 1]))
    print(task5())
    print(task6("text.txt"))
    encrypted_message = xor_cipher("Hello, World!", "michael")
    print(encrypted_message)
    print(decrypt(encrypted_message, "michael"))


if name == "main":
    main()