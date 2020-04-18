def old_macdonald(name):
    return name[0:3].capitalize() + name[3:].capitalize()

x = old_macdonald("clemente")
y = old_macdonald("macdonald")

print(f'clemente: {x}')
print(f'macdonald: {y}')
