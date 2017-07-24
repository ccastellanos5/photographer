from django.db import models

TYPE_CHOICES = (
('W','weddings'),
('B','babys'),
('F', 'family'),
('S', 'sesion'),
('G', 'Graduation'),
)
class Album(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class Image(models.Model):
    img = models.ImageField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.album.name
