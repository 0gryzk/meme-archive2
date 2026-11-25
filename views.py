from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Meme, Category
from .forms import MemeForm


def meme_list(request):
    memes = Meme.objects.select_related('category').all()
    categories = Category.objects.all()

    # Список доступных годов из уже добавленных мемов (от новых к старым)
    years = (
        Meme.objects.order_by('-year')
        .values_list('year', flat=True)
        .distinct()
    )

    search_query = request.GET.get('q', '').strip()
    selected_year = request.GET.get('year', '').strip()
    selected_category = request.GET.get('category', '').strip()

    if search_query:
        memes = memes.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    if selected_year:
        memes = memes.filter(year=selected_year)

    if selected_category:
        memes = memes.filter(category_id=selected_category)

    context = {
        'memes': memes,
        'categories': categories,
        'years': years,
        'search_query': search_query,
        'selected_year': selected_year,
        'selected_category': selected_category,
    }
    return render(request, 'memes/index.html', context)


def meme_detail(request, pk):
    meme = get_object_or_404(Meme.objects.select_related('category'), pk=pk)
    return render(request, 'memes/detail.html', {'meme': meme})


def meme_create(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save()
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm()
    return render(request, 'memes/form.html', {
        'form': form,
        'page_title': 'Добавить мем',
        'submit_text': 'Сохранить мем'
    })


def meme_update(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            form.save()
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm(instance=meme)
    return render(request, 'memes/form.html', {
        'form': form,
        'meme': meme,
        'page_title': f'Редактировать: {meme.title}',
        'submit_text': 'Сохранить изменения'
    })


def meme_delete(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if request.method == 'POST':
        meme.delete()
        return redirect('meme_list')
    return render(request, 'memes/confirm_delete.html', {'meme': meme})