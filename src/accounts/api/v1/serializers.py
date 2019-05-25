from django.contrib.auth import get_user_model

from rest_framework.serializers import (ModelSerializer)

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password',

                  ]
        extra_kwargs = {"password": {"write_only": True}}


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token',

        ]
        extra_kwargs = {"password": {"write_only": True}}