from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79098765432"),
    Smartphone("Xiaomi", "13 Pro", "+79234567890"),
    Smartphone("Google", "Pixel 7", "+79345678901"),
    Smartphone("OnePlus", "11", "+79456789012")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")