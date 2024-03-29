# Generated by Django 2.0.2 on 2018-04-10 22:10

from django.db import migrations

def add_default_skills(apps, schema_editor):
    Skill = apps.get_model('profiles', 'Skill')
    skills = [
        "CPR", "First Aid", "Diaper Changing", "Experience with Infants", "Experience with Toddlers",
        "Experience with ages 3+", "Basic Cooking", "Willing to Transport", "Willing to provide light house cleaning",
        "Willing to care for sick children", "Will to watch child w/ special needs", "Willing to watch dogs", 
        "Willing to house sit",
    ]

    for skill_name in skills:
        s = Skill(name=skill_name)
        s.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180410_1446'),
    ]

    operations = [
        migrations.RunPython(add_default_skills),
    ]
