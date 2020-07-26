# Develop: vmgabriel

"""Module for Control of Forms Validate"""

from django import forms

from .models import Priority, TypeConsume


class PriorityForm(forms.ModelForm):
    """Class For Priority Form"""
    class Meta:
        """Meta Class for Form"""
        model = Priority
        fields = '__all__'

    def clean_name(self):
        """Clean Name form"""
        return self.cleaned_data['name']

    def clean_description(self):
        """Clean Description form"""
        return self.cleaned_data['description']

    def save(self, commit=True):
        """Save Data Valid"""
        instance = super(PriorityForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class TypeConsumeForm(forms.ModelForm):
    """Class For Type Consume Form"""
    class Meta:
        """Meta Class for Form"""
        model = TypeConsume
        fields = '__all__'

    def clean_name(self):
        """Clean Name form"""
        return self.cleaned_data['name']

    def clean_description(self):
        """Clean Description form"""
        return self.cleaned_data['description']

    def save(self, commit=True):
        """Save Data Valid"""
        instance = super(TypeConsumeForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
