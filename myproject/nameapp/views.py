from django.shortcuts import render
from django.http import HttpResponse

def show_name(request, username):
    return HttpResponse(f"Hello, {username}!")