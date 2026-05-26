from django.shortcuts import render, get_object_or_404

from .models import (
    KPI, Revision, CreditDistribution, OverviewSkillGrowth, FlexibilityMetric,
    NewCourseSummary, NewCourseGrowth, NewCourse, SkillSummary, SkillGrowth, CertificationTrack,
    EntrepreneurshipSummary, EntrepreneurshipInitiative, GlobalBenchmarkSummary, GlobalPartner,
    CurriculumGap, GapCategory, Recommendation, UGCComplianceSummary, UGCComplianceScore,
    UGCObservation, UGCRequirement, UGCYearSummary, EmployabilitySummary, EmployabilityInitiative,
    IndustrySkillSummary, IndustrySkillInitiative, IncrementalGrowthSummary, IncrementalGrowthMetric,
    MSCGrowthMetric, MSCGrowthAnalysis
)



def overview(request):

    credit_distribution = CreditDistribution.objects.all()

    skill_growth = OverviewSkillGrowth.objects.all()

    context = {

        "kpis": KPI.objects.all(),

        "revisions": Revision.objects.all(),

        "credit_distribution": credit_distribution,

        "skill_growth": skill_growth,

        # Credit Distribution Chart

        "credit_labels": [x.year for x in credit_distribution],

        "core_data": [x.core for x in credit_distribution],

        "minor_data": [x.minor_track for x in credit_distribution],

        "oe_data": [x.open_elective for x in credit_distribution],

        "value_data": [x.value_education for x in credit_distribution],

        "skill_data": [x.skill_enhancement for x in credit_distribution],

        "ability_data": [x.ability_enhancement for x in credit_distribution],

        "elective_data": [x.elective for x in credit_distribution],

        # Skill Growth Chart

        "growth_labels": [x.year for x in skill_growth],

        "internship_data": [x.internship for x in skill_growth],

        "growth_value_data": [x.value_education for x in skill_growth],

        "growth_skill_data": [x.skill_enhancement for x in skill_growth],

        "growth_ability_data": [x.ability_enhancement for x in skill_growth],

    }

    return render(
        request,
        "dashboard/overview.html",
        context
    )


def swot_revision(request):

    revisions = Revision.objects.prefetch_related(
        'swot_entries'
    )

    selected_revision = request.GET.get('revision')

    if selected_revision:

        current_revision = get_object_or_404(
            Revision,
            id=selected_revision
        )

    else:

        current_revision = revisions.first()

    return render(
        request,
        'dashboard/swot_revision.html',
        {
            'revisions': revisions,
            'current_revision': current_revision
        }
    )


def curriculum_flexibility(request):

    metrics = FlexibilityMetric.objects.select_related(
        'revision'
    ).order_by('revision__year')

    return render(
        request,
        'dashboard/curriculum_flexibility.html',
        {
            'metrics': metrics,
            'latest_metric': metrics.last(),
        }
    )




def new_courses(request):

    summary = NewCourseSummary.objects.first()

    growth = NewCourseGrowth.objects.all()

    courses = NewCourse.objects.all()

    context = {

        "summary": summary,

        "growth": growth,

        "courses": courses

    }

    return render(
        request,
        "dashboard/new_courses.html",
        context
    )

def skill_courses(request):

    summary = SkillSummary.objects.first()

    growth = SkillGrowth.objects.all()

    tracks = CertificationTrack.objects.all()

    context = {

        "summary": summary,

        "growth": growth,

        "tracks": tracks

    }

    return render(
        request,
        "dashboard/skill_courses.html",
        context
    )


def employability(request):

    summary = EmployabilitySummary.objects.first()

    employability_items = EmployabilityInitiative.objects.filter(
        category='Employability'
    )

    ethics_items = EmployabilityInitiative.objects.filter(
        category='Ethics'
    )

    sustainability_items = EmployabilityInitiative.objects.filter(
        category='Sustainability'
    )

    context = {

        "summary": summary,

        "employability_items": employability_items,

        "ethics_items": ethics_items,

        "sustainability_items": sustainability_items,

    }

    return render(
        request,
        "dashboard/employability.html",
        context
    )


def entrepreneurship(request):

    summary = EntrepreneurshipSummary.objects.first()

    entrepreneurship_items = EntrepreneurshipInitiative.objects.filter(
        category='Entrepreneurship'
    )

    research_items = EntrepreneurshipInitiative.objects.filter(
        category='Research'
    )

    higher_studies_items = EntrepreneurshipInitiative.objects.filter(
        category='Higher Studies'
    )

    context = {

        "summary": summary,

        "entrepreneurship_items": entrepreneurship_items,

        "research_items": research_items,

        "higher_studies_items": higher_studies_items,

        "entrepreneurship_count": entrepreneurship_items.count(),

        "research_count": research_items.count(),

        "higher_studies_count": higher_studies_items.count(),

        "total_count":
            entrepreneurship_items.count()
            + research_items.count()
            + higher_studies_items.count(),

    }

    return render(
        request,
        "dashboard/entrepreneurship.html",
        context
    )


