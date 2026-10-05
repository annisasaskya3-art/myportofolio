from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_project_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='stars',
            field=models.ManyToManyField(blank=True, related_name='starred_experiences', to=settings.AUTH_USER_MODEL),
        ),
    ]
