# # Latihan 1 
print("\n====LATIHAN NO.1====")
def buat_menu(data):
    menu = {}
    for id, parent, label in data:
        menu[id] = {'label': label, 'children': []}
    
    hasil = []
    for id, parent, _ in data:
        if parent == 0:
            hasil.append(menu[id])
        else:
            menu[parent]['children'].append(menu[id])
    return hasil

def cetak_menu(menu, indent=0):
    for item in menu:
        print(" " * indent + item['label'])
        cetak_menu(item['children'], indent + 4)

n = int(input("Jumlah menu: "))
data = []

for _ in range(n):
    id = int(input("ID: "))
    parent = int(input("Parent: "))
    label = input("Label: ")
    data.append((id, parent, label))

print("\nStruktur Menu:")
cetak_menu(buat_menu(data))

# Latihan 2
print("\n====LATIHAN NO.1====")
def palindrom(b):
    if len(b) <= 1:
        return True
    elif not b[0].isalpha() :  
        return palindrom(b[1:])
    elif not b[-1].isalpha() :  
        return palindrom(b[:-1])
    elif b[0] == b[-1]:
        return palindrom(b[1:-1])
    
    return False

a = input("Masukkan Kata: ").lower().replace(" ", "")
if palindrom(a):
    print("Palindrom")
else:
    print("Bukan Palindrom")