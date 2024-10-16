import random

# HEXITS = ['0', '1', '2', '3', '4', '5', '6', '7',
#           '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

# def random_hexit():
#     return HEXITS[random.randint(0,15)]

# def get_uuid():
#     sections = []
#     sections.append(''.join([random_hexit() for num in range(8)]))
#     sections.append(''.join([random_hexit() for num in range(4)]))
#     sections.append(''.join([random_hexit() for num in range(4)]))
#     sections.append(''.join([random_hexit() for num in range(4)]))
#     sections.append(''.join([random_hexit() for num in range(12)]))
#     return '-'.join(sections)

# print(get_uuid())


def generate_uuid():
    hex_chars = "0123456789abcdef"
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append("".join(chars))

    return "-".join(uuid)

print(generate_uuid())
