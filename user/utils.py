from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Función para crear paginación
def get_paginated_users(request, users, page_number):
    # Divide en página de 10 películas
    paginator = Paginator(users, page_number)
    page_number = request.query_params.get('page', 1)

    try:
        # Obtener la página solicitada
        users_page = paginator.page(page_number)

    except PageNotAnInteger:
        # Número de página no es un entero
        users_page = paginator.page(1)

    except EmptyPage:
        # Página fuera del rango
        users_page = paginator.page(paginator.num_pages)
    
    return users_page