from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PrincipalView(TemplateView):
    template_name = "paginas/principal.html"


@method_decorator(login_required, name='dispatch')
class PaginaUm(TemplateView):
    template_name = "paginas/pagina_um.html"

@method_decorator(login_required, name='dispatch')
class PaginaDois(TemplateView):
    template_name = "paginas/pagina_dois.html"
