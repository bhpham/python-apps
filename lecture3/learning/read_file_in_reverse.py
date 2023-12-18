# list = []
# with open('sample.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         list.append(line)


# print(list[::-1])

multiline_string = """bobby
hadz
.
com"""


# ✅ read first line of string (str.partition())
first_line = multiline_string.partition('\n')[0]
print(first_line)  # 👉️ bobby
