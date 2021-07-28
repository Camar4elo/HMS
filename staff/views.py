from django.shortcuts import render
from staff.models import Staff
from django.views.generic.base import View
from django.views import generic


class StaffView(View):
    def get(self, request):
        staff = Staff.objects.all()
        return render(request, "staff_list.html", {"staff": staff})


class StaffDetailView(generic.DetailView):
    def get(self, request, pk):
        employee = Staff.objects.filter(pk=pk).first()
        return render(request, "staff_detail.html", {"employee": employee})
