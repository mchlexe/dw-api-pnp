from django.shortcuts import render
from .forms import CsvModelForm
from .models import Aluno, Ciclo_Curso, Matricula
from django.contrib.auth.models import User
from datetime import datetime

