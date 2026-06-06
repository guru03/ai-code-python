from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from apps.angular.models import Angular
from apps.angular.serializers import AngularSerializer


class AngularViewSet(viewsets.ModelViewSet):
    queryset = Angular.objects.all()
    serializer_class = AngularSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "serial_number",
        "created_at",
        "updated_at",
    ]  # specify fields you want to allow ordering
    ordering = ["serial_number"]  # default ordering

    @action(detail=False, methods=["get"])
    def ascending(self, request):
        queryset = Angular.objects.all().order_by("serial_number")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def descending(self, request):
        queryset = Angular.objects.all().order_by("-serial_number")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Custom action: publish
    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        angular = self.get_object()
        angular.content_status = WorkStatus.Approved.value
        angular.save()
        return Response(
            {"message": f"Angular {pk} published successfully"},
            status=status.HTTP_200_OK,
        )

    # Custom action: archive
    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        angular = self.get_object()
        angular.content_status = WorkStatus.Archived.value
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
