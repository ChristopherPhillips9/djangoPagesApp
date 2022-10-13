from django.views.generic import TemplateView

# Had to include pages/xxxx.html because it would not find the pages otherwise.
# TODO Fix pages/xxxx.html


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
