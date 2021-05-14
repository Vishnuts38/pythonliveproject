# Generated by Django 3.1.7 on 2021-04-21 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vendor', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='user/')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_date', models.DateField()),
                ('Order_total', models.FloatField()),
                ('Delivery_date', models.DateField()),
                ('Is_delivered', models.CharField(blank=True, max_length=40, null=True)),
                ('Payment_method', models.CharField(blank=True, max_length=40, null=True)),
                ('Payment_Status', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Ordered', 'Ordered'), ('Accepted', 'Accepted'), ('Out for Delivery', 'Out for Delivery'), ('Order Cancel', 'Order Cancel'), ('Customer Cancel', 'Customer Cancel'), ('Delivered', 'Delivered'), ('Added to Cart', 'Added to Cart'), ('Assigned to Driver', 'Assigned to Driver')], default='ordered', max_length=50, null=True)),
                ('Customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vend_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vend')),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Qty', models.IntegerField()),
                ('Product_Price', models.FloatField()),
                ('Subtotal', models.IntegerField()),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.order')),
                ('Product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
