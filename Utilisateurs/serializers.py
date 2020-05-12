from rest_framework import serializers
from Utilisateurs.models import *



class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model                = role
        fields               = '__all__'


class infoPersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model                = infoPersonel
        fields               = '__all__'


class compteUtilisateurSerializer(serializers.ModelSerializer):
    roles = roleSerializer(many=True, required=False)
    infos = infoPersonelSerializer(required=False, read_only=True)

    def create(self, validated_data):
        obj = compteUtilisateur.objects.create(**validated_data)
        obj.save()
        return obj

    class Meta:
        model                = compteUtilisateur
        read_only_fields = ('is_admin', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')
        exclude =('password',)


class TokenSerializer(serializers.ModelSerializer):
    user = compteUtilisateurSerializer(many=False, read_only=True)
    class Meta:
        model = Token
        fields = ('key', 'user')