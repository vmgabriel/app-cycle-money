# Develop: vmgabriel

"""Module for Control of Forms Validate"""

from django import forms

from .models import Priority


class PriorityForm(forms.ModelForm):
    """Class For Priority Form"""

    class Meta:
        model = Priority
        fields = '__all__'

    def clean_name(self):
        print('clean name - {}'.format(self.cleaned_data['name']))
        return self.cleaned_data['name']

    def clean_description(self):
        print('clean description - {}'.format(
            self.cleaned_data['description']
        ))
        return self.cleaned_data['description']

    def save(self, commit=True):
        """Save Data Valid"""
        instance = super(PriorityForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
