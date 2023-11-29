from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView

from custom_auth.forms import CustomUserCreateForm, LoginForm


class RegisterView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('books_list')
    template_name = 'custom_auth/registration.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('books_list')
    else:
        form = LoginForm()
    return render(request, 'custom_auth/login.html', context={'form': form})
