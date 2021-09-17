from django.http.response import json
from rest_framework import generics
from ..api import serializers
from ..models import Aluno, Curso, Ciclo, Matricula
from datetime import datetime

class AlunoList(generics.ListCreateAPIView):
    serializer_class = serializers.AlunoSerializer
        
    def get_queryset(self):
        received_json_data = json.loads(self.request.body)
      
        dt_inicio = received_json_data['dt_inicio']
        dt_fim = received_json_data['dt_fim']
        situacao_matricula = received_json_data['situacao_matricula'].upper()
        ano_base = received_json_data['ano_base']

        query = f"SELECT * FROM STAGING_AREA_ALUNO WHERE COD_ALUNO IN (SELECT COD_ALUNO FROM STAGING_AREA_MATRICULA WHERE DT_OCORRENCIA_MATRICULA BETWEEN '{dt_inicio}' AND '{dt_fim}' AND SITUACAO_MATRICULA LIKE '{situacao_matricula}' AND ANO_BASE = {ano_base})"

        return Aluno.objects.raw(query)

class CursoList(generics.ListCreateAPIView):
    serializer_class = serializers.CursoSerializer
        
    def get_queryset(self):
        received_json_data = json.loads(self.request.body)
      
        dt_inicio = received_json_data['dt_inicio']
        dt_fim = received_json_data['dt_fim']
        situacao_matricula = received_json_data['situacao_matricula'].upper()
        ano_base = received_json_data['ano_base']

        query = f"SELECT * FROM STAGING_AREA_CURSO WHERE COD_CURSO IN (SELECT COD_CURSO FROM STAGING_AREA_MATRICULA WHERE DT_OCORRENCIA_MATRICULA BETWEEN '{dt_inicio}' AND '{dt_fim}' AND SITUACAO_MATRICULA LIKE '{situacao_matricula}' AND ANO_BASE = {ano_base})"

        return Curso.objects.raw(query)


class CicloList(generics.ListCreateAPIView):
    serializer_class = serializers.CicloSerializer
        
    def get_queryset(self):
        received_json_data = json.loads(self.request.body)
      
        dt_inicio = received_json_data['dt_inicio']
        dt_fim = received_json_data['dt_fim']
        situacao_matricula = received_json_data['situacao_matricula'].upper()
        ano_base = received_json_data['ano_base']

        query = f"SELECT * FROM STAGING_AREA_CICLO WHERE COD_CICLO_MATRICULA IN (SELECT COD_CICLO FROM STAGING_AREA_MATRICULA WHERE DT_OCORRENCIA_MATRICULA BETWEEN '{dt_inicio}' AND '{dt_fim}' AND SITUACAO_MATRICULA LIKE '{situacao_matricula}' AND ANO_BASE = {ano_base})"

        return Ciclo.objects.raw(query)


class MatriculaList(generics.ListCreateAPIView):
    serializer_class = serializers.MatriculaSerializer
    
    def get_queryset(self):
        received_json_data = json.loads(self.request.body)

        dt_inicio = received_json_data['dt_inicio']
        dt_fim = received_json_data['dt_fim']
        situacao_matricula = received_json_data['situacao_matricula'].upper()
        ano_base = received_json_data['ano_base']

        query = f"SELECT * FROM STAGING_AREA_MATRICULA WHERE DT_OCORRENCIA_MATRICULA BETWEEN '{dt_inicio}' AND '{dt_fim}' AND SITUACAO_MATRICULA LIKE '{situacao_matricula}' AND ANO_BASE = {ano_base}"

        return Matricula.objects.raw(query)





