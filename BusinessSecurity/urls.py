from django.urls import path
from BusinessSecurity import views

# app_name = 'bcs_app'

urlpatterns = [
    path('', views.indexView, name='home'),

    path('about_us/', views.aboutUsView, name='aboutus'),
    path('enterprise_cybersecurity/', views.enterpriseCyberSecurityView,
         name='enterprise_cybersecurity'),
    path('vulnerability_assessment/', views.vulnerabilityAssessmentView,
         name='vulnerability_assessment'),
    path('red_team_penetration_testing/', views.redTeamPenetrationTestingView,
         name='red_team_penetration_testing'),
    path('cybersecurity_risk_assessment/', views.cybersecurityRiskAssessmentView,
         name='cybersecurity_risk_assessment'),
    path('incident_response_service/', views.incidentResponseServiceView,
         name='incident_response_services'),
    path('hack_recovery_service/', views.hackRecoveryServiceView,
         name='hack_recovery_services'),
    path('best_malware_removal/', views.bestMalwareRemovalView,
         name='best_malware_removal'),
    path('digital_forensic_investigation/', views.digitalForensicInvestigationView,
         name='digital_forensic_investigation'),
    path('compliance_consulting/', views.complianceConsultingView,
         name='compliance_consulting'),
    path('iso27001/', views.ISO27001View, name='iso27001'),
    path('pci_dss_compliance/', views.pciDssComplianceView,
         name='pci_dss_compliance'),
    path('gdpr_compliance/', views.gdprComplianceView, name='gdpr_compliance'),
    path('hippa_compliance_consulting/', views.hippaComplianceConsultingView,
         name='hippa_compliance_consulting'),
    path('small_business_cybersecurity/', views.smallBusinessCybersecurityView,
         name='small_business_cybersecurity'),
    path('managed_cybersecurity_service/', views.managedCybersecurityServiceView,
         name='managed_cybersecurity_service'),
    path('plug_and_play_cyber_security/', views.plugAndPlayCyberCecurityView,
         name='plug_and_play_cyber_security'),

    path('leader/', views.leaderView, name='leader'),
    path('testimonial/', views.testimonialView, name='testimonial'),
    path('partner/', views.partnerView, name='partner'),
    path('partner_faq/', views.partnerFaqView, name='partner_faq'),
    path('franchise/', views.franchiseView, name='franchise'),
    path('franchise_faq/', views.franchiseFaqView, name='franchise_faq'),
    path('investor/', views.investorView, name='investor'),
    path('career/', views.careerView, name='career'),
    path('events/', views.eventsView, name='events'),
    path('policy/', views.policyView, name='policy'),
    path('terms/', views.termsView, name='terms'),

    path('bcs_form/', views.BCSFormView, name='bcs_form'),
    path('bpartner/', views.bPartnerView, name='bpartner'),

    path('trust/', views.trustView, name='trust'),
    path('findus/', views.findUsView, name='findus'),

    path('get_start/', views.getStartView, name='get_start'),

    path('appoinment/', views.appoinmentView, name='appoinment'),
    path('open_tickets/', views.openTicketView, name='open_tickets'),
    path('ticket_details/', views.ticketDetailView, name='ticket_details'),
    path('ticket_details/<id>/', views.ticketDetailView, name='ticket_details'),
    # main admin panel

    path('main_admin_dashboard/', views.mainAdminDashboardView,
         name='main_admin_dashboard'),
    path('main_admin_profile/', views.mainAdminProfileView,
         name='main_admin_profile'),
    path('main_admin_quotations/', views.mainAdminQuotationsView,
         name='main_admin_quotations'),
    path('main_admin_orders/', views.mainAdminOrdersView, name='main_admin_orders'),
    path('main_admin_order_detail/', views.mainAdminOrdersDetailView,
         name='main_admin_order_detail'),
    path('main_admin_order_detail/<id>/',
         views.mainAdminOrdersDetailView, name='main_admin_order_detail'),
    path('main_admin_notification/', views.mainAdminNotificationView,
         name='main_admin_notification'),
    path('main_admin_notification_delete/', views.mainAdminNotificationDeleteView,
         name='main_admin_notification_delete'),
    path('main_admin_notification_delete/<id>/', views.mainAdminNotificationDeleteView,
         name='main_admin_notification_delete'),
    path('main_admin_events/', views.mainAdminEventsView, name='main_admin_events'),
    path('main_admin_events_delete/<id>', views.mainAdminEventsDeleteView,
         name='main_admin_events_delete'),
    path('main_admin_events_edit/<id>', views.mainAdminEventsEditView,
         name='main_admin_events_edit'),
    path('main_admin_event_detail/<id>', views.mainAdminEventDetailView,
         name='main_admin_event_detail'),
    path('main_admin_support_view/', views.mainAdminSupportView,
         name='main_admin_support_view'),
    path('main_admin_user/', views.mainAdminProfileView, name='main_admin_user'),
    path('main_admin_user/<id>/', views.mainAdminProfileView, name='main_admin_user'),
    path('main_admin_user_edit/', views.mainAdminSupportEditView, name='main_admin_user_edit'),
    path('main_admin_user_edit/<id>/', views.mainAdminSupportEditView, name='main_admin_user_edit'),
    path('main_admin_support_delete_view/<id>/', views.mainAdminSupportDeleteView,
         name='main_admin_support_delete_view'),
    path('main_admin_stuff_view/', views.mainAdminSupportStuffView,
         name='main_admin_stuff_view'),
    path('main_admin_all_tickets/', views.mainAdminTicketsView,
         name='main_admin_all_tickets'),
    path('main_admin_tickets_detail/', views.mainAdminTicketsDetailView,
         name='main_admin_tickets_detail'),
    path('main_admin_tickets_detail/<id>',
         views.mainAdminTicketsDetailView, name='main_admin_tickets_detail'),
    path('tickets_status_change/', views.ticketOpenCloseView,
         name='tickets_status_change'),
    path('tickets_status_change/<id>/',
         views.ticketOpenCloseView, name='tickets_status_change'),

    # bcs user panel
    path('bcs_user_dashboard/', views.userDashboardView, name='bcs_user_dashboard'),
    path('create_business/', views.createBusinessView, name='create_business'),
    path('bcs_user_services/', views.userServicesView, name='bcs_user_services'),
    path('bcs_user_course_details/', views.bcsUserCourseDetail, name='bcs_user_course_details'),
    path('bcs_user_course_details/<id>/', views.bcsUserCourseDetail, name='bcs_user_course_details'),
    path('bcs_user_course_payment/', views.bcsUserCoursePayment, name='bcs_user_course_payment'),
    path('bcs_user_course_payment/<id>/', views.bcsUserCoursePayment, name='bcs_user_course_payment'),
    path('bcs_user_quotations_history/', views.userQuotationsHistoryView,
         name='bcs_user_quotations_history'),
    path('bcs_user_order_history/', views.userOrderHistoryView,
         name='bcs_user_order_history'),
    path('bcs_user_order_details/', views.userOrderDetailsView,
         name='bcs_user_order_details'),
    path('bcs_user_order_details/<id>/',
         views.userOrderDetailsView, name='bcs_user_order_details'),

    path('bcs_user_accept_quotation/', views.quotationAcceptView, name='bcs_user_accept_quotation'),
    path('bcs_user_accept_quotation/<id>/', views.quotationAcceptView, name='bcs_user_accept_quotation'),
    path('bcs_user_accept_nda_nca/', views.ndaNcaAcceptView, name='bcs_user_accept_nda_nca'),
    path('bcs_user_accept_nda_nca/<id>/', views.ndaNcaAcceptView, name='bcs_user_accept_nda_nca'),
    path('bcs_user_order_reject/', views.orderRejectView, name='bcs_user_order_reject'),
    path('bcs_user_order_reject/<id>/', views.orderRejectView, name='bcs_user_order_reject'),

    path('bcs_user_subscriptions/', views.userSubscriptionsView,
         name='bcs_user_subscriptions'),
    path('bcs_subscription_payment/', views.subscriptionPayment,
         name='bcs_subscription_payment'),
    path('bcs_subscription_payment/<id>/', views.subscriptionPayment,
         name='bcs_subscription_payment'),
    path('bcs_subscription_cancel/<id>/', views.subscriptionCancelView, name='bcs_subscription_cancel'),
    path('bcs_subscription_cancel/', views.subscriptionCancelView, name='bcs_subscription_cancel'),
    path('bcs_user_events/', views.userEventsView, name='bcs_user_events'),
    path('bcs_user_event_register/<id>/',
         views.userEventRegisterView, name='bcs_user_event_register'),
    path('bcs_user_notifications/', views.userNotificationsView,
         name='bcs_user_notifications'),
    path('bcs_user_settings/', views.userSettingsView, name='bcs_user_settings'),
    path('bcs_user_my_team/', views.bcsUserMyTeamView, name='bcs_user_my_team'),
    path('bcs_user_team_service_form/<id>/', views.bcsUserTeamFormView, name='bcs_user_team_service_form'),
    path('bcs_user_my_team_user/', views.bcsUserMyTeamProfileView,
         name='bcs_user_my_team_user'),
    path('bcs_user_my_team_user/<id>/',
         views.bcsUserMyTeamProfileView, name='bcs_user_my_team_user'),
    path('bcs_user_team_member_delete/', views.bcsUserTeamMemberDeleteView,
         name='bcs_user_team_member_delete'),
    path('bcs_user_team_member_delete/<id>/',
         views.bcsUserTeamMemberDeleteView, name='bcs_user_team_member_delete'),
    path('employee_training_program/', views.employeeTrainingProgramView,
         name='employee_training_program'),

    path('bcs_appointment/', views.bcsAppointmentView, name='bcs_appointment'),

    # bcs admin panel
    path('bcs_admin_dashboard/', views.bcsAdminDashboardView,
         name='bcs_admin_dashboard'),
    path('bcs_admin_revenue/', views.bcsAdminRevenueView, name='bcs_admin_revenue'),

    # path('bcs_admin_reading_list/', views.bcsAdminReadingListView, name='bcs_admin_reading_list'),
    path('bcs_admin_services_category/', views.bcsAdminServiceCategoryView,
         name='bcs_admin_services_category'),
    path('bcs_admin_services_category_delete/<id>/', views.bcsAdminServiceCategoryDeleteView,
         name='bcs_admin_services_category_delete'),
    path('bcs_admin_services_category_edit/<id>/', views.bcsAdminServiceCategoryEditView,
         name='bcs_admin_services_category_edit'),
    path('bcs_admin_services/', views.bcsAdminServiceView,
         name='bcs_admin_services'),
    path('bcs_admin_subscription_services/', views.bcsAdminSubscriptionServiceView,
         name='bcs_admin_subscription_services'),
    path('bcs_admin_subscription_services_delete/<id>/',
         views.bcsAdminSubscriptionServiceDeleteView, name='bcs_admin_subscription_services_delete'),
    path('bcs_admin_services_delete/<id>/',
         views.bcsAdminServiceDeleteView, name='bcs_admin_services_delete'),
    path('bcs_admin_subscription_services_edit/<id>/',
         views.bcsAdminSubscriptionServiceEditView, name='bcs_admin_subscription_services_edit'),
    path('bcs_admin_services_edit/<id>/',
         views.bcsAdminServiceEditView, name='bcs_admin_services_edit'),
    path('bcs_admin_sub_services/', views.bcsAdminSubServiceView,
         name='bcs_admin_sub_services'),
    path('bcs_admin_sub_services_delete/<id>/', views.bcsAdminSubServiceDeleteView,
         name='bcs_admin_sub_services_delete'),
    path('bcs_admin_sub_services_edit/<id>/',
         views.bcsAdminSubServiceEditView, name='bcs_admin_sub_services_edit'),
    path('bcs_admin_sub_services_form/', views.bcsSubServiceFormView,
         name='bcs_admin_sub_services_form'),
    path('bcs_admin_sub_services_form_delete/<id>/', views.bcsAdminSubServiceFormDeleteView,
         name='bcs_admin_sub_services_form_delete'),
    path('bcs_admin_sub_services_form_edit/<id>/', views.bcsAdminSubServiceFormEditView,
         name='bcs_admin_sub_services_form_edit'),
    path('bcs_admin_subscription_fields/', views.bcsAdminSubscriptionFieldView,
         name='bcs_admin_subscription_fields'),
    path('bcs_admin_subscription_fields_edit/<id>/',
        views.bcsAdminSubscriptionFieldEditView, name='bcs_admin_subscription_fields_edit'),

    # bcs admin panel
    path('bcs_admin_subscription_packages/', views.bcsAdminSubscriptionPack,
         name='bcs_admin_subscription_packages'),
    path('bcs_admin_subscription_packages_delete/', views.bcsAdminSubscriptionPackDelete,
         name='bcs_admin_subscription_packages_delete'),
    path('bcs_admin_subscription_packages_delete/<id>/', views.bcsAdminSubscriptionPackDelete,
         name='bcs_admin_subscription_packages_delete'),
    path('bcs_admin_subscription_packages_edit/', views.bcsAdminSubscriptionPackEdit,
         name='bcs_admin_subscription_packages_edit'),
    path('bcs_admin_subscription_packages_edit/<id>/', views.bcsAdminSubscriptionPackEdit,
         name='bcs_admin_subscription_packages_edit'),
    path('bcs_admin_subscription_packages_feature_delete/', views.bcsAdminSubscriptionPackFeatureDelete,
         name='bcs_admin_subscription_packages_feature_delete'),
    path('bcs_admin_subscription_packages_feature_delete/<id>/', views.bcsAdminSubscriptionPackFeatureDelete,
         name='bcs_admin_subscription_packages_feature_delete'),
    path('bcs_admin_individual_business/', views.bcsAdminIndividualBusiness,
         name='bcs_admin_individual_business'),
    path('bcs_admin_individual_business_panel/<id>/', views.bcsAdminIndividualBusinessPanel,
         name='bcs_admin_individual_business_panel'),
    # path('bcs_admin_list/', views.bcsAdminList, name='bcs_admin_list'),
    path('bcs_admin_edit/<id>/', views.bcsAdminEdit, name='bcs_admin_edit'),
    path('bcs_admin_profile/<id>/',
         views.bcsAdminProfile, name='bcs_admin_profile'),
    # path('bcs_admin_user_interest/', views.bcsAdminUserInterest, name='bcs_admin_user_interest'),
    path('bcs_admin_single_user_interest/<id>/', views.bcsAdminSingleUserInterest,
         name='bcs_admin_single_user_interest'),
    path('bcs_admin_notifications/', views.adminNotificationsView,
         name='bcs_admin_notifications'),
    path('bcs_admin_training_category/', views.bcsAdminTrainingCategoryView, name='bcs_admin_training_category'),
    path('bcs_admin_training_category_edit/', views.bcsAdminTrainingCategoryEditView,
         name='bcs_admin_training_category_edit'),
    path('bcs_admin_training_category_edit/<id>/', views.bcsAdminTrainingCategoryEditView,
         name='bcs_admin_training_category_edit'),
    path('bcs_admin_training_category_delete/', views.bcsAdminTrainingCategoryDelete,
         name='bcs_admin_training_category_delete'),
    path('bcs_admin_training_category_delete/<id>/', views.bcsAdminTrainingCategoryDelete,
         name='bcs_admin_training_category_delete'),
    path('bcs_admin_training/', views.bcsAdminTraining, name='bcs_admin_training'),
    path('bcs_admin_training_delete/<id>/',
         views.bcsAdminTrainingDelete, name='bcs_admin_training_delete'),
    path('bcs_admin_training_edit/<id>/',
         views.bcsAdminTrainingEdit, name='bcs_admin_training_edit'),
    path('bcs_admin_course_detail/<id>/',
         views.bcsAdminCourseDetail, name='bcs_admin_course_detail'),
    path('bcs_admin_course_section_edit/<id>/',
         views.bcsAdminCourseSectionEdit, name='bcs_admin_course_section_edit'),
    path('bcs_admin_course_content_delete/<id>/', views.bcsAdminCourseContentDelete,
         name='bcs_admin_course_content_delete'),
    path('bcs_admin_course_content_edit/<id>/', views.bcsAdminCourseContentEdit,
         name='bcs_admin_course_content_edit'),

    path('bcs_admin_course_packages/', views.bcsAdminCourseSubscriptionPack,
         name='bcs_admin_course_packages'),
    path('bcs_admin_course_packages_delete/', views.bcsAdminCourseSubscriptionPackDelete,
         name='bcs_admin_course_packages_delete'),
    path('bcs_admin_course_packages_delete/<id>/', views.bcsAdminCourseSubscriptionPackDelete,
         name='bcs_admin_course_packages_delete'),
    path('bcs_admin_course_packages_edit/', views.bcsAdminCourseSubscriptionPackEdit,
         name='bcs_admin_course_packages_edit'),
    path('bcs_admin_course_packages_edit/<id>/', views.bcsAdminCourseSubscriptionPackEdit,
         name='bcs_admin_course_packages_edit'),
    path('bcs_admin_course_packages_feature_delete/', views.bcsAdminCourseSubscriptionPackFeatureDelete,
         name='bcs_admin_course_packages_feature_delete'),
    path('bcs_admin_course_packages_feature_delete/<id>/', views.bcsAdminCourseSubscriptionPackFeatureDelete,
         name='bcs_admin_course_packages_feature_delete'),

    path('bcs_admin_quotations/', views.bcsAdminQuotationsView,
         name='bcs_admin_quotations'),
    path('bcs_admin_orders/', views.bcsAdminOrdersView, name='bcs_admin_orders'),
    path('bcs_admin_subscriptions/', views.bcsAdminSubscriptionView, name='bcs_admin_subscriptions'),
    # path('bcs_admin_subscriptions_list/', views.bcsAdminSubscriptionListView,
    #      name='bcs_admin_subscriptions_list'),
    path('bcs_admin_new_order/', views.bcsAdminNewOrdersView,
         name='bcs_admin_new_order'),
    path('bcs_admin_order_detail/', views.bcsAdminOrdersDetailView,
         name='bcs_admin_order_detail'),
    path('bcs_admin_order_detail/<id>/',
         views.bcsAdminOrdersDetailView, name='bcs_admin_order_detail'),
    path('bcs_admin_subscription_detail/', views.bcsAdminSubscriptionDetailView,
         name='bcs_admin_subscription_detail'),
    path('bcs_admin_subscription_detail/<id>/',
         views.bcsAdminSubscriptionDetailView, name='bcs_admin_subscription_detail'),
    path('bcs_admin_order_new/', views.bcsAdminOrderNewView,
         name='bcs_admin_order_new'),
    path('bcs_admin_order_new/<id>/',
         views.bcsAdminOrderNewView, name='bcs_admin_order_new'),
    path('bcs_admin_order_attending/', views.bcsAdminOrderAttendingView,
         name='bcs_admin_order_attending'),
    path('bcs_admin_order_attending/<id>/',
         views.bcsAdminOrderAttendingView, name='bcs_admin_order_attending'),
    path('bcs_admin_order_completed/', views.bcsAdminOrderCompletedView,
         name='bcs_admin_order_completed'),
    path('bcs_admin_order_completed/<id>/',
         views.bcsAdminOrderCompletedView, name='bcs_admin_order_completed'),
    path('bcs_admin_order_canceled/', views.bcsAdminOrderCanceledView,
         name='bcs_admin_order_canceled'),
    path('bcs_admin_order_canceled/<id>/',
         views.bcsAdminOrderCanceledView, name='bcs_admin_order_canceled'),
    path('bcs_admin_all_tickets/', views.bcsAdminTicketsView,
         name='bcs_admin_all_tickets'),
    path('bcs_admin_tickets_detail/', views.bcsAdminTicketsDetailView,
         name='bcs_admin_tickets_detail'),
    path('bcs_admin_tickets_detail/<id>/', views.bcsAdminTicketsDetailView,
         name='bcs_admin_tickets_detail'),

    # team invidual user panel
    path('team_user_services/', views.teamUserServicesView,
         name='team_user_services'),
    path('team_user_my_team/', views.teamUserMyTeamView, name='team_user_my_team'),
    path('team_user_subscriptions/', views.teamUserSubscriptionsView,
         name='team_user_subscriptions'),
    path('team_user_events/', views.teamUserEventsView, name='team_user_events'),
    path('team_user_notifications/', views.teamUserNotificationsView,
         name='team_user_notifications'),
    path('team_user_settings/', views.teamUserSettingsView,
         name='team_user_settings'),
    path('email_invitation/', views.emailInvitationView, name='email_invitation'),
    # path('test_view/', views.TestView, name='test_view'),
]
