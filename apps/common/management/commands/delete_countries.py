from django.core.management import BaseCommand
from apps.common.models import Country  

class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    
    def add_arguments(self, parser):
        parser.add_argument('ico_code', type=str, nargs='+', help='The ico_code of the country')

    def handle(self, *args, **options):
       Country.objects.filter(ico_code__in=options.get('ico_code')).delete()