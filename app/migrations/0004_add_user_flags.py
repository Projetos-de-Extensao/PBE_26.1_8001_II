from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_candidatura"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
