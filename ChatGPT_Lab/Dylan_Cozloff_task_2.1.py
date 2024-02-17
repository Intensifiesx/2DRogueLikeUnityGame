from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
import uuid

from .models import Meal, Fast
from .serializers import MealSerializer, FastSerializer

def parse_repeat_days(data):
    repeat_days = data.get('repeatDays')
    if repeat_days:
        week_days_order = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
        return ','.join(sorted(repeat_days, key=lambda day: week_days_order[day]))
    return None

def get_object_and_check_permission(model, user, object_id):
    obj = model.objects.get(pk=object_id)
    if obj.user != user:
        raise PermissionDenied
    return obj

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_meals(request):
    meals = Meal.objects.filter(user=request.user)
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_meal(request, meal_id):
    meal = get_object_and_check_permission(Meal, request.user, meal_id)
    serializer = MealSerializer(meal)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_meal(request):
    data = request.data
    data['repeat_days'] = parse_repeat_days(data)
    data['meal_id'] = str(uuid.uuid4())
    serializer = MealSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_meal(request, meal_id):
    meal = get_object_and_check_permission(Meal, request.user, meal_id)
    serializer = MealSerializer(meal, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_meal(request, meal_id):
    meal = get_object_and_check_permission(Meal, request.user, meal_id)
    meal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_fast(request):
    data = request.data
    data['repeat_days'] = parse_repeat_days(data)
    data['fast_id'] = str(uuid.uuid4())
    serializer = FastSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
