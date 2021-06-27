from django.forms import ModelForm
from videogames.models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        #fields = ['console','developer','game_name','game_release_year','game_cover']
        #fields = ['console','developer','game_name']
    
    '''
    game_name = forms.CharField(max_length = 200)
    game_release_year = forms.IntegerField()
    developer = forms.IntegerField()
    console = forms.IntegerField()
    game_cover = forms.CharField(max_length = 200)
    '''
    
    