import json
from pathlib import Path
from apps.common.models import City, District


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
    
    def execute(self):

        self._create_cities()