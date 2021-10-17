from rest_framework import serializers
from jobs.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"
    
    def validate(self, data):
        if data["company_name"] == data["job_title"]:
            raise serializers.ValidationError("Company name and Job title must be different from one another")
        return data
    
    def validate_job_title(self, value):
        if len(value) > 60:
            raise serializers.ValidationError("The job title has to be less than 60 chars")
        return value



# class JobOfferSerializer(serializers.Serializer):
#     id              = serializers.IntegerField(read_only=True)
#     company_name    = serializers.CharField()
#     company_email   = serializers.CharField()
#     job_title       = serializers.CharField()
#     job_description = serializers.CharField()
#     salary          = serializers.IntegerField()
#     city            = serializers.CharField()
#     state           = serializers.CharField()
#     created_at      = serializers.DateTimeField(read_only=True)
#     available       = serializers.BooleanField()

#     def create(self, validated_data):
#         return JobOffer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.company_name = validated_data('company_name', instance.company_name)
#         instance.company_email = validated_data('company_email', instance.company_email)
#         instance.job_title = validated_data('job_title', instance.job_title)
#         instance.job_description = validated_data('job_description', instance.job_description)
#         instance.salary = validated_data('salary', instance.salary)
#         instance.city = validated_data('city', instance.city)
#         instance.state = validated_data('state', instance.state)
#         instance.available = validated_data('available', instance.available)
#         instance.save()

#         return instance

#     def validate(self, data):
#         if data["company_name"] == data["job_title"]:
#             raise serializers.ValidationError("Company name and Job title must be different from one another")
#         return data

#     def validate_job_title(self, value):
#         if len(value) > 60:
#             raise serializers.ValidationError("The job title has to be less than 60 chars")
#         return value


