"""
test: read, readline, readlines
"""

in_file_name = "testowy.txt"
out_file_name = "test_writelines.txt"
file_path = "d:\\dane\\"     # "d:\dane\"


try:
    # otwarcie pliku do odczytu
    f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do odczytu")
    exit()

while True:
    content = f_in.read(100)
    if not content:
        break
    print(content)
    print(f"Odczytałem {len(content)} znaków")

print("\n\n")
f_in.seek(0)

lines = f_in.readlines()
for line in lines:
    print(line)

print("\n\n")
f_in.seek(0)

while True:
    line = f_in.readline(200)
    if not line:
        break
    print(line)
    print(f"Odczytałem {len(line)} znaków")

f_in.close()

try:
    # otwarcie pliku do zapisu
    f_out = open(file_path + out_file_name, "wt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do odczytu")
    exit()


print("\n\n")
lines = ['Linia 1\n', 'Linia 2\n', 'Linia 3\n']
f_out.writelines(lines)

f_out.close()
