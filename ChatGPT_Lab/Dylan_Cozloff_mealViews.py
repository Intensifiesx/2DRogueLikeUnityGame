from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import uuid

from .models import Meal
from .serializers import MealSerializer, FastSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_meals(request):
    meals = Meal.objects.filter(user=request.user)
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_meal(request, meal_id):
    try:
        meal = Meal.objects.get(meal_id=meal_id)
    except Meal.DoesNotExist:
        return Response({'error': 'Meal not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check if the current user owns the meal
    if meal.user != request.user:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = MealSerializer(meal)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_meal(request):
    data = JSONParser().parse(request)

    repeat_days = data.get('repeatDays')
    if repeat_days:
        week_days_order = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
        repeat_days = sorted(repeat_days, key=lambda day: week_days_order[day])
        repeat_days = ','.join(repeat_days)
    else:
        repeat_days = None

    meal_id = str(uuid.uuid4())
    
    # Convert keys to snake_case
    formatted_data = {
        'meal_id': meal_id,
        'user': request.user.id,
        'meal_name': data.get('formName'),
        'meal_duration': data.get('duration'),
        'start_time': data.get('startTime'),
        'repeat_checked': data.get('repeatChecked'),
        'repeat_days': repeat_days,
        'repeat_end_date': data.get('repeatEndDate'),
        'repeat_indefinitely': data.get('repeatIndefinitely'),
    }

    serializer = MealSerializer(data=formatted_data)
    
    if serializer.is_valid():
        serializer.save()

        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_meal(request, meal_id):
    try:
        meal = Meal.objects.get(meal_id=meal_id)
    except Meal.DoesNotExist:
        return Response({'error': 'Meal not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check if the current user owns the meal
    if meal.user != request.user:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    repeat_days = request.data.get('repeatDays')

    # Reset meal data except for the meal_id
    meal.meal_name = request.data.get('formName')
    meal.meal_duration = request.data.get('duration')
    meal.start_time = request.data.get('startTime')
    meal.repeat_checked = request.data.get('repeatChecked')
    meal.repeat_days = repeat_days
    meal.repeat_end_date = request.data.get('repeatEndDate')
    meal.repeat_indefinitely = request.data.get('repeatIndefinitely')

    # Save the updated meal
    meal.save()

    serializer = MealSerializer(meal)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view ([('DELETE')])
@permission_classes ([IsAuthenticated])
def delete_meal(request, meal_id): 
    try:
        meal = Meal.objects.get(meal_id=meal_id)
    except Meal.DoesNotExist:
        return Response({'error': 'Meal not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check if the current user owns the meal
    if meal.user != request.user:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    meal.delete()
    
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_fast(request):
    data = JSONParser().parse(request)

    repeat_days = data.get('repeatDays')
    if repeat_days:
        week_days_order = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
        repeat_days = sorted(repeat_days, key=lambda day: week_days_order[day])
        repeat_days = ','.join(repeat_days)
    else:
        repeat_days = None

    fast_id = str(uuid.uuid4())

    print(data)
    
    # Convert keys to snake_case
    formatted_data = {
        'fast_id': fast_id,
        'user': request.user.id,
        'fast_name': data.get('formName'),
        'fast_duration': data.get('duration'),
        'start_time': data.get('startTime'),
        'repeat_checked': data.get('repeatChecked'),
        'repeat_days': repeat_days,
        'repeat_end_date': data.get('repeatEndDate'),
        'repeat_indefinitely': data.get('repeatIndefinitely'),
    }

    serializer = FastSerializer(data=formatted_data)

    print(serializer)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(serializer.errors)  # Add this line
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)