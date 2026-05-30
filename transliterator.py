from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Library supports Indic scripts only
LANG_MAP = {
    "hindi": sanscript.DEVANAGARI,
    "telugu": sanscript.TELUGU,
    "tamil": sanscript.TAMIL
}

def transliterate_item(word, lang):
    if lang == "english":
        return word

    if lang == "urdu":
        return word  # Urdu not supported by library

    if lang in LANG_MAP:
        local = transliterate(word, sanscript.ITRANS, LANG_MAP[lang])
        return f"{local} ({word})"

    return word
