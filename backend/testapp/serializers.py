from rest_framework import serializers

from .models import Note, Test


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'test']
        read_only_fields = ['id']


class TestSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(read_only=True, many=True)
    note = serializers.CharField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = Test
        fields = ['id', 'note', 'notes']
        read_only_fields = ['id', 'notes']

    def create(self, validated_data):
        note_text = validated_data.pop('note', None)
        instance = Test.objects.create(**validated_data)
        
        if note_text:
            print(self.context['request'].user)
            Note.objects.create(test=instance, title=note_text)

        return instance