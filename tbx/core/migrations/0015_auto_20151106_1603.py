# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import tbx.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0014_workpage_show_in_play_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='author_left',
            field=models.CharField(blank=True, help_text='author who has left Torchbox', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', tbx.core.models.ImageFormatChoiceBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_video_id',
            field=models.IntegerField(blank=True, null=True, help_text='Optional. The numeric ID of a Vimeo video to replace the background image.'),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='servicespagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='servicespagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', tbx.core.models.ImageFormatChoiceBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='standardpageclients',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpageclients',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='torchboximage',
            name='created_at',
            field=models.DateTimeField(verbose_name='Created at', db_index=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='torchboximage',
            name='file_size',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', tbx.core.models.ImageFormatChoiceBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')))),
        ),
    ]
