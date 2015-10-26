from django.forms import ModelForm, Form
from django import forms
from classpicker.models import Pick, PickUser


class PickStartForm(ModelForm):
    opponent_battle_tag = forms.CharField(label='opponent', max_length=20)

    class Meta:
        model = PickUser
        fields = ['battle_tag']
        

class PickForm(Form):
    paladin = forms.BooleanField(label='Paladin')
    hunter = forms.BooleanField(label='Hunter')
    mage = forms.BooleanField(label='Mage')
    priest = forms.BooleanField(label='Priest')
    shaman = forms.BooleanField(label='Shaman')
    warrior = forms.BooleanField(label='Warrior')
    warlock = forms.BooleanField(label='Warlock')
    druid = forms.BooleanField(label='Druid')
    rogue = forms.BooleanField(label='Rogue')

#
#
# class BanForm(ModelForm):
#     class Meta:
#         model = Pick
#         fields = ['first_bans_paladin',
#                   'first_bans_mage',
#                   'first_bans_warrior',
#                   'first_bans_shaman',
#                   'first_bans_priest',
#                   'first_bans_rogue',
#                   'first_bans_hunter',
#                   'first_bans_warlock',
#                   'first_bans_druid',
#                   ]
