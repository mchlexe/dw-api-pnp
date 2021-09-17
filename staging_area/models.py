from django.db import models

class Pnp2017(models.Model):
    carga_horaria = models.CharField(max_length=255, null=True)
    carga_horaria_min = models.CharField(max_length=255, null=True)
    cod_ciclo_matricula = models.CharField(max_length=255, null=True)
    cod_matricula = models.CharField(max_length=255, null=True)
    cor_raca = models.CharField(max_length=255, null=True)
    dt_fim_previsto = models.CharField(max_length=255, null=True)
    dt_inicio = models.CharField(max_length=255, null=True)
    dt_ocorrencia_matricula = models.CharField(max_length=255, null=True)
    eixo_tecnologico = models.CharField(max_length=255, null=True)
    fator_esforco_curso = models.CharField(max_length=255, null=True)
    mes_ocorrencia = models.CharField(max_length=255, null=True)
    modalidade = models.CharField(max_length=255, null=True)
    nome_curso = models.CharField(max_length=255, null=True)
    fonte_financiamento = models.CharField(max_length=255, null=True)
    renda_familiar = models.CharField(max_length=255, null=True)
    sigla_instituicao = models.CharField(max_length=255, null=True)
    sexo_aluno = models.CharField(max_length=255, null=True)
    situacao_matricula = models.CharField(max_length=255, null=True)
    sub_eixo_tecnologico = models.CharField(max_length=255, null=True)
    tipo_curso = models.CharField(max_length=255, null=True)
    tipo_oferta = models.CharField(max_length=255, null=True)
    total_inscritos = models.CharField(max_length=255, null=True)
    turno = models.CharField(max_length=255, null=True)
    unidade_ensino = models.CharField(max_length=255, null=True)
    vagas_ofertadas = models.CharField(max_length=255, null=True)


class Pnp2018(models.Model):
    sexo_aluno = models.CharField(max_length=255, null=True)
    renda_familiar = models.CharField(max_length=255, null=True)
    cor_raca = models.CharField(max_length=255, null=True)
    idade = models.CharField(max_length=255, null=True)  # new
    faixa_etaria = models.CharField(max_length=255, null=True)  # new
    cod_matricula = models.CharField(max_length=255, null=True)
    dt_ocorrencia_matricula = models.CharField(max_length=255, null=True)
    situacao_matricula = models.CharField(max_length=255, null=True)
    categoria_situacao = models.CharField(max_length=255, null=True)
    mes_ocorrencia = models.CharField(max_length=255, null=True)
    turno = models.CharField(max_length=255, null=True)
    cod_ciclo_matricula = models.CharField(max_length=255, null=True)
    dt_inicio = models.CharField(max_length=255, null=True)
    dt_fim_previsto = models.CharField(max_length=255, null=True)
    vagas_ofertadas = models.CharField(max_length=255, null=True)
    total_inscritos = models.CharField(max_length=255, null=True)
    fonte_financiamento = models.CharField(max_length=255, null=True)
    carga_horaria = models.CharField(max_length=255, null=True)
    carga_horaria_min = models.CharField(max_length=255, null=True)
    eixo_tecnologico = models.CharField(max_length=255, null=True)
    sub_eixo_tecnologico = models.CharField(max_length=255, null=True)
    modalidade = models.CharField(max_length=255, null=True)
    tipo_curso = models.CharField(max_length=255, null=True)
    tipo_oferta = models.CharField(max_length=255, null=True)
    nome_curso = models.CharField(max_length=255, null=True)
    fator_esforco_curso = models.CharField(max_length=255, null=True)
    cod_unidade_ensino = models.CharField(max_length=255, null=True)  # new
    unidade_ensino = models.CharField(max_length=255, null=True)
    cod_municipio = models.CharField(max_length=255, null=True)  # new
    municipio = models.CharField(max_length=255, null=True)  # new
    sigla_instituicao = models.CharField(max_length=255, null=True)
    uf = models.CharField(max_length=255, null=True)  # new
    microregiao = models.CharField(max_length=255, null=True)  # new
    mesorregiao = models.CharField(max_length=255, null=True)  # new
    regiao = models.CharField(max_length=255, null=True)  # new


