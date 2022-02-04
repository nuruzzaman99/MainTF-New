import base64

import requests
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

from BusinessSecurity import forms, models
from Academy.forms import BCSCourseCreateForm, SectionCreateForm, ContentCreateForm, CourseCategoryCreateForm, \
    BCSSectionCreateForm, BCSContentCreateForm, AddCoursePackageForm, AddCoursePackageFeatureForm, \
    AddCourseIndividualPackageFeatureForm
from Account.models import User, Permissions, Interest
from Account.forms import SelectBCSPermissionForm, InterestForm
from Academy.models import Course, Section, Content, CourseCategory, BCSCourse, BCSSection, BCSContent, CoursePackage, \
    PackageFeatures, CourseOrder, CoursePurchase
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import datetime
from django.utils.dateparse import parse_date
from django.utils.formats import get_format
from Blog.models import Post


def date_parser(date_str):
    """Parse date from string by DATE_INPUT_FORMATS of current language"""
    for item in get_format('DATE_INPUT_FORMATS'):
        try:
            return datetime.datetime.strptime(date_str, item).date()
        except (ValueError, TypeError):
            continue

    return None


# Create your views here.
def superuser_permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


# def main_super_admin_permission_check(user):
#     return user.is_superuser or (
#                 user.permission_user.is_superadmin and user.permission_user.is_admin and user.permission_user.is_moderator and user.permission_user.is_editor)


def main_admin_permission_check(user):
    return user.is_staff and user.is_superuser


def main_admin_permission_check_order_page(user):
    return user.is_staff and user.is_superuser


def bcs_admin_permission_check(user):
    try:
        return user.is_staff and user.is_superuser or user.is_bcs_head
    except:
        return user.is_staff and user.is_superuser


def bcs_admin_permission_check_order(user):
    try:
        return user.is_staff and user.is_superuser or user.is_bcs_head or user.is_sales
    except:
        return user.is_staff and user.is_superuser


def ticket_admin(user):
    try:
        return user.is_staff and user.is_superuser or user.is_bcs_head or user.is_pcs_head or user.is_sales
    except:
        return user.is_staff and user.is_superuser


def indexView(request):
    context = {

    }

    return render(request, 'index.html', context)


def getStartView(request):
    context = {

    }

    return render(request, 'pages/get_start.html', context)


def aboutUsView(request):
    context = {

    }

    return render(request, 'pages/aboutus.html', context)


def enterpriseCyberSecurityView(request):
    context = {

    }
    return render(request, 'pages/enterprise_cybersecurity.html', context)


# ---------------------------------------------


def vulnerabilityAssessmentView(request):
    context = {

    }
    return render(request, 'pages/vulnerability_assessment.html', context)


def redTeamPenetrationTestingView(request):
    context = {

    }
    return render(request, 'pages/red_team_penetration_testing.html', context)


def cybersecurityRiskAssessmentView(request):
    context = {

    }
    return render(request, 'pages/cybersecurity_risk_assessment.html', context)


def incidentResponseServiceView(request):
    context = {

    }
    return render(request, 'pages/incident_response_service.html', context)


def hackRecoveryServiceView(request):
    context = {

    }
    return render(request, 'pages/hack_recovery_service.html', context)


def bestMalwareRemovalView(request):
    context = {

    }
    return render(request, 'pages/best_malware_removal.html', context)


def digitalForensicInvestigationView(request):
    context = {

    }
    return render(request, 'pages/digital_forensic_investigation.html', context)


def complianceConsultingView(request):
    context = {

    }
    return render(request, 'pages/compliance_consulting.html', context)


def ISO27001View(request):
    context = {

    }
    return render(request, 'pages/iso27001.html', context)


def pciDssComplianceView(request):
    context = {

    }
    return render(request, 'pages/pci_dss_compliance.html', context)


def gdprComplianceView(request):
    context = {

    }
    return render(request, 'pages/gdpr_compliance.html', context)


def hippaComplianceConsultingView(request):
    context = {

    }
    return render(request, 'pages/hippa_compliance_consulting.html', context)


def smallBusinessCybersecurityView(request):
    context = {

    }
    return render(request, 'pages/small_business_cybersecurity.html', context)


def managedCybersecurityServiceView(request):
    context = {

    }
    return render(request, 'pages/managed_cybersecurity_service.html', context)


def plugAndPlayCyberCecurityView(request):
    context = {

    }
    return render(request, 'pages/plug_and_play_cyber_security.html', context)


def leaderView(request):
    context = {

    }
    return render(request, 'pages/leader.html', context)


def testimonialView(request):
    context = {

    }
    return render(request, 'pages/testimonial.html', context)


def partnerView(request):
    context = {

    }
    return render(request, 'pages/partner.html', context)


def partnerFaqView(request):
    context = {

    }
    return render(request, 'pages/partner_faq.html', context)


def franchiseView(request):
    context = {

    }
    return render(request, 'pages/franchise.html', context)


def franchiseFaqView(request):
    context = {

    }
    return render(request, 'pages/franchise_faq.html', context)


def investorView(request):
    context = {

    }
    return render(request, 'pages/investor.html', context)


def careerView(request):
    context = {

    }
    return render(request, 'pages/career.html', context)


def eventsView(request):
    context = {

    }
    return render(request, 'pages/events.html', context)


def policyView(request):
    context = {

    }
    return render(request, 'pages/policy.html', context)


def termsView(request):
    context = {

    }
    return render(request, 'pages/terms.html', context)


def BCSFormView(request):
    context = {

    }
    return render(request, 'pages/bcs_form.html', context)


def bPartnerView(request):
    context = {

    }
    return render(request, 'pages/bpartner.html', context)


def trustView(request):
    context = {

    }
    return render(request, 'pages/trust.html', context)


def findUsView(request):
    context = {

    }
    return render(request, 'pages/findus.html', context)


def appoinmentView(request):
    context = {

    }
    return render(request, 'pages/appoinment.html', context)


# Business Section
@login_required
def createBusinessView(request):
    current_user = request.user
    if not request.user.is_bcs:
        form = forms.CreateBusinessForm()
        if request.POST:
            if 'new' in request.POST:
                form = forms.CreateBusinessForm(request.POST, request.FILES)
                position = request.POST.get('position')
                business = form.save(commit=True)
                current_user.is_bcs = True
                current_user.save()
                user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                    position=position, privilege='admin')
                user_business.save()
                return HttpResponseRedirect(reverse('bcs_user_dashboard'))
            elif 'join' in request.POST:
                joining_key = request.POST.get('joining_key')
                try:
                    business = models.Business.objects.get(
                        unique_id=joining_key)
                    current_user.is_bcs = True
                    current_user.save()
                    user_business = models.UsersBusiness.objects.create(user=current_user, business=business,
                                                                        position='staff', privilege='general_staff')
                    user_business.save()
                    return HttpResponseRedirect(reverse('bcs_user_my_team'))
                except:
                    message = 'Wrong Business Key'
                    context = {
                        'form': form,
                        'message': message,
                    }
                    return render(request, 'user_panel/bcs/redirection.html', context)

        context = {
            'form': form,
        }
        return render(request, 'user_panel/bcs/redirection.html', context)
    else:
        return HttpResponseRedirect(reverse('bcs_user_dashboard'))


@login_required
def userDashboardView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            current_business = request.user.business_user.business
            notifications = models.Notification.objects.filter(
                category_choice='bcs').order_by('-notification_time')[:2]

            events = models.Events.objects.filter(
                status='active', category='for_business_security')
            registered_event = models.RegisteredEvents.objects.filter(
                user=request.user).values_list('event', flat=True)
            orders = models.Order.objects.filter(
                Q(user__business_user__business=current_business, category_choice='bcs') & ~Q(
                    Q(order_status='new') | Q(order_status='attending'))).order_by('-order_date')[:2]
            subscriptions = models.SubscriptionOrder.objects.filter(user__business_user__business=current_business,
                                                                    is_active=True, category_choice='bcs')

            posts = Post.objects.all().order_by('date')[:2]
            context = {
                'events': events,
                'registered_event': registered_event,
                'orders': orders,
                'subscriptions': subscriptions,
                'notifications': notifications,
                'posts': posts,
            }
            return render(request, 'user_panel/bcs/dashboard.html', context)


