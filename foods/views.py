from rest_framework import response
from rest_framework import status 
from django.http import JsonResponse
from .models import Food
from .serializers import FoodSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def food_list(request):     #不需要
    # 處理 GET 請求
    if request.method == 'GET':
        foods = Food.objects.all() # 取得所有食物
        serializer = FoodSerializer(foods, many=True)# 序列化食物
        return JsonResponse({'Foods': serializer.data})# 返回 JSON 
    # 處理 POST 請求
    if request.method == 'POST':
        serializer = FoodSerializer(data = request.data)# 使用請求數據初始化序列化器
        if serializer.is_valid():
            serializer.save() # 保存
            return response(serializer.data, status=status.HTTP_201_CREATED)# 回傳成功回應 




@api_view(['GET'])
def food_detail(request, pk):
    try:
        food = Food.objects.get(pk=pk)# 根據主鍵取得特定食物
        serializer = FoodSerializer(food)# 序列化食物
        return JsonResponse(serializer.data)# 返回 JSON 
    except Food.DoesNotExist:
        # 回傳錯誤回應
        return JsonResponse({'error': 'Food not found'}, status=status.HTTP_404_NOT_FOUND)
