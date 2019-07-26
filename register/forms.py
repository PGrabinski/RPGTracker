from django.contrib.auth.forms import UserCreationForm
from history.models import Player
# from pprint import pprint

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            css_class = 'validate center-align'
            field.field.widget.attrs['class'] = css_class

    class Meta(UserCreationForm.Meta):
        model = Player
        fields = UserCreationForm.Meta.fields + ('email','first_name', 'last_name', 'nickname', )