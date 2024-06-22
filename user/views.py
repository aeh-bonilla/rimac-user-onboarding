from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from .utils import get_paginated_users


# Logica para obtener todas las películas
@api_view(['GET'])
def gets(request):
    #  Obtiene todas las películas
    users = User.objects.all()
    
    # Obtiene la página solicitada de películas
    users_page = get_paginated_users(request, users, 10)
    
    # Serializa los datos de la película
    serializer = UserSerializer(users_page, many=True)

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'Users found successfully',
        'data': {
            'users': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Logica para buscar una película
@api_view(['GET'])
def search(request):
    # Obtener el parámetro de búsqueda
    query = request.GET.get('query')

    # Comprueba que se proporcione un parámetro de búsqueda
    if not query:
        return Response({
            'status': 'error',
            'message': 'Incorrect search parameters'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Busca las películas que coincidan
    users = User.objects.filter(
        Q(title__icontains=query),
    ).distinct()

    # No existe películas con el titulo
    if not users:
        return Response({
            'status': 'error',
            'message': 'No users found matching your search'
        }, status=status.HTTP_404_NOT_FOUND)

    # Serializa los datos de la película
    serializer = UserSerializer(users, many=True)

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'Users found successfully',
        'data': {
            'users': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Logica para crear una película
@api_view(['POST'])
def create(request):
    # Serializa los datos recibidos en la solicitud
    serializer = UserSerializer(data=request.data)

    # Verifica los datos válidos
    if serializer.is_valid():
        # Guarda los datos de la película
        serializer.save()

        # Devuelve los datos
        return Response({
            'status': 'success',
            'message': 'User created successfully',
            'data': {
                'user': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Devuelve los errores de validación
    return Response({
        'status': 'error',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Logica para actualizar la pelicula
@api_view(['PUT'])
def update(request, user_id):
    # Obtiene la película por su ID
    user = get_object_or_404(User, id=user_id)

    # Serializa los datos de la película
    serializer = UserSerializer(user, data=request.data)

    # Verifica los datos válidos
    if serializer.is_valid():
        # Guarda los datos de la película
        serializer.save()

        # Devuelve los datos
        return Response({
            'status': 'success',
            'message': 'User updated successfully',
            'data': {
                'user': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Devuelve los errores de validación
    return Response({
        'status': 'error',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Logica para eliminar la película
@api_view(['DELETE'])
def delete(request, user_id):
    # Obtine la película por su ID
    user = get_object_or_404(User, id=user_id)

    # Elimina la película
    user.delete()

    # Devuelve los datos
    return Response({
        'status': 'success',
        'message': 'User deleted successfully'
    }, status=status.HTTP_204_NO_CONTENT)
