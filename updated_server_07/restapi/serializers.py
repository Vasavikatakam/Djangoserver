from rest_framework import serializers
from .models import House
from .models import mem_details
from .models import imagetable
from .models import videotable
from .models import FarmTable
from .models import farmpoints
from .models import farmcroptable
from .models import newfarmcroptable
from .models import welltable
from .models import wellinfo
class HouseSerializer(serializers.ModelSerializer):
     class Meta:
     		model=House
     		#fields=('ticker','volume')
     		fields='__all__'    
class mem_detailsSerializer(serializers.ModelSerializer):
     class Meta:
     		model=mem_details
     		#fields=('ticker','volume')
     		fields='__all__'    
class imagetableSerializer(serializers.ModelSerializer):
     class Meta:
     		model=imagetable
     		#fields=('ticker','volume')
     		fields='__all__'    
class videotableSerializer(serializers.ModelSerializer):
     class Meta:
     		model=videotable
     		#fields=('ticker','volume')
     		fields='__all__'    
class FarmTableSerializer(serializers.ModelSerializer):
     class Meta:
     		model=FarmTable
     		#fields=('ticker','volume')
     		fields='__all__'    
class farmpointsSerializer(serializers.ModelSerializer):
     class Meta:
     		model=farmpoints
     		#fields=('ticker','volume')
     		fields='__all__'    
class farmcroptableSerializer(serializers.ModelSerializer):
     class Meta:
     		model=farmcroptable
     		#fields=('ticker','volume')
     		fields='__all__'    
class welltableSerializer(serializers.ModelSerializer):
     class Meta:
     		model=welltable
     		#fields=('ticker','volume')
     		fields='__all__'    
class wellinfoSerializer(serializers.ModelSerializer):
     class Meta:
                model=wellinfo
                #fields=('ticker','volume')
                fields='__all__'
class newfarmcroptableSerializer(serializers.ModelSerializer):
     class Meta:
                model=newfarmcroptable
                #fields=('ticker','volume')
                fields='__all__'



       		     		     		     		     		     		     		


