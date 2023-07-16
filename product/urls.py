from django.urls import path


app_name='product'

from .views import productList,productDetail,brand_list,brand_detail,add_review,productlist,search_filter,shop_colum4,shop_colum3,shop_colum2,shop_colum1,add_to_wishlist


from .api import peoductList_api , productListApi , productDetailApi,BrandListApi,BrandDetailView


urlpatterns =[

    
    path('',productList. as_view(),name='product_list'),
    path('<slug:slug>',productDetail.as_view(),name='product_detail'),
    path('<slug:slug>/add_review',add_review,name='add_review'),
    path('brands/',brand_list.as_view(),name='brand_list'),
    path('brands/<slug:slug>',brand_detail.as_view(),name='brand_detail'),
    path('debug/',productlist,name='debug'),
    path('search/',search_filter,name='search_results'),
    path('shop_colum4/',shop_colum4,name='shop_colum4'),
    path('shop_colum3/',shop_colum3,name='shop_colum3'),
    path('shop_colum2/',shop_colum2,name='shop_colum2'),
    path('shop_colum1/',shop_colum1,name='shop_colum1'),
    path('wish_list/',add_to_wishlist,name='wish_list'),
    
    
    
    
    #api url
    
    #path('api/list',peoductList_api,name='api-list'),
    path('api/list',productListApi.as_view(),name='api-list'),
    path('api/brandlist',BrandListApi.as_view(),name='api-list'),
    path('api/brandlist/<slug:slug>',BrandDetailView.as_view(),name='productDetailApi-list'),
    path('api/list/<slug:slug>',productDetailApi.as_view(),name='productDetailApi-list'),
    
]
