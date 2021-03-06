# Generated by Django 2.1.2 on 2018-11-28 15:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import economy.models
import grants.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0124_auto_20181128_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('tx_id', models.CharField(default='0x0', help_text='The transaction ID of the Contribution.', max_length=255)),
                ('from_address', models.CharField(default='0x0', help_text='The wallet address tokens are sent from.', max_length=255)),
                ('to_address', models.CharField(default='0x0', help_text='The wallet address tokens are sent to.', max_length=255)),
                ('token_address', models.CharField(default='0x0', help_text='The token address to be used with the Subscription.', max_length=255)),
                ('token_amount', models.DecimalField(decimal_places=4, default=1, help_text='The promised contribution amount per period.', max_digits=50)),
                ('period_seconds', models.DecimalField(decimal_places=0, default=0, help_text='The number of seconds thats constitues a period.', max_digits=50)),
                ('gas_price', models.DecimalField(decimal_places=4, default=0, help_text='The amount of token used to incentivize subminers.', max_digits=50)),
                ('nonce', models.DecimalField(decimal_places=0, default=0, help_text='The of the subscription metaTx.', max_digits=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('active', models.BooleanField(default=True, help_text='Whether or not the Grant is active.')),
                ('title', models.CharField(default='', help_text='The title of the Grant.', max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('description', models.TextField(blank=True, default='', help_text='The description of the Grant.')),
                ('reference_url', models.URLField(blank=True, help_text='The associated reference URL of the Grant.')),
                ('logo', models.ImageField(blank=True, help_text='The Grant logo image.', null=True, upload_to=grants.utils.get_upload_filename)),
                ('logo_svg', models.FileField(blank=True, help_text='The Grant logo SVG.', null=True, upload_to=grants.utils.get_upload_filename)),
                ('admin_address', models.CharField(default='0x0', help_text='The wallet address for the administrator of this Grant.', max_length=255)),
                ('amount_goal', models.DecimalField(decimal_places=4, default=1, help_text='The contribution goal amount for the Grant.', max_digits=50)),
                ('amount_received', models.DecimalField(decimal_places=4, default=0, help_text='The total amount received for the Grant.', max_digits=50)),
                ('token_address', models.CharField(default='0x0', help_text='The token address to be used with the Grant.', max_length=255)),
                ('token_symbol', models.CharField(default='', help_text='The token symbol to be used with the Grant.', max_length=255)),
                ('contract_address', models.CharField(default='0x0', help_text='The contract address of the Grant.', max_length=255)),
                ('contract_version', models.DecimalField(decimal_places=0, default=0, help_text='The contract version the Grant.', max_digits=3)),
                ('transaction_hash', models.CharField(default='0x0', help_text='The transaction hash of the Grant.', max_length=255)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='The Grant metadata. Includes creation and last synced block numbers.')),
                ('network', models.CharField(default='mainnet', help_text='The network in which the Grant contract resides.', max_length=8)),
                ('required_gas_price', models.DecimalField(decimal_places=0, default='0', help_text='The required gas price for the Grant.', max_digits=50)),
                ('admin_profile', models.ForeignKey(help_text="The Grant administrator's profile.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_admin', to='dashboard.Profile')),
                ('team_members', models.ManyToManyField(help_text='The team members contributing to this Grant.', related_name='grant_teams', to='dashboard.Profile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('title', models.CharField(help_text='The Milestone title.', max_length=255)),
                ('description', models.TextField(help_text='The Milestone description.')),
                ('due_date', models.DateField(help_text='The requested Milestone completion date.')),
                ('completion_date', models.DateField(blank=True, default=None, help_text='The Milestone completion date.', null=True)),
                ('grant', models.ForeignKey(help_text='The associated Grant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to='grants.Grant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('active', models.BooleanField(default=True, help_text='Whether or not the Subscription is active.')),
                ('subscription_hash', models.CharField(default='', help_text="The contributor's Subscription hash.", max_length=255)),
                ('contributor_signature', models.CharField(default='', help_text="The contributor's signature.", max_length=255)),
                ('contributor_address', models.CharField(default='', help_text="The contributor's wallet address of the Subscription.", max_length=255)),
                ('amount_per_period', models.DecimalField(decimal_places=4, default=1, help_text='The promised contribution amount per period.', max_digits=50)),
                ('real_period_seconds', models.DecimalField(decimal_places=0, default=2592000, help_text='The real payout frequency of the Subscription in seconds.', max_digits=50)),
                ('frequency_unit', models.CharField(default='', help_text='The text version of frequency units e.g. days, months', max_length=255)),
                ('frequency', models.DecimalField(decimal_places=0, default=0, help_text='The real payout frequency of the Subscription in seconds.', max_digits=50)),
                ('token_address', models.CharField(default='0x0', help_text='The token address to be used with the Subscription.', max_length=255)),
                ('token_symbol', models.CharField(default='0x0', help_text='The token symbol to be used with the Subscription.', max_length=255)),
                ('gas_price', models.DecimalField(decimal_places=4, default=1, help_text='The required gas price for the Subscription.', max_digits=50)),
                ('network', models.CharField(default='mainnet', help_text='The network in which the Subscription resides.', max_length=8)),
                ('contributor_profile', models.ForeignKey(help_text="The Subscription contributor's Profile.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_contributor', to='dashboard.Profile')),
                ('grant', models.ForeignKey(help_text='The associated Grant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='grants.Grant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contribution',
            name='subscription',
            field=models.ForeignKey(help_text='The associated Subscription.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_contribution', to='grants.Subscription'),
        ),
    ]
