# متجر قطع غيار هيونداي إلنترا N
# ==================================
# قائمة القطع الحقيقية مأخوذة من متجر whoosh motorsports (whooshmotorsports.com)
# البرنامج يبحث عن القطعة، ويجهز رابط واتساب برسالة جاهزة يرسلها المستخدم
# لرقم المتجر — وإرسال الرسالة يعني إننا بنراجع الطلب ونرد إذا كانت متوفرة.

import webbrowser
import urllib.parse

WHATSAPP_NUMBER = "966546300074"  # 0546300074 بصيغة دولية

parts_store = [
    {"name": "whoosh motorsports JDM Style Single Exit Exhaust Kit", "price": 399.99},
    {"name": "whoosh motorsports 4\" Full Length Downpipe", "price": 399.99},
    {"name": "whoosh motorsports 4\" Titanium Single Exit RACE Exhaust Kit", "price": 525.00},
    {"name": "whoosh motorsports Titanium Mid Pipe Kit", "price": 574.99},
    {"name": "whoosh motorsports Titanium Axle Back Exhaust Kit", "price": 999.99},
    {"name": "whoosh motorsports 3\" Titanium Single Exit RACE Exhaust Kit", "price": 449.99},
    {"name": "PURE450 Hybrid Turbo Upgrade", "price": 1095.00},
    {"name": "PURE550 Hybrid Turbo Upgrade", "price": 1595.00},
    {"name": "T51R Mod PURE550 Hybrid Turbo Upgrade", "price": 2195.00},
    {"name": "Hyundai MOBIS CN7 OEM Turbocharger", "price": 1149.99},
    {"name": "Ramair Performance Intake Kit", "price": 399.99},
    {"name": "whoosh motorsports 4\" POWDER COATED Titanium Intake Kit", "price": 524.99},
    {"name": "whoosh motorsports 4\" Titanium Intake Kit", "price": 449.99},
    {"name": "whoosh motorsports V2 4\" Titanium Intake Kit", "price": 499.99},
    {"name": "whoosh motorsports Silicone Breather Hose", "price": 19.99},
    {"name": "Lap3 Tuning STAGE 1", "price": 1600.00},
    {"name": "Lap3 Tuning STAGE 1.5", "price": 1750.00},
    {"name": "Lap3 Tuning STAGE 2", "price": 1850.00},
    {"name": "Lap3 Tuning STAGE 2.5", "price": 1950.00},
    {"name": "Lap3 Tuning Track eLSD ECU Tune", "price": 850.00},
    {"name": "whoosh motorsports Coolant Hose Kit", "price": 139.99},
    {"name": "Koyo Racing Radiator", "price": 469.99},
    {"name": "HKS Super Power Flow Air Filter Upgrade Kit", "price": 199.99},
    {"name": "AWE SwitchPath Cat-Back Exhaust System", "price": 1695.00},
    {"name": "AWE Track Edition Cat-Back Exhaust System", "price": 1245.00},
    {"name": "Carbon Fiber Mirror Caps", "price": 249.99},
    {"name": "LIQUI MOLY 5W-40 Oil Change Service Kit", "price": 79.99},
    {"name": "N Performance Engine Oil 0W-30", "price": 39.99},
    {"name": "XCLUTCH Stage 1 Clutch Kit", "price": 1540.04},
    {"name": "Brake Cooling Ducts Upgrade", "price": 59.99},
    {"name": "whoosh motorsports Brake Fluid Reservoir Sock", "price": 14.99},
    {"name": "whoosh motorsports Coolant Reservoir", "price": 349.99},
    {"name": "whoosh motorsports AEVS Active Exhaust Valve Spring", "price": 18.99},
    {"name": "whoosh motorsports Premium HD AEVS", "price": 24.99},
    {"name": "whoosh motorsports Titanium Clamp-On Exhaust Tips", "price": 99.99},
    {"name": "whoosh motorsports Black Coated Stainless Exhaust Tips", "price": 89.99},
    {"name": "whoosh motorsports Front Mount Intercooler Upgrade", "price": 675.00},
    {"name": "Megan Racing Front Mount Intercooler Kit", "price": 489.99},
    {"name": "Forge Motorsport Intercooler", "price": 1070.00},
    {"name": "Forge Cold Side Boost Pipe", "price": 299.99},
    {"name": "aFe Silver Bullet Throttle Body Spacer Kit", "price": 139.00},
    {"name": "Berrys Magnetic Paddle Shifters", "price": 420.00},
    {"name": "N Performance Sabelt Tow Strap Set", "price": 329.99},
    {"name": "Forge Motorsport Oil Cooler Kit", "price": 899.00},
    {"name": "whoosh motorsports Turbo Inlet Kit", "price": 149.00},
    {"name": "A.O. Customs PTFE Turbo Inlet Gasket", "price": 14.99},
    {"name": "WELDSPEED Intake Manifold", "price": 1499.00},
    {"name": "N Performance Carbon Fiber Exhaust Tips", "price": 499.99},
    {"name": "whoosh motorsports Lower Torque Arm Bushing Set", "price": 24.99},
    {"name": "whoosh motorsports Trunk Pull Strap", "price": 19.99},
    {"name": "whoosh motorsports HKS Blow Off Valve Adapter Kit", "price": 44.99},
    {"name": "TurboXS HKS Blow Off Valve Adapter Kit", "price": 54.99},
    {"name": "whoosh motorsports Performance Coil Packs (Set of 4)", "price": 124.99},
    {"name": "whoosh motorsports Lightweight Water Pump Pulley", "price": 49.99},
    {"name": "whoosh motorsports Performance Downpipe", "price": 289.99},
    {"name": "XFORCE 4\" Turbo Downpipe with Hi-Flow Cat", "price": 835.00},
    {"name": "Custom Performance Engineering QKspl Cast Bellmouth Downpipe", "price": 664.05},
    {"name": "whoosh motorsports Titanium Downpipe Stud Kit", "price": 49.99},
    {"name": "ARP Downpipe Hardware Kit", "price": 64.99},
    {"name": "Hyundai OEM Turbo to Downpipe Gasket", "price": 50.84},
    {"name": "whoosh motorsports Exhaust Hanger for Downpipe", "price": 14.99},
    {"name": "OEM Hyundai Replacement Exhaust Hanger for Downpipe", "price": 24.95},
    {"name": "Hyundai OEM Downpipe to Mid Pipe Gasket", "price": 19.99},
    {"name": "Mishimoto Exhaust Heat Wrap Set", "price": 74.00},
    {"name": "whoosh motorsports Turbo Inlet Bolt Kit", "price": 14.99},
    {"name": "whoosh motorsports Titanium License Plate Bolt Kit", "price": 14.99},
    {"name": "whoosh motorsports Titanium Coil Pack Bolt Kit", "price": 19.99},
    {"name": "Forge Short and Side Shifter Kit", "price": 152.01},
    {"name": "SYSTEM UPGRADE Korea Short Shifter Kit", "price": 280.00},
    {"name": "Velossa Tech BIG MOUTH Ram Air Intake Snorkel", "price": 159.00},
    {"name": "Velossa Tech BIG MOUTH Ram Air Intake Snorkel Lit Kit", "price": 299.00},
    {"name": "Torcon Trunk Puller Strap", "price": 29.00},
    {"name": "EPR Carbon Fiber V2M Hood", "price": 999.99},
    {"name": "Seibon OEM-Style Carbon Fiber Hood", "price": 1188.00},
    {"name": "EPR Carbon Fiber Vented Hood", "price": 999.99},
    {"name": "EPR Carbon Fiber TYPE-V Vented Hood", "price": 999.99},
    {"name": "EPR Carbon Fiber OEM Style Hood", "price": 999.99},
    {"name": "EPR Carbon Fiber Trunk", "price": 799.99},
    {"name": "Genuine Carbon Fiber Rear Spoiler Extension", "price": 1099.99},
    {"name": "MAXTON DESIGN Rear Spoiler Cap", "price": 225.00},
    {"name": "N Performance Intake Kit", "price": 574.99},
    {"name": "Forge Motorsport Revised Induction Kit", "price": 529.00},
    {"name": "Injen Cold Air Intake - Red Wrinkle Finish", "price": 334.95},
    {"name": "Injen Cold Air Intake - Black Wrinkle Finish", "price": 334.95},
    {"name": "Injen Cold Air Intake - Polished Finish", "price": 334.95},
    {"name": "Injen Hydroshield Water Repellant Pre-Filter Cover", "price": 27.95},
    {"name": "aFe Takeda Momentum Cold Air Intake w/Pro 5R Filter", "price": 416.00},
    {"name": "aFe Takeda Momentum Cold Air Intake w/Pro DRY S Filter", "price": 416.00},
    {"name": "aFe Takeda Stage-2 Cold Air Intake w/Pro 5R Filter", "price": 368.00},
    {"name": "aFe Takeda Stage-2 Cold Air Intake w/Pro DRY S Filter", "price": 368.00},
    {"name": "K&N Typhoon Intake System", "price": 449.99},
    {"name": "Forge Motorsport Turbo Inlet Adapter", "price": 227.42},
    {"name": "aFe Takeda Turbo Inlet", "price": 149.99},
    {"name": "whoosh motorsports aFe Takeda Inlet Hose Replacement", "price": 49.99},
    {"name": "whoosh motorsports Replacement FOAM Filter", "price": 74.99},
    {"name": "whoosh motorsports Replacement Pleated Filter", "price": 74.99},
    {"name": "Forge Motorsport Replacement Pleated Filter", "price": 126.44},
    {"name": "Forge Motorsport Replacement FOAM Filter", "price": 133.04},
    {"name": "Heat Defense GOLD Protective Tape", "price": 52.04},
    {"name": "Pierburg BOV Solenoid Upgrade", "price": 119.99},
    {"name": "whoosh motorsports VTA BOV Block-Off Cap", "price": 19.99},
    {"name": "Go Fast Bits TMS Respons Blow Off Valve Kit", "price": 307.80},
    {"name": "Turbosmart Kompact Dual Port Blow Off Valve", "price": 261.89},
    {"name": "Forge Motorsport Atmospheric and Recirculating Valve", "price": 301.19},
    {"name": "SPEEDY Blow Off Valve Kit", "price": 273.00},
    {"name": "HKS SQV IV BLACK EDITION Blow Off Valve", "price": 324.50},
    {"name": "HKS SQV IV SILVER Blow Off Valve", "price": 324.50},
    {"name": "HKS SSQV BOV Inserts", "price": 27.50},
    {"name": "Forge Motorsport Valve Spring Tuning Kit", "price": 36.94},
    {"name": "whoosh motorsports Billet Oil Filler Cap", "price": 39.99},
    {"name": "HKS Billet Oil Filler Cap", "price": 99.99},
    {"name": "Forge Motorsport Carbon Fiber Engine Cover", "price": 591.50},
    {"name": "Hyundai Upgraded High Pressure Fuel Pump", "price": 299.99},
    {"name": "Hyundai G70 High Pressure Fuel Pump Upgrade", "price": 309.99},
    {"name": "Hyundai +8% Flow Injector Set of 4 w/Install Kit", "price": 374.99},
    {"name": "Hyundai +15% Flow Injector Set of 4 w/Install Kit", "price": 349.99},
    {"name": "Hyundai Fuel Injector Service Kit", "price": 49.99},
    {"name": "ARP Custom Aged CA625+ Head Stud Kit", "price": 499.99},
]


