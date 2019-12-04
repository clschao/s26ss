
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm02.settings")
    import django
    django.setup()

    from app01 import models

    ret = models.Book.objects.all().values('title')
    print(ret)

















