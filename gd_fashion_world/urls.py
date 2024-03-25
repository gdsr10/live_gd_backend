"""
URL configuration for gd_fashion_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import Login, Register, ForgotPassword, ResetPassword, ItemList, ItemDetailsList
from api.views import OnlineOrder, CustomizeDesignOrder, CustomizeThemeDesignWomenOrder, CustomizeThemeDesignMenOrder, CustomizeThemeDesignKidOrder
from api.views import PendingOrder, CancelOrder, ConfirmOrder
from api.views import ConfirmViewOrder, CancelViewOrder
from api.views import AdPendingOrder, AdConfirmViewOrder, AdCancelViewOrder

urlpatterns = [

    path('admin/', admin.site.urls),

    # API to post/Login Scheme
    path('api/login/', Login.LoginView.as_view()),

    # API to post/Register Scheme
    path('api/register/', Register.RegisterView.as_view()),

    # API to post/ForgotPassword Scheme
    path('api/forgotpassword/', ForgotPassword.ForgotPasswordView.as_view()),

    # API to post/OTPVerify Scheme
    path('api/resetpassword/', ResetPassword.ResetPasswordView.as_view()),

    # API to post/OTPVerify Scheme
    path('api/itemlist/', ItemList.ItemListView.as_view()),

    # API to post/OTPVerify Scheme
    path('api/itemdetailslist/', ItemDetailsList.ItemDetailsListView.as_view()),

    # API to post/OnlineOrder Scheme
    path('api/onlineorder/', OnlineOrder.OnlineOrderView.as_view()),
    
    # API to post/customizedesignorder Scheme
    path('api/customizedesignorder/', CustomizeDesignOrder.CustomizeDesignOrderView.as_view()),

    # API to post/customizethemedesignorder Scheme
    path('api/customizethemedesignorderwomen/', CustomizeThemeDesignWomenOrder.CustomizeThemeDesignWomenOrderView.as_view()),

    # API to post/customizethemedesignorder Scheme
    path('api/customizethemedesignordermen/', CustomizeThemeDesignMenOrder.CustomizeThemeDesignMenOrderView.as_view()),

    # API to post/customizethemedesignorder Scheme
    path('api/customizethemedesignorderkid/', CustomizeThemeDesignKidOrder.CustomizeThemeDesignKidOrderView.as_view()),

    # API to post/pendingorder Scheme
    path('api/pendingorder/', PendingOrder.PendingOrderview.as_view()),

    # API to post/pendingorder Scheme
    path('api/adpendingorder/', AdPendingOrder.AdPendingOrderview.as_view()),

    # API to post/pendingorder Scheme
    path('api/cancelorder/', CancelOrder.CancelOrderview.as_view()),

    # API to post/confirmorder Scheme
    path('api/confirmorder/', ConfirmOrder.ConfirmOrderview.as_view()),

    # API to post/confirmorder Scheme
    path('api/confirmvieworder/', ConfirmViewOrder.ConfirmViewOrderview.as_view()),

    # API to post/confirmorder Scheme
    path('api/adconfirmvieworder/', AdConfirmViewOrder.AdConfirmViewOrderview.as_view()),

    # API to post/confirmorder Scheme
    path('api/cancelvieworder/', CancelViewOrder.CancelViewOrderview.as_view()),

    # API to post/confirmorder Scheme
    path('api/adcancelvieworder/', AdCancelViewOrder.AdCancelViewOrderview.as_view()),

]