def search_part(query):
    """يبحث عن القطعة داخل المتجر بالاسم (بحث جزئي غير حساس لحالة الأحرف)."""
    query = query.strip().lower()
    return [p for p in parts_store if query in p["name"].lower()]


def build_whatsapp_url(part_name, price):
    """يجهز رابط واتساب برسالة جاهزة للاستفسار عن القطعة."""
    message = (
        f"مرحباً، أبغى أستفسر عن توفر هذي القطعة لسيارة إلنترا N:\n\n"
        f"\"{part_name}\"\n"
        f"السعر التقريبي: ${price:.2f}\n\n"
        f"ياليت تتأكدون من التوفر وترجعون لي."
    )
    encoded_message = urllib.parse.quote(message)
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"


def main():
    print("==========================================")
    print("   متجر قطع غيار هيونداي إلنترا N")
    print(f"   عدد القطع المتوفرة: {len(parts_store)}")
    print("==========================================\n")

    query = input("اكتب اسم القطعة التي تبحث عنها: ")
    results = search_part(query)

    if results:
        print(f"\nتم العثور على {len(results)} نتيجة/نتائج مطابقة:\n")
        for part in results:
            print(f"- {part['name']} | السعر: ${part['price']:.2f}")

        chosen = results[0]
        url = build_whatsapp_url(chosen["name"], chosen["price"])
        print(f"\nجاري فتح واتساب للاستفسار عن: {chosen['name']}")
        print("إرسال الرسالة يعني إننا بنراجع الطلب، وإذا كانت القطعة متوفرة حنرد عليك.")
        webbrowser.open(url)
    else:
        print("\nلم يتم العثور على هذه القطعة في قائمة المتجر.")
        url = build_whatsapp_url(query, 0)
        print("بنفتح لك واتساب على نفس الرقم عشان تسأل عنها يدوياً.")
        webbrowser.open(url)


if __name__ == "__main__":
    main()
