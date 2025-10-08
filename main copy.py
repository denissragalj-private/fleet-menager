'''
- ispis svih vozila
- ispis detalja jednog vozila
- dodavanje novog vozila
'''
import json
from typing import Dict, List


FILE_PATH = 'sample_data/trucks_sample_eu.json'


#region FUNKCIJE
def load_from_json() -> List:
    try:
        with open(FILE_PATH, 'r') as file_reader:
            return json.load(file_reader)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
        return []

def save_to_json(data: List) -> None:
    try:
        with open(FILE_PATH, 'w') as file_writer:
            json.dump(data, file_writer, indent=4)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')  
        return []
    

def display_vehicle_data(vehicle: Dict) -> None:
    field_width = 20  # širina polja za nazive
    value_width = 40  # širina polja za vrijednosti
    
    print("\n" + "=" * (field_width + value_width))
    print(f"{'ID:':<{field_width}}{vehicle['id']:>{value_width}}")
    print(f"{'Broj šasije:':<{field_width}}{vehicle['vin']:>{value_width}}")
    print(f"{'Proizvođač:':<{field_width}}{vehicle['make']:>{value_width}}")
    print(f"{'Model:':<{field_width}}{vehicle['model']:>{value_width}}")
    print(f"{'Godina:':<{field_width}}{vehicle['year']:>{value_width}}")
    print(f"{'Tip:':<{field_width}}{vehicle['type']:>{value_width}}")
    print(f"{'Broj osovina:':<{field_width}}{vehicle['axle_config']:>{value_width}}")
    print(f"{'Euro standard:':<{field_width}}{vehicle['euro_standard']:>{value_width}}")
    print(f"{'Snaga motora (kW):':<{field_width}}{vehicle['engine_power_kw']:>{value_width}}")
    print(f"{'Gorivo:':<{field_width}}{vehicle['fuel']:>{value_width}}")
    print(f"{'GVW (kg):':<{field_width}}{vehicle['gvw_kg']:>{value_width}}")
    print(f"{'Payload (kg):':<{field_width}}{vehicle['payload_kg']:>{value_width}}")
    print(f"{'Dužina (m):':<{field_width}}{vehicle['length_m']:>{value_width}}")
    print(f"{'Širina (m):':<{field_width}}{vehicle['width_m']:>{value_width}}")
    print(f"{'Visina (m):':<{field_width}}{vehicle['height_m']:>{value_width}}")
    print(f"{'Datum kupovine:':<{field_width}}{vehicle['purchase_date']:>{value_width}}")
    print(f"{'Datum registracije:':<{field_width}}{vehicle['registration_date']:>{value_width}}")
    print(f"{'Kod države:':<{field_width}}{vehicle['country_code']:>{value_width}}")
    print(f"{'Registarska oznaka:':<{field_width}}{vehicle['license_plate']:>{value_width}}")
    print(f"{'Boja:':<{field_width}}{vehicle['color']:>{value_width}}")
    print("=" * (field_width + value_width) + "\n")

def display_all_vehicles(data: List): # prikaz svih vozila
    for truck in data:              # prolazak kroz sva vozila
        display_vehicle_data(truck)  #

def add_new_vehicle(data: List) -> None:
    new_vehicle = {
        "id": input("Unesite ID vozila: "),
        "vin": input("Unesite VIN vozila: "),
        "make": input("Unesite proizvođača vozila: "),
        "model": input("Unesite model vozila: "),
        "year": int(input("Unesite godinu proizvodnje vozila: ")),
        "type": input("Unesite tip vozila: "),
        "axle_config": input("Unesite broj osaovina vozila: "),
        "euro_standard": input("Unesite euro standard vozila: "),
        "engine_power_kw": int(input("Unesite snagu motora u kW: ")),
        "fuel": input("Unesite gorivo vozila: "),
        "gvw_kg": int(input("Unesite ukupnu masu vozila u kg: ")),
        "payload_kg": int(input("Unesite nosivost vozila u kg: ")),
        "length_m": float(input("Unesite duzinu vozila u metrima: ")),
        "width_m": float(input("Unesite sirinu vozila u metrima: ")),
        "height_m": float(input("Unesite visinu vozila u metrima: ")),
        "purchase_date": input("Unesite datum kupovine (YYYY-MM-DD): "),
        "registration_date": input("Unesite datum registracije (YYYY-MM-DD): "),
        "country_code": input("Unesite drzavni kod registracije: "),
        "license_plate": input("Unesite registarsku oznaku vozila: "),
        "color": input("Unesite boju vozila: ")
    }


    data.append(new_vehicle)
    # Spremanje podataka natrag u JSON datoteku
    save_to_json(data)
    print("Novo vozilo je uspješno dodano.")

#endregion


data = load_from_json()
print(data[0] if len(data) > 0 else 'Nema podataka u datoteci')
display_all_vehicles(data)


#region MAIN

# 0️⃣
# 1️⃣
# 2️⃣
# 3️⃣
# 4️⃣
# 5️⃣
# 6️⃣
# 7️⃣
# 8️⃣
# 9️⃣
# 🔟
while True:
    print('1️⃣. Ispis svih vozila')
    print('2️⃣. Ispis detalja jednog vozila')
    print('3️⃣. Dodavanje novog vozila')
    print('0️⃣. Izlaz')
    choice = input('Izaberite opciju: ')

    if choice == '1':
        display_all_vehicles(data)
    elif choice == '2':
        vehicle_id = input('Unesite ID vozila: ')
        vehicle = next((v for v in data if v['id'] == vehicle_id), None)
        if vehicle:
            display_vehicle_data(vehicle)
        else:
            print('Vozilo nije pronađeno.')
    elif choice == '3':
        add_new_vehicle(data)
    elif choice == '0':
        print('Izlaz iz programa.')
        break
    else:
        print('Nepoznata opcija. Molimo pokušajte ponovo.')