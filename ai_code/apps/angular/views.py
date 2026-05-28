from django.shortcuts import render

from angular.models import Angular
from angular.serializers import AngularSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
class AngularViewSet(viewsets.ModelViewSet):
    queryset = Angular.objects.all()
    serializer_class = AngularSerializer
 
    
@api_view(["POST"])
def update_angular(request):
    try:
        data = request.data
        serial_number = data.get("serial_number")
        category = data.get("category")
        topic = data.get("topic")
        content_status = data.get("content_status")
        visible = data.get("visible", True)
        question = data.get("question")
        answer = data.get("answer")
        answer2 = data.get("answer2")
        image_url = data.get("image_url")
        image2_url = data.get("image2_url")
        image3_url = data.get("image3_url")
        angular_questions = data.get("angular_questions")

        angular, created = Angular.objects.update_or_create(
            serial_number=serial_number,
            defaults={
                "category": category,
                "topic": topic,
                "content_status": content_status,
                "visible": visible,
                "question": question,
                "answer": answer,
                "answer2": answer2,
                "image_url": image_url,
                "image2_url": image2_url,
                "image3_url": image3_url,
                "angular_questions": angular_questions,
            },
        )

        if created:
            return Response(
                {"message": "Angular created successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Angular updated successfully"}, status=status.HTTP_200_OK
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
