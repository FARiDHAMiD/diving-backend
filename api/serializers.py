from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class CourseFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFeature
        fields = '__all__'

class CourseLearningPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLearningPoint
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'rating', 'review']

class CourseSerializer(serializers.ModelSerializer):
    features = CourseFeatureSerializer(many=True, read_only=True)
    learning_points = CourseLearningPointSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    favorites = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'favorites']
