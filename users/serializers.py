from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'invite_code', 'ref_code',)


class ProfileSerializer(serializers.ModelSerializer):
    reference = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'country', 'invite_code', 'ref_code', 'reference')

    def get_reference(self, obj):
        user_list = User.objects.filter(ref_code=obj.invite_code)
        return [user.phone for user in user_list]
