from django.views import generic


class IndexView(generic.RedirectView):
    url = "https://documenter.getpostman.com/view/8475386/2s8YKGjgb2"
    permanent = True