@login_required
def userServicesView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            courses = BCSCourse.objects.all()
            courses_categories = CourseCategory.objects.filter(course_type='Business')
            service_category = models.ServiceCategory.objects.filter(
                category_choice='bcs')
            services = models.Service.objects.filter(category_choice='bcs')
            subscription_services = models.SubscriptionServices.objects.filter(
                category_choice='bcs')
            if request.method == 'POST':
                data_list = request.POST
                file_list = request.FILES
                # print(data_list)
                # print(file_list)

                current_service = get_object_or_404(models.Service, service_title=data_list['service_name'],
                                                    category_choice='bcs')

                for data in data_list:
                    if data != 'csrfmiddlewaretoken' and data != 'service_name':
                        current_input = models.SubServiceInput.objects.get(
                            id=data)
                        input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                                inputinfo=data_list[data])
                        input_data.save()
                        order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                                   service=current_service, category_choice='bcs')

                        order[0].subserviceinput.add(input_data)
                for files in file_list:
                    current_input = models.SubServiceInput.objects.get(
                        id=files)
                    myfile = file_list[files]
                    fs = FileSystemStorage()
                    filename = fs.save(myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)
                    input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                            inputinfo=uploaded_file_url)
                    input_data.save()
                    order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                               service=current_service, category_choice='bcs')

                    order[0].subserviceinput.add(input_data)

                order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                           service=current_service, category_choice='bcs')

                if not order[0].orderstaff_order.all().exists():
                    tracking = models.Tracking.objects.get(
                        service=current_service)
                    persons = tracking.persons
                    persons_list = list(filter(None, persons.split(',')))
                    person = persons_list.pop(0)
                    persons_list.append(person)
                    tracking.persons = ','.join(persons_list)
                    tracking.save()
                    current_staff = models.User.objects.get(id=person)
                    order_staff = models.OrderStaff.objects.create(
                        staff=current_staff, order=order[0])
                    order_staff.save()

                notification = models.AdminNotification.objects.create(category_choice='bcs',
                                                                       business=request.user.business_user.business,
                                                                       notification=f'Got a New Quotation. ID: {order[0].id} <a href="https://main.techforing.com/bcs_user_order_details/{order[0].id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                notification.save()
                return render(request, 'user_panel/bcs/thanks.html')
            context = {
                'service_category': service_category,
                'services': services,
                'services_headings': list(services.values_list('service_title', flat=True)),
                'subscription_services': subscription_services,
                'subscription_services_headings': list(subscription_services.values_list('service_title', flat=True)),
                'courses_categories': courses_categories,
                'courses': courses,
                'courses_headings': list(courses.values_list('course_name', flat=True)),
            }
            return render(request, 'user_panel/bcs/services.html', context)


@login_required
def bcsUserCourseDetail(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        course = BCSCourse.objects.get(id=id)
        sections = BCSSection.objects.filter(course=course)
        context = {
            'course': course,
            'sections': sections,
        }
        return render(request, 'user_panel/bcs/courseDetails.html', context)


@login_required
def bcsUserCoursePayment(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        course = BCSCourse.objects.get(id=id)
        context = {
            'course': course,
        }
        return render(request, 'user_panel/bcs/course_payment.html', context)


@login_required
def userQuotationsHistoryView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            orders = models.Order.objects.filter(
                Q(user=request.user, category_choice='bcs') & Q(
                    Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
                '-order_date')
            context = {
                'orders': orders,
                'message': 'Quotations',
            }
            return render(request, 'user_panel/bcs/order_history.html', context)


@login_required
def userOrderHistoryView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            orders = models.Order.objects.filter(
                Q(user=request.user, category_choice='bcs') & ~Q(
                    Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
                '-order_date')
            print(orders.query)
            context = {
                'orders': orders,
                'message': 'Orders',
            }
            return render(request, 'user_panel/bcs/order_history.html', context)


@login_required
def userOrderDetailsView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            try:
                order = models.Order.objects.get(id=id, category_choice='bcs')
                if order.user.business_user.business == request.user.business_user.business:
                    current_order = models.Order.objects.get(id=id, category_choice='bcs')
                    try:
                        current_quotation = models.Quotation.objects.get(order=current_order)
                        current_agreement = models.QuotationAgreement.objects.get(quotation=current_quotation)
                        form = forms.QuotationAgreementForm(instance=current_agreement)
                        if request.method == 'POST':
                            form = forms.QuotationAgreementForm(data=request.POST, files=request.FILES,
                                                                instance=current_agreement)
                            if form.is_valid():
                                quotation = form.save(commit=False)
                                quotation.quotation = current_quotation
                                quotation.save()
                                if quotation.agreement == 'agree':
                                    current_quotation.agreement = 'agree'
                                    current_quotation.save()

                                return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    except:
                        current_quotation = models.Quotation.objects.get(order=current_order)
                        form = forms.QuotationAgreementForm()
                        if request.method == 'POST':
                            form = forms.QuotationAgreementForm(data=request.POST, files=request.FILES)
                            if form.is_valid():
                                quotation = form.save(commit=False)
                                quotation.quotation = current_quotation
                                quotation.save()
                                if quotation.agreement == 'agree':
                                    current_quotation.agreement = 'agree'
                                    current_quotation.save()

                                return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    context = {
                        'current_order': current_order,
                        'form': form,
                    }
                    return render(request, 'user_panel/bcs/order_detail.html', context)
                else:
                    return HttpResponse("You don't have permission to view this page")
            except:
                return HttpResponse("You don't have permission to view this page")


@login_required
def quotationAcceptView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            order = models.Order.objects.get(id=id, category_choice='bcs')
            if order.user.business_user.business == request.user.business_user.business:
                current_order = models.Order.objects.get(id=id, category_choice='bcs')
                current_quotation = models.Quotation.objects.get(order=current_order)
                current_quotation.agree_to_quotation = 'agree'
                current_order.order_status = 'agreed_to_quotation'
                current_quotation.save()
                current_order.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                return HttpResponse("You don't have permission to view this page")
        except:
            return HttpResponse("You don't have permission to view this page")


@login_required
def ndaNcaAcceptView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            order = models.Order.objects.get(id=id, category_choice='bcs')
            if order.user.business_user.business == request.user.business_user.business:
                current_order = models.Order.objects.get(id=id, category_choice='bcs')
                current_quotation = models.Quotation.objects.get(order=current_order)
                current_quotation.agree_to_nda_nca = 'agree'
                current_order.order_status = 'agreed_to_nda_nca'
                current_quotation.save()
                current_order.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                return HttpResponse("You don't have permission to view this page")
        except:
            return HttpResponse("You don't have permission to view this page")


@login_required
def orderRejectView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            current_order = models.Order.objects.get(
                user=request.user, id=id, category_choice='bcs')
            current_quotation = models.Quotation.objects.get(order=current_order)
            current_quotation.agree_to_quotation = 'disagree'
            current_quotation.agree_to_nda_nca = 'disagree'
            current_order.order_status = 'disagreed'
            current_quotation.save()
            current_order.save()

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        except:
            return HttpResponse("You don't have permission to view this page")


@login_required
def bcsUserMyTeamView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            current_business = models.UsersBusiness.objects.get(
                user=request.user)

            business = current_business.business
            admins = business.business_business.filter(
                privilege='admin').count()

            image_form = forms.BusinessLogoForm(
                instance=current_business.business)
            info_form = forms.BusinessInfoForm(
                instance=current_business.business)
            if request.method == 'POST':
                if 'img-btn' in request.POST:
                    image_form = forms.BusinessLogoForm(
                        request.POST, request.FILES, instance=current_business.business)
                    if image_form.is_valid():
                        image_form.save()
                elif 'info-btn' in request.POST:
                    info_form = forms.BusinessInfoForm(
                        request.POST, instance=current_business.business)
                    if info_form.is_valid():
                        info_form.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
                elif 'inv-btn' in request.POST:
                    emails = request.POST['email'].split()
                    # print(emails)
                    err_mail = []
                    suc_mail = []
                    for mail in emails:
                        try:
                            added_user = models.User.objects.get(email=mail)
                            added_user.is_bcs = True
                            added_user.save()
                            user_business = models.UsersBusiness.objects.get_or_create(user=added_user,
                                                                                       business=current_business.business)
                            user_business[0].save()
                            suc_mail.append(mail)
                            context = {
                                'current_business': current_business,
                                'image_form': image_form,
                                'info_form': info_form,
                                'admins': admins,
                                'success': f'User with given email {suc_mail} added'
                            }

                        except:
                            err_mail.append(mail)
                            context = {
                                'current_business': current_business,
                                'image_form': image_form,
                                'info_form': info_form,
                                'admins': admins,
                                'message': f'User with given email {err_mail} not found'
                            }
                    return render(request, 'user_panel/bcs/my_team.html', context)

                    # if added_user is not None:
                    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    # else:
                    #     return render(request, 'user_panel/bcs/my_team.html', context)
                    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    # user_business = models.UsersBusiness.objects.get_or_create(user=added_user, business=current_business.business)
                    # user_business[0].save()
                    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    # try:
                    #     added_user = models.User.objects.get(email=request.POST.get('email'))
                    #     user_business = models.UsersBusiness.objects.get_or_create(user=added_user, business=current_business.business)
                    #     user_business[0].save()
                    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])
                    # except:
                    #     context = {
                    #         'current_business': current_business,
                    #         'image_form': image_form,
                    #         'info_form': info_form,
                    #         'message': 'User with given email not found'
                    #     }
                    #     return render(request, 'user_panel/bcs/my_team.html', context)
            context = {
                'current_business': current_business,
                'image_form': image_form,
                'info_form': info_form,
                'admins': admins,
            }
            return render(request, 'user_panel/bcs/my_team.html', context)
        except:
            return HttpResponse("You don't have permission to view this page.")

@login_required
def bcsUserTeamFormView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        try:
            current_business = models.UsersBusiness.objects.get(
                user=request.user)

            business = current_business.business
            current_subscription_order = models.SubscriptionOrder.objects.get(id=id)

            current_subscription_team = models.SubscriptionTeam.objects.get(business=business, user=request.user, subscription_order=current_subscription_order)
            field_id = current_subscription_team.subscription_order.subscription_service.subscriptionservice_service.id

            # Form Submit
            print(request.POST)
            if request.method == 'POST':
                data_list = request.POST
                file_list = request.FILES
                # print(data_list)
                # print(file_list)

                # current_service = get_object_or_404(models.SubscriptionServices, service_title=data_list['service_name'],
                #                                     category_choice='bcs')
                current_subscription_service = current_subscription_order.subscription_service
                print(current_subscription_service)

                for data in data_list:
                    if data != 'csrfmiddlewaretoken' and data != 'service_name':
                        current_input = models.SubServiceInput.objects.get(
                            id=data)
                        input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                                inputinfo=data_list[data])
                        input_data.save()
                        order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                                   service=current_subscription_service, category_choice='bcs')

                        order[0].subserviceinput.add(input_data)
                for files in file_list:
                    current_input = models.SubServiceInput.objects.get(
                        id=files)
                    myfile = file_list[files]
                    fs = FileSystemStorage()
                    filename = fs.save(myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)
                    input_data = models.UserSubserviceInput(user=request.user, inputfield=current_input,
                                                            inputinfo=uploaded_file_url)
                    input_data.save()
                    order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                               service=current_subscription_service, category_choice='bcs')

                    order[0].subserviceinput.add(input_data)

                order = models.Order.objects.get_or_create(user=request.user, order_status='new',
                                                           service=current_subscription_service, category_choice='bcs')

                if not order[0].orderstaff_order.all().exists():
                    tracking = models.Tracking.objects.get(
                        service=current_subscription_service)
                    persons = tracking.persons
                    persons_list = list(filter(None, persons.split(',')))
                    person = persons_list.pop(0)
                    persons_list.append(person)
                    tracking.persons = ','.join(persons_list)
                    tracking.save()
                    current_staff = models.User.objects.get(id=person)
                    order_staff = models.OrderStaff.objects.create(
                        staff=current_staff, order=order[0])
                    order_staff.save()

                notification = models.AdminNotification.objects.create(category_choice='bcs',
                                                                       business=request.user.business_user.business,
                                                                       notification=f'Got a New Quotation. ID: {order[0].id} <a href="https://main.techforing.com/bcs_user_order_details/{order[0].id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                notification.save()
                return render(request, 'user_panel/bcs/thanks.html')


            context = {
                'current_business': current_business,
                'field_id': field_id,
            }
            return render(request, 'user_panel/bcs/teamform.html', context)
        except:
            return HttpResponse("You don't have permission to view this page.")

@login_required
def bcsUserTeamMemberDeleteView(request, id):
    if request.user.business_user.privilege == 'general_staff':
        return HttpResponse("You don't have permission to view this page")
    else:
        current_employee = models.UsersBusiness.objects.get(id=id)
        current_user = models.User.objects.get(id=current_employee.user.id)
        if current_user == request.user \
                or current_user.business_user.privilege == 'general_admin' \
                or current_employee.privilege == 'admin':
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            current_user.is_bcs = False
            current_user.save()
            current_employee.delete()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def bcsUserMyTeamProfileView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        current_user = models.User.objects.get(business_user__id=id)
        context = {
            'current_user': current_user,
        }
        return render(request, 'user_panel/bcs/profile.html', context)


@login_required
def subscriptionPayment(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    else:
        current_package = models.SubscriptionBasedPackage.objects.get(id=id)

        context = {
            'current_package': current_package,
        }

    return render(request, 'user_panel/bcs/subscription_payment.html', context)


@login_required
def subscriptionCancelView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    else:
        username = 'AfTmv1E8P0HbJCkRMtm7s_07rqkJCGvp4WufOBxLWUl5AFujlsqmn6WdpMZo-nQr-yKVTnogZOQYgLnl'
        password = 'EOsLHpTI748BbKSwcWlQpgmuJZXyudRnJP50Gc8H5Anf8VnDfk8FtEtRYwJ_iU1T9sgH5DOv53BuqeyH'
        busername = str(base64.b64encode(bytes(username, 'utf-8')))[1:].replace("'", "").replace("=", '')
        bpassword = str(base64.b64encode(bytes(password, 'utf-8')))[1:].replace("'", "")
        bearer = f"Basic {busername}6{bpassword}"

        current_package = models.SubscriptionBasedPackage.objects.get(id=id)
        current_order = models.SubscriptionOrder.objects.get(
            user__business_user__business=request.user.business_user.business,
            subscription_package=current_package,
            category_choice='bcs',
            subscription_service=current_package.service_id,
            is_active=True
        )

        current_order.is_active = False
        current_order.save()
        url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{current_order.paypal_subscription_id}/cancel'
        headers = {
            'Content-type': 'application/json',
            'Authorization': bearer
        }
        r = requests.post(url, headers=headers)
        print(r.status_code)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def userSubscriptionsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            services = models.SubscriptionServices.objects.filter(
                category_choice='bcs')
            context = {
                'services': services,
            }
            return render(request, 'user_panel/bcs/subscriptions.html', context)


@login_required
def userEventsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        registered_event = models.RegisteredEvents.objects.filter(
            user=request.user).values_list('event', flat=True)

        business_user = models.UsersBusiness.objects.get(user=request.user)

        events = models.Events.objects.filter(category='for_business_security',
                                              registered_event_event__user__business_user=business_user)

        context = {
            'events': events,
            'registered_event': registered_event,
        }
        return render(request, 'user_panel/bcs/events.html', context)


@login_required
def userEventRegisterView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))
    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            current_event = models.Events.objects.get(id=id)
            is_register = models.RegisteredEvents.objects.filter(
                user=request.user, event=current_event)
            if not is_register:
                models.RegisteredEvents.objects.get_or_create(
                    user=request.user, event=current_event)
            else:
                is_register.delete()
            try:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except:
                return HttpResponseRedirect(reverse('pcs_user_dashboard'))


