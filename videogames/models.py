from django.db import models

# Create your models here.

class Platform(models.Model):
    platform_name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    platform_release_year = models.IntegerField()

    def __str__(self):
        return self.platform_name

class Developer(models.Model):
    developer_name = models.CharField(max_length = 200)
    developer_location = models.CharField(max_length = 200)
    developer_fundation_year = models.IntegerField()

    def __str__(self):
        return self.developer_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length = 200)
    publisher_location = models.CharField(max_length = 200)
    publisher_fundation_year = models.IntegerField()

    def __str__(self):
        return self.publisher_name

class Game_Genre(models.Model):
    genre_name = models.CharField(max_length = 100)
    desc_genre = models.CharField(max_length = 300)

    def __str__(self):
        return self.genre_name

class Game_Status(models.Model):
    game_status = models.CharField(max_length = 100)
    desc_status = models.CharField(max_length = 300)

    def __str__(self):
        return self.game_status

class Game_Format(models.Model):
    game_format = models.CharField(max_length = 100)
    desc_format = models.CharField(max_length = 300)

    def __str__(self):
        return self.game_format

class Purchase_Status(models.Model):
    purchase_status = models.CharField(max_length = 100)
    desc_purchase_status = models.CharField(max_length = 300)

    def __str__(self):
        return self.purchase_status

class Game(models.Model):
    game_name = models.CharField(max_length = 200)
    platform_name = models.ForeignKey(Platform, on_delete=models.CASCADE)
    developer_name = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    game_release_date = models.DateField()
    genre_name = models.ForeignKey(Game_Genre, on_delete=models.CASCADE)
    game_cover = models.CharField(max_length = 200)
    purchase_price = models.FloatField()
    game_purchase_date = models.DateField()
    game_status = models.ForeignKey(Game_Status, on_delete=models.CASCADE)
    game_format = models.ForeignKey(Game_Format, on_delete=models.CASCADE)
    purchase_status = models.ForeignKey(Purchase_Status, on_delete=models.CASCADE)

    def __str__(self):
            #return [self.gameName, self.gamereleaseYear, self.developer, self.console]
            return self.game_name