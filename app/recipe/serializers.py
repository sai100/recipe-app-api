'''
Serializers for recipe APIS.
'''

from rest_framework import serializers

from core.models import (
    Recipe,
    Tag,
)


class RecipeSerializer(serializers.ModelSerializer):
    '''Serializer for recipes.'''

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'price', 'link', 'time_minutes']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    '''Serializer for recipe detail view.'''

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    '''Serializer for tag objects.'''

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
