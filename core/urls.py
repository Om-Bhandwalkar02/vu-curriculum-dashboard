from django.urls import path
from .views import (overview, swot_revision, incremental_growth, curriculum_flexibility,
                    new_courses, skill_courses, employability, entrepreneurship,
                    industry_skills, global_benchmarking, ugc_compliance, lacunae_gaps)

urlpatterns = [
    path('', overview, name='overview'),
    path('swot-revision/', swot_revision, name='swot_revision'),
    path('incremental-growth/', incremental_growth, name='incremental_growth'),
    path('curriculum-flexibility/', curriculum_flexibility, name='curriculum_flexibility'),
    path('new-courses/', new_courses, name='new_courses'),
    path('skill-courses/', skill_courses, name='skill_courses'),
    path('employability/', employability, name='employability'),
    path('entrepreneurship/', entrepreneurship, name='entrepreneurship'),
    path('industry-skills/', industry_skills, name='industry_skills'),
    path('global-benchmarking/', global_benchmarking, name='global_benchmarking'),
    path('ugc-compliance/', ugc_compliance, name='ugc_compliance'),
    path('lacunae-gaps/', lacunae_gaps, name='lacunae_gaps'),]