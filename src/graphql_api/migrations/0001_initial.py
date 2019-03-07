# Generated by Django 2.1.4 on 2018-12-20 04:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gluon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('relation', models.TextField(max_length=255)),
                ('prefix', models.TextField(blank=True, max_length=255)),
                ('suffix', models.TextField(blank=True, max_length=255)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('start_accuracy', models.CharField(blank=True, max_length=10)),
                ('end_accuracy', models.CharField(blank=True, max_length=10)),
                ('is_momentary', models.BooleanField(blank=True, default=False)),
                ('url', models.URLField(blank=True)),
                ('is_private', models.BooleanField(blank=True, default=False)),
                ('is_exclusive', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GluonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('caption_ja', models.CharField(max_length=255)),
                ('sort', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QpropertyGtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gluon_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belonging_quark_properties', to='graphql_api.GluonType')),
            ],
        ),
        migrations.CreateModel(
            name='QpropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QtypeProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image_path', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('start_accuracy', models.CharField(blank=True, max_length=10)),
                ('end_accuracy', models.CharField(blank=True, max_length=10)),
                ('is_momentary', models.BooleanField(blank=True, default=False)),
                ('url', models.URLField(blank=True)),
                ('affiliate', models.URLField(blank=True)),
                ('gender', models.CharField(blank=True, max_length=3)),
                ('is_private', models.BooleanField(blank=True, default=False)),
                ('is_exclusive', models.BooleanField(blank=True, default=True)),
                ('wid', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_quarks', to=settings.AUTH_USER_MODEL)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_quarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuarkProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('caption_ja', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuarkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_path', models.CharField(blank=True, max_length=255)),
                ('name_prop', models.CharField(max_length=255)),
                ('start_prop', models.CharField(max_length=255)),
                ('end_prop', models.CharField(max_length=255)),
                ('has_gender', models.BooleanField(blank=True, default=False)),
                ('sort', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quark',
            name='quark_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarks', to='graphql_api.QuarkType'),
        ),
        migrations.AddField(
            model_name='qtypeproperty',
            name='quark_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belonging_quark_types', to='graphql_api.QuarkProperty'),
        ),
        migrations.AddField(
            model_name='qtypeproperty',
            name='quark_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='having_quark_properties', to='graphql_api.QuarkType'),
        ),
        migrations.AddField(
            model_name='qpropertytype',
            name='quark_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='having_quark_types', to='graphql_api.QuarkProperty'),
        ),
        migrations.AddField(
            model_name='qpropertytype',
            name='quark_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belonging_quark_properties', to='graphql_api.QuarkType'),
        ),
        migrations.AddField(
            model_name='qpropertygtype',
            name='quark_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='having_gluon_types', to='graphql_api.QuarkProperty'),
        ),
        migrations.AddField(
            model_name='gluon',
            name='gluon_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gluons', to='graphql_api.GluonType'),
        ),
        migrations.AddField(
            model_name='gluon',
            name='last_modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_gluons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gluon',
            name='object_quark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belongings', to='graphql_api.Quark'),
        ),
        migrations.AddField(
            model_name='gluon',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_gluons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gluon',
            name='subject_quark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='havings', to='graphql_api.Quark'),
        ),
    ]