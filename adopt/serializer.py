from .models import Adopt
from .models import Quiz
from rest_framework import serializers

class AdoptSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Adopt
        fields = ('pk','title','body','author_name','image')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('pk','title','body','answer') 