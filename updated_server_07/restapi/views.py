# -*- coding: utf-8 -*-`
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import House
from .models import mem_details
from .models import imagetable
from .models import videotable
from .models import FarmTable
from .models import farmpoints
from .models import farmcroptable
from .models import welltable
from .models import wellinfo
from .models import newfarmcroptable
from .serializers import HouseSerializer
from .serializers import mem_detailsSerializer
from .serializers import imagetableSerializer
from .serializers import videotableSerializer
from .serializers import FarmTableSerializer
from .serializers import farmpointsSerializer
from .serializers import farmcroptableSerializer
from .serializers import welltableSerializer
from .serializers import wellinfoSerializer
from .serializers import newfarmcroptableSerializer


# Create your views here.
#creating REST API from the data of the serializer object for each table of the database

class HouseList(APIView):
	def get(self,request):
		houses=House.objects.all()
		serializer=HouseSerializer(houses,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class mem_detailsList(APIView):
	def get(self,request):
		mem_details_obj=mem_details.objects.all()
		serializer=mem_detailsSerializer(mem_details_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class imagetableList(APIView):
	def get(self,request):
		imagetable_obj=imagetable.objects.all()
		serializer=imagetableSerializer(imagetable_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class videotableList(APIView):
	def get(self,request):
		videotable_obj=videotable.objects.all()
		serializer=videotableSerializer(videotable_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class FarmTableList(APIView):
	def get(self,request):
		FarmTable_obj=FarmTable.objects.all()
		serializer=FarmTableSerializer(FarmTable_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class farmcroptableList(APIView):
	def get(self,request):
		farmcroptable_obj=farmcroptable.objects.all()
		serializer=farmcroptableSerializer(farmcroptable_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class welltableList(APIView):
	def get(self,request):
		welltable_obj=welltable.objects.all()
		serializer=welltableSerializer(welltable_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class farmpointsList(APIView):
	def get(self,request):
		farmpoints_obj=farmpoints.objects.all()
		serializer=farmpointsSerializer(farmpoints_obj,many=True)
		return Response(serializer.data)
	def post(self):
		pass
class wellinfoList(APIView):
        def get(self,request):
                wellinfo_obj=wellinfo.objects.all()
                serializer=wellinfoSerializer(wellinfo_obj,many=True)
                return Response(serializer.data)
        def post(self):
                pass
class newfarmcroptableList(APIView):
        def get(self,request):
                newfarmcroptable_obj=newfarmcroptable.objects.all()
                serializer=newfarmcroptableSerializer(newfarmcroptable_obj,many=True)
                return Response(serializer.data)
        def post(self):
                pass


