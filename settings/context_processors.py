from django.conf import settings


def about_links(request):
    return {
        "github_link": settings.AB_GITHUB_LINK,
        "linkedin_link": settings.AB_LINKEDIN_LINK,
        "cv_link": settings.AB_CV_LINK,
        "email_link": settings.AB_EMAIL_LINK,
    }
