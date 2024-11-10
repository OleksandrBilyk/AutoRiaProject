from django.db.models import TextChoices


class CurrencyChoices(TextChoices):
    UAH = "UAH"
    USD = "USD"
    EUR = "EUR"


class CarBrandChoices(TextChoices):
    BMW = "BMW"
    AUDI = "AUDI"
    Fiat = 'Fiat'
    Mazda = 'Mazda'
    Nissan = 'Nissan'
    Scoda = 'Scoda'
    Chevrolet = 'Chevrolet'
    Ford = 'Ford'
    Honda = 'Honda'
    Hyundai = 'Hyundai'
    KIA = 'KIA'
    Lexus = 'Lexus'
    Mercedes_Benz = 'Mercedes-Benz'
    Mitsubishi = 'Mitsubishi'
    Opel = 'Opel'
    Peugeot = 'Peugeot'
    Toyota = 'Toyota'
    Volvo = 'Volvo'
    Volkswagen = 'Volkswagen'
    Other = 'Other'


class RegionChoices(TextChoices):
    Kyiv = "Kyiv"
    Sevastopol = "Sevastopol"
    Avtonomna_Respublika_Krym= "Avtonomna Respublika Krym"
    Vinnytska = "Vinnytska"
    Volynska = "Volynska "
    Dnipropetrovska = "Dnipropetrovska"
    Donetska = "Donetska"
    Zhytomyrskа = "Zhytomyrskа"
    Zakarpatska = "Zakarpatska"
    Zaporizka = "Zaporizka"
    Ivano_Frankivska = "Ivano-Frankivska"
    Kyivska = "Kyivska"
    Kirovohradska = "Kirovohradska"
    Luhanska = "Luhanska"
    Lvivska = "Lvivska"
    Mykolaivska = "Mykolaivska"
    Odeska = "Odeska"
    Poltavska = "Poltavska"
    Rivnenska = "Rivnenska"
    Sumska = "Sumska"
    Ternopilska = "Ternopilska"
    Kharkivska = "Kharkivska"
    Khersonska = "Khersonska"
    Khmelnytska = "Khmelnytska"
    Cherkaska = "Cherkaska"
    Chernivetska = "Chernivetska"
    Chernihivska= "Chernihivska"

