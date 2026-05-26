from django.db import models


class SiteSettings(models.Model):

    university_name = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    dashboard_title = models.CharField(max_length=255)
    hod_name = models.CharField(max_length=255)

    footer_left = models.TextField()
    footer_right = models.TextField()

    logo = models.ImageField(
        upload_to='logos/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.university_name


class NavigationItem(models.Model):

    title = models.CharField(max_length=100)

    url_name = models.CharField(max_length=100)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class Revision(models.Model):

    name = models.CharField(max_length=100)

    year = models.CharField(max_length=50)

    credits = models.IntegerField(default=0)

    courses = models.IntegerField(default=0)

    description = models.TextField()

    tags = models.TextField()

    color_class = models.CharField(
        max_length=100,
        blank=True
    )

    border_class = models.CharField(
        max_length=100,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} ({self.year})"


class KPI(models.Model):

    title = models.CharField(max_length=100)

    value = models.CharField(max_length=100)

    tag = models.CharField(max_length=100)

    change = models.CharField(max_length=100)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class CreditDistribution(models.Model):

    year = models.CharField(max_length=20)

    core = models.IntegerField()

    minor_track = models.IntegerField()

    open_elective = models.IntegerField()

    value_education = models.IntegerField()

    skill_enhancement = models.IntegerField()

    ability_enhancement = models.IntegerField()

    elective = models.IntegerField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class OverviewSkillGrowth(models.Model):

    year = models.CharField(max_length=20)

    internship = models.IntegerField()

    value_education = models.IntegerField()

    skill_enhancement = models.IntegerField()

    ability_enhancement = models.IntegerField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class SWOTEntry(models.Model):

    CATEGORY_CHOICES = [
        ('Strength', 'Strength'),
        ('Weakness', 'Weakness'),
        ('Opportunity', 'Opportunity'),
        ('Threat', 'Threat'),
    ]

    revision = models.ForeignKey(
        Revision,
        on_delete=models.CASCADE,
        related_name='swot_entries'
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.revision} - {self.category}"


class FlexibilityMetric(models.Model):

    revision = models.OneToOneField(
        Revision,
        on_delete=models.CASCADE
    )

    core = models.IntegerField(default=0)

    minor_track = models.IntegerField(default=0)

    open_elective = models.IntegerField(default=0)

    value_education = models.IntegerField(default=0)

    skill_enhancement = models.IntegerField(default=0)

    ability_enhancement = models.IntegerField(default=0)

    elective = models.IntegerField(default=0)

    flexibility_index = models.IntegerField(default=0)

    def __str__(self):
        return self.revision.name


class NewCourseSummary(models.Model):

    new_courses_added = models.IntegerField()

    percentage_growth = models.IntegerField()

    new_credits = models.IntegerField()

    industry_facing = models.IntegerField()

    courses_dropped = models.IntegerField()

    def __str__(self):
        return "New Courses Summary"


class NewCourseGrowth(models.Model):

    year = models.CharField(max_length=20)

    core = models.IntegerField()

    elective = models.IntegerField()

    skill = models.IntegerField()

    experiential = models.IntegerField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class NewCourse(models.Model):

    course_name = models.CharField(max_length=255)

    course_code = models.CharField(max_length=100)

    introduced_year = models.CharField(max_length=20)

    category = models.CharField(max_length=50)

    credit = models.IntegerField()

    semester = models.IntegerField()

    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class SkillSummary(models.Model):

    total_skill_courses = models.IntegerField()

    percentage_of_curriculum = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    previous_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    certification_tracks = models.IntegerField()

    semester_skill_labs = models.IntegerField()

    growth_percentage = models.IntegerField()

    def __str__(self):
        return "Skill Courses Summary"


class SkillGrowth(models.Model):

    year = models.CharField(max_length=20)

    credits = models.IntegerField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class CertificationTrack(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


class EmployabilitySummary(models.Model):

    employability_text = models.TextField()

    ethics_text = models.TextField()

    sustainability_text = models.TextField()

    vision_statement = models.TextField()

    def __str__(self):
        return "Employability Summary"


class EmployabilityInitiative(models.Model):

    CATEGORY_CHOICES = [
        ('Employability', 'Employability'),
        ('Ethics', 'Ethics'),
        ('Sustainability', 'Sustainability'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=255)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title



class EntrepreneurshipSummary(models.Model):

    entrepreneurship_text = models.TextField()

    research_text = models.TextField()

    higher_studies_text = models.TextField()

    vision_statement = models.TextField()

    notable_achievement = models.TextField(
        blank=True
    )

    def __str__(self):
        return "Entrepreneurship Summary"


class EntrepreneurshipInitiative(models.Model):

    CATEGORY_CHOICES = [
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Research', 'Research'),
        ('Higher Studies', 'Higher Studies'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=255)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class IndustrySkillSummary(models.Model):

    skill_development_text = models.TextField()

    tcs_text = models.TextField()

    certification_text = models.TextField()

    linkedin_text = models.TextField()

    hackerrank_text = models.TextField()

    github_text = models.TextField()

    live_projects_text = models.TextField()

    practical_learning_text = models.TextField()

    vision_statement = models.TextField()

    def __str__(self):
        return "Industry Skill Summary"


class IndustrySkillInitiative(models.Model):

    CATEGORY_CHOICES = [
        ('Platform', 'Platform'),
        ('Skill Domain', 'Skill Domain'),
        ('Project Domain', 'Project Domain'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=255)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class GlobalBenchmarkSummary(models.Model):

    benchmarking_text = models.TextField()

    exchange_program_text = models.TextField()

    research_text = models.TextField()

    impact_text = models.TextField()

    student_achievement = models.TextField()

    vision_statement = models.TextField()

    def __str__(self):
        return "Global Benchmarking Summary"


class GlobalPartner(models.Model):

    name = models.CharField(max_length=255)

    country = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


class UGCComplianceSummary(models.Model):

    overview = models.TextField()

    conclusion = models.TextField()

    def __str__(self):
        return "UGC Compliance Summary"


class UGCComplianceScore(models.Model):

    year = models.CharField(max_length=20)

    compliance_percentage = models.IntegerField()

    flexibility_index = models.IntegerField()

    compliance_level = models.CharField(
        max_length=100
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class UGCObservation(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class UGCRequirement(models.Model):

    requirement = models.CharField(
        max_length=255
    )

    year_2018 = models.CharField(
        max_length=100
    )

    year_2019 = models.CharField(
        max_length=100
    )

    year_2021 = models.CharField(
        max_length=100
    )

    year_2023 = models.CharField(
        max_length=100
    )

    year_2024 = models.CharField(
        max_length=100
    )

    year_2025 = models.CharField(
        max_length=100
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.requirement


class UGCYearSummary(models.Model):

    year = models.CharField(
        max_length=20
    )

    interpretation = models.TextField()

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class GapCategory(models.Model):

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


class Recommendation(models.Model):

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Future', 'Future'),
    ]

    category = models.ForeignKey(
        GapCategory,
        on_delete=models.CASCADE,
        related_name='recommendations'
    )

    title = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title[:60]


class CurriculumGap(models.Model):

    SEVERITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title = models.CharField(max_length=255)

    description = models.TextField()

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )

    present_years = models.CharField(
        max_length=255
    )

    removed_years = models.CharField(
        max_length=255
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title



class IncrementalGrowthSummary(models.Model):

    program_name = models.CharField(
        max_length=100
    )

    total_credits = models.IntegerField()

    total_courses = models.IntegerField()

    core_cs_credits = models.IntegerField()

    elective_variety = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.program_name


class IncrementalGrowthMetric(models.Model):

    year = models.CharField(
        max_length=20
    )

    total_credits = models.IntegerField()

    total_courses = models.IntegerField()

    core_cs_credits = models.IntegerField()

    internship_credits = models.IntegerField()

    elective_variety = models.CharField(
        max_length=50
    )

    ai_ml_courses = models.CharField(
        max_length=50
    )

    hss_value_credits = models.CharField(
        max_length=50
    )

    multidisciplinary = models.CharField(
        max_length=50
    )

    cloud_cyber_courses = models.IntegerField()

    theory_hours = models.IntegerField()

    practical_hours = models.IntegerField()

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year


class MSCGrowthMetric(models.Model):

    year = models.CharField(
        max_length=20
    )

    total_credits = models.IntegerField()

    total_courses = models.IntegerField()

    core_cs_credits = models.IntegerField()

    internship_credits = models.IntegerField()

    elective_variety = models.CharField(
        max_length=50
    )

    ai_ml_courses = models.IntegerField()

    cloud_cyber_courses = models.IntegerField()

    theory_hours = models.IntegerField()

    practical_hours = models.IntegerField()

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.year

class MSCGrowthAnalysis(models.Model):

    dimension = models.CharField(
        max_length=100
    )

    value_2021 = models.CharField(
        max_length=100
    )

    value_2024 = models.CharField(
        max_length=100
    )

    value_2025 = models.CharField(
        max_length=100
    )

    trend = models.CharField(
        max_length=100
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.dimension