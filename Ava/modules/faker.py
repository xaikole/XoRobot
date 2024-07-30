import random
from faker import Faker
from pyrogram import filters
from Ava import Jarvis as app
import requests

# Mapping of country codes to country names, their corresponding phone codes, and Faker locales
COUNTRY_CODES = {
    "ad": ("Andorra", "+376", "es_ES"), "ae": ("United Arab Emirates", "+971", "ar_AE"), "af": ("Afghanistan", "+93", "en_US"),
    # (Include all country codes here with their corresponding locale)
    "zm": ("Zambia", "+260", "en_US"), "zw": ("Zimbabwe", "+263", "en_US")
}

def generate_temp_email():
    response = requests.get("https://api.temp-mail.org/request/domains/format/json")
    domains = response.json()
    fake = Faker()
    local_part = fake.user_name()
    temp_email = f"{local_part}@{random.choice(domains)}"
    return temp_email

def generate_fake_passport(country_code="us"):
    country_info = COUNTRY_CODES.get(country_code, ("Unknown Country", "", "en_US"))
    country_name, country_phone_code, locale = country_info
    fake = Faker(locale)
    mobile_number = f"{country_phone_code} {fake.phone_number()}"
    temp_email = generate_temp_email()
    return {
        "Name": fake.name(),
        "Gender": fake.random_element(elements=('Male', 'Female')),
        "Street Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "Pincode": fake.postcode(),
        "Country": country_name,
        "Mobile Number": mobile_number,
        "Email": temp_email,
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
