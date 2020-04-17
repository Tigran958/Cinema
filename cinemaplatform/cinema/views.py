from django.shortcuts import render, get_object_or_404, redirect
# from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from . models import *
from .serializers import PresentationSerializer, BookingSerializer
from django.views.generic import CreateView, ListView
from django.forms import modelformset_factory, inlineformset_factory
from . forms import BookingForm

# Create your views here.

class HomeViewSet(APIView):
	# renderer_classes = [TemplateHTMLRenderer]
	# template_name = 'cinema/home.html'

	def get(self, request):
		queryset = Presentation.objects.all()
		serializer = PresentationSerializer(queryset, many=True)
		return Response({'profiles': serializer.data})

	def post(self, request):
		serializer = PresentationSerializer(data=request.data, many=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors)

class PresentationDetail(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'cinema/profile_detail.html'

    def get(self, request, pk):
        presentation = Presentation.objects.get(pk=pk)
        serializer = PresentationSerializer(presentation)
        return Response(serializer.data)

    def post(self, request, pk):
        presentation = get_object_or_404(Presentation, pk=pk)
        serializer = PresentationSerializer(presentation, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    def put(self, request, pk):
        presentation = get_object_or_404(Presentation, pk=pk)
        serializer = PresentationSerializer(presentation, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
    	presentation = get_object_or_404(Presentation, pk=pk)
    	
    	presentation.delete()
    	return redirect('/')
# def booking(request):
# 	a = Booking.objects.all()

# 	context = {"a":a}
# 	p = a.get(id=1)
# 	b = list(p.seats)
# 	print(b)
# 	return render(request, "cinema/booking.html", context)

class BookingViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
					mixins.RetrieveModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):

	serializer_class = BookingSerializer
	queryset = Booking.objects.all()

	def create(self, request):
		serializer = BookingSerializer(data=request.data, many=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors)
		




# BookingInlineFormset = inlineformset_factory(Booking,Presentation,fields='__all__')	
BookingFormset = modelformset_factory(Booking, form=BookingForm, fields=('custommer_email','movie','phone','seats'), extra=2)

class BookingCreate(CreateView):
	template_name = 'cinema/booking.html'
	model = Booking
	form_class = BookingForm
	# queryset = Booking.objects.none()

	def get_context_data(self, **kwargs):
		context = super(BookingCreate, self).get_context_data(**kwargs)
		context['formset'] = BookingFormset(queryset=Booking.objects.none())
		return context

	def post(self, request, *args, **kwargs):
		formset = BookingFormset(request.POST)
		if formset.is_valid():
			print(formset)
			return self.form_valid(formset)

	def form_valid(self, formset):
		formset.save()
		return redirect('/')	

class BookingList(ListView):
	template_name = 'cinema/booking_list.html'
	queryset = Booking.objects.all()
