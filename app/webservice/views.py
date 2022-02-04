# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *
from .functions import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


def main(request):
    context = {}
    return render(request, 'base.html', context)


class VpsView(APIView):
    def get(self, request):
        uid = self.request.query_params.get('uid')
        cpu = self.request.query_params.get('cpu')
        ram = self.request.query_params.get('ram')
        hdd = self.request.query_params.get('hdd')
        status = self.request.query_params.get('status')

        kwargs = {}
        if uid:
            uidlist = uid.split(',')
            validate_uuid = validate_list_uuid4(uidlist)
            if not validate_uuid:
                return Response({"error": "Значение uid пусто или неккоректно"})
            kwargs.update(dict(id__in = validate_uuid))
        if cpu:
            kwargs.update(dict(cpu=cpu))
        if ram:
            kwargs.update(dict(ram=ram))
        if hdd:
            kwargs.update(dict(hdd=hdd))
        if status:
            kwargs.update(dict(status=status))
            
        if not kwargs:
            return Response({"error": "Введите хотя бы один параметр"})

        valid_data = VpsFindSerializer(data = kwargs)
        valid_data.is_valid(raise_exception=True)

        try:
            vps = Vps.objects.filter(**kwargs)
            if not vps:
                return Response({"error": "С такими параметрами нет ни одного vps"})

            serializer = VpsFindSerializer(vps, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Еще нет ни одного vps"})


    def post(self, request):
        new_vps = request.data.get("data")
        serializer = VpsMethodSerializer(data=new_vps)
        if serializer.is_valid(raise_exception=True):
            object_saved = serializer.save()
        return Response({"success": "Object '{}' created successfully".format(object_saved)})


    def put(self, request):
        data = self.request.data
        uid = data.get('uid')
        if not validate_uuid4(uid):
            return Response({"error": "Значение uid пусто или неккоректно"})

        saved_object = get_object_or_404(Vps.objects.all(), pk=uid)
        serializer = VpsMethodSerializer(
            instance=saved_object, 
            data=data, 
            partial=True
        )
        if not data.get('status'):
            return Response({"error": "Cтатус не указан"})
        if serializer.is_valid(raise_exception=True):
            object_saved = serializer.save()
        return Response({
            "success": "Object '{}' updated successfully".format(object_saved)
        })
