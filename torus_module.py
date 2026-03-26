import math
from deep_translator import GoogleTranslator

def check_point_in_torus(x, y, r, R):
    distance = math.hypot(x, y)
    min_r = min(r, R)
    max_r = max(r, R)
    is_inside = min_r <= distance <= max_r
    return distance, is_inside

def translate_text(text, target_lang):
    target_lang = target_lang.strip().lower()
    
    if target_lang in ['uk', 'ukr', 'ukrainian', 'українська']:
        return text
        
    try:
        translator = GoogleTranslator(source='uk', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        return text