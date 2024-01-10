from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 
                  'title', 'code', 'linenos', 'language', 'style']


