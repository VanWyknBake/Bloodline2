from django.db import models
from django.contrib.auth.models import User

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=50)
    
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career






# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    title = models.CharField(default="Video Title", max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Portfolio {self.id}'

# STREAMER SECTION

class Streamers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name


# Tournament section

class Tourn(models.Model):
    tp = models.CharField(max_length=100, default='Tournament / Scrim')
    host = models.CharField(max_length=50)
    macth = models.CharField(max_length=20)
    details = models.TextField(blank=False)
    
    room = models.CharField(max_length=500, null=True, blank=True)

    when = models.DateTimeField(null=True)

    updated = models.DateTimeField(auto_now=True)
    

  

    def __str__(self):
        return self.host


class Results(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    gametype = models.CharField(max_length=2, default="MP/BR")
    game = models.ForeignKey(Tourn, on_delete=models.CASCADE)
    result = models.CharField(max_length=100, default="WIN 5-0")
    when = models.DateField(null=True)

    def __str__(self):
        return self.result
    

# News 

# ABOUT SECTION

class News(models.Model):
    topic = models.CharField(max_length=50)
    
    content = models.TextField(blank=False)
    img = models.ImageField(upload_to='news/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


class Profile2(models.Model):
    about = models.ForeignKey(News,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=15)
    link = models.URLField(max_length=200)

class Store(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='store/')
    link = models.URLField(max_length=200)
    price = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name
    



