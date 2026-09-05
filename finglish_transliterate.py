import re

# دیکشنری کلمات پرکاربرد فینگلیش -> فارسی (اسپم + محاوره‌ای رایج)
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
    "e": "",  # حرف اضافه/رابط باقیمانده از کلمات خط‌تیره‌دار (vam-e)
}


def split_hyphenated(text):
    """کلمات دارای خط‌تیره را از هم جدا می‌کند (vam-e -> vam e)."""
    return re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", text)


def merge_spaced_letters(text):
    """
    حروف لاتین که تک‌تک با هر نوع جداکننده (فاصله، نقطه، ایموجی، ستاره،
    آندرلاین، خط‌تیره و...) از هم جدا شده‌اند را به یک کلمه می‌چسباند.
    مثال‌ها: 'b r a n d e', 'b.r.a.n.d.e', 'b*r*a*n*d*e', 'b_r_a_n_d_e',
    'b😊r😊a😊n😊d😊e' -> همه به 'brande' تبدیل می‌شوند.
    """
    # الگو: یک حرف لاتین، سپس (۱ تا ۳ کاراکتر غیرحرف/غیررقم/غیرفارسی + یک حرف لاتین)
    # حداقل دو بار تکرار (یعنی حداقل ۳ حرف لاتین جدا از هم)، با مرز کلمه در دو طرف
    # تا وسط یک کلمه‌ی معمولی یا ابتدای کلمه‌ی بعدی را نبلعد
    pattern = re.compile(
        r"\b[A-Za-z](?:[^A-Za-z0-9\u0600-\u06FF]{1,3}[A-Za-z]){2,}\b"
    )

    def merge(match):
        letters = re.findall(r"[A-Za-z]", match.group(0))
        return "".join(letters)

    return pattern.sub(merge, text)


def collapse_latin_elongation(word):
    """کشیدگی حروف در کلمات لاتین را حذف می‌کند (baraaande -> barande)."""
    return re.sub(r"([a-zA-Z])\1{1,}", r"\1", word)


def transliterate_word(word):
    """اگر کلمه لاتین در دیکشنری بود، معادل فارسی برگردان."""
    lw = word.lower().strip(".,!?؟،؛:'")
    if lw in FINGLISH_DICT:
        return FINGLISH_DICT[lw]
    # اگر تطابق مستقیم نبود، کشیدگی حروف را حذف و دوباره امتحان کن
    collapsed = collapse_latin_elongation(lw)
    if collapsed in FINGLISH_DICT:
        return FINGLISH_DICT[collapsed]
    return word


def transliterate_finglish(text):
    """
    هر کلمه‌ی لاتین موجود در متن را (در صورت وجود در دیکشنری) به فارسی تبدیل می‌کند.
    کلماتی که در دیکشنری نیستند دست‌نخورده باقی می‌مانند.
    """
    if not isinstance(text, str):
        return ""
    text = split_hyphenated(text)
    text = merge_spaced_letters(text)
    words = text.split()
    result = []
    for w in words:
        # فقط کلمات لاتین را بررسی کن
        if re.fullmatch(r"[A-Za-z\.\,\!\?']+", w):
            translated = transliterate_word(w)
            if translated:  # اگر خالی نبود (مثل حرف رابط "e") اضافه کن
                result.append(translated)
        else:
            result.append(w)
    return " ".join(result)


if __name__ == "__main__":
    tests = [
        "barande shodid! click konid va jayeze begirid",
        "salam khoobi? farda saate chand jalase darim?",
        "vam-e fori bedoone zamanat, sari eghdam konid ta forsat az dast nare.",
        "sarmaye gozari mota'men ba soode 30 darsad mahane. moshavere rayegan.",
        "ok, fardaa mibinamet, thanks",
    ]
    for t in tests:
        print(f"قبل : {t}")
        print(f"بعد : {transliterate_finglish(t)}")
        print()
