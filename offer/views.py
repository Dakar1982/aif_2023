from django.shortcuts import render
from offer.models import Offer
# from _decimal import Decimal
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView,\
    DeleteView
from offer.forms import SearchForm, OfferForm
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class OfferListView(FormView):
    template_name = "offer/offer_list.html"
    form_class = SearchForm
    success_url = "."

    def get_context_data(self, **kwargs):
        print(self.request.user)
        return {
            "offers": Offer.objects.filter(),
            "form": self.form_class()}

    def form_valid(self, form):
        filter_ = Q()
        if form.cleaned_data["fraze"] != "":
            filter_ |= Q(
                Q(title__icontains=form.cleaned_data["fraze"])
                |Q(description__icontains=form.cleaned_data["fraze"]))

        offers = Offer.objects.filter(filter_).order_by("-date_from", )
        return render(
            request=self.request,
            template_name=self.template_name,
            context={
                "form": form,
                "offers": offers})

    def form_invalid(self, form):
        return render(
            request=self.request,
            template_name=self.template_name,
            context={
                "form": form,
                "offers": Offer.objects.filter()})


class OfferDetailsView(TemplateView):
    template_name = "offer/offer_details.html"

    def get_context_data(self, **kwargs):
        offer_id = self.kwargs.get("pk", None)
        return {"offer": Offer.objects.get(pk=offer_id)}


class OfferCreateView(
        LoginRequiredMixin,
        CreateView):
    model = Offer
    form_class = OfferForm
    template_name = "offer/offer_update.html"
    success_url = reverse_lazy("offer-list")


class OfferUpdateView(
        LoginRequiredMixin,
        UpdateView):
    model = Offer
    form_class = OfferForm
    template_name = "offer/offer_update.html"
    success_url = reverse_lazy("offer-list")

class OfferDeleteView(
        LoginRequiredMixin,
        DeleteView):
    model = Offer
    template_name = "offer/offer_delete.html"
    success_url = reverse_lazy("offer-list")


def offer_list(request):
    # new_offer = Offer.objects.create(
        # title="Strzyżenie owiec",
        # price=10000,
        # date_from="2023-04-01",
        # date_to="2023-05-01",
        # description="Teraz albo nigdy!")
    # offer = Offer.objects.get(id=4)
    # offer.price = round(offer.price*Decimal(1.184))
    # offer.save()
#     filter_ = Q(Q(price__lte=50)|
#                 Q(price__gt=10000))
    offers = Offer.objects.filter().order_by("-date_from", )
    print(offers.query)
    return render(request=request,
                  template_name="offer/offer_list.html",
                  context={"offers": offers})
    
