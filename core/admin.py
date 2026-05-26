from django.contrib import admin

admin.site.site_header = "Vishwakarma University Curriculum Dashboard"
admin.site.site_title  = "VU Curriculum"
admin.site.index_title = "Welcome to Vishwakarma University Curriculum Dashboard"

from .models import (
    SiteSettings,
    NavigationItem,
    Revision,
    KPI,
    CreditDistribution,
    OverviewSkillGrowth,
    SWOTEntry,
    FlexibilityMetric,
    NewCourseSummary,
    NewCourseGrowth,
    NewCourse,
    SkillSummary,
    SkillGrowth,
    CertificationTrack,
    EmployabilitySummary,
    EmployabilityInitiative,
    CurriculumGap,
    EntrepreneurshipSummary,
    EntrepreneurshipInitiative,
    IndustrySkillSummary,
    IndustrySkillInitiative,
    GlobalBenchmarkSummary,
    GlobalPartner,
    UGCComplianceSummary,
    UGCComplianceScore,
    UGCObservation,
    UGCRequirement,
    UGCYearSummary,
    GapCategory,
    Recommendation,
    IncrementalGrowthSummary,
    IncrementalGrowthMetric,
    MSCGrowthMetric,
    MSCGrowthAnalysis,
)



@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(NavigationItem)

admin.site.register(Revision)

admin.site.register(KPI)

admin.site.register(CreditDistribution)

admin.site.register(OverviewSkillGrowth)

admin.site.register(SWOTEntry)

admin.site.register(FlexibilityMetric)

admin.site.register(NewCourseSummary)

admin.site.register(NewCourseGrowth)

admin.site.register(NewCourse)

admin.site.register(SkillSummary)

admin.site.register(SkillGrowth)

admin.site.register(CertificationTrack)

admin.site.register(EmployabilitySummary)

admin.site.register(EmployabilityInitiative)

admin.site.register(EntrepreneurshipSummary)

admin.site.register(EntrepreneurshipInitiative)

admin.site.register(IndustrySkillSummary)

admin.site.register(IndustrySkillInitiative)

admin.site.register(GlobalBenchmarkSummary)

admin.site.register(GlobalPartner)

admin.site.register(UGCComplianceSummary)

admin.site.register(UGCComplianceScore)

admin.site.register(UGCObservation)

admin.site.register(UGCRequirement)

admin.site.register(UGCYearSummary)

admin.site.register(GapCategory)

admin.site.register(Recommendation)

admin.site.register(CurriculumGap)

admin.site.register(IncrementalGrowthSummary)

admin.site.register(IncrementalGrowthMetric)

admin.site.register(MSCGrowthMetric)

admin.site.register(MSCGrowthAnalysis)
