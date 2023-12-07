from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    ordering_fields = ['name', 'email', 'phone']  # Добавляем поля для сортировки
    search_fields = ['name', 'email'] # Добавляем поля для поиска


    def get_queryset(self):
        # queryset = Contact.objects.all(): 
        # Создает изначальный queryset, который включает все объекты 
        # модели Contact.
        queryset = Contact.objects.all()
        
        # search_term = self.request.query_params.get('search', None): 
        # Извлекает значение параметра search из параметров запроса 
        # (query_params). Если параметр не указан, search_term будет 
        # равен None.
        search_term = self.request.query_params.get('search', None)
        
        # if search_term:: Проверяет, есть ли значение search_term. 
        # Если значение существует (не является None), 
        # выполняется следующий блок кода.
        if search_term:
            
            # queryset = queryset.filter(name__icontains=search_term) | 
            # queryset.filter(email__icontains=search_term): 
            # Фильтрует queryset, оставляя только те объекты, 
            # у которых поле name или email содержит подстроку, 
            # заданную в search_term. Оператор | представляет логическое ИЛИ, 
            # что означает, что результат будет объект, у которого либо поле 
            # name, либо поле email соответствует поисковому запросу, 
            # или оба поля соответствуют.
            queryset = queryset.filter(name__icontains=search_term) |\
                       queryset.filter(email__icontains=search_term) 
        
        return queryset
    
    def post(self, request, *args, **kwargs):
        if len(request.data.get('name', '')) < 10:
            return Response(
                {'error': 'Имя не может быть меньше 10 символов.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return super().post(request, *args, **kwargs)
    


class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'  # Указываем, что для обновления или удаления объекта 
                         # используется поле id, а не имя объекта.
                         
    # def get_queryset(self):
    #     queryset = Contact.objects.all()
    #     search_term = self.request.query_params.get('search', None)
    #     if search_term:
    #         queryset = queryset.filter(name__icontains=search_term) |\
    #                    queryset.filter(email__icontains=search_term)
    #     return queryset
    

"""
viewset Contact
    - name
    - email
    - phone
    - description
"""

"""
generics Contact
    - name
    - email
    - phone
    - description

if post:
    if len(name) < 10:
        return 'Имя не может быть меньше 10 символов.
"""