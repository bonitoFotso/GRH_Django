from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
# Create your views here.


class EmployerCreateView(CreateView):
    model = Employer
    template_name = "employer/emp_reg.html"
    fields = ('nom', 'prenom', 'tel', 'tel_pro', )
    success_url = reverse_lazy('list')
    
class EmployerUpdateView(UpdateView):
    model = Employer
    fields = ('nom', 'prenom', 'tel', 'tel_pro', )
    template_name = "employer/emp_reg.html"
    success_url = reverse_lazy('list')
    
class EmployerDeleteView(DeleteView):
    model = Employer
    template_name = "employer/emp_conf_del.html"
    success_url = reverse_lazy('list')

class EmployerList(ListView):
    model = Employer
    fields = ('nom', 'prenom', 'tel', 'tel_pro', )
    template_name='employer/emp_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field"] = self.fields
        return context
    

class EmployerDetail(DetailView):
    model = Employer
    template_name='employer/emp_detail.html'


class CrudCreateView(CreateView):
    model = ''
    fields = ['title', 'content', 'created_at', 'last_modified']
    template_name = 'crud/crud_form.html'
    success_url = reverse_lazy('crud:crud_list')

