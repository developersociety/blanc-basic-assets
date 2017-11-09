from itertools import groupby

from django.db import models
from django.forms.models import ModelChoiceField
from django.utils.encoding import force_text


class GroupedModelChoiceField(ModelChoiceField):
    def __init__(self, queryset, group_by_field='category', group_label=None, *args, **kwargs):
        """
        group_by_field is the name of a field on the model
        group_label is a function to return a label for each choice group
        """
        super(GroupedModelChoiceField, self).__init__(queryset, *args, **kwargs)
        self.group_by_field = group_by_field
        if group_label is None:
            self.group_label = lambda group: force_text(group)
        else:
            self.group_label = group_label

        # Need correct ordering, and category titles
        self.queryset = self.queryset.select_related().order_by('category', 'title')

    def _get_choices(self):
        """
        Exactly as per ModelChoiceField except returns new iterator class
        """
        if hasattr(self, '_choices'):
            return self._choices
        return GroupedModelChoiceIterator(self)
    choices = property(_get_choices, ModelChoiceField._set_choices)


class GroupedModelChoiceIterator(object):
    def __init__(self, field):
        self.field = field
        self.queryset = field.queryset

    def __iter__(self):
        if self.field.empty_label is not None:
            yield ('', self.field.empty_label)

        queryset = self.queryset.all()
        # Can't use iterator() when queryset uses prefetch_related()
        if not queryset._prefetch_related_lookups:
            queryset = queryset.iterator()

        grouped_queryset = groupby(
            queryset, key=lambda row: getattr(row, self.field.group_by_field)
        )
        for group, choices in grouped_queryset:
            yield (self.field.group_label(group), [self.choice(obj) for obj in choices])

    def choice(self, obj):
        return (self.field.prepare_value(obj), self.field.label_from_instance(obj))


class AssetForeignKey(models.ForeignKey):
    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', GroupedModelChoiceField)
        return super(AssetForeignKey, self).formfield(**kwargs)
