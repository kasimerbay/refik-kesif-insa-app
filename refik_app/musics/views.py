from django.views.generic import DeleteView, CreateView, DetailView, ListView, UpdateView
from .models import Musics
from .forms import MusicForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MusicListView(LoginRequiredMixin, ListView):
    model = Musics
    context_object_name = "musics"
    login_url ="/login"

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)

        fields = [str(i).split(".")[2] for i in Musics._meta.fields]
        print(fields)
        objects = Musics.objects.all()
        values = sorted([i for i in objects.values_list()])
        iters = [list(i) for i in zip(values,objects)]

        context["items"] = {
            "fields":fields,
            "model_name":"Müzikler",
            "iters":iters,
            "objects": objects,
            "values":values
        }

        return context

    def get_queryset(self):
        return self.request.user.hadisler.all()
    

class MusicDetailView(DetailView):
    model = Musics
    context_object_name = "object"

class MusicCreateView(CreateView):
    model = Musics
    success_url = "/musics"
    form_class = MusicForm
    context_object_name = "object"

class MusicDeleteView(DeleteView):
    model = Musics
    success_url = "/musics"
    context_object_name = "object"

class MusicUpdateView(UpdateView):
    model = Musics
    success_url = "/musics"
    form_class = MusicForm
    context_object_name = "object"