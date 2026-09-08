# متجر قطع غيار هيونداي إلنترا N
# ==================================
# برنامج بسيط يعرض قطع غيار السيارة، ويتيح للمستخدم البحث عن قطعة.
# إذا وجدت القطعة في المتجر يتم عرضها، ثم يفتح البرنامج بحث Google عن القطعة تلقائياً.

import webbrowser

# قائمة قطع الغيار المتوفرة في المتجر (اسم القطعة، السعر، التوفر)
parts_store = [
    {"name": "طقم فحمات فرامل أمامية (Brake Pads)", "price": 350, "available": True},
    {"name": "توربو أصلي (Turbocharger)", "price": 4200, "available": True},
    {"name": "شكمان رياضي (Cat-Back Exhaust)", "price": 3100, "available": True},
    {"name": "مساعدات كويلوفر (Coilovers)", "price": 3800, "available": False},
    {"name": "قفل تفاضلي (Limited-Slip Differential)", "price": 5200, "available": True},
    {"name": "فلتر هواء رياضي (Cold Air Intake)", "price": 650, "available": True},
    {"name": "بواجي احتراق (Spark Plugs)", "price": 180, "available": True},
    {"name": "طقم دبرياج معزز (Performance Clutch Kit)", "price": 2900, "available": True},
    {"name": "رديتر مبرد إضافي (Intercooler)", "price": 2200, "available": True},
    {"name": "جنوط رياضية 19 إنش (Sport Wheels)", "price": 6500, "available": False},
]


def search_part(query):
    """يبحث عن القطعة داخل المتجر بالاسم (بحث جزئي غير حساس لحالة الأحرف)."""
    query = query.strip().lower()
    results = [p for p in parts_store if query in p["name"].lower()]
    return results


def open_google_search(part_name):
    """يفتح بحث Google عن القطعة مع اسم السيارة."""
    search_query = f"{part_name} Hyundai Elantra N شراء"
    url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
    print(f"\nجاري فتح بحث Google عن: {part_name}")
    webbrowser.open(url)


def main():
    print("==========================================")
    print("   متجر قطع غيار هيونداي إلنترا N")
    print("==========================================\n")

    query = input("اكتب اسم القطعة التي تبحث عنها: ")
    results = search_part(query)

    if results:
        print(f"\nتم العثور على {len(results)} نتيجة/نتائج مطابقة:\n")
        for part in results:
            status = "متوفرة ✅" if part["available"] else "غير متوفرة حالياً ❌"
            print(f"- {part['name']} | السعر: {part['price']} ريال | {status}")
        # نفتح بحث Google عن أول نتيجة مطابقة
        open_google_search(results[0]["name"])
    else:
        print("\nلم يتم العثور على هذه القطعة في المتجر.")
        # حتى لو ما كانت موجودة بالمتجر، نبحث عنها في Google
        open_google_search(query)


if __name__ == "__main__":
    main()
