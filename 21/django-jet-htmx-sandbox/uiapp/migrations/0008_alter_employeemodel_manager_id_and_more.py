# Generated by Django 4.1 on 2022-08-04 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0007_alter_employeemodel_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uiapp.employeemodel'),
        ),
        migrations.AddConstraint(
            model_name='employeemodel',
            constraint=models.CheckConstraint(check=models.Q(('salary__gte', 0)), name='salary_gt_0'),
        ),
        migrations.AddConstraint(
            model_name='employeemodel',
            constraint=models.UniqueConstraint(fields=('email',), name='email_unique'),
        ),
    ]