from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from menus.models import Menu


class MenuViewSet(ModelViewSet):
    model = Menu
    menu_label = "Menu 관리"
    menu_icon = "list-ul"  # 사이드바용 아이콘
    icon = "list-ul"  # header 아이콘용 ← 필수!
    menu_order = 300
    add_to_admin_menu = True  # ✅ 이 줄이 있어야 메뉴 자동 등록됨
    exclude_from_explorer = True  # 페이지 트리에서는 제외


menu_viewset = MenuViewSet()


@hooks.register("register_admin_viewset")
def register_menu_viewset():
    return menu_viewset
