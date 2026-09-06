import re

FINGLISH_DICT = {
    "salam": "سلام", "khoobi": "خوبی", "khubi": "خوبی", "chetori": "چطوری",
    "khoob": "خوب", "khoobam": "خوبم", "mamnun": "ممنون", "mersi": "مرسی",
    "khodahafez": "خداحافظ", "khodafez": "خداحافظ",
    "barande": "برنده", "barandeh": "برنده", "shodid": "شدید", "shodi": "شدی",
    "click": "کلیک", "konid": "کنید", "kon": "کن", "koni": "کنی",
    "jayeze": "جایزه", "begirid": "بگیرید", "begir": "بگیر",
    "vam": "وام", "fori": "فوری", "bedoone": "بدون", "bedoon": "بدون",
    "zamanat": "ضمانت", "zamin": "ضامن",
    "takhfif": "تخفیف", "forush": "فروش", "vizhe": "ویژه",
    "kasb": "کسب", "daramad": "درآمد", "internet": "اینترنت",
    "sarmaye": "سرمایه", "gozari": "گذاری", "moshavere": "مشاوره",
    "rayegan": "رایگان", "soode": "سود", "mahane": "ماهانه", "tazmini": "تضمینی",
    "sabt": "ثبت", "nam": "نام", "zarfiat": "ظرفیت", "mahdood": "محدود",
    "shoma": "شما", "hastam": "هستم", "hasti": "هستی", "hastid": "هستید",
    "man": "من", "to": "تو", "ma": "ما", "shoma": "شما",
    "miram": "میرم", "miam": "میام", "miai": "میای", "miayad": "میاد",
    "khune": "خونه", "daneshgah": "دانشگاه", "jalase": "جلسه", "farda": "فردا",
    "emruz": "امروز", "emshab": "امشب", "alan": "الان", "hala": "حالا",
    "faghat": "فقط", "hamin": "همین", "vaghti": "وقتی", "chizi": "چیزی",
    "khoresh": "خوراک", "khordam": "خوردم", "residam": "رسیدم", "residi": "رسیدی",
    "daftar": "دفتر", "kelid": "کلید", "kojast": "کجاست",
    "gharardad": "قرارداد", "emza": "امضا", "kardam": "کردم",
    "ostad": "استاد", "nomre": "نمره", "proje": "پروژه", "sabt": "ثبت", "nashode": "نشده",
    "mishe": "میشه", "check": "چک", "khahesh": "خواهش", "mikonam": "میکنم",
    "file": "فایل", "barresi": "بررسی", "tamas": "تماس", "begirid": "بگیرید",
    "shomare": "شماره", "vared": "وارد", "konid": "کنید",
    "hesab": "حساب", "bank": "بانک", "bankiye": "بانکی", "mashkuk": "مشکوک",
    "tayid": "تایید", "hoviat": "هویت",
    "package": "بسته", "tamoom": "تمام", "shode": "شده", "tamdid": "تمدید",
    "link": "لینک", "zir": "زیر", "baz": "باز",
    "gooshi": "گوشی", "iphone": "آیفون", "tahvil": "تحویل",
    "kart": "کارت", "shomare": "شماره",
    "webinar": "وبینار", "amoozesh": "آموزش", "dolari": "دلاری",
    "cheragh": "چراغ", "sabz": "سبز", "roshan": "روشن", "eghdam": "اقدام",
    "forsat": "فرصت", "talaee": "طلایی", "pool": "پول",
    "dar": "در", "biyarid": "بیارید",
    "toman": "تومان", "million": "میلیون", "hezar": "هزار",
    "khastegar": "خواستگار", "avalie": "اولیه", "kafie": "کافیه", "start": "استارت",
    "code": "کد", "codeye": "کد", "fa'al": "فعال", "saat": "ساعت", "az": "از", "dast": "دست",
    "nadid": "ندید", "arz": "ارز", "digital": "دیجیتال", "ruzane": "روزانه",
    "ozv": "عضو", "shid": "شید", "ja": "جا", "khali": "خالی", "nadarim": "نداریم",
    "ta": "تا", "payane": "پایان", "hafte": "هفته", "moatabar": "معتبر", "ast": "است",
    "va": "و", "ba": "با", "ke": "که", "ro": "رو", "be": "به", "ye": "یه",
    "in": "این", "un": "اون", "on": "اون",
    "saate": "ساعت", "chand": "چند", "darim": "داریم", "dari": "داری",
    "darsad": "درصد", "sari": "سریع", "nare": "نره", "mota'men": "مطمئن",
    "motmaen": "مطمئن", "fardaa": "فردا", "mibinamet": "می‌بینمت",
    "reschedule": "تغییر زمان", "kelas": "کلاس", "hich": "هیچ", "kar": "کار",
    "ziad": "زیاد", "bud": "بود", "shod": "شد", "shodam": "شدم", "raftam": "رفتم",
    "khaste": "خسته", "nabashi": "نباشی", "zahmat": "زحمت", "zahmatet": "زحمتت",
    "komak": "کمک", "komaket": "کمکت",
    "e": "",
}


def split_hyphenated(text):
    return re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", text)


def merge_spaced_letters(text):
    pattern = re.compile(
        r"\b[A-Za-z](?:[^A-Za-z0-9\u0600-\u06FF]{1,3}[A-Za-z]){2,}\b"
    )

    def merge(match):
        letters = re.findall(r"[A-Za-z]", match.group(0))
        return "".join(letters)

    return pattern.sub(merge, text)


def collapse_latin_elongation(word):
    return re.sub(r"([a-zA-Z])\1{1,}", r"\1", word)


def transliterate_word(word):
    lw = word.lower().strip(".,!?؟،؛:'")
    if lw in FINGLISH_DICT:
        return FINGLISH_DICT[lw]
    collapsed = collapse_latin_elongation(lw)
    if collapsed in FINGLISH_DICT:
        return FINGLISH_DICT[collapsed]
    return word


def transliterate_finglish(text):
    if not isinstance(text, str):
        return ""
    text = split_hyphenated(text)
    text = merge_spaced_letters(text)
    words = text.split()
    result = []
    for w in words:
        if re.fullmatch(r"[A-Za-z\.\,\!\?']+", w):
            translated = transliterate_word(w)
            if translated:  
                result.append(translated)
        else:
            result.append(w)
    return " ".join(result)


