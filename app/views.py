from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import BookTable, AboutUs, Feedback, ItemList, Items
from app.models import BookTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BookTable
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
