from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    paginate_by = 10
    template_name = 'employees/employee_list.html'
  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        email = self.request.GET.get('email')
        mobile = self.request.GET.get('mobile')
        date_of_birth = self.request.GET.get('date_of_birth')
        sort_by = self.request.GET.get('sort')
        order = self.request.GET.get('order')
        employees_obj = Employee.objects.all()
        

        if name:
            employees_obj = employees_obj.filter(
                Q(first_name__icontains=name) | 
                Q(last_name__icontains=name)
            )
        if email:
            employees_obj = employees_obj.filter(
                Q(email__icontains=email) 
            )

        if mobile:
            employees_obj = employees_obj.filter(
                Q(mobile__icontains=mobile)
            )
        if date_of_birth:
            employees_obj = employees_obj.filter(
                Q(date_of_birth__icontains=date_of_birth) 
            )
        
        if order and sort_by:
            if order == 'asc':
                employees_obj = employees_obj.order_by(sort_by)
            else:
                employees_obj = employees_obj.order_by("-"+sort_by)

        page = self.request.GET.get('page')
        paginator = Paginator(employees_obj, self.paginate_by)

        try:
            employees_obj = paginator.page(page)
        except PageNotAnInteger:
            employees_obj = paginator.page(1)
        except EmptyPage:
            employees_obj = paginator.page(1)
        except Http404:
            employees_obj = paginator.page(1)
        context['employees_obj'] = employees_obj
        return context
class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    # template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')
