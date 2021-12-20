import itertools

from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models
from BusinessSecurity import models as bcsmodels
from rest_framework import permissions, pagination, filters
from datetime import date
from django.db.models import Q
from rest_framework.response import Response
from Api import apipermissions


# Create your views here.

class PostApi(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostSerializer


class CategoryApi(generics.ListAPIView):
    permission_classes = [apipermissions.IsBlogAdmin]
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializer.CategorySerializer


class SubCategoryApi(generics.ListAPIView):
    # queryset = models.BlogSubCategory.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.SubCategorySerializer

    def get_queryset(self):
        category = self.kwargs['id']
        return models.BlogSubCategory.objects.filter(category=category)


class FilterApi(generics.ListAPIView):
    # queryset = models.FilterOption.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.FilterSerializer

    def get_queryset(self):
        category = self.kwargs['id']
        subcategory = self.kwargs['sub_id']
        return models.FilterOption.objects.filter(sub_category=subcategory, sub_category__category=category)


class Page(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5


class AllCommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['comment_date']


class CommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page

    def get_queryset(self):
        post = self.kwargs['post_id']
        return models.Comment.objects.filter(post=post)


class BlogFilterApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        return models.Post.objects.filter(
            Q(category__category__iexact=category, title__icontains=text) | Q(category__category__iexact=category,
                                                                              short_description__icontains=text))


class BlogFilterDateApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer
    today = date.today()

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        if text == 'month':
            return models.Post.objects.filter(category__category__iexact=category, date__month=self.today.month)
        elif text == 'year':
            return models.Post.objects.filter(category__category__iexact=category, date__year=self.today.year)


class PackageListViewApi(generics.ListAPIView):
    serializer_class = serializer.PackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionBasedPackage.objects.filter(service_id=service_id)


class ServiceListApiView(generics.ListAPIView):
    serializer_class = serializer.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    # queryset = bcsmodels.Service.objects.all()

    def get_queryset(self):
        cat_type = self.kwargs['cat']
        return bcsmodels.Service.objects.filter(category_choice=cat_type)


class SubServiceApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubService.objects.filter(service_id=service_id)


class SubServiceInputApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceInputSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubServiceInput.objects.filter(subservice_id=service_id)


class ChoiceApiView(generics.ListAPIView):
    serializer_class = serializer.ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        return bcsmodels.SelectChoiceRelation.objects.filter(input_field_id=id)


class UserSubServiceOrderApiView(generics.ListAPIView):
    serializer_class = serializer.UserSubServiceOrderSerializer

    def get_queryset(self):
        subservice_id = self.kwargs['id']
        return bcsmodels.Order.objects.filter(id=subservice_id)


class TeamPermissionApiView(generics.RetrieveUpdateAPIView):
    serializer_class = serializer.TeamPermissionSerializer
    permission_classes = [apipermissions.IsTeamAdmin]
    lookup_field = 'id'
    queryset = bcsmodels.UsersBusiness


class BCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()
    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_years,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class BCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().month
        # print(end_date)
        all_months = list(range(start_date, end_date + 1))
        # print(all_months)

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class BCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().day
        # print(end_date)
        all_dates = list(range(start_date, end_date + 1))
        # print(all_dates)

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class PCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class PCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class PCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class MainAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.all()

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class MainAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.all()

        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class MainAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.all()

        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class SubscriptionApiView(generics.ListAPIView):
    serializer_class = serializer.SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'service'

    def get_queryset(self):
        service_id = self.kwargs['service']
        return bcsmodels.Order.objects.filter(service__id=service_id, user=self.request.user,
                                              service__is_subscription_based=True).order_by('-order_date')

    # def list(self, request, *args, **kwargs):
    #     ser = self.get_serializer(self.get_queryset(), many=True)
    #     responseData = ser.data
    #     print(self.get_queryset())
    #     responseData.append({
    #         'price': '1223'
    #     })
    #     return Response(responseData)
