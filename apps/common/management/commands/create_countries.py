import json
import requests
from django.core.management import BaseCommand
from pathlib import Path
from django.core.files.base import ContentFile
from apps.common.models import Country  

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        path = Path(__file__).resolve().parent / 'countries.json'
        
        with open(path, 'r') as f:
            countries = json.loads(f.read())
        
        self.stdout.write(self.style.SUCCESS('json data successfully loaded'))

        for country in countries:
            try:
                response = requests.get(url=country['icon'])
                response.raise_for_status()

                self.stdout.write(self.style.SUCCESS('request successfully'))

                content = ContentFile(response.content)

                country_obj, _ = Country.objects.get_or_create(
                    ico_code=country['ico_code'],
                    defaults={'name': country['name']}
                )

                country_obj.icon.save(f"{country['name']}.png", content, save=True)  

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Request failed: {e}"))
                continue
