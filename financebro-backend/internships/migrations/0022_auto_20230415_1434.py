# Generated by Django 4.1.7 on 2023-04-15 14:34

from django.db import migrations


REGIONS = [
    {
        'code': 'AMERICAS',
        'name': 'Americas'
    },
    {
        'code': 'ASIA',
        'name': 'Asia Pacific'
    },
    {
        'code': 'EMEA',
        'name': 'Europe, Middle East and Africa'
    }
]


def add_regions_in_db(apps, schema_editor):
    if schema_editor.connection.alias != "default":
        return

    region_model = apps.get_model('internships', 'Region')
    for region_dict in REGIONS:
        if not region_model.objects.filter(code=region_dict['code']).exists():
            region_model.objects.create(
                code=region_dict['code'],
                name=region_dict['name']
            )


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0021_program_found_in_latest_scrape'),
    ]

    operations = [
        migrations.RunPython(add_regions_in_db),
    ]