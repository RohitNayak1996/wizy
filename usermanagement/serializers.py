from rest_framework import serializers

from usermanagement.models import Movies, CustomUser


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','password')
        extra_kwargs = {'password':{'write_only':True,
                                    'required' :True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user