
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsManager, IsAssignee

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    #filterset_fields = ['status', 'assignee']
    
    def get_queryset(self):
        queryset = Task.objects.all()
        user = self.request.user
        if not user.is_staff:
            return Task.objects.filter(assignee=user)
        
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        assignee = self.request.query_params.get('assignee')
        if assignee:
            queryset = queryset.filter(assignee=assignee)
        due_date_from = self.request.query_params.get('due_date_from')
        due_date_to = self.request.query_params.get('due_date_to')
        if due_date_from and due_date_to:
            queryset = queryset.filter(due_date__range=[due_date_from, due_date_to])

        return queryset

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsManager | IsAssignee]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        user = self.request.user
        if 'status' in request.data and request.data['status'] == 'completed':
            if not task.can_be_completed():
                return Response(
                    {"error": "This task cannot be marked as completed until all dependencies are completed."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        if not user.is_staff:
            if set(request.data.keys()) != {"status"}:
                return Response(
                    {"error": "Only status updates are allowed"},
                    status=status.HTTP_403_FORBIDDEN
                )
        
       
        
        return super().update(request, partial=True)
