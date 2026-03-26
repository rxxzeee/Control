import json
import sys
import os
from torus_module import check_point_in_torus, translate_text

DATA_FILE = 'MyData.json'

def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            x, y = data['x'], data['y']
            r, R = data['r'], data['R']
            lang = data['lang']
            
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print("Приклад 1 (при відсутності або некоректних даних в файлі MyData)")
        coords_input = input("Введіть координати точки А(x,y): ").split()
        
        try:
            x, y = float(coords_input[0]), float(coords_input[1])
            r = float(input("Введіть радіус першого кола r: "))
            R = float(input("Введіть радіус другого кола R: "))
        except ValueError:
            print("Помилка: введено некоректні числові дані.")
            sys.exit(1)
            
        lang = input("Введіть мову інтерфейсу (наприклад, en, pl, de, uk): ").strip()

        new_data = {'x': x, 'y': y, 'r': r, 'R': R, 'lang': lang}
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
            
        print(f"Дані збережено в файл {DATA_FILE}")
        sys.exit(0)

    distance, is_inside = check_point_in_torus(x, y, r, R)

    fx, fy = (int(x) if x.is_integer() else x), (int(y) if y.is_integer() else y)
    fr, fR = (int(r) if r.is_integer() else r), (int(R) if R.is_integer() else R)
    
    dist_str = f"{distance:.2f}".replace('.', ',') if lang.lower() in ['uk', 'ukr', 'українська'] else f"{distance:.2f}"

    lbl_lang = translate_text("Мова:", lang)
    lbl_coords = translate_text("Координати точки А(x,y):", lang)
    lbl_r = translate_text("Радіус першого кола r:", lang)
    lbl_R = translate_text("Радіус другого кола R:", lang)
    lbl_dist = translate_text("Відстань до точки A:", lang)

    if is_inside:
        result_text = translate_text("Точка A знаходиться всередині тора.", lang)
    else:
        result_text = translate_text("Точка A не знаходиться всередині тора.", lang)
    
    result_text = result_text.replace("A ", f"A({fx}, {fy}) ")

    print(translate_text("Приклад 2 (при успішному читанні даних з файлу MyData)", lang))
    print(f"{lbl_lang} {lang}")
    print(f"{lbl_coords} {fx} {fy}")
    print(f"{lbl_r} {fr}")
    print(f"{lbl_R} {fR}")
    print(f"{lbl_dist} {dist_str}")
    print(result_text)

if __name__ == "__main__":
    main()