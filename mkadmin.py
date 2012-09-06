#!/usr/bin/env python
from wsgi import *
from django.contrib.auth.models import User
import sys

sys.path.append('gallery')

u, created = User.objects.get_or_create(username='cong')
if created:
    u.set_password('043500')
    u.is_superuser = True
    u.is_staff = True
    u.save()
