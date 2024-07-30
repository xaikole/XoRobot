import random
import string
from faker import Faker
from pyrogram import filters
from Ava import Jarvis as app

# Mapping of country codes to country names and their corresponding phone codes
COUNTRY_CODES = {
    "ad": ("Andorra", "+376"), "ae": ("United Arab Emirates", "+971"), "af": ("Afghanistan", "+93"),
    "ag": ("Antigua and Barbuda", "+1-268"), "ai": ("Anguilla", "+1-264"), "al": ("Albania", "+355"),
    "am": ("Armenia", "+374"), "ao": ("Angola", "+244"), "aq": ("Antarctica", "+672"), "ar": ("Argentina", "+54"),
    "as": ("American Samoa", "+1-684"), "at": ("Austria", "+43"), "au": ("Australia", "+61"), "aw": ("Aruba", "+297"),
    "ax": ("Åland Islands", "+358-18"), "az": ("Azerbaijan", "+994"), "ba": ("Bosnia and Herzegovina", "+387"),
    "bb": ("Barbados", "+1-246"), "bd": ("Bangladesh", "+880"), "be": ("Belgium", "+32"), "bf": ("Burkina Faso", "+226"),
    "bg": ("Bulgaria", "+359"), "bh": ("Bahrain", "+973"), "bi": ("Burundi", "+257"), "bj": ("Benin", "+229"),
    "bl": ("Saint Barthélemy", "+590"), "bm": ("Bermuda", "+1-441"), "bn": ("Brunei Darussalam", "+673"),
    "bo": ("Bolivia", "+591"), "bq": ("Bonaire, Sint Eustatius and Saba", "+599"), "br": ("Brazil", "+55"),
    "bs": ("Bahamas", "+1-242"), "bt": ("Bhutan", "+975"), "bv": ("Bouvet Island", ""), "bw": ("Botswana", "+267"),
    "by": ("Belarus", "+375"), "bz": ("Belize", "+501"), "ca": ("Canada", "+1"), "cc": ("Cocos (Keeling) Islands", "+61"),
    "cd": ("Congo, Democratic Republic of the", "+243"), "cf": ("Central African Republic", "+236"),
    "cg": ("Congo", "+242"), "ch": ("Switzerland", "+41"), "ci": ("Côte d'Ivoire", "+225"), "ck": ("Cook Islands", "+682"),
    "cl": ("Chile", "+56"), "cm": ("Cameroon", "+237"), "cn": ("China", "+86"), "co": ("Colombia", "+57"),
    "cr": ("Costa Rica", "+506"), "cu": ("Cuba", "+53"), "cv": ("Cabo Verde", "+238"), "cw": ("Curaçao", "+599"),
    "cx": ("Christmas Island", "+61"), "cy": ("Cyprus", "+357"), "cz": ("Czechia", "+420"), "de": ("Germany", "+49"),
    "dj": ("Djibouti", "+253"), "dk": ("Denmark", "+45"), "dm": ("Dominica", "+1-767"), "do": ("Dominican Republic", "+1-809"),
    "dz": ("Algeria", "+213"), "ec": ("Ecuador", "+593"), "ee": ("Estonia", "+372"), "eg": ("Egypt", "+20"),
    "eh": ("Western Sahara", "+212"), "er": ("Eritrea", "+291"), "es": ("Spain", "+34"), "et": ("Ethiopia", "+251"),
    "fi": ("Finland", "+358"), "fj": ("Fiji", "+679"), "fm": ("Micronesia", "+691"), "fo": ("Faroe Islands", "+298"),
    "fr": ("France", "+33"), "ga": ("Gabon", "+241"), "gb": ("United Kingdom", "+44"), "gd": ("Grenada", "+1-473"),
    "ge": ("Georgia", "+995"), "gf": ("French Guiana", "+594"), "gg": ("Guernsey", "+44-1481"), "gh": ("Ghana", "+233"),
    "gi": ("Gibraltar", "+350"), "gl": ("Greenland", "+299"), "gm": ("Gambia", "+220"), "gn": ("Guinea", "+224"),
    "gp": ("Guadeloupe", "+590"), "gq": ("Equatorial Guinea", "+240"), "gr": ("Greece", "+30"), "gt": ("Guatemala", "+502"),
    "gu": ("Guam", "+1-671"), "gw": ("Guinea-Bissau", "+245"), "gy": ("Guyana", "+592"), "hk": ("Hong Kong", "+852"),
    "hm": ("Heard Island and McDonald Islands", ""), "hn": ("Honduras", "+504"), "hr": ("Croatia", "+385"),
    "ht": ("Haiti", "+509"), "hu": ("Hungary", "+36"), "id": ("Indonesia", "+62"), "ie": ("Ireland", "+353"), "il": ("Israel", "+972"),
    "im": ("Isle of Man", "+44-1624"), "in": ("India", "+91"), "io": ("British Indian Ocean Territory", "+246"), "iq": ("Iraq", "+964"),
    "ir": ("Iran", "+98"), "is": ("Iceland", "+354"), "it": ("Italy", "+39"), "je": ("Jersey", "+44-1534"), "jm": ("Jamaica", "+1-876"),
    "jn": ("Jinmen", "+886"), "jo": ("Jordan", "+962"), "jp": ("Japan", "+81"), "ke": ("Kenya", "+254"), "kg": ("Kyrgyzstan", "+996"),
    "kh": ("Cambodia", "+855"), "ki": ("Kiribati", "+686"), "km": ("Comoros", "+269"), "kn": ("Saint Kitts and Nevis", "+1-869"),
    "kp": ("North Korea", "+850"), "kr": ("South Korea", "+82"), "kw": ("Kuwait", "+965"), "ky": ("Cayman Islands", "+1-345"),
    "kz": ("Kazakhstan", "+7"), "la": ("Lao People's Democratic Republic", "+856"), "lb": ("Lebanon", "+961"),
    "lc": ("Saint Lucia", "+1-758"), "li": ("Liechtenstein", "+423"), "lk": ("Sri Lanka", "+94"), "lr": ("Liberia", "+231"),
    "ls": ("Lesotho", "+266"), "lt": ("Lithuania", "+370"), "lu": ("Luxembourg", "+352"), "lv": ("Latvia", "+371"), "ly": ("Libya", "+218"),
    "ma": ("Morocco", "+212"), "mc": ("Monaco", "+377"), "md": ("Moldova", "+373"), "me": ("Montenegro", "+382"),
    "mf": ("Saint Martin", "+590"), "mg": ("Madagascar", "+261"), "mh": ("Marshall Islands", "+692"), "mk": ("North Macedonia", "+389"),
    "ml": ("Mali", "+223"), "mm": ("Myanmar", "+95"), "mn": ("Mongolia", "+976"), "mo": ("Macao", "+853"), "mp": ("Northern Mariana Islands", "+1-670"),
    "mq": ("Martinique", "+596"), "mr": ("Mauritania", "+222"), "ms": ("Montserrat", "+1-664"), "mt": ("Malta", "+356"), "mu": ("Mauritius", "+230"),
    "mv": ("Maldives", "+960"), "mw": ("Malawi", "+265"), "mx": ("Mexico", "+52"), "my": ("Malaysia", "+60"), "mz": ("Mozambique", "+258"),
    "na": ("Namibia", "+264"), "nc": ("New Caledonia", "+687"), "ne": ("Niger", "+227"), "nf": ("Norfolk Island", "+672"),
    "ng": ("Nigeria", "+234"), "ni": ("Nicaragua", "+505"), "nl": ("Netherlands", "+31"), "no": ("Norway", "+47"), "np": ("Nepal", "+977"),
    "nr": ("Nauru", "+674"), "nu": ("Niue", "+683"), "nz": ("New Zealand", "+64"), "om": ("Oman", "+968"), "pa": ("Panama", "+507"),
    "pe": ("Peru", "+51"), "pf": ("French Polynesia", "+689"), "pg": ("Papua New Guinea", "+675"), "ph": ("Philippines", "+63"),
    "pk": ("Pakistan", "+92"), "pl": ("Poland", "+48"), "pm": ("Saint Pierre and Miquelon", "+508"), "pn": ("Pitcairn", "+64"),
    "pr": ("Puerto Rico", "+1-787"), "pt": ("Portugal", "+351"), "pw": ("Palau", "+680"), "py": ("Paraguay", "+595"), "qa": ("Qatar", "+974"),
    "re": ("Réunion", "+262"), "ro": ("Romania", "+40"), "rs": ("Serbia", "+381"), "ru": ("Russia", "+7"), "rw": ("Rwanda", "+250"),
    "sa": ("Saudi Arabia", "+966"), "sb": ("Solomon Islands", "+677"), "sc": ("Seychelles", "+248"), "sd": ("Sudan", "+249"),
    "se": ("Sweden", "+46"), "sg": ("Singapore", "+65"), "sh": ("Saint Helena", "+290"), "si": ("Slovenia", "+386"),
    "sj": ("Svalbard and Jan Mayen", "+47"), "sk": ("Slovakia", "+421"), "sl": ("Sierra Leone", "+232"), "sm": ("San Marino", "+378"),
    "sn": ("Senegal", "+221"), "so": ("Somalia", "+252"), "sr": ("Suriname", "+597"), "ss": ("South Sudan", "+211"),
    "st": ("São Tomé and Príncipe", "+239"), "sv": ("El Salvador", "+503"), "sx": ("Sint Maarten", "+1-721"),
    "sy": ("Syria", "+963"), "sz": ("Eswatini", "+268"), "tc": ("Turks and Caicos Islands", "+1-649"), "td": ("Chad", "+235"),
    "tf": ("French Southern Territories", ""), "tg": ("Togo", "+228"), "th": ("Thailand", "+66"), "tj": ("Tajikistan", "+992"),
    "tk": ("Tokelau", "+690"), "tl": ("Timor-Leste", "+670"), "tm": ("Turkmenistan", "+993"), "tn": ("Tunisia", "+216"),
    "to": ("Tonga", "+676"), "tr": ("Turkey", "+90"), "tt": ("Trinidad and Tobago", "+1-868"), "tv": ("Tuvalu", "+688"),
    "tz": ("Tanzania", "+255"), "ua": ("Ukraine", "+380"), "ug": ("Uganda", "+256"), "um": ("United States Minor Outlying Islands", ""),
    "us": ("United States", "+1"), "uy": ("Uruguay", "+598"), "uz": ("Uzbekistan", "+998"), "va": ("Vatican City", "+379"),
    "vc": ("Saint Vincent and the Grenadines", "+1-784"), "ve": ("Venezuela", "+58"), "vg": ("British Virgin Islands", "+1-284"),
    "vi": ("U.S. Virgin Islands", "+1-340"), "vn": ("Vietnam", "+84"), "vu": ("Vanuatu", "+678"), "wf": ("Wallis and Futuna", "+681"),
    "ws": ("Samoa", "+685"), "xk": ("Kosovo", "+383"), "ye": ("Yemen", "+967"), "yt": ("Mayotte", "+262"), "za": ("South Africa", "+27"),
    "zm": ("Zambia", "+260"), "zw": ("Zimbabwe", "+263")
}

