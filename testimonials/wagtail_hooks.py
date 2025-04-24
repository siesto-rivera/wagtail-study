# wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import Testimonial


class TestimonialAdmin(ModelViewSet):
    model = Testimonial
    menu_label = "Testimonials"
    icon = "user"
    menu_order = 290
    add_to_admin_menu = True  # ✅ 메뉴 자동 추가됨
    exclude_from_explorer = True
    exclude_form_fields = ["slug"]

    list_display = (
        "quote",
        "attribution",
    )
    search_fields = (
        "quote",
        "attribution",
    )


testimonial_admin = TestimonialAdmin()


@hooks.register("register_admin_viewset")
def register_testimonial_admin():
    return testimonial_admin
