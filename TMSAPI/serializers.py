from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    dependencies = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all(), required=False)
    
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate(self, data):
        """Ensure that a task cannot be completed if dependencies are not completed."""
        if 'status' in data and data['status'] == 'completed':
            instance = self.instance  # Get the existing task instance
            if instance and not instance.can_be_completed():
                raise serializers.ValidationError("This task cannot be marked as completed until all dependencies are completed.")
        return data