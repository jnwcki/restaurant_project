from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse

from main.models import Restaurant, Order, Item
from main.forms import NewUserCreationForm, NewManagerCreationForm


class SignupConsumer(CreateView):
    model = User
    form_class = NewUserCreationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.user = new_user
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class SignupManager(CreateView):
    model = User
    form_class = NewManagerCreationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.user = new_user
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.is_staff = True
        new_user.save()
        return super().form_valid(form)


class RestaurantListView(ListView):
    model = Restaurant


class RestaurantDetailView(DetailView):
    model = Restaurant


class OrderHistoryView(ListView):
    model = Order
    template_name = 'main/orderhistory_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.userprofile).order_by('-date')


class OrderCreateView(CreateView):
    model = Order
    fields = ('items', 'notes')

    def form_valid(self, form):
        order_object = form.save(commit=False)
        order_object.restaurant = Restaurant.objects.get(pk=self.kwargs.get('pk'))
        order_object.user = self.request.user.userprofile
        order_object.save()
        order_items = form.cleaned_data['items']
        for item in order_items:
            order_object.items.add(item)
        total_price = sum([item.price for item in order_object.items.all()])
        order_object.total_price = total_price
        return super().form_valid(form)

    def get_success_url(self):
        order = Order.objects.filter(user=self.request.user.userprofile).last()
        return reverse('order_detail_view', args=(order.pk, ))


class OrderConfirmationView(DetailView):
    model = Order
    template_name = 'main/order_confirmation.html'


class OrderDetailView(DetailView):
    model = Order


class OrderUpdateView(UpdateView):
    model = Order
    fields = ('items', 'notes')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        order = Order.objects.filter(user=self.request.user.userprofile).last()
        return reverse('order_detail_view', args=(order.pk, ))


class ItemDetailView(DetailView):
    model = Item




































class MainView(TemplateView):
    template_name = 'index.html'
