from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import Skill, Category, Review, Booking

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created! You can now log in.")
        return response

class SkillListView(ListView):
    model = Skill
    template_name = 'skills/skill_list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        queryset = Skill.objects.filter(is_available=True)
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(title__icontains=query)
        if category:
            queryset = queryset.filter(category_id=category)
            
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class DashboardView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'skills/dashboard.html'
    context_object_name = 'my_skills'

    def get_queryset(self):
        return Skill.objects.filter(owner=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Requests sent TO me (as owner)
        context['received_bookings'] = Booking.objects.filter(skill__owner=self.request.user).order_by('-created_at')
        # Requests sent BY me (as requester)
        context['my_requests'] = Booking.objects.filter(requester=self.request.user).order_by('-created_at')
        return context

class SkillDetailView(DetailView):
    model = Skill
    template_name = 'skills/skill_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-created_at')
        # Check if user already requested this
        if self.request.user.is_authenticated:
            context['has_requested'] = Booking.objects.filter(skill=self.object, requester=self.request.user).exists()
        return context

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    template_name = 'skills/skill_form.html'
    fields = ['title', 'description', 'category', 'price', 'is_free', 'contact_preference', 'is_available']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Skill post created!")
        return super().form_valid(form)

class SkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Skill
    template_name = 'skills/skill_form.html'
    fields = ['title', 'description', 'category', 'price', 'is_free', 'contact_preference', 'is_available']
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.request.user == self.get_object().owner

class SkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skill
    template_name = 'skills/skill_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.request.user == self.get_object().owner

# --- NEW FEATURES ---

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['message']
    
    def form_valid(self, form):
        skill = get_object_or_404(Skill, pk=self.kwargs['pk'])
        if skill.owner == self.request.user:
            messages.error(self.request, "You can't book your own skill!")
            return redirect('skill_detail', pk=skill.pk)
            
        form.instance.skill = skill
        form.instance.requester = self.request.user
        messages.success(self.request, "Request sent to the owner!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('skill_detail', kwargs={'pk': self.kwargs['pk']})

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'comment']

    def form_valid(self, form):
        skill = get_object_or_404(Skill, pk=self.kwargs['pk'])
        form.instance.skill = skill
        form.instance.reviewer = self.request.user
        messages.success(self.request, "Thank you for your review!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('skill_detail', kwargs={'pk': self.kwargs['pk']})

class BookingStatusUpdateView(LoginRequiredMixin, View):
    def post(self, request, pk, status):
        booking = get_object_or_404(Booking, pk=pk)
        if booking.skill.owner == request.user:
            if status in ['approved', 'rejected', 'completed']:
                booking.status = status
                booking.save()
                messages.success(request, f"Request status updated to {status}.")
        return redirect('dashboard')
