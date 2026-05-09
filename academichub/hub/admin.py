# from django.contrib import admin
# from .models import Semester, Branch, Subject, File, FileCategory

# # 🔹 Branch Admin
# @admin.register(Branch)
# class BranchAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     search_fields = ['name']


# # 🔹 Semester Admin
# @admin.register(Semester)
# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     ordering = ['id']


# # 🔹 Subject Admin
# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'semester']
#     list_filter = ['semester', 'branches']
#     search_fields = ['name']


# # 🔹 File Category Admin
# @admin.register(FileCategory)
# class FileCategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']


# # 🔹 File Admin
# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'subject', 'category', 'uploaded_at']
#     list_filter = ['category', 'subject']
#     search_fields = ['title']
#     ordering = ['-uploaded_at']



from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Semester,
    Branch,
    Subject,
    File,
    FileCategory
)

# =========================================
# BRANCH ADMIN
# =========================================

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = [

        'id',
        'name',
        'total_subjects'

    ]

    search_fields = ['name']

    ordering = ['id']

    # SUBJECT COUNT

    def total_subjects(self, obj):

        return Subject.objects.filter(
            branches=obj
        ).count()

    total_subjects.short_description = 'Subjects'


# =========================================
# SEMESTER ADMIN
# =========================================

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):

    list_display = [

        'id',
        'name'

    ]

    ordering = ['id']

    search_fields = ['name']


# =========================================
# SUBJECT ADMIN
# =========================================

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = [

        'id',
        'name',
        'semester',
        'branch_list'

    ]

    list_filter = [

        'semester',
        'branches'

    ]

    search_fields = ['name']

    ordering = ['semester']

    # SHOW BRANCHES

    def branch_list(self, obj):

        return ", ".join(

            [branch.name for branch in obj.branches.all()]

        )

    branch_list.short_description = 'Branches'


# =========================================
# FILE CATEGORY ADMIN
# =========================================

@admin.register(FileCategory)
class FileCategoryAdmin(admin.ModelAdmin):

    list_display = [

        'id',
        'name',
        'total_files'

    ]

    search_fields = ['name']

    # FILE COUNT

    def total_files(self, obj):

        return File.objects.filter(
            category=obj
        ).count()

    total_files.short_description = 'Files'


# =========================================
# FILE ADMIN
# =========================================

@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    list_display = [

        'id',
        'title',
        'subject',
        'category',
        'uploaded_at',
        'view_pdf'

    ]

    list_filter = [

        'category',
        'subject',
        'uploaded_at'

    ]

    search_fields = [

        'title',
        'subject__name'

    ]

    ordering = ['-uploaded_at']

    readonly_fields = ['preview_link']

    # PDF BUTTON

    def view_pdf(self, obj):

        if obj.file:

            return format_html(

                '<a class="button" href="{}" target="_blank">View PDF</a>',

                obj.file.url

            )

        return "No File"

    view_pdf.short_description = 'Preview'

    # PREVIEW LINK

    def preview_link(self, obj):

        if obj.file:

            return format_html(

                '<a href="{}" target="_blank">Open File</a>',

                obj.file.url

            )

        return "No File"

    preview_link.short_description = 'PDF Preview'