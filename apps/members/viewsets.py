from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.members.models import *
from apps.members.serializers import *

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['member_id']
    
    @action(detail=False, methods=('POST',), url_path='signup', http_method_names=('post',))
    def partner_signup(self, request, *args, **kwargs):
        member_id = request.POST["member_id"]
        passwd = request.POST["passwd"]
        name = request.POST["name"]
        email = request.POST["email"]
        height = request.POST["height"]
        weight = request.POST["weight"]
        gender = request.POST["gender"]
        purpose = request.POST["purpose"]
        age = request.POST["age"]

        rs = Member.objects.filter(member_id=member_id)
        print(111, rs)
        if rs.exists():
            return Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={'message': '해당 아이디가 이미 존재합니다.'})
        else:
            member = Member.objects.create(
                member_id=member_id, passwd=passwd, name=name, email=email, height=height,
                weight=weight, gender=gender, purpose=purpose, age=age)
            
            return Response(
                            status = status.HTTP_201_CREATED,
                            data={'message': '회원가입이 성공적으로 완료되었습니다.',
                                  'member': MembersSerializer(member).data
                                }
                        )
            
            
    @action(detail=False, methods=('POST',), url_path='signin', http_method_names=('post',))
    def partner_signin(self, request, *args, **kwargs):
        member_id = request.POST.get('member_id')
        passwd = request.POST.get('passwd')

        # 로그인 체크하기
        rs = Member.objects.filter(member_id=member_id, passwd=passwd).first()

        if rs is not None:
            request.session['m_id'] = member_id
            request.session['m_name'] = rs.name
            return Response(
                            status = status.HTTP_200_OK,
                            data={'message': '로그인이 성공적으로 완료되었습니다.',
                                  'member': MembersSerializer(rs).data
                                }
                        )

        else:
            return Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={'message': '아이디 비번 맞지 않음'})