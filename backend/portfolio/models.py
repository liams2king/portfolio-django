from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('uiux', 'UI/UX Design'),
        ('frontend', 'Développement Web'),
        ('fullstack', 'Développement Full-Stack'),
        ('data', 'Analyse de Données'),
        ('perf', 'Optimisation de Performance'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='frontend')
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Message(models.Model):
        nom = models.CharField(max_length=100)
        email = models.EmailField()
        sujet = models.CharField(max_length=200)
        contenu = models.TextField()
        date_envoye = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.nom} - {self.sujet}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name