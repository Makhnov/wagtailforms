# Generated by Django 5.0.4 on 2024-04-17 11:57

import django.db.models.deletion
import wagtail.blocks
import wagtailstreamforms.fields
import wagtailstreamforms.streamfield
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0092_query_searchpromotion_querydailyhits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, help_text='Used to identify the form in template tags', max_length=255, unique=True, verbose_name='Slug')),
                ('template_name', models.CharField(choices=[('widgets/forms/contact.html', 'Formulaire de contact'), ('widgets/forms/amicale.html', "Inscription à l'amicale"), ('widgets/forms/sortie.html', "Sorties de l'amicale"), ('widgets/forms/agents.html', 'Formulaire pour les agents'), ('widgets/forms/administration.html', 'Formulaire pour les élus'), ('widgets/forms/home.html', 'Formulaire pour les pages génériques'), ('streamforms/form_block.html', 'Formulaire par défaut')], max_length=255, verbose_name='Template')),
                ('fields', wagtailstreamforms.streamfield.FormFieldsStreamField([('singleline', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='placeholder', label='Text field (single line)')), ('multiline', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='placeholder', label='Text field (multi line)')), ('date', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='date', label='Date field')), ('datetime', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='time', label='Time field')), ('email', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='mail', label='Email field')), ('url', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='link', label='URL field')), ('number', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='placeholder', label='Number field')), ('dropdown', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('empty_label', wagtail.blocks.CharBlock(label='Empty Label', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Option'), label='Options'))], icon='arrow-down-big', label='Dropdown field')), ('radio', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Option'), label='Options'))], icon='radio-empty', label='Radio buttons')), ('checkboxes', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Option'), label='Options'))], icon='tick-inverse', label='Checkboxes')), ('checkbox', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False))], icon='tick-inverse', label='Checkbox field')), ('hidden', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default Value', required=False))], icon='no-view', label='Hidden field')), ('singlefile', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False))], icon='doc-full-inverse', label='File field')), ('multifile', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.CharBlock(label='Help Text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False))], icon='doc-full-inverse', label='Files field'))], verbose_name='Fields')),
                ('submit_button_text', models.CharField(default='Submit', max_length=100, verbose_name='Submit button text')),
                ('success_message', models.CharField(blank=True, help_text='An optional success message to show when the form has been successfully submitted', max_length=255, verbose_name='Success message')),
                ('error_message', models.CharField(blank=True, help_text='An optional error message to show when the form has validation errors', max_length=255, verbose_name='Error message')),
                ('process_form_submission_hooks', wagtailstreamforms.fields.HookSelectField(blank=True, verbose_name='Submission hooks')),
                ('post_redirect_page', models.ForeignKey(blank=True, help_text='The page to redirect to after a successful submission', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Post redirect page')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_data', models.TextField(verbose_name='Form data')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='Submit time')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailstreamforms.form', verbose_name='Form')),
            ],
            options={
                'verbose_name': 'Form submission',
                'ordering': ['-submit_time'],
            },
        ),
        migrations.CreateModel(
            name='FormSubmissionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, verbose_name='Field')),
                ('file', models.FileField(upload_to='streamforms/', verbose_name='File')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='wagtailstreamforms.formsubmission', verbose_name='Submission')),
            ],
            options={
                'verbose_name': 'Form submission file',
                'ordering': ['field', 'file'],
            },
        ),
    ]
