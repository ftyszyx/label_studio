"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
# Generated by Django 3.1.4 on 2021-03-03 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('io_storages', '0001_initial'), ('io_storages', '0002_auto_20210302_1827')]

    initial = True

    dependencies = [
        ('projects', '0001_squashed_0065_auto_20210223_2014'),
        ('tasks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AzureBlobStorageMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.TextField(blank=True, help_text='Azure blob container', null=True, verbose_name='container')),
                ('prefix', models.TextField(blank=True, help_text='Azure blob prefix name', null=True, verbose_name='prefix')),
                ('regex_filter', models.TextField(blank=True, help_text='Cloud storage regex for filtering objects', null=True, verbose_name='regex_filter')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
                ('account_name', models.TextField(blank=True, help_text='Azure Blob account name', null=True, verbose_name='account_name')),
                ('account_key', models.TextField(blank=True, help_text='Azure Blob account key', null=True, verbose_name='account_key')),
            ],
        ),
        migrations.CreateModel(
            name='GCSStorageMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.TextField(blank=True, help_text='GCS bucket name', null=True, verbose_name='bucket')),
                ('prefix', models.TextField(blank=True, help_text='GCS bucket prefix', null=True, verbose_name='prefix')),
                ('regex_filter', models.TextField(blank=True, help_text='Cloud storage regex for filtering objects', null=True, verbose_name='regex_filter')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
            ],
        ),
        migrations.CreateModel(
            name='RedisStorageMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(blank=True, help_text='Storage prefix (optional)', null=True, verbose_name='path')),
                ('host', models.TextField(blank=True, help_text='Server Host IP (optional)', null=True, verbose_name='host')),
                ('port', models.TextField(blank=True, help_text='Server Port (optional)', null=True, verbose_name='port')),
                ('password', models.TextField(blank=True, help_text='Server Password (optional)', null=True, verbose_name='password')),
                ('regex_filter', models.TextField(blank=True, help_text='Cloud storage regex for filtering objects', null=True, verbose_name='port')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
            ],
        ),
        migrations.CreateModel(
            name='S3ExportStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('bucket', models.TextField(blank=True, help_text='S3 bucket name', null=True, verbose_name='bucket')),
                ('prefix', models.TextField(blank=True, help_text='S3 bucket prefix', null=True, verbose_name='prefix')),
                ('regex_filter', models.TextField(blank=True, help_text='Cloud storage regex for filtering objects', null=True, verbose_name='regex_filter')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
                ('aws_access_key_id', models.TextField(blank=True, help_text='AWS_ACCESS_KEY_ID', null=True, verbose_name='aws_access_key_id')),
                ('aws_secret_access_key', models.TextField(blank=True, help_text='AWS_SECRET_ACCESS_KEY', null=True, verbose_name='aws_secret_access_key')),
                ('aws_session_token', models.TextField(blank=True, help_text='AWS_SESSION_TOKEN', null=True, verbose_name='aws_session_token')),
                ('region_name', models.TextField(blank=True, help_text='AWS Region', null=True, verbose_name='region_name')),
                ('s3_endpoint', models.TextField(blank=True, help_text='S3 Endpoint', null=True, verbose_name='s3_endpoint')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_s3exportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='S3ImportStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('bucket', models.TextField(blank=True, help_text='S3 bucket name', null=True, verbose_name='bucket')),
                ('prefix', models.TextField(blank=True, help_text='S3 bucket prefix', null=True, verbose_name='prefix')),
                ('regex_filter', models.TextField(blank=True, help_text='Cloud storage regex for filtering objects', null=True, verbose_name='regex_filter')),
                ('use_blob_urls', models.BooleanField(default=False, help_text='Interpret objects as BLOBs and generate URLs', verbose_name='use_blob_urls')),
                ('aws_access_key_id', models.TextField(blank=True, help_text='AWS_ACCESS_KEY_ID', null=True, verbose_name='aws_access_key_id')),
                ('aws_secret_access_key', models.TextField(blank=True, help_text='AWS_SECRET_ACCESS_KEY', null=True, verbose_name='aws_secret_access_key')),
                ('aws_session_token', models.TextField(blank=True, help_text='AWS_SESSION_TOKEN', null=True, verbose_name='aws_session_token')),
                ('region_name', models.TextField(blank=True, help_text='AWS Region', null=True, verbose_name='region_name')),
                ('s3_endpoint', models.TextField(blank=True, help_text='S3 Endpoint', null=True, verbose_name='s3_endpoint')),
                ('presign', models.BooleanField(default=True, help_text='Generate presigned URLs', verbose_name='presign')),
                ('presign_ttl', models.PositiveSmallIntegerField(default=1, help_text='Presigned URLs TTL (in minutes)', verbose_name='presign_ttl')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_s3importstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AzureBlobExportStorage',
            fields=[
                ('azureblobstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.azureblobstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_azureblobexportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.azureblobstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='AzureBlobImportStorage',
            fields=[
                ('azureblobstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.azureblobstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('presign', models.BooleanField(default=True, help_text='Generate presigned URLs', verbose_name='presign')),
                ('presign_ttl', models.PositiveSmallIntegerField(default=1, help_text='Presigned URLs TTL (in minutes)', verbose_name='presign_ttl')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_azureblobimportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.azureblobstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='GCSExportStorage',
            fields=[
                ('gcsstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.gcsstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_gcsexportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.gcsstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='GCSImportStorage',
            fields=[
                ('gcsstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.gcsstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('presign', models.BooleanField(default=True, help_text='Generate presigned URLs', verbose_name='presign')),
                ('presign_ttl', models.PositiveSmallIntegerField(default=1, help_text='Presigned URLs TTL (in minutes)', verbose_name='presign_ttl')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_gcsimportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.gcsstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='RedisExportStorage',
            fields=[
                ('redisstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.redisstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('db', models.PositiveSmallIntegerField(default=2, help_text='Server Database', verbose_name='db')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_redisexportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.redisstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='RedisImportStorage',
            fields=[
                ('redisstoragemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='io_storages.redisstoragemixin')),
                ('title', models.CharField(help_text='Cloud storage title', max_length=256, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Cloud storage description', null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('db', models.PositiveSmallIntegerField(default=1, help_text='Server Database', verbose_name='db')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_redisimportstorages', to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=('io_storages.redisstoragemixin', models.Model),
        ),
        migrations.CreateModel(
            name='S3ImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.s3importstorage')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_s3importstoragelink', to='tasks.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='S3ExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_s3exportstoragelink', to='tasks.taskcompletion')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.s3exportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RedisImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_redisimportstoragelink', to='tasks.task')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.redisimportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RedisExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_redisexportstoragelink', to='tasks.taskcompletion')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.redisexportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GCSImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_gcsimportstoragelink', to='tasks.task')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.gcsimportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GCSExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_gcsexportstoragelink', to='tasks.taskcompletion')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.gcsexportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AzureBlobImportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(help_text='External link key', verbose_name='key')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_azureblobimportstoragelink', to='tasks.task')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.azureblobimportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AzureBlobExportStorageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_exists', models.BooleanField(default=True, help_text='Whether object under external link still exists', verbose_name='object exists')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation time', verbose_name='created at')),
                ('annotation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='io_storages_azureblobexportstoragelink', to='tasks.taskcompletion')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='io_storages.azureblobexportstorage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
