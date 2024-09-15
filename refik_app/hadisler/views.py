from django.views.generic import DeleteView, CreateView, DetailView, ListView, UpdateView
from .models import Hadisler
from .forms import HadislerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

# Create your views here.

class HadislerListView(LoginRequiredMixin, ListView):
    model = Hadisler
    context_object_name = "object"
    login_url ="/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = [str(i).split(".")[2] for i in Hadisler._meta.fields[:5]]
        model_name = Hadisler._meta.app_label.capitalize()
        objects = Hadisler.objects.all()
        values = sorted([i[:] for i in objects.values_list()])

        context["items"] = {
            "fields":fields,
            "model_name":model_name,
 
            "objects": objects,
            "values":values
        }
        return context

    def get_queryset(self):
        return self.request.user.hadisler.all()

class HadisDetailView(DetailView):
    model = Hadisler
    context_object_name = "object"

class HadislerCreateView(CreateView):
    model = Hadisler
    success_url = "/hadisler"
    form_class = HadislerForm
    context_object_name = "object"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class HadislerDeleteView(DeleteView):
    model = Hadisler
    success_url = "/hadisler"
    context_object_name = "object"

class HadislerUpdateView(UpdateView):
    model = Hadisler
    success_url = "/hadisler"
    form_class = HadislerForm
    context_object_name = "object"