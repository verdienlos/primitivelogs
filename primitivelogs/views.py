# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

# Create your views here.

from .models import PrimitiveLog

class PrimitiveLogListView(ListView):
    model = PrimitiveLog
    template_name = 'primitivelog/plog_list.html'
    context_object_name = "plog_list"
    #paginate_by = 5

    queryset = PrimitiveLog.objects.filter(archived=False)
    
    @method_decorator(permission_required('primitivelog.moderate_primitivelog', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(PrimitiveLogListView, self).dispatch(*args, **kwargs)


