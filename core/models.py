from django.db import models
from django.contrib.gis.db import models as gis_models

class InvestPlace(models.Model):
    name = models.CharField()
    preferential_treatment = models.CharField(null=True)
    preferential_treatment_id = models.PositiveIntegerField(null=True)
    preferential_treatment_name = models.CharField(null=True)
    support_object_type = models.CharField(null=True)
    support_object_id = models.PositiveIntegerField(null=True)
    support_object_name = models.CharField(null=True)
    region = models.CharField()
    address = models.CharField()
    nearest_city = models.CharField()
    class PlaceType(models.TextChoices):
        FIELD = "Земельный участок"
        ROOM = "Помещение"
    place_type = models.CharField(choices=PlaceType)
    class InvestingFieldType(models.TextChoices):
        GREENFIELD = "Гринфилд"
        BROWNFIELD = "Браунфилд"
    novelty_type = models.CharField(choices=InvestingFieldType)
    class OwnreshipType(models.TextChoices):
        PRIVATE = "Частная"
        GOV = "Государственная до разграничения"
        CITY = "Муниципальная"
        REGION = "Региональная"
    ownership = models.CharField(choices=OwnreshipType)
    class TradeType(models.TextChoices):
        AUCTION_SALE = "Продажа через аукцион"
        AUCTION_RENT = "Аренда через аукцион"
        SALE = "Продажа"
        RENT = "Аренда"
    trade_type = models.CharField(choices=TradeType)
    price = models.FloatField()
    year_price_ga = models.FloatField(null=True)
    year_price_m2 = models.FloatField(null=True)
    rent_time_constraits = models.CharField(null=True)
    price_setting_rule = models.CharField(null=True)
    danger_class = models.CharField(null=True)
    capital_constructions_description = models.TextField(null=True)
    free_land_ga = models.FloatField(null=True)
    cadastral_number_land = models.CharField(null=True)
    allowed_buisnesses = models.TextField(null=True)
    surveying = models.BooleanField(null=True)
    land_category = models.CharField(null=True)
    free_room_m2 = models.FloatField(null=True)
    cadastral_number_room = models.CharField(null=True)
    tech_building_characteristics = models.TextField(null=True)
    owner_name = models.CharField()
    owner_inn = models.PositiveIntegerField()
    owner_url = models.URLField()
    note = models.TextField()
    class SupplyLinesAvailability(models.TextChoices):
        YES = "Да",
        NO = "Нет",
        ABILITY = "Возможно создание"
    water_supply = models.CharField(choices=SupplyLinesAvailability)
    water_cost = models.FloatField(null=True)
    water_cost_transportation = models.FloatField(null=True)
    water_facilities_max_power = models.FloatField(null=True)
    water_facilities_free_power = models.FloatField(null=True)
    water_facilities_note = models.TextField(null=True)
    water_throughput = models.FloatField(null=True)
    sewage_supply = models.CharField(choices=SupplyLinesAvailability)
    sewage_cost = models.FloatField(null=True)
    sewage_cost_transportation = models.FloatField(null=True)
    sewage_facilities_max_power = models.FloatField(null=True)
    sewage_facilities_free_power = models.FloatField(null=True)
    sewage_facilities_note = models.TextField(null=True)
    sewage_throughput = models.FloatField(null=True)
    gas_supply = models.CharField(choices=SupplyLinesAvailability)
    gas_cost = models.CharField(null=True) #у них указано "от .. до", поэтому char field
    gas_cost_transportation = models.CharField(null=True)
    gas_facilities_max_power = models.FloatField(null=True)
    gas_facilities_free_power = models.FloatField(null=True)
    gas_facilities_note = models.TextField(null=True)
    gas_throughput = models.FloatField(null=True)
    electricity_supply = models.CharField(choices=SupplyLinesAvailability)
    electricity_cost = models.CharField(null=True) #у них указано "от .. до", поэтому char field
    electricity_cost_transportation = models.CharField(null=True)
    electricity_facilities_max_power = models.FloatField(null=True)
    electricity_facilities_free_power = models.FloatField(null=True)
    electricity_facilities_note = models.TextField(null=True)
    electricity_throughput = models.FloatField(null=True)
    heat_supply = models.FloatField(choices=SupplyLinesAvailability)
    heat_cost = models.FloatField(null=True) #у них указано "от .. до", поэтому char field
    heat_cost_transportation = models.FloatField(null=True)
    heat_facilities_max_power = models.FloatField(null=True)
    heat_facilities_free_power = models.FloatField(null=True)
    heat_facilities_note = models.TextField(null=True)
    heat_throughput = models.FloatField(null=True)
    tko_availability = models.BooleanField(null=True)
    tko_cost_ton = models.FloatField(null=True)
    tko_cost_m3 = models.FloatField(null=True)
    access_roads_availability = models.BooleanField(null=True)
    raild_roads_availability = models.BooleanField(null=True)
    cargo_parking_availability = models.BooleanField(null=True)
    other_characteristics = models.TextField(null=True)
    application_process_description = models.TextField(null=True)
    application_documents = models.TextField(null=True)
    application_url = models.URLField()
    possible_businesses = models.TextField(null=True)

    urban_planning_characteristics_and_limitations = models.TextField(null = True)
    territorial_planining_documents = models.CharField(null = True) # нет ни одного экземпляра
    other_informmation = models.TextField(null = True)
    photos_object_url = models.URLField(max_length=1000, null = True)
    class AvallabilityMaip(models.TextChoices):
        YES = "да",
        NO = "нет"
    description_benefit = models.TextField(null = True)
    coordinates = gis_models.PointField(null = True) # нужно проверить, задаётся через django.contib.gis.geos.Point()

class SpecialEconomicsZonesAndTechn(models.Model):
    object_category = models.CharField(max_length=200)
    sez = models.CharField(max_length=200, null = True)
    top = models.CharField(max_length=50, null = True) # нет ни одного экземпляра
    name_object = models.CharField(max_length=500, null = True)
    region = models.Charfield(max_length = 50, null = True)
    municipal_formation = models.CharField(max_length=300, null = True)
    nearest_city = models.CharField(max_length=70, null = True)
    number_residents = models.PositiveIntegerField()
    photos_object_url = models.URLField(max_length=1000, null = True)
    documents_object_url = models.URLField(max_length=1000, null = True)
    year_object_formation = models.IntegerField(null = True) # мб есть какой-то тип с годом, чтобы не весь int пихать
    validation_period_object = models.DateField(null = True) # принимает только 2 значения 10 и 31.12.2054
    total_area = models.IntegerField(null = True)
    minimal_rental_price = models.IntegerField(null = True)
    class Possibility_buying_premises(models.TextChoices):
        YES = "да",
        NO = "нет"
    list_industries = models.TextField(null = True)
    restrictions_on_types_activities = models.TextField(null = True)
    infrastructure_and_services = models.TextField(null = True)
    additional_services_management_company = models.TextField(null = True) # нет ни одного экхемпляра
    name_admin_object = models.CharField(max_length=500, null = True)
    address_admin_object = models.CharField(max_length=500, null = True)
    link_site = documents_object_url = models.URLField(max_length=100, null = True)
    working_hours = models.TimeField(null = True) # вроде оно, но тут может не быть именно промежутка времени, а только конкретное время