def industry_skills(request):

    summary = IndustrySkillSummary.objects.first()

    platforms = IndustrySkillInitiative.objects.filter(
        category='Platform'
    )

    skills = IndustrySkillInitiative.objects.filter(
        category='Skill Domain'
    )

    projects = IndustrySkillInitiative.objects.filter(
        category='Project Domain'
    )

    context = {

        "summary": summary,

        "platforms": platforms,

        "skills": skills,

        "projects": projects,

        "platform_count": platforms.count(),

        "skill_count": skills.count(),

        "project_count": projects.count(),

        "total_count":
            platforms.count()
            + skills.count()
            + projects.count(),
    }

    return render(
        request,
        "dashboard/industry_skills.html",
        context
    )


def global_benchmarking(request):

    summary = GlobalBenchmarkSummary.objects.first()

    partners = GlobalPartner.objects.all()

    country_count = len(
        set(
            partners.values_list(
                'country',
                flat=True
            )
        )
    )

    context = {

        "summary": summary,

        "partners": partners,

        "partner_count": partners.count(),

        "country_count": country_count,

    }

    return render(
        request,
        "dashboard/global_benchmarking.html",
        context
    )

def ugc_compliance(request):

    summary = UGCComplianceSummary.objects.first()

    scores = UGCComplianceScore.objects.all()

    observations = UGCObservation.objects.all()

    requirements = UGCRequirement.objects.all()

    year_summaries = UGCYearSummary.objects.all()

    latest = scores.last()

    context = {

        "summary": summary,

        "scores": scores,

        "observations": observations,

        "requirements": requirements,

        "year_summaries": year_summaries,

        "latest": latest,

        "years": [x.year for x in scores],

        "compliance_data": [
            x.compliance_percentage
            for x in scores
        ],

        "flexibility_data": [
            x.flexibility_index
            for x in scores
        ],

    }

    return render(
        request,
        "dashboard/ugc_compliance.html",
        context
    )


def lacunae_gaps(request):

    gaps = CurriculumGap.objects.all()

    categories = GapCategory.objects.prefetch_related(
        'recommendations'
    )

    recommendations = Recommendation.objects.all()

    high_count = gaps.filter(
        severity='High'
    ).count()

    medium_count = gaps.filter(
        severity='Medium'
    ).count()

    future_count = recommendations.filter(
        priority='Future'
    ).count()

    context = {

        "gaps": gaps,

        "categories": categories,

        "recommendations": recommendations,

        "high_count": high_count,

        "medium_count": medium_count,

        "future_count": future_count,

        "total_gaps": gaps.count(),

    }

    return render(
        request,
        "dashboard/lacunae_gaps.html",
        context
    )


def incremental_growth(request):

    summary = IncrementalGrowthSummary.objects.first()

    bsc_metrics = IncrementalGrowthMetric.objects.all()

    msc_metrics = MSCGrowthMetric.objects.all()

    msc_analysis = MSCGrowthAnalysis.objects.all()

    years = [m.year for m in bsc_metrics]

    credits_data = [
        m.total_credits
        for m in bsc_metrics
    ]

    theory_data = [
        m.theory_hours
        for m in bsc_metrics
    ]

    practical_data = [
        m.practical_hours
        for m in bsc_metrics
    ]

    course_data = [
        m.total_courses
        for m in bsc_metrics
    ]

    internship_data = [
        m.internship_credits
        for m in bsc_metrics
    ]
    core_cs_data = [
        m.core_cs_credits
        for m in bsc_metrics
    ]

    msc_years = [m.year for m in msc_metrics]

    msc_credits_data = [
        m.total_credits
        for m in msc_metrics
    ]

    msc_courses_data = [
        m.total_courses
        for m in msc_metrics
    ]

    msc_theory_data = [
        m.theory_hours
        for m in msc_metrics
    ]

    msc_practical_data = [
        m.practical_hours
        for m in msc_metrics
    ]

    context = {

        "summary": summary,

        "bsc_metrics": bsc_metrics,

        "msc_metrics": msc_metrics,

        "msc_analysis": msc_analysis,

        "years": years,

        "credits_data": credits_data,

        "theory_data": theory_data,

        "practical_data": practical_data,

        "course_data": course_data,

        "internship_data": internship_data,

        "core_cs_data": core_cs_data,

        "msc_years": msc_years,
        "msc_credits_data": msc_credits_data,
        "msc_courses_data": msc_courses_data,
        "msc_theory_data": msc_theory_data,
        "msc_practical_data": msc_practical_data,

    }

    return render(
        request,
        "dashboard/incremental_growth.html",
        context
    )


