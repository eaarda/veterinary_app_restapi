import json
from pathlib import Path
from apps.common.models import City, District, Color, Specie, ProductType, Unit


class CommonMock():

    def _create_cities(self):

        WORKING_DIR = Path(__file__).resolve().parent
        with open("{}/cities_data.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)
            cities_data = data["data"]

            count = len(cities_data)        
            
            for index, city_data in enumerate(cities_data):
                city_name = city_data["il_adi"]
                city, created = City.objects.get_or_create(name=city_name)

                for district_data in city_data["ilceler"]:
                    district_name = district_data["ilce_adi"]
                    district, created = District.objects.get_or_create(name=district_name, city=city)
    

    def __create_colors(self):

        WORKING_DIR = Path(__file__).resolve().parent
        with open("{}/colors_data.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)
            colors_data = data["data"]

            count = len(colors_data)

            for index, color_data in enumerate(colors_data):
                color_name = color_data["dsColor"]
                color, created = Color.objects.get_or_create(name=color_name)
    

    def __create_species(self):

        WORKING_DIR = Path(__file__).resolve().parent
        with open("{}/species_data.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)
            species_data = data["data"]

            count = len(species_data)

            for index, specie_data in enumerate(species_data):
                specie_name = specie_data["dsSpecies"]
                specie, created = Specie.objects.get_or_create(name=specie_name)
    

    def __create_product_type(self):

        WORKING_DIR = Path(__file__).resolve().parent
        with open("{}/product_type_data.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)
            product_types_data = data["data"]

            count = len(product_types_data)

            for index, product_type_data in enumerate(product_types_data):
                product_type_name = product_type_data["dsProductType"]
                product_type, created = ProductType.objects.get_or_create(name=product_type_name)
        
    
    def __create_units(self):

        WORKING_DIR = Path(__file__).resolve().parent
        with open("{}/units_data.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)
            units_data = data["data"]

            count = len(units_data)

            for index, unit_data in enumerate(units_data):
                unit_name = unit_data["dsUnit"]
                unit, created = Unit.objects.get_or_create(name=unit_name)


    def execute(self):

        self._create_cities()
        self.__create_colors()
        self.__create_species()
        self.__create_product_type()
        self.__create_units()