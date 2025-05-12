#print("hello dream")
def valyuta_konvertor():
    print("Valyuta konvertoriga xush kelibsiz!")
    kurslar = {
        "USD": 12500,
        "EUR": 13500
    }

    miqdor = float(input("So‘m miqdorini kiriting: "))
    valyuta = input("Qaysi valyutaga o‘tkazmoqchisiz? (USD/EUR): ").upper()

    if valyuta in kurslar:
        natija = miqdor / kurslar[valyuta]
        print(f"{miqdor} so‘m = {natija:.2f} {valyuta}")
    else:
        print("Noto‘g‘ri valyuta kiritildi!")

valyuta_konvertor()