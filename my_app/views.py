from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
import os

class ReactAppView(View):
    def get(self, request):
        try:
            react_path = os.path.join(os.getcwd(), 'frontend', 'build', 'index.html')
            print('REACT PATH', react_path)
            with open(react_path) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )
