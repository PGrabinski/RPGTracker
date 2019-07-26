from django.forms import ModelForm
from .models import Character

class AddCharacterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            css_class = 'validate center-align'
            field.field.widget.attrs['class'] = css_class
    class Meta:
        model = Character
        fields = ['name', 'career_path', 'career_level', 'story']