@login_required
def userNotificationsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            notifications = models.Notification.objects.filter(
                Q(category_choice='bcs') | Q(
                    category_choice__iexact=request.user.business_user.business.company_name)).order_by(
                '-notification_time')

            new_notifications = []
            all_notifications = []
            for notification in notifications:
                if notification.notification_time.date() == datetime.datetime.today().date():
                    if notification not in new_notifications:
                        new_notifications.append(notification)
                elif notification.notification_time.date() != datetime.datetime.today().date():
                    if notification.notification_time.date() < datetime.datetime.today().date():
                        if notification not in all_notifications:
                            all_notifications.append(notification)
            context = {
                'notifications': new_notifications,
                'all_notifications': all_notifications,
            }
            for n in all_notifications:
                n.is_read = True
                n.save()
            for n in new_notifications:
                n.is_read = True
                n.save()
            return render(request, 'user_panel/bcs/notifications.html', context)


@login_required
def userSettingsView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            context = {

            }
            return render(request, 'user_panel/bcs/settings.html', context)


@login_required
def employeeTrainingProgramView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/thanks.html', context)


@login_required
def bcsAppointmentView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        context = {

        }
        return render(request, 'user_panel/bcs/appoinment.html', context)


# Team Member Section
@login_required
def teamUserServicesView(request):
    context = {

    }
    return render(request, 'user_panel/team/services.html', context)


@login_required
def teamUserMyTeamView(request):
    context = {

    }
    return render(request, 'user_panel/team/my_team.html', context)


@login_required
def teamUserSubscriptionsView(request):
    context = {

    }
    return render(request, 'user_panel/team/subscribed.html', context)


@login_required
def teamUserEventsView(request):
    context = {

    }
    return render(request, 'user_panel/team/events.html', context)


@login_required
def teamUserNotificationsView(request):
    context = {

    }
    return render(request, 'user_panel/team/notifications.html', context)


@login_required
def teamUserSettingsView(request):
    context = {

    }
    return render(request, 'user_panel/team/settings.html', context)


@login_required
def emailInvitationView(request):
    context = {

    }
    return render(request, 'user_panel/team/thanks.html', context)


