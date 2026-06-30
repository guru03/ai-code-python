from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.db.models import IntegerField
from django.db.models.functions import Cast

from common_utils.sorting import natural_sort

from .models import Coding, CodingExample
from .serializers import CodingSerializer, CodingExampleSerializer


class CodingViewSet(viewsets.ModelViewSet):
    # * This is just for the backup
    queryset = Coding.objects.all()
    serializer_class = CodingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["serial_number", "created_at", "updated_at"]
    ordering = ["serial_number"]

    @action(detail=False, methods=["get"])
    def ascending(self, request):
        queryset_sorted = natural_sort(Coding.objects.all(), field="serial_number")
        serializer = self.get_serializer(queryset_sorted, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def descending(self, request):
        queryset_sorted = natural_sort(
            Coding.objects.all(), field="serial_number", reverse=True
        )
        serializer = self.get_serializer(queryset_sorted, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=["get"])
    # def ascending(self, request):
    #     queryset = Coding.objects.annotate(
    #         serial_number_int=Cast("serial_number", IntegerField())
    #     ).order_by("serial_number_int")
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=["get"])
    # def descending(self, request):
    #     queryset = Coding.objects.annotate(
    #         serial_number_int=Cast("serial_number", IntegerField())
    #     ).order_by("-serial_number_int")
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # Custom action: publish
    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        coding = self.get_object()
        coding.content_status = WorkStatus.Approved.value
        coding.save()
        return Response(
            {"message": f"Coding {pk} published successfully"},
            status=status.HTTP_200_OK,
        )

    # Custom action: archive
    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        coding = self.get_object()
        coding.content_status = WorkStatus.Archived.value
        coding.save()
        return Response(
            {"message": f"Coding {pk} archived successfully"},
            status=status.HTTP_200_OK,
        )


class CodingExampleViewSet(viewsets.ModelViewSet):
    queryset = CodingExample.objects.all()
    serializer_class = CodingExampleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "code_language", "code_title"]
    ordering = ["created_at"]


@api_view(["POST"])
def update_coding(request):
    try:
        data = request.data
        serial_number = data.get("serial_number")
        coding, created = Coding.objects.update_or_create(
            serial_number=serial_number,
            defaults=data,
        )

        if created:
            return Response(
                {"message": "Coding created successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Coding updated successfully"}, status=status.HTTP_200_OK
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
