from django.shortcuts import render
from .models import Product,ProductImages,Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django. shortcuts import get_object_or_404

def productlist(request,category_slug=None):
    category=None
    productlist = Product.objects.all()
    categorylist=Category.objects.annotate(total_products=Count('product'))
    
    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        productlist = productlist.filter (category=category)

    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query)
        )

    paginator = Paginator(productlist, 3)  #we can set number of products displayed 
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    template = 'Product/product_list.html'

    context = {'product_list' : productlist,'category_list' : categorylist,'category':category}
    return render(request, template , context)

def productdetail(request,product_slug):
   
    productdetail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    category=productdetail.category
    template = 'Product/product_detail.html'
    context = {'product_detail' : productdetail,'product_images':productimages,'category':category}
    return render(request, template , context)      