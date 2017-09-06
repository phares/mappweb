from django.db import models

# Create your models here.


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='customers', blank=False, on_delete=models.CASCADE)
    message = models.CharField(max_length=140, blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.message)
