from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=220)
  pub_date = models.DateField()
  body = models.TextField()
  image = models.ImageField(upload_to='images/')


  # to make the blogs to show title
  def __str__(self):
    return self.title

  # to limit body text
  def summary(self):
    return self.body[200]

  # making date pretty
  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %y')


