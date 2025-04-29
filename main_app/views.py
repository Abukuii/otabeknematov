from django.shortcuts import render

# Create your views here.

def login_page(request):
    """
    This is the login page
    """
    return render(request, "login.html")


def main_page(request):
    """
    This is the main page
    :param request: Django request
    :return: Results
    """
    return render(request, "index.html")


def sale_page(request):
    """
    This is the sale page for Sales Assistants
    :param request: Products or Product id
    :return: Products
    """
    return render(request, "sale.html")



# Products View, Add, Edit and Delete
def products_page(request):
    """
    This is the products page for Products Add, Edit or Delete for Sales Assistants
    :param request: Products or Product id
    :return: Products
    """
    return render(request, "products.html")


def debtors_page(request):
    """
    This is the debtors page for Debtors View or Delete for Debtors Assistants
    :param request: Debtors or Debtor id
    :return: Debtors
    """
    return render(request, "debtors.html")


def reduced_products_page(request):
    """
    This is Reduced Products Page for Reduced Products View or Delete for Reduced Products Assistants
    :param request: Reduced Products or Product id
    :return: Reduced Products
    """
    return render(request, "reduced_products.html")


def profile_page(request):
    """
    This is the profile page for Profile Login Password View or Delete for Profile Assistants
    :param request: GET
    :return: Profile Login Password
    """
    return render(request, "profile.html")


