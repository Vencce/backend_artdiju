from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Subscriber
from .serializers import ProductSerializer, SubscriberSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        # 1. Cria o produto normalmente
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # 2. Verifica se o admin marcou a opção de notificar
        # O frontend envia como string 'true' ou 'false' dentro do FormData
        notify = request.data.get('notify_users') == 'true'
        
        # 3. Se marcado, dispara os e-mails
        if notify:
            self.send_notification_email(serializer.instance)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def send_notification_email(self, product):
        # Pega todos os e-mails do banco
        subscribers = Subscriber.objects.values_list('email', flat=True)
        
        if not subscribers:
            return

        subject = f'Novidade na Art Di Ju: {product.name}!'
        
        # Monta a mensagem do e-mail
        message = (
            f'Olá!\n\n'
            f'Acabamos de adicionar uma peça exclusiva na nossa loja: {product.name}.\n'
            f'Venha conferir antes que acabe!\n\n'
            f'Categoria: {product.category}\n'
            f'Preço: R$ {product.price}\n\n'
            f'Acesse agora nossa vitrine para ver os detalhes.'
        )
        
        try:
            # Envia o e-mail em massa
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, # Remetente (configurado no settings.py)
                list(subscribers),        # Lista de destinatários
                fail_silently=True,       # Se falhar, não trava o app
            )
            print(f"E-mail enviado para {len(subscribers)} inscritos.")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

# View para salvar novos inscritos da Newsletter
class SubscribeView(APIView):
    permission_classes = [AllowAny] # Qualquer um pode se inscrever

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)