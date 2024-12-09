# Generated by Django 5.1.3 on 2024-12-09 18:30

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Depart_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Depart_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('D_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hms.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('P_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('Medicine_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Medicine_name', models.CharField(max_length=200)),
                ('Cost', models.IntegerField()),
                ('Side_effect', models.CharField(max_length=200)),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Test',
            fields=[
                ('Test_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Test_name', models.CharField(max_length=200)),
                ('Test_date', models.DateField()),
                ('Test_result', models.CharField(max_length=255)),
                ('D_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.doctor')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact_P', models.IntegerField()),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('Bill_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Total_amount', models.IntegerField()),
                ('Pay_date', models.DateField()),
                ('Pay_method', models.CharField(choices=[('Cash', 'Cash'), ('Credit/Debit Card', 'Credit/Debit Card'), ('Mobile Wallet', 'Mobile Wallet'), ('Insurance', 'Insurance'), ('UPI', 'UPI')], max_length=100)),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.doctor')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appointment_datetime', models.DateTimeField()),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Rescheduled', 'Rescheduled'), ('Completed', 'Completed'), ('No-Show', 'No-Show')], default='PENDING', max_length=255)),
                ('D_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.doctor')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.medicine')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Room_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Room_no', models.IntegerField()),
                ('Room_type', models.CharField(choices=[('General Ward', 'General Ward'), ('ICU', 'ICU'), ('Maternity Room', 'Maternity Room'), ('Isolation Room', 'Isolation Room'), ('Day Care Room', 'Day Care Room'), ('Delux Room', 'Delux Room')], max_length=200)),
                ('status', models.CharField(choices=[('available', 'available'), ('occupied', 'occupied')], max_length=100)),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Staff_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Role', models.CharField(choices=[('ADMIN', 'Administrator'), ('DOCTOR', 'Doctor'), ('NURSE', 'Nurse'), ('RECEPTIONIST', 'Receptionist'), ('TECHNICIAN', 'Technician'), ('Medical Staff', 'Medical Staff'), ('Support Staff', 'Support Staff')], max_length=150, null=True)),
                ('Depart_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hms.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
