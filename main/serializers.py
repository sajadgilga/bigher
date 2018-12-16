from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.compat import get_username_field, PasswordField, Serializer
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from django.utils.translation import ugettext as _
from rest_framework_jwt.settings import api_settings

from main.models import User_profile

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomJWTSerializer(JSONWebTokenSerializer):
    """
       Serializer class used to validate a username and password, or custom email and password.

       'username' is identified by the custom UserModel.USERNAME_FIELD.

       Returns a JSON Web Token that can be used to authenticate later calls.
    """

    def validate(self, attrs):
        # user_obj = self.create_guest_user()
        user_obj = User.objects.get(username=attrs['username'])
        # user_obj.save()

        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': attrs['password']
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                # user_profile = Profile.objects.create(user=user_obj)
                # user_profile.save()
                if user:
                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.required_field)
                raise serializers.ValidationError(msg)


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = ('user', 'name', 'XP',
                  'picture', 'accepted_challenges', 'follows')
