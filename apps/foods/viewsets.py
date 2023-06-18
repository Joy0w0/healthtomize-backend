from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.foods.models import *
from apps.members.models import *
from apps.foods.serializers import *

class FoodsViewSet(viewsets.ModelViewSet):
    queryset = food.objects.all()
    serializer_class = FoodsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['food_name']
    
    @action(detail=False, methods=('POST',), url_path='estimate', http_method_names=('post',))
    def food_estimate(self, request, *args, **kwargs):
        context = {}

        food_name = request.POST.get('food_name')
        serving_size = request.POST.get('serving_size')
        
        the_food = food.objects.filter(food_name = food_name).first()

        calories = the_food.calories
        carbon = the_food.carbon
        protein = the_food.protein
        fat = the_food.fat
        cholesterol = the_food.cholesterol
        food_serving_size = the_food.serving_size
        rate = int(serving_size)/int(food_serving_size)
        
        return Response(
                            status = status.HTTP_201_CREATED,
                            data={'message': '성공',
                                  'data': {
                                      'food_name':food_name, 'serving_size':serving_size, 'calories':calories, 'carbon':carbon, 'protein':protein, 'fat':fat, 'cholesterol':cholesterol, 'rate':rate
                                  }
                                }
                        )
        
    @action(detail=False, methods=('POST',), url_path='feedback', http_method_names=('post',))
    def food_feedback(self, request, *args, **kwargs):
        member_id=request.POST.get('member_id')
        used_calories = request.POST.get('used_calories')
        food_calories = request.POST.get('food_calories')

        if used_calories is not None:
            members = Member.objects.get(member_id=member_id)

            if members.gender=='남자':
                base_calories= 66+13.7*int(members.weight)+(5*int(members.height))-(6.5*int(members.age))

            else:
                base_calories=665 + 9.6 * int(members.weight) + (1.8 * int(members.height)) - (4.7 * int(members.age))

            calories=abs(round(float(food_calories)-float(used_calories)-float(base_calories)))
            if float(food_calories)-float(used_calories)-float(base_calories) <= 0:
                potato_ea=round(calories/130,1)
                egg_ea = round(calories / 75, 1)
                chest_ea =round(calories / 115, 1)
                banana_ea =round(calories / 95, 1)
                
                return Response(
                            status = status.HTTP_201_CREATED,
                            data={'message': '성공',
                                  'data': {
                                      'status': 'less',
                                      'used_calories': used_calories, 'food_calories':food_calories, 'base_calories': base_calories, 'calories': calories, 'potato_ea': potato_ea, 'egg_ea': egg_ea, 'chest_ea': chest_ea, 'banana_ea': banana_ea
                                  }
                                }
                        )
                
            else:
                squat_m=round(calories/9.8)
                bike_m=round(calories/3.4)
                pushup_m = round(calories / 4.2)
                swim_m = round(calories / 17)
                run_m = round(calories / 9.4)
                
                return Response(
                                status = status.HTTP_201_CREATED,
                                data={'message': '성공',
                                    'data': {
                                        'status': 'much',
                                        'used_calories': used_calories, 'food_calories':food_calories, 'base_calories': base_calories, 'calories': calories, 'squat_m': squat_m, 'bike_m': bike_m, 'pushup_m': pushup_m, 'swim_m': swim_m, 'run_m': run_m
                                    }
                                    }
                            )