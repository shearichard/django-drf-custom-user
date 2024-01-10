from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
#
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)




