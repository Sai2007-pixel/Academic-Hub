from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from django.core.mail import send_mail

from .models import (
    Branch,
    Semester,
    Subject,
    File,
    FileCategory
)

# =========================================
# HOME PAGE
# =========================================

def home(request):

    branches = Branch.objects.all()

    total_courses = Branch.objects.count()

    total_semesters = Semester.objects.count()

    total_resources = File.objects.count()

    return render(request, 'home.html', {

        'branches': branches,

        'total_courses': total_courses,

        'total_semesters': total_semesters,

        'total_resources': total_resources,

    })


# =========================================
# SEMESTERS PAGE
# =========================================

def semesters(request, branch_id):

    branch = get_object_or_404(
        Branch,
        id=branch_id
    )

    semesters = Semester.objects.all().order_by('id')

    active_sem_ids = list(

        Subject.objects.filter(
            branches__id=branch_id
        ).values_list(
            'semester_id',
            flat=True
        )

    )

    return render(request, 'semesters.html', {

        'branch': branch,
        'semesters': semesters,
        'active_sem_ids': active_sem_ids

    })


# =========================================
# SUBJECTS PAGE
# =========================================

def subjects(request, sem_id, branch_id):

    branch = get_object_or_404(
        Branch,
        id=branch_id
    )

    semester = get_object_or_404(
        Semester,
        id=sem_id
    )

    subjects = Subject.objects.filter(

        semester_id=sem_id,
        branches__id=branch_id

    ).distinct()

    return render(request, 'subjects.html', {

        'subjects': subjects,
        'branch': branch,
        'semester': semester

    })


# =========================================
# CATEGORY PAGE
# =========================================

def categories_view(request, subject_id):

    subject = get_object_or_404(
        Subject,
        id=subject_id
    )

    categories = FileCategory.objects.all()

    category_data = []

    for category in categories:

        file_count = File.objects.filter(

            subject=subject,
            category=category

        ).count()

        category_data.append({

            'category': category,
            'file_count': file_count

        })

    context = {

        'subject': subject,
        'category_data': category_data

    }

    return render(
        request,
        'categories.html',
        context
    )


# =========================================
# FILES PAGE
# =========================================

def files(request, subject_id, category_id):

    subject = get_object_or_404(
        Subject,
        id=subject_id
    )

    category = get_object_or_404(
        FileCategory,
        id=category_id
    )

    files = File.objects.filter(

        subject=subject,
        category=category

    ).order_by('-uploaded_at')

    return render(request, 'files.html', {

        'files': files,
        'category': category,
        'subject': subject

    })

def view_file(request, file_id):

    file = get_object_or_404(File, id=file_id)

    return render(request, 'view_pdf.html', {
        'file': file
    })

def about(request):
    return render(request, 'about.html')



def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        full_message = f"""
Name: {name}

Email: {email}

Message:
{message}
"""

        send_mail(

            subject='Academic Hub Contact Message',

            message=full_message,

            from_email='thedigitalhub16@gmail.com',

            recipient_list=['thedigitalhub16@gmail.com'],

            fail_silently=False,

        )

        return render(request, 'contact.html', {

            'success': True

        })

    return render(request, 'contact.html')

def maintenance(request):

    return render(request,'maintenance.html')