class Pnp2019(models.Model):
    teste = models.CharField(max_length=255, null=True)  # new
    carga_horaria = models.CharField(max_length=255, null=True)
    carga_horaria_min = models.CharField(max_length=255, null=True)
    categoria_situacao = models.CharField(max_length=255, null=True)
    cod_ciclo_matricula = models.CharField(max_length=255, null=True)
    cod_matricula = models.CharField(max_length=255, null=True)
    cod_unidade_sistec = models.CharField(max_length=255, null=True)  # new
    cod_unidade_ensino = models.CharField(max_length=255, null=True)  # new
    cor_raca = models.CharField(max_length=255, null=True)
    dt_inicio = models.CharField(max_length=255, null=True)
    dt_fim_previsto = models.CharField(max_length=255, null=True)
    dt_ocorrencia_matricula = models.CharField(max_length=255, null=True)
    eixo_tecnologico = models.CharField(max_length=255, null=True)
    faixa_etaria = models.CharField(max_length=255, null=True)  # new
    fator_esforco_curso = models.CharField(max_length=255, null=True)
    fonte_financiamento = models.CharField(max_length=255, null=True)
    idade = models.CharField(max_length=255, null=True)  # new
    total_inscritos = models.CharField(max_length=255, null=True)
    sigla_instituicao = models.CharField(max_length=255, null=True)
    mes_ocorrencia = models.CharField(max_length=255, null=True)
    modalidade = models.CharField(max_length=255, null=True)
    cod_municipio = models.CharField(max_length=255, null=True)  # new
    municipio = models.CharField(max_length=255, null=True)  # new
    vagas_ofertadas = models.CharField(max_length=255, null=True)
    nome_curso = models.CharField(max_length=255, null=True)
    num_registros = models.CharField(max_length=255, null=True)  # new
    regiao = models.CharField(max_length=255, null=True)  # new
    renda_familiar = models.CharField(max_length=255, null=True)
    sexo_aluno = models.CharField(max_length=255, null=True)
    situacao_matricula = models.CharField(max_length=255, null=True)
    sub_eixo_tecnologico = models.CharField(max_length=255, null=True)
    tipo_oferta = models.CharField(max_length=255, null=True)
    tipo_curso = models.CharField(max_length=255, null=True)
    turno = models.CharField(max_length=255, null=True)
    uf = models.CharField(max_length=255, null=True)  # new
    unidade_ensino = models.CharField(max_length=255, null=True)
    vagas_extraordinarias_ac = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_110 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_113 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_114 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_11 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_12 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_15 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_16 = models.CharField(max_length=255, null=True)  # new
    vagas_extraordinarias_19 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_ac = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_110 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_113 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_114 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_11 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_12 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_15 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_16 = models.CharField(max_length=255, null=True)  # new
    vagas_regulares_19 = models.CharField(max_length=255, null=True)  # new


class Aluno(models.Model):
    cod_aluno = models.AutoField(primary_key=True)
    cor_raca = models.CharField(max_length=50, null=True)
    renda_familiar = models.CharField(max_length=100, null=True)
    sexo_aluno = models.CharField(max_length=1, null=True)


class Ciclo(models.Model):
    cod_ciclo_matricula = models.PositiveIntegerField()
    dt_fim_previsto = models.DateField(null=True)
    dt_inicio = models.DateField(null=True)
    total_inscritos = models.PositiveIntegerField(null=True)
    vagas_ofertadas = models.PositiveIntegerField(null=True)


class Curso(models.Model):
    cod_curso = models.AutoField(primary_key=True)
    carga_horaria = models.PositiveIntegerField(null=True)
    carga_horaria_min = models.PositiveIntegerField(default=0, null=True)
    eixo_tecnologico = models.CharField(max_length=200, null=True)
    sub_eixo_tecnologico = models.CharField(max_length=200, null=True)
    fator_esforco_curso = models.FloatField(null=True)
    modalidade = models.CharField(max_length=200, null=True)
    instituicao = models.CharField(max_length=20, null=True)
    nome_curso = models.CharField(max_length=255, null=True) #new
    tipo_curso = models.CharField(max_length=200, null=True)
    tipo_oferta = models.CharField(max_length=200, null=True)
    turno = models.CharField(max_length=100, null=True)
    unidade_ensino = models.CharField(max_length=200, null=True)


class Matricula(models.Model):
    cod_aluno = models.PositiveIntegerField(null=True)
    cod_ciclo = models.PositiveIntegerField(null=True)
    cod_curso = models.PositiveIntegerField(null=True)
    dt_ocorrencia_matricula = models.DateField(null=True)
    situacao_matricula = models.CharField(max_length=200, null=True)
    ano_base = models.PositiveIntegerField(null=True)
    quantidade = models.PositiveIntegerField(null=True)