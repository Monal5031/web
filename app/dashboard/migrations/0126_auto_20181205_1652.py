# Generated by Django 2.1.2 on 2018-12-05 16:52

from django.db import migrations


def forwards_func(apps, schema_editor):
    BlockedUser = apps.get_model('dashboard', 'BlockedUser')
    Profile = apps.get_model('dashboard', 'Profile')
    handles = ['lazaridiscom', 'NOTLAZ', 'omidmahboubian']
    kwargs = {
        'active': True,
        'comments': 'Automatically blocked during the initial migration: dashboard.migrations.0125_auto_20181205_1652'
    }
    for handle in handles:
        try:
            profile = Profile.objects.select_related('user').filter(handle__iexact=handle, user__isnull=False).last()
            if profile:
                kwargs['user'] = profile.user
        except Profile.DoesNotExist:
            pass

        BlockedUser.objects.create(handle=handle, **kwargs)


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0125_blockeduser'),
    ]

    operations = [migrations.RunPython(forwards_func, ), ]