@login_required
def openTicketView(request):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            form = forms.TicketCreateForm()
            tickets = models.Ticket.objects.filter(
                user=request.user, category_choice='bcs').order_by('-ticket_date')
            if request.method == 'POST':
                u_file = request.FILES['ticket_attachment']
                extension = str(u_file).split(".")[1].lower()
                # print(u_file.content_type)
                if extension not in ['php', 'exe', '', 'html', 'htm', 'asp']:
                    form = forms.TicketCreateForm(request.POST, request.FILES)
                    if form.is_valid():
                        ticket = form.save(commit=False)
                        ticket.user = request.user
                        ticket.category_choice = 'bcs'
                        ticket.ticket_status = 'open'
                        ticket.ticket_category = request.POST.get(
                            'ticket_category')
                        ticket.save()
                        notification = models.AdminNotification.objects.create(category_choice='bcs',
                                                                               business=request.user.business_user.business,
                                                                               notification=f'New Ticket Created. <a href="https://main.techforing.com/bcs_admin_tickets_detail/{ticket.id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                        notification.save()
                        return HttpResponseRedirect(request.META['HTTP_REFERER'])
            context = {
                'form': form,
                'tickets': tickets,
            }
            return render(request, 'user_panel/bcs/ticket.html', context)


@login_required
def ticketDetailView(request, id):
    if not request.user.is_bcs:
        return HttpResponseRedirect(reverse('create_business'))

    elif request.user.is_bcs:
        if request.user.business_user.privilege == 'general_staff':
            return HttpResponse("You don't have permission to view this page")
        else:
            ticket = models.Ticket.objects.get(id=id)
            commentform = forms.TicketCommentForm()
            if request.method == 'POST':
                commentform = forms.TicketCommentForm(request.POST)
                if commentform.is_valid():
                    comment = commentform.save(commit=False)
                    comment.user = request.user
                    comment.ticket = ticket
                    comment.save()
                    notification = models.AdminNotification.objects.create(category_choice='bcs',
                                                                           business=request.user.business_user.business,
                                                                           notification=f'New Comment on Ticket. <a href="https://main.techforing.com/bcs_admin_tickets_detail/{ticket.id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                    notification.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            context = {
                'ticket': ticket,
                'commentform': commentform,
            }
            return render(request, 'user_panel/bcs/ticket_detail.html', context)


# Main Admin Sections
@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminDashboardView(request):
    total_user = models.User.objects.all()
    service_categories_bcs = models.ServiceCategory.objects.filter(
        category_choice='bcs')
    service_categories_pcs = models.ServiceCategory.objects.filter(
        category_choice='pcs')
    context = {
        'total_user': total_user,
        'total_business_user': total_user.filter(is_bcs=True),
        'service_categories_bcs': service_categories_bcs,
        'service_categories_pcs': service_categories_pcs,
    }
    return render(request, 'admin_panel/mainTF/dashboard.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminProfileView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/myProfile.html', context)


@user_passes_test(main_admin_permission_check_order_page, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def mainAdminQuotationsView(request):
    orders = models.Order.objects.filter(
        Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned')).order_by('-order_date')
    context = {
        'orders': orders,
        'message': 'Quotations',
    }
    return render(request, 'admin_panel/mainTF/orders.html', context)


@user_passes_test(main_admin_permission_check_order_page, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def mainAdminOrdersView(request):
    orders = models.Order.objects.filter(
        ~Q(Q(order_status='new') | Q(order_status='attending') | Q(order_status='assigned'))).order_by(
        '-order_date')
    context = {
        'orders': orders,
        'message': 'Orders',
    }
    return render(request, 'admin_panel/mainTF/orders.html', context)


@user_passes_test(main_admin_permission_check_order_page, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def mainAdminOrdersDetailView(request, id):
    try:
        current_order = models.Order.objects.get(id=id)

        try:
            order_staff = models.OrderStaff.objects.get(order=current_order)
            form1 = forms.OrderAssignForm(instance=order_staff)
        except:
            form1 = forms.OrderAssignForm()

        current_price = models.OrderPrice.objects.get(order=current_order)
        form2 = forms.OrderPriceForm(instance=current_price)
        if request.method == 'POST':
            if 'assign-btn' in request.POST:
                try:
                    form1 = forms.OrderAssignForm(
                        request.POST, instance=order_staff)
                except:
                    form1 = forms.OrderAssignForm(request.POST)
                if form1.is_valid():
                    form = form1.save(commit=False)
                    form.order = current_order
                    form.save()
                    current_order.order_status = 'assigned'
                    current_order.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            elif 'price-btn' in request.POST:
                form2 = forms.OrderPriceForm(
                    request.POST, instance=current_price)
                if form2.is_valid():
                    current_order.order_status = 'on_progress'
                    current_order.save()
                    new_staff = models.OrderStaff.objects.get_or_create(
                        order=current_order, staff=request.user)
                    form2.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        context = {
            'current_order': current_order,
            'form1': form1,
            'form2': form2,
        }
        return render(request, 'admin_panel/mainTF/order_detail.html', context)
    except:
        return HttpResponse("You don't have permission to view this page")


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminNotificationView(request):
    form = forms.NotificationForm()
    notifications = models.Notification.objects.all().order_by('-notification_time')

    if 'instant-btn' in request.POST:
        if 'date_range' not in request.POST:
            form = forms.NotificationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'date_range' in request.POST:
            notification = request.POST.get('notification')
            input_date = request.POST.get('date_range')
            start_date = input_date.split(' - ')[0]
            end_date = input_date.split(' - ')[1]
            users = models.User.objects.filter(
                date_joined__gte=datetime.datetime.strptime(start_date, '%m/%d/%Y').date(),
                date_joined__lte=datetime.datetime.strptime(end_date, '%m/%d/%Y').date())
            # print(users)
            for user in users:
                note = models.Notification.objects.create(category_choice=user.email, notification=notification)
                note.save()
            # print(date_parser(start_date))
            # print(start_date, end_date)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'form': form,
        'notifications': notifications,
    }
    return render(request, 'admin_panel/mainTF/notification.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminNotificationDeleteView(request, id):
    current_notification = models.Notification.objects.get(id=id)
    current_notification.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminEventsView(request):
    form = forms.EventCreateForm()
    events = models.Events.objects.all().order_by('-created_date')
    if request.method == 'POST':
        form = forms.EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'events': events,
        'previous': events.filter(status='completed'),
        'active': events.filter(status='active'),
        'canceled': events.filter(status='canceled'),
    }
    return render(request, 'admin_panel/mainTF/eventWebinar.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminEventsDeleteView(request, id):
    current_event = models.Events.objects.get(id=id)
    current_event.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminEventsEditView(request, id):
    current_event = models.Events.objects.get(id=id)
    form = forms.EventCreateForm(instance=current_event)
    if request.method == 'POST':
        form = forms.EventCreateForm(request.POST, instance=current_event)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('main_admin_events'))
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/mainTF/editForm.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminEventDetailView(request, id):
    event = models.Events.objects.get(id=id)
    context = {
        'event': event,
    }
    return render(request, 'admin_panel/mainTF/eventDetail.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminSupportView(request):
    admin_list = User.objects.filter(is_staff=True)
    user_lists = User.objects.filter(is_staff=False)
    sales = User.objects.filter(is_sales=True)
    blogger = User.objects.filter(is_blogger=True)
    bcs_head = User.objects.filter(is_bcs_head=True)
    pcs_head = User.objects.filter(is_pcs_head=True)
    form = forms.AssignToServiceForm()

    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_permission = request.POST.get('user_permission')
        current_user = User.objects.get(email=user_email)
        if 'sales' in request.POST.getlist('user_permission'):
            current_user.is_staff = True
            current_user.is_sales = True
            form = forms.AssignToServiceForm(request.POST)
            if form.is_valid():
                assigned = form.save(commit=False)
                assigned.user = current_user
                for service_id in request.POST.getlist('service'):
                    service = models.Service.objects.get(id=service_id)
                    tracking = models.Tracking.objects.get_or_create(
                        service=service)
                    person = tracking[0].persons
                    tracking[0].persons = f'{person},{current_user.id}'
                    tracking[0].save()
                assigned.save()
                form.save_m2m()
                current_user.save()
        else:
            for item in request.POST.getlist('user_permission'):
                if 'blogger' in request.POST.getlist('user_permission'):
                    current_user.is_staff = True
                    current_user.is_blogger = True
                    current_user.save()
                if 'bcs_head' in request.POST.getlist('user_permission'):
                    current_user.is_staff = True
                    current_user.is_bcs_head = True
                    current_user.save()
                if 'pcs_head' in request.POST.getlist('user_permission'):
                    current_user.is_staff = True
                    current_user.is_pcs_head = True
                    current_user.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'admin_list': admin_list,
        'sales': sales,
        'blogger': blogger,
        'bcs_head': bcs_head,
        'pcs_head': pcs_head,
        'user_lists': user_lists,
        'form': form,
    }
    return render(request, 'admin_panel/mainTF/support.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminProfileView(request, id):
    current_user = models.User.objects.get(id=id)
    context = {
        'current_user': current_user,
    }
    return render(request, 'admin_panel/mainTF/profile.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminSupportEditView(request, id):
    current_user = User.objects.get(id=id)
    admin_list = User.objects.filter(is_staff=True)
    user_lists = User.objects.filter(is_staff=False)
    sales = User.objects.filter(is_sales=True)
    blogger = User.objects.filter(is_blogger=True)
    bcs_head = User.objects.filter(is_bcs_head=True)
    pcs_head = User.objects.filter(is_pcs_head=True)
    try:
        current_service_assigned = models.ServiceAssigned.objects.get(user=current_user)
        form = forms.AssignToServiceForm(instance=current_service_assigned)
    except:
        form = forms.AssignToServiceForm()

    def tracking_delete():
        trackings = models.Tracking.objects.filter(~Q(service__in=request.POST.getlist('service')))
        for tracking in trackings:
            persons = tracking.persons
            persons_list = list(filter(None, persons.split(',')))
            try:
                persons_list.remove(str(current_user.id))
                tracking.persons = ','.join(persons_list)
                tracking.save()
            except:
                pass

    def assigned_delete():
        try:
            service_assigned = models.ServiceAssigned.objects.get(user=current_user)
            service_assigned.delete()
        except:
            pass

    if request.method == 'POST':

        if 'sales' in request.POST.getlist('user_permission'):
            current_user.is_staff = True
            current_user.is_sales = True

            current_user.is_blogger = False
            current_user.is_bcs_head = False
            current_user.is_pcs_head = False
            try:
                form = forms.AssignToServiceForm(request.POST, instance=current_service_assigned)
            except:
                form = forms.AssignToServiceForm(request.POST)

            if form.is_valid():
                assigned = form.save(commit=False)
                assigned.user = current_user

                tracking_delete()

                for service_id in request.POST.getlist('service'):
                    service = models.Service.objects.get(id=service_id)

                    tracking = models.Tracking.objects.get_or_create(
                        service=service)
                    person = tracking[0].persons
                    if str(current_user.id) not in person.split(','):
                        tracking[0].persons = f'{person},{current_user.id}'
                        tracking[0].save()

                assigned.save()
                form.save_m2m()
                current_user.save()
        else:
            for item in request.POST.getlist('user_permission'):
                if 'blogger' in request.POST.getlist('user_permission'):
                    tracking_delete()
                    assigned_delete()
                    current_user.is_sales = False
                    current_user.is_staff = True
                    current_user.is_blogger = True
                    current_user.save()
                if 'bcs_head' in request.POST.getlist('user_permission'):
                    tracking_delete()
                    assigned_delete()
                    current_user.is_sales = False
                    current_user.is_staff = True
                    current_user.is_bcs_head = True
                    current_user.save()
                if 'pcs_head' in request.POST.getlist('user_permission'):
                    tracking_delete()
                    assigned_delete()
                    current_user.is_sales = False
                    current_user.is_staff = True
                    current_user.is_pcs_head = True
                    current_user.save()
                if 'blogger' not in request.POST.getlist('user_permission'):
                    current_user.is_blogger = False
                    current_user.save()
                if 'bcs_head' not in request.POST.getlist('user_permission'):
                    current_user.is_bcs_head = False
                    current_user.save()
                if 'pcs_head' not in request.POST.getlist('user_permission'):
                    current_user.is_pcs_head = False
                    current_user.save()
        return HttpResponseRedirect(reverse('main_admin_support_view'))

    context = {
        'support_edit': 'support_edit',
        'current_user': current_user,
        'admin_list': admin_list,
        'sales': sales,
        'blogger': blogger,
        'bcs_head': bcs_head,
        'pcs_head': pcs_head,
        'user_lists': user_lists,
        'form': form,
    }

    return render(request, 'admin_panel/mainTF/editForm.html', context)


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminSupportDeleteView(request, id):
    current_user = User.objects.get(id=id)
    if current_user.is_superuser:
        pass
    else:
        if current_user.is_sales:
            current_user.is_staff = False
            current_user.is_sales = False
            current_user.save()
            assigned = models.ServiceAssigned.objects.get(user=current_user)
            trackings = models.Tracking.objects.filter(
                persons__icontains=current_user.id)
            for tracking in trackings:
                persons = tracking.persons
                persons_list = list(filter(None, persons.split(',')))
                persons_list.remove(str(current_user.id))
                tracking.persons = ','.join(persons_list)
                tracking.save()
            assigned.delete()
        if current_user.is_blogger:
            current_user.is_staff = False
            current_user.is_blogger = False
            current_user.save()
        if current_user.is_bcs_head:
            current_user.is_staff = False
            current_user.is_bcs_head = False
            current_user.save()
        if current_user.is_pcs_head:
            current_user.is_staff = False
            current_user.is_pcs_head = False
            current_user.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(main_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def mainAdminSupportStuffView(request):
    context = {

    }
    return render(request, 'admin_panel/mainTF/supportStuffView.html', context)


@user_passes_test(main_admin_permission_check_order_page, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def mainAdminTicketsView(request):
    tickets = models.Ticket.objects.all()
    open_tickets = models.Ticket.objects.filter(ticket_status='open')
    close_tickets = models.Ticket.objects.filter(ticket_status='closed')
    context = {
        'tickets': tickets,
        'open_tickets': open_tickets,
        'close_tickets': close_tickets,
    }
    return render(request, 'admin_panel/mainTF/allTickets.html', context)


@user_passes_test(main_admin_permission_check_order_page, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def mainAdminTicketsDetailView(request, id):
    ticket = models.Ticket.objects.get(id=id)
    commentform = forms.TicketCommentForm()
    if request.method == 'POST':
        commentform = forms.TicketCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'ticket': ticket,
        'commentform': commentform,
    }
    return render(request, 'admin_panel/mainTF/ticket_detail.html', context)


@user_passes_test(ticket_admin, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def ticketOpenCloseView(request, id):
    current_ticket = models.Ticket.objects.get(id=id)
    if current_ticket.ticket_status == 'open':
        current_ticket.ticket_status = 'closed'
        current_ticket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    elif current_ticket.ticket_status == 'closed':
        current_ticket.ticket_status = 'open'
        current_ticket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# BCS Admin Section
@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminDashboardView(request):
    service_categories = models.ServiceCategory.objects.filter(
        category_choice='bcs')

    context = {
        'service_categories': service_categories
    }
    return render(request, 'admin_panel/bcsTF/dashboard.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceCategoryView(request):
    categories = models.ServiceCategory.objects.filter(category_choice='bcs')
    form = forms.AddServiceCategoryForm()

    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.category_choice = 'bcs'
            category.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'admin_panel/bcsTF/serviceCategory.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceCategoryDeleteView(request, id):
    current_category = models.ServiceCategory.objects.get(
        id=id, category_choice='bcs')
    current_category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceCategoryEditView(request, id):
    current_category = models.ServiceCategory.objects.get(
        id=id, category_choice='bcs')
    form = forms.AddServiceCategoryForm(instance=current_category)

    if request.method == 'POST':
        form = forms.AddServiceCategoryForm(
            request.POST, instance=current_category)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_services_category'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceView(request):
    form = forms.AddServiceForm()
    sales_persons = models.User.objects.filter(Q(is_staff=True, is_sales=True))
    services = models.Service.objects.filter(category_choice='bcs')

    if request.method == 'POST':
        form = forms.AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.category_choice = 'bcs'
            service.save()
            for sale_id in request.POST.getlist('sales'):
                current_sales = models.User.objects.get(id=sale_id)
                current_assigned = models.ServiceAssigned.objects.get_or_create(
                    user=current_sales)
                current_assigned[0].service.add(service)
                current_assigned[0].save()
                tracking = models.Tracking.objects.get_or_create(
                    service=service)
                person = tracking[0].persons
                tracking[0].persons = f'{person},{sale_id}'
                tracking[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'sales_persons': sales_persons,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/service.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionServiceView(request):
    form = forms.AddSubscriptionServiceForm()
    # sales_persons = models.User.objects.filter(Q(is_staff=True, is_sales=True))
    services = models.SubscriptionServices.objects.filter(
        category_choice='bcs')

    if request.method == 'POST':
        form = forms.AddSubscriptionServiceForm(request.POST, request.FILES)
        # print(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.category_choice = 'bcs'
            service.product_id = request.POST.get('product_id')
            service.save()

            # for sale_id in request.POST.getlist('sales'):
            #     current_sales = models.User.objects.get(id=sale_id)
            #     current_assigned = models.ServiceAssigned.objects.get_or_create(user=current_sales)
            #     current_assigned[0].service.add(service)
            #     current_assigned[0].save()
            #     tracking = models.Tracking.objects.get_or_create(service=service)
            #     person = tracking[0].persons
            #     tracking[0].persons = f'{person},{sale_id}'
            #     tracking[0].save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        # 'sales_persons': sales_persons,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/subscription-service.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionServiceDeleteView(request, id):
    current_service = models.SubscriptionServices.objects.get(id=id)
    current_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceDeleteView(request, id):
    current_service = models.Service.objects.get(id=id)
    current_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionServiceEditView(request, id):
    current_service = models.SubscriptionServices.objects.get(id=id)
    form = forms.AddSubscriptionServiceForm(instance=current_service)

    if request.method == 'POST':
        form = forms.AddSubscriptionServiceForm(
            request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_subscription_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminServiceEditView(request, id):
    current_service = models.Service.objects.get(id=id)
    form = forms.AddServiceForm(instance=current_service)

    if request.method == 'POST':
        form = forms.AddServiceForm(
            request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubServiceView(request):
    form = forms.AddSubServiceForm()
    sub_services = models.SubService.objects.filter(
        service__category_choice='bcs')
    if request.method == 'POST':
        form = forms.AddSubServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'sub_services': sub_services,
    }
    return render(request, 'admin_panel/bcsTF/subService.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubServiceDeleteView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    current_sub_service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubServiceEditView(request, id):
    current_sub_service = models.SubService.objects.get(id=id)
    form = forms.AddSubServiceForm(instance=current_sub_service)

    if request.method == 'POST':
        form = forms.AddSubServiceForm(
            request.POST, instance=current_sub_service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_sub_services'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionFieldView(request):
    sub_services = models.SubscriptionServices.objects.filter(
        category_choice='bcs')

    context = {
        'sub_services': sub_services,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionFields.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionFieldEditView(request, id):
    current_subscription_service = models.SubscriptionServices.objects.get(id=id)
    try:
        current_subscription = models.SubscriptionField.objects.get(subscriptionservice=current_subscription_service)
        form = forms.AddSubscriptionFieldsForm(instance=current_subscription)

        if request.method == 'POST':
            form = forms.AddSubscriptionFieldsForm(
                request.POST, instance=current_subscription)
            if form.is_valid():
                subscription_form = form.save(commit=True)
                subscription_form.subscriptionservice = current_subscription_service
                subscription_form.save()
                return HttpResponseRedirect(reverse('bcs_admin_subscription_fields'))
    except:
        form = forms.AddSubscriptionFieldsForm()

        if request.method == 'POST':
            form = forms.AddSubscriptionFieldsForm(request.POST)
            if form.is_valid():
                subscription_form = form.save(commit=True)
                subscription_form.subscriptionservice = current_subscription_service
                subscription_form.save()
                return HttpResponseRedirect(reverse('bcs_admin_subscription_fields'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionField.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsSubServiceFormView(request):
    form = forms.AddForm()
    form_lists = models.InputFields.objects.all()
    select_choices = list(
        models.SelectChoice.objects.all().values('id', 'choices'))

    # print(request.POST)
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            current_input = form.save()
            # print(current_input.id)
            current_input_field = models.InputFields.objects.get(
                id=current_input.id)
            # print(request.POST.getlist('options'))
            if request.POST.getlist('options'):
                for i in request.POST.getlist('options'):
                    field = models.SelectChoice.objects.get(id=i)
                    # print(field)
                    new_choices = models.SelectChoiceRelation.objects.get_or_create(
                        input_field=current_input_field)
                    new_choices[0].choice_field.add(field)
                    new_choices[0].save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'form': form,
        'form_lists': form_lists,
        'select_choices': select_choices,
    }
    return render(request, 'admin_panel/bcsTF/subserviceForms.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubServiceFormDeleteView(request, id):
    input_field = models.InputFields.objects.get(id=id)
    input_field.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubServiceFormEditView(request, id):
    current_input_field = models.InputFields.objects.get(id=id)
    form = forms.AddForm(instance=current_input_field)

    if request.method == 'POST':
        form = forms.AddForm(request.POST, instance=current_input_field)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('bcs_admin_sub_services_form'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


# @user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
# def bcsAdminReadingListView(request):
#     context = {
#
#     }
#     return render(request, 'admin_panel/bcsTF/readingList.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminRevenueView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/revenue.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionListView(request):
    context = {

    }
    return render(request, 'admin_panel/bcsTF/subscriptionList.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionPack(request):
    form = forms.AddPackageForm()
    services = models.SubscriptionServices.objects.filter(
        category_choice='bcs')

    if request.method == 'POST':
        feature_names = request.POST.getlist('featureName')
        features = request.POST.getlist('feature')
        form = forms.AddPackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.category_choice = 'bcs'
            package.package_id = request.POST.get('package_id')

            package.save()
            for feature_name, feature in zip(feature_names, features):
                package_feature = models.SubscriptionFeatures.objects.get_or_create(package=package,
                                                                                    feature_name=feature_name,
                                                                                    feature=feature)
                package_feature[0].save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'services': services,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionPack.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionPackEdit(request, id):
    current_package = models.SubscriptionBasedPackage.objects.get(id=id)
    package_features = models.SubscriptionFeatures.objects.filter(
        package=current_package)
    form = forms.AddPackageForm(instance=current_package)
    form2 = forms.AddIndividualPackageFeatureForm()
    if request.method == 'POST':
        if 'package-btn' in request.POST:
            form = forms.AddPackageForm(request.POST, instance=current_package)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('bcs_admin_subscription_packages'))
        elif 'feature-btn' in request.POST:
            print(request.POST)
            current_feature = models.SubscriptionFeatures.objects.get(
                id=request.POST.get('feature_id'))
            current_feature.feature_name = request.POST.get('feature_name')
            current_feature.feature = request.POST.get('feature')
            current_feature.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'add-feature-btn' in request.POST:
            form2 = forms.AddIndividualPackageFeatureForm(request.POST)
            if form2.is_valid():
                feature = form2.save(commit=False)
                feature.package = current_package
                feature.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'form': form,
        'form2': form2,
        'package_features': package_features,
    }
    return render(request, 'admin_panel/bcsTF/subscriptionPackEdit.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionPackDelete(request, id):
    current_package = models.SubscriptionBasedPackage.objects.get(id=id)
    current_package.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSubscriptionPackFeatureDelete(request, id):
    current_feature = PackageFeatures.objects.get(id=id)
    current_feature.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminIndividualBusiness(request):
    businesses = models.Business.objects.all()
    context = {
        'businesses': businesses,
    }
    return render(request, 'admin_panel/bcsTF/users.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminIndividualBusinessPanel(request, id):
    current_business = models.Business.objects.get(id=id)
    orders = models.Order.objects.filter(user__business_user__business_id=id)

    context = {
        'current_business': current_business,
        'orders': orders,
    }
    return render(request, 'admin_panel/bcsTF/userPanel.html', context)


# @user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
# def bcsAdminList(request):
#     permission_form = SelectBCSPermissionForm()
#     admin_list = Permissions.objects.filter(admin_type='bcs_admin')
#     super_admin_count = Permissions.objects.filter(admin_type='bcs_admin', is_superadmin=True).count()
#     admin_count = Permissions.objects.filter(admin_type='bcs_admin', is_admin=True).count()
#     moderator_count = Permissions.objects.filter(admin_type='bcs_admin', is_moderator=True).count()
#     editor_count = Permissions.objects.filter(admin_type='bcs_admin', is_editor=True).count()
#     if request.method == 'POST':
#         try:
#             permission_form = SelectBCSPermissionForm(request.POST)
#             admin_type = 'bcs_admin'
#             form = permission_form.save(commit=False)
#             form.admin_type = admin_type
#             form.save()
#             return HttpResponseRedirect(request.META['HTTP_REFERER'])
#         except:
#             return HttpResponseRedirect(request.META['HTTP_REFERER'])
#     context = {
#         'permission_form': permission_form,
#         'admin_list': admin_list,
#         'super_admin_count': super_admin_count,
#         'admin_count': admin_count,
#         'moderator_count': moderator_count,
#         'editor_count': editor_count,
#     }
#     return render(request, 'admin_panel/bcsTF/adminUsers.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminEdit(request, id):
    current_admin = Permissions.objects.get(id=id)
    permission_form = SelectBCSPermissionForm(instance=current_admin)
    if request.method == 'POST':
        permission_form = SelectBCSPermissionForm(
            request.POST, instance=current_admin)
        if permission_form.is_valid():
            permission_form.save()
            return HttpResponseRedirect(reverse('bcs_admin_list'))
    context = {
        'form': permission_form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminProfile(request, id):
    return render(request, 'admin_panel/bcsTF/myProfile.html')


# @user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
# def bcsAdminUserInterest(request):
#     users_list = User.objects.all()
#     interests = Interest.objects.filter(user__is_bcs=True)
#     context = {
#         'users_list': users_list,
#         'interests': interests,
#     }
#     return render(request, 'admin_panel/bcsTF/userInterest.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminSingleUserInterest(request, id):
    selected_interest = Interest.objects.get(id=id)
    form = InterestForm(instance=selected_interest)
    if request.method == 'POST':
        form = InterestForm(request.POST, instance=selected_interest)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bcs_admin_user_interest'))

    context = {
        'selected_interest': selected_interest,
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def adminNotificationsView(request):
    notifications = models.AdminNotification.objects.filter(category_choice='bcs').order_by('-notification_time')

    new_notifications = []
    all_notifications = []
    for notification in notifications:
        if notification.notification_time.date() == datetime.datetime.today().date():
            if notification not in new_notifications:
                new_notifications.append(notification)
        elif notification.notification_time.date() != datetime.datetime.today().date():
            if notification.notification_time.date() < datetime.datetime.today().date():
                if notification not in all_notifications:
                    all_notifications.append(notification)
    context = {
        'notifications': new_notifications,
        'all_notifications': all_notifications,
    }
    for n in all_notifications:
        n.is_read = True
        n.save()
    for n in new_notifications:
        n.is_read = True
        n.save()
    return render(request, 'admin_panel/bcsTF/notifications.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTrainingCategoryView(request):
    form = CourseCategoryCreateForm()
    categories = CourseCategory.objects.filter(course_type='Business')
    if request.method == 'POST':
        form = CourseCategoryCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_type = 'Business'
            course.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'admin_panel/bcsTF/trainingCategory.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTrainingCategoryEditView(request, id):
    current_category = CourseCategory.objects.get(id=id)
    form = CourseCategoryCreateForm(instance=current_category)
    if request.method == 'POST':
        form = CourseCategoryCreateForm(request.POST, instance=current_category)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')

            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('bcs_admin_training_category'))
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/pcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/')
def bcsAdminTrainingCategoryDelete(request, id):
    current_category = CourseCategory.objects.get(id=id)
    current_category.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminTraining(request):
    form = BCSCourseCreateForm()
    courses = BCSCourse.objects.all()
    if request.method == 'POST':
        form = BCSCourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.product_id = request.POST.get('product_id')
            course.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'courses': courses,
    }
    return render(request, 'admin_panel/bcsTF/training.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminTrainingDelete(request, id):
    current_course = BCSCourse.objects.get(id=id)
    current_course.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminTrainingEdit(request, id):
    current_course = BCSCourse.objects.get(id=id)
    form = BCSCourseCreateForm(instance=current_course)

    if request.method == 'POST':
        form = BCSCourseCreateForm(request.POST, instance=current_course)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(reverse('bcs_admin_training'))

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseDetail(request, id):
    course = BCSCourse.objects.get(id=id)
    sections = BCSSection.objects.filter(course=course)
    form = BCSSectionCreateForm()
    form2 = BCSContentCreateForm()
    if request.method == 'POST':
        if 'add_section' in request.POST:
            form = BCSSectionCreateForm(request.POST)
            if form.is_valid():
                section = form.save(commit=False)
                section.course = course
                section.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'add_content' in request.POST:
            form2 = BCSContentCreateForm(request.POST, request.FILES)
            if form2.is_valid():
                content = form2.save(commit=False)
                section_id = int(request.POST.get('section_name'))
                current_section = BCSSection.objects.get(id=section_id)
                content.section = current_section
                content.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'course': course,
        'sections': sections,
        'form': form,
        'form2': form2,
    }
    return render(request, 'admin_panel/bcsTF/courseDetail.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseContentDelete(request, id):
    current_content = BCSContent.objects.get(id=id)
    current_content.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseContentEdit(request, id):
    current_content = BCSContent.objects.get(id=id)
    form = BCSContentCreateForm(instance=current_content)
    if request.method == 'POST':
        form = BCSContentCreateForm(
            request.POST, request.FILES, instance=current_content)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseSectionEdit(request, id):
    current_section = BCSSection.objects.get(id=id)
    form = BCSSectionCreateForm(instance=current_section)
    if request.method == 'POST':
        form = BCSSectionCreateForm(
            request.POST, request.FILES, instance=current_section)
        if form.is_valid():
            form.save()
            next_page = request.POST.get('next', '/')
            if next_page:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/bcsTF/editForm.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseSubscriptionPack(request):
    form = AddCoursePackageForm()
    courses = BCSCourse.objects.all()

    if request.method == 'POST':
        feature_names = request.POST.getlist('featureName')
        features = request.POST.getlist('feature')
        form = AddCoursePackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.package_id = request.POST.get('package_id')
            package.save()
            for feature_name, feature in zip(feature_names, features):
                package_feature = PackageFeatures.objects.get_or_create(package=package,
                                                                        feature_name=feature_name,
                                                                        feature=feature)
                package_feature[0].save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
        'courses': courses,
    }
    return render(request, 'admin_panel/bcsTF/coursePack.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseSubscriptionPackEdit(request, id):
    current_package = CoursePackage.objects.get(id=id)
    package_features = PackageFeatures.objects.filter(
        package=current_package)
    form = AddCoursePackageForm(instance=current_package)
    form2 = AddCourseIndividualPackageFeatureForm()
    if request.method == 'POST':
        if 'package-btn' in request.POST:
            form = AddCoursePackageForm(request.POST, instance=current_package)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('bcs_admin_course_packages'))
        elif 'feature-btn' in request.POST:
            # print(request.POST)
            current_feature = PackageFeatures.objects.get(
                id=request.POST.get('feature_id'))
            current_feature.feature_name = request.POST.get('feature_name')
            current_feature.feature = request.POST.get('feature')
            current_feature.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        elif 'add-feature-btn' in request.POST:
            form2 = forms.AddIndividualPackageFeatureForm(request.POST)
            if form2.is_valid():
                feature = form2.save(commit=False)
                feature.package = current_package
                feature.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])

    context = {
        'form': form,
        'form2': form2,
        'package_features': package_features,
    }
    return render(request, 'admin_panel/bcsTF/coursePackEdit.html', context)


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseSubscriptionPackDelete(request, id):
    current_package = CoursePackage.objects.get(id=id)
    current_package.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check, login_url='/accounts/login/', redirect_field_name='/account/profile/')
def bcsAdminCourseSubscriptionPackFeatureDelete(request, id):
    current_feature = models.SubscriptionFeatures.objects.get(id=id)
    current_feature.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminQuotationsView(request):
    if request.user.is_sales:
        orders = models.Order.objects.filter(
            Q(orderstaff_order__staff=request.user) & Q(Q(order_status='new') | Q(order_status='attending')
                                                        | Q(order_status='assigned'))).order_by('-order_date')
        context = {
            'orders': orders.filter(category_choice='bcs'),
            'message': 'Quotations',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)
    else:
        orders = models.Order.objects.filter(
            Q(category_choice='bcs') & Q(Q(order_status='new') | Q(order_status='attending')
                                         | Q(order_status='assigned'))).order_by('-order_date')
        context = {
            'orders': orders,
            'message': 'Quotations',
            'admin': 'admin',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrdersView(request):
    if request.user.is_sales:
        orders = models.Order.objects.filter(
            Q(orderstaff_order__staff=request.user) & ~Q(
                Q(order_status='new') | Q(order_status='attending')
                | Q(order_status='agreed_to_quotation') | Q(order_status='agreed_to_nda_nca')
                | Q(order_status='assigned'))).order_by(
            '-order_date')
        context = {
            'orders': orders,
            'message': 'Orders',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)
    else:
        orders = models.Order.objects.filter(
            Q(category_choice='bcs') & ~Q(
                Q(order_status='new') | Q(order_status='attending')
                | Q(order_status='agreed_to_quotation') | Q(order_status='agreed_to_nda_nca')
                | Q(order_status='assigned'))).order_by(
            '-order_date')
        context = {
            'orders': orders,
            'message': 'Orders',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminSubscriptionView(request):
    if request.user.is_sales:
        orders = models.SubscriptionOrder.objects.filter(category_choice='bcs').order_by('-create_time')
        context = {
            'orders': orders,
            'message': 'Subscriptions',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)
    else:
        orders = models.SubscriptionOrder.objects.filter(category_choice='bcs').order_by('-create_time')
        context = {
            'orders': orders,
            'message': 'Subscriptions',
        }
        return render(request, 'admin_panel/bcsTF/orders.html', context)


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminNewOrdersView(request):
    if request.user.is_superuser:
        service_category = models.ServiceCategory.objects.filter(category_choice='bcs')
        user_lists = models.User.objects.all()
        services = models.Service.objects.filter(category_choice='bcs')
        order_price_form = forms.OrderPriceForm()

        if request.method == 'POST':
            data_list = request.POST
            file_list = request.FILES
            current_customer = models.User.objects.get(
                email=data_list.get('customer'))

            current_service = get_object_or_404(
                models.Service, service_title=data_list['service_name'])

            for data in data_list:
                if data != 'csrfmiddlewaretoken' and data != 'service_name' \
                        and data != 'customer' and data != 'price' \
                        and data != 'currency' and data != 'payment_method':
                    current_input = models.SubServiceInput.objects.get(id=data)
                    input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                            inputinfo=data_list[data])
                    input_data.save()
                    order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                               service=current_service, category_choice='bcs')

                    order[0].subserviceinput.add(input_data)
            for files in file_list:
                current_input = models.SubServiceInput.objects.get(id=files)
                myfile = file_list[files]
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                        inputinfo=uploaded_file_url)
                input_data.save()
                order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                           service=current_service, category_choice='bcs')

                order[0].subserviceinput.add(input_data)

            order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                       service=current_service, category_choice='bcs')
            # print(order)
            if not order[0].orderstaff_order.all().exists():
                tracking = models.Tracking.objects.get(service=current_service)
                persons = tracking.persons
                persons_list = list(filter(None, persons.split(',')))
                person = persons_list.pop(0)
                persons_list.append(person)
                tracking.persons = ','.join(persons_list)
                tracking.save()
                current_staff = models.User.objects.get(id=person)
                order_staff = models.OrderStaff.objects.create(
                    staff=current_staff, order=order[0])
                order_staff.save()
            order[0].order_status = 'on_progress'
            order[0].save()

            order_price = models.OrderPrice.objects.get(order=order[0])
            order_quotation = models.Quotation.objects.get(order=order[0])
            order_price.price = data_list.get('price')
            order_price.payment_method = data_list.get('payment_method')
            order_price.currency = data_list.get('currency')
            order_quotation.agree_to_quotation = 'agree'
            order_quotation.agree_to_nda_nca = 'agree'
            order_quotation.save()
            order_price.save()
            return HttpResponseRedirect(reverse('bcs_admin_orders'))
    else:
        service_category = models.ServiceCategory.objects.filter(category_choice='bcs',
                                                                 service_category__service_assigned_service__user=request.user)
        user_lists = models.User.objects.filter(is_bcs=True)
        services = models.Service.objects.filter(
            category_choice='bcs', service_assigned_service__user=request.user)

        order_price_form = forms.OrderPriceForm()

        if request.method == 'POST':
            data_list = request.POST
            file_list = request.FILES
            current_customer = models.User.objects.get(
                email=data_list.get('customer'))

            current_service = get_object_or_404(
                models.Service, service_title=data_list['service_name'])

            for data in data_list:
                if data != 'csrfmiddlewaretoken' and data != 'service_name' and data != 'customer':
                    current_input = models.SubServiceInput.objects.get(id=data)
                    input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                            inputinfo=data_list[data])
                    input_data.save()
                    order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                               service=current_service, category_choice='bcs')

                    order[0].subserviceinput.add(input_data)

            for files in file_list:
                current_input = models.SubServiceInput.objects.get(id=files)
                myfile = file_list[files]
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                input_data = models.UserSubserviceInput(user=current_customer, inputfield=current_input,
                                                        inputinfo=uploaded_file_url)
                input_data.save()
                order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                           service=current_service, category_choice='bcs')

                order[0].subserviceinput.add(input_data)

            order = models.Order.objects.get_or_create(user=current_customer, order_status='new',
                                                       service=current_service, category_choice='bcs')

            order[0].order_status = 'on_progress'
            order[0].save()
            order_staff = models.OrderStaff.objects.get_or_create(
                staff=request.user, order=order[0])
            order_staff[0].save()
            order_price = models.OrderPrice.objects.get(order=order[0])
            order_quotation = models.Quotation.objects.get(order=order[0])
            order_price.price = data_list.get('price')
            order_price.payment_method = data_list.get('payment_method')
            order_price.currency = data_list.get('currency')
            order_quotation.agree_to_quotation = 'agree'
            order_quotation.agree_to_nda_nca = 'agree'
            order_quotation.save()
            order_price.save()
            return HttpResponseRedirect(reverse('bcs_admin_orders'))
    context = {
        'service_category': service_category,
        'services': services,
        'user_lists': user_lists,
        'order_price_form': order_price_form,
        'services_headings': list(services.values_list('service_title', flat=True)),
    }
    return render(request, 'admin_panel/bcsTF/create_user_services.html', context)


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrdersDetailView(request, id):
    if request.user.is_superuser or request.user.is_bcs_head:
        current_order = models.Order.objects.get(id=id)
        current_price = models.OrderPrice.objects.get(order=current_order)
        current_quotation = models.Quotation.objects.get(order=current_order)
        form = forms.OrderPriceForm(instance=current_price)
        quotation_form = forms.QuotationForm(instance=current_quotation)
        if request.method == 'POST':
            form = forms.OrderPriceForm(request.POST, instance=current_price)
            quotation_form = forms.QuotationForm(
                files=request.FILES, data=request.POST, instance=current_quotation)
            if form.is_valid():
                current_order.order_status = 'on_progress'
                current_order.save()
                # new_staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
                form.save()

                send_mail(
                    f'Price Set for order ID: {current_order.id}',
                    f'Price: {current_order.orderprice_order.price} {current_order.orderprice_order.currency} '
                    f'has been set for your order ID: {current_order.id} '
                    f'Please visit: https://main.techforing.com/bcs_user_order_details/{current_order.id}/ for more info',
                    'admin@techforing.com',
                    [current_order.user.business_user.business.email],
                    fail_silently=False,
                )
                notification = models.Notification.objects.create(
                    category_choice=current_order.user.business_user.business.company_name,
                    notification=f'Price Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
                                 f'target="_blank" class="btn '
                                 f'btn-success">Visit Now</a>',
                    notification_time=timezone.now())
                notification.save()

                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            if quotation_form.is_valid():
                current_order.order_status = 'attending'
                current_order.save()
                quotation_form.save()
                send_mail(
                    f'Quotation Set for order ID: {current_order.id}',
                    f'NDA: https://main.techforing.com/{current_order.quotation_order.nda.url} '
                    f'NCA: https://main.techforing.com/{current_order.quotation_order.nca.url} '
                    f'has been set for your order ID: {current_order.id} '
                    f'Please sign them and submit a copy to https://main.techforing.com/bcs_user_order_details/{current_order.id}/ '
                    f'Please visit: https://main.techforing.com/bcs_user_order_details/{current_order.id}/ for more info',
                    'admin@techforing.com',
                    [current_order.user.business_user.business.email],
                    fail_silently=False,
                )
                notification = models.Notification.objects.create(
                    category_choice=current_order.user.business_user.business.company_name,
                    notification=f'Quotation Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
                                 f'target="_blank" class="btn '
                                 f'btn-success">Visit Now</a>',
                    notification_time=timezone.now())
                notification.save()
                try:
                    current_quotation_agreement = models.QuotationAgreement.objects.get(quotation=current_quotation)
                    current_quotation_agreement.delete()
                except:
                    pass
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        context = {
            'current_order': current_order,
            'form': form,
            'quotation_form': quotation_form,
        }
        return render(request, 'admin_panel/bcsTF/order_detail.html', context)
    else:
        try:
            current_order = models.Order.objects.get(
                id=id, orderstaff_order__staff=request.user)
            current_quotation = models.Quotation.objects.get(
                order=current_order)
            current_price = models.OrderPrice.objects.get(order=current_order)
            form = forms.OrderPriceForm(instance=current_price)
            quotation_form = forms.QuotationForm(instance=current_quotation)
            if request.method == 'POST':
                form = forms.OrderPriceForm(
                    request.POST, instance=current_price)
                quotation_form = forms.QuotationForm(
                    files=request.FILES, data=request.POST, instance=current_quotation)
                if form.is_valid():
                    current_order.order_status = 'on_progress'
                    # new_staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
                    form.save()
                    send_mail(
                        f'Price Set for order ID: {current_order.id}',
                        f'Price: {current_order.orderprice_order.price} {current_order.orderprice_order.currency} '
                        f'has been set for your order ID: {current_order.id} '
                        f'Please visit: https://main.techforing.com/bcs_user_order_details/{current_order.id}/ for more info',
                        'admin@techforing.com',
                        [current_order.user.business_user.business.email],
                        fail_silently=False,
                    )
                    notification = models.Notification.objects.create(
                        category_choice=current_order.user.business_user.business.company_name,
                        notification=f'Price Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
                                     f'target="_blank" class="btn '
                                     f'btn-success">Visit Now</a>',
                        notification_time=timezone.now())
                    notification.save()
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
                if quotation_form.is_valid():
                    current_order.order_status = 'attending'
                    current_order.save()
                    # new_staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
                    quotation_form.save()
                    send_mail(
                        f'Quotation Set for order ID: {current_order.id}',
                        f'NDA: https://main.techforing.com/{current_order.quotation_order.nda.url} '
                        f'NCA: https://main.techforing.com/{current_order.quotation_order.nca.url} '
                        f'has been set for your order ID: {current_order.id} '
                        f'Please sign them and submit a copy to https://main.techforing.com/bcs_user_order_details/{current_order.id}/ '
                        f'Please visit: https://main.techforing.com/bcs_user_order_details/{current_order.id}/ for more info',
                        'admin@techforing.com',
                        [current_order.user.business_user.business.email],
                        fail_silently=False,
                    )
                    notification = models.Notification.objects.create(
                        category_choice=current_order.user.business_user.business.company_name,
                        notification=f'Quotation Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
                                     f'target="_blank" class="btn '
                                     f'btn-success">Visit Now</a>',
                        notification_time=timezone.now())
                    notification.save()
                    try:
                        current_quotation_agreement = models.QuotationAgreement.objects.get(quotation=current_quotation)
                        current_quotation_agreement.delete()
                    except:
                        pass
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            context = {
                'current_order': current_order,
                'form': form,
                'quotation_form': quotation_form,
            }
            return render(request, 'admin_panel/bcsTF/order_detail.html', context)
        except:
            return HttpResponse("You don't have permission to view this page!")


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminSubscriptionDetailView(request, id):
    if request.user.is_superuser or request.user.is_bcs_head:
        current_order = models.SubscriptionOrder.objects.get(id=id)

        # send_mail(
        #     f'Price Set for order ID: {current_order.id}',
        #     f'has been set for your order ID: {current_order.id} '
        #     f'Please visit: https://main.techforing.com/bcs_user_subscription_details/{current_order.id}/ for more info',
        #     'admin@techforing.com',
        #     [current_order.user.business_user.business.email],
        #     fail_silently=False,
        # )
        # notification = models.Notification.objects.create(category_choice=current_order.user.business_user.business.company_name,
        #                                                   notification=f'Price Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
        #                                                                f'target="_blank" class="btn '
        #                                                                f'btn-success">Visit Now</a>',
        #                                                   notification_time=timezone.now())
        # notification.save()

        context = {
            'current_order': current_order,
        }
        return render(request, 'admin_panel/bcsTF/subscription_detail.html', context)
    else:
        try:
            current_order = models.SubscriptionOrder.objects.get(id=id)

            # send_mail(
            #     f'Price Set for order ID: {current_order.id}',
            #     f'has been set for your order ID: {current_order.id} '
            #     f'Please visit: https://main.techforing.com/bcs_user_subscription_details/{current_order.id}/ for more info',
            #     'admin@techforing.com',
            #     [current_order.user.business_user.business.email],
            #     fail_silently=False,
            # )
            # notification = models.Notification.objects.create(
            #     category_choice=current_order.user.business_user.business.company_name,
            #     notification=f'Price Set for Order ID: {current_order.id} <a href="https://main.techforing.com/bcs_user_order_details/{current_order.id}/" '
            #                  f'target="_blank" class="btn '
            #                  f'btn-success">Visit Now</a>',
            #     notification_time=timezone.now())
            # notification.save()

            context = {
                'current_order': current_order,
            }
            return render(request, 'admin_panel/bcsTF/subscription_detail.html', context)
        except:
            return HttpResponse("You don't have permission to view this page!")


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrderNewView(request, id):
    # print(request.user.is_staff)
    try:
        # current_order = models.Order.objects.get(
        #     Q(id=id, orderstaff_order__staff=request.user, orderstaff_order__staff__is_staff=True,
        #       orderstaff_order__staff__is_sales_head=True) | Q(id=id, orderstaff_order__staff__is_superuser=True) | Q(
        #         id=id, orderstaff_order__staff__is_staff=True, orderstaff_order__staff__is_sales_head=True))
        if request.user.is_superuser or request.user.is_bcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)
        # print(request.user.is_bcs_head)
        current_order.order_status = 'new'
        current_order.price = 0
        # if current_order.orderstaff_order.exists():
        #     for staff in current_order.orderstaff_order.all():
        #         staff.delete()
        current_order.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrderAttendingView(request, id):
    try:
        if request.user.is_superuser or request.user.is_bcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'attending'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrderCompletedView(request, id):
    try:
        if request.user.is_superuser or request.user.is_bcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'completed'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminOrderCanceledView(request, id):
    try:
        if request.user.is_superuser or request.user.is_bcs_head:
            current_order = models.Order.objects.get(id=id)
        else:
            current_order = models.Order.objects.get(id=id, orderstaff_order__staff=request.user,
                                                     orderstaff_order__staff__is_staff=True,
                                                     orderstaff_order__staff__is_sales=True)

        current_order.order_status = 'canceled'
        current_order.save()
        # staff = models.OrderStaff.objects.get_or_create(order=current_order, staff=request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminTicketsView(request):
    tickets = models.Ticket.objects.filter(category_choice='bcs').order_by('-ticket_date')
    context = {
        'tickets': tickets,
    }
    return render(request, 'admin_panel/bcsTF/allTickets.html', context)


@user_passes_test(bcs_admin_permission_check_order, login_url='/accounts/login/',
                  redirect_field_name='/account/profile/')
def bcsAdminTicketsDetailView(request, id):
    ticket = models.Ticket.objects.get(id=id)
    commentform = forms.TicketCommentForm()
    if request.method == 'POST':
        commentform = forms.TicketCommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()
            notification = models.Notification.objects.create(
                category_choice=ticket.user.business_user.business.company_name,
                notification=f'New Reply on Ticket. <a href="https://main.techforing.com/ticket_details/{ticket.id}/" '
                             f'target="_blank" class="btn '
                             f'btn-success">Visit Now</a>',
                notification_time=timezone.now())
            notification.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    context = {
        'ticket': ticket,
        'commentform': commentform,
    }
    return render(request, 'admin_panel/bcsTF/ticket_detail.html', context)