def generate_fake_passport(country_code="us"):
    fake = Faker()
    country_info = COUNTRY_CODES.get(country_code, ("Unknown Country", ""))
    country_name, country_phone_code = country_info
    mobile_number = f"{country_phone_code} {fake.phone_number()}"
    return {
        "Name": fake.name(),
        "Gender": fake.random_element(elements=('Male', 'Female')),
        "Street Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "Pincode": fake.postcode(),
        "Country": country_name,
        "Mobile Number": mobile_number,
        "Email": fake.email(),
    }


def format_passport_details(passport_details):
    country = passport_details.get("Country", "Unknown Country")
    response = [
        f"**{country} Address Generated** ✅",
        "", 
        "▰▰▰▰▰▰▰▰▰▰▰▰▰"
    ]
    for key, value in passport_details.items():
        response.append(f"•➥ **{key}**: `{value}`")
    return "\n".join(response)


@app.on_message(filters.command(["fake"], prefixes=[".", "/"]))
async def send_fake_passport_details(client, message):
    command_text = message.text.split()
    country_code = command_text[1] if len(command_text) > 1 and command_text[1] in COUNTRY_CODES else "us"
    passport_details = generate_fake_passport(country_code)
    formatted_details = format_passport_details(passport_details)
    await client.send_message(message.chat.id, formatted_details)
