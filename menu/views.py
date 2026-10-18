from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, MenuItem

def home(request):
    categories = Category.objects.filter(active=True)
    items = MenuItem.objects.filter(available=True).select_related("category")
    selected = request.GET.get("category", "").strip()
    query = request.GET.get("q", "").strip()
    if selected:
        items = items.filter(category__slug=selected)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
    return render(request, "menu/home.html", {
        "categories": categories,
        "items": items,
        "selected_category": selected,
        "search_query": query,
    })

def item_detail(request, slug):
    item = get_object_or_404(MenuItem.objects.select_related("category"), slug=slug, available=True)
    return render(request, "menu/item_detail.html", {"item": item})
