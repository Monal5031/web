# Generated by Django 2.1.2 on 2018-11-18 01:48

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0116_merge_20181115_2252'),
        ('kudos', '0008_auto_20181116_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkTransferCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('num_uses_total', models.IntegerField()),
                ('num_uses_remaining', models.IntegerField()),
                ('current_uses', models.IntegerField(default=0)),
                ('secret', models.CharField(max_length=255, unique=True)),
                ('comments_to_put_in_kudos_transfer', models.CharField(blank=True, max_length=255)),
                ('sender_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulk_transfers', to='dashboard.Profile')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulk_transfers', to='kudos.Token')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BulkTransferRedemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('ip_address', models.GenericIPAddressField(default=None, null=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulk_transfer_redemptions', to='kudos.BulkTransferCoupon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bulktransferredemption',
            name='kudostransfer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulk_transfer_redemptions', to='kudos.KudosTransfer'),
        ),
        migrations.AddField(
            model_name='bulktransferredemption',
            name='redeemed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulk_transfer_redemptions', to='dashboard.Profile'),
        ),
    ]
