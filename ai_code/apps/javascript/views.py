from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from apps.javascript.serializers import JavascriptSerializer
from apps.javascript.models import Javascript


class JavascriptViewSet(viewsets.ModelViewSet):
    queryset = Javascript.objects.all()
    serializer_class = JavascriptSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "serial_number",
        "created_at",
        "updated_at",
    ]  # specify fields you want to allow ordering
    ordering = ["serial_number"]  # default ordering

    @action(detail=False, methods=["get"])
    def ascending(self, request):
        queryset = Javascript.objects.all().order_by("serial_number")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def descending(self, request):
        queryset = Javascript.objects.all().order_by("-serial_number")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Custom action: publish
    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        javascript = self.get_object()
        javascript.content_status = WorkStatus.Approved.value
        javascript.save()
        return Response(
            {"message": f"Javascript {pk} published successfully"},
            status=status.HTTP_200_OK,
        )

    # Custom action: archive
    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        javascript = self.get_object()
        javascript.content_status = WorkStatus.Archived.value
        javascript.save()
        return Response(
            {"message": f"Javascript {pk} archived successfully"},
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
def update_javascript(request):
    try:
        data = request.data
        serial_number = data.get("serial_number")
        javascript, created = Javascript.objects.update_or_create(
            serial_number=serial_number,
            defaults=data,
        )

        if created:
            return Response(
                {"message": "Javascript created successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Javascript updated successfully"}, status=status.HTTP_200_OK
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
