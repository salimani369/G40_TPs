from django.db import models

# Create your models here.


class Message(models.Model):
    # Expéditeur du message (max 60 caractères)
    source = models.CharField(max_length=60)
    # Destinataire du message (max 60 caractères)
    to = models.CharField(max_length=60)
    # Corps du message (texte libre)
    body = models.TextField()

    def __str__(self):
        # Représentation lisible : "source -> destinataire : message"
        return self.source + ' -> ' + self.to + ' : ' + self.body
