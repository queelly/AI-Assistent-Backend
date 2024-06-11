from django.db import models

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
    