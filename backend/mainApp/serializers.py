from rest_framework.serializers import ModelSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
    """
    Serializer dla modelu Comment.

    Mapuje pola modelu Comment na format JSON i obsługuje walidację danych wejściowych.

    Fields:
    - title (str): Tytuł komentarza.
    - date_time (datetime): Data i czas utworzenia komentarza.
    - comment (str): Treść komentarza.
    """
    class Meta:
        model = Comment
        fields = ['title', 'date_time', 'comment']