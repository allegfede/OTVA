# START Multiple Choice model field - snippet #1200 (mod)

#In order for this to work with south, add the following at the top of the file you put this code in (change path to match):
#from south.modelsinspector import add_introspection_rules  
#add_introspection_rules([], ["^appname\.fields\.MultiSelectField"])

from django.db import models
from django import forms
from django.utils.text import capfirst
from django.core import exceptions
from OTVA_server.ingesting.widgets import ColumnCheckboxSelectMultiple

class MultiSelectFormField(forms.MultipleChoiceField):
    widget = ColumnCheckboxSelectMultiple
    
    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 0)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        if value and self.max_choices and len(value) > self.max_choices:
            raise forms.ValidationError('You must select a maximum of %s choice%s.'
                    % (apnumber(self.max_choices), pluralize(self.max_choices)))
        return value

class MultiSelectField(models.Field):
    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return "CharField"

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def _get_FIELD_display(self, field):
        value = getattr(self, field.attname)
        choicedict = dict(field.choices)

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name), 
                    'help_text': self.help_text, 'choices':self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)
    
    """
    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)
    
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    
    def get_prep_value(self, value):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)

    def to_python(self, value):
        if isinstance(value, basestring):
            return value.split(',')
        elif isinstance(value, list):
            return value
        return ''
    """

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(',')

    def get_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list))
        return ','.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        return self.get_prep_value(self._get_val_from_obj(obj))

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(self.choices):",".join([choicedict.get(value,value) for value in getattr(self,fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)

    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if (opt_select not in arr_choices): 
                raise exceptions.ValidationError(self.error_messages['invalid_choice'] % value)    
        return

    #def validate(self, value, model_instance):
    #    return

    def get_choices_selected(self, arr_choices=''):
        if not arr_choices:
            return False
        list = []
        for choice_selected in arr_choices:
            list.append(choice_selected[0])
        return list

# END Multiple Choice model field - snippet #1200 (mod)

# START MultiSelectField - snippet #2708
'''
# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import force_unicode
from django.utils.text import capfirst


class MultiSelectField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def get_db_prep_value(self, value):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ','.join(value)
        return ''

    def to_python(self, value):
        if isinstance(value, basestring):
            return value.split(',')
        elif isinstance(value, list):
            return value
        return ''

    def value_to_string(self, obj):
        # We need this to proper dump data.
        return self.get_db_prep_value(self._get_val_from_obj(obj))

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def formfield(self, form_class=forms.MultipleChoiceField, **kwargs):
        # Using super() won't work because this would replace the form_class.
        defaults = {
            'required': not self.blank,
            'label': capfirst(self.verbose_name),
            'help_text': self.help_text,
            'choices': self.get_choices(include_blank=False),
        }
        if self.has_default():
            if callable(self.default):
                defaults['initial'] = self.default
                defaults['show_hidden_initial'] = True
            else:
                defaults['initial'] = self.get_default()
        defaults.update(kwargs)

        return form_class(**defaults)

    def validate(self, value, model_instance):
        if isinstance(value, list):
            valid_choices = [k for k, v in self.choices]
            for choice in value:
                if choice not in valid_choices:
                    raise ValidationError(
                        self.error_messages['invalid_choice'] % choice)

    def _get_display(field):
        def _inner(self):
            values = getattr(self, field.attname)
            return ', '.join([force_unicode(
                field.choices_dict.get(value, value),
                strings_only=True
            ) for value in values])
        return _inner

    def contribute_to_class(self, cls, name):
        self.set_attributes_from_name(name)
        self.model = cls
        cls._meta.add_field(self)
        self.choices_dict = dict(self.choices)
        setattr(cls, 'get_%s_display' % self.name, self._get_display())
'''
# END MultiSelectField - snippet #2708
