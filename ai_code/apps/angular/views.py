from apps.angular.models import Angular
from apps.angular.serializers import AngularSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response


# Create your views here.
class AngularViewSet(viewsets.ModelViewSet):
    queryset = Angular.objects.all()
    serializer_class = AngularSerializer

    # Custom action: publish
    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        angular = self.get_object()
        angular.content_status = "approved"
        angular.save()
        return Response(
            {"message": f"Angular {pk} published successfully"},
            status=status.HTTP_200_OK,
        )

    # Custom action: archive
    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        angular = self.get_object()
        angular.content_status = "archived"
        angular.save()
        return Response(
            {"message": f"Angular {pk} archived successfully"},
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
def update_angular(request):
    try:
        data = request.data
        serial_number = data.get("serial_number")
        angular, created = Angular.objects.update_or_create(
            serial_number=serial_number,
            defaults=data,
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
