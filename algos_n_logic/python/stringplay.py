message_old = 'software engineering is awesome!'
message_new = ''

for char in message_old:
    if char == 's' or char == 'e':
        message_new += char.upper()
    else:
        message_new += char

print(message_new)