from rest_framework import serializers

from ..models import Carlist, Showroomlist ,Review

class ReviewSerializers(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        exclude = ('car',)
        # fields = "__all__"


# This is the code for normal serializers

# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description =serializers.CharField()
#     active = serializers.CharField(read_only=True)
#     chassisnumber = serializers.CharField(validators = [alphanumeric])
#     price = serializers.DecimalField(max_digits=9, decimal_places=2)

#     def create(self, validated_data):
#         return Carlist.objects.create(**validated_data)
    
#     def update(self , instance ,validated_data):
#         instance.name =validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.chassisnumber = validated_data.get('chassisnumber',instance.chassisnumber)
#         instance.price = validated_data.get('price',instance.price)
#         instance.save()
#         return instance



    #This is the code for Model serializers

class CarSerializer(serializers.ModelSerializer):

    discounted_price = serializers.SerializerMethodField()
    Reviews = ReviewSerializers(many=True,read_only=True)
    class Meta:
        model = Carlist
        fields = "__all__"
        # exclude = ['name']
        #fields = ['name','description']

    def get_discounted_price(self, object):
        discountprice = object.price - 5000
        return discountprice

    #field level validation

    def validate_price(self,value):
        if value <= 20000.00:
            raise serializers.ValidationError('Price must be greater than 20000')
        return value

    #object level validation

    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    
class ShowroomSerializer(serializers.ModelSerializer):

    # Showrooms = CarSerializer(many=True, read_only =True)

    Showrooms = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta :
        model = Showroomlist
        fields = "__all__"

