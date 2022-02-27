from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.conf import settings


#We are going to set our rest API so that only authenticated user can interact with our application
#Automatically redirected to login form
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        template_name="index.html"
        return template_name