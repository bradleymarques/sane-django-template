from django.forms import ModelForm

from core.forms.mixins import BaseFormMixin


class BaseModelForm(ModelForm, BaseFormMixin):
    pass
