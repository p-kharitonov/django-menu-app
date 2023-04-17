from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, name):
    qs = MenuItem.objects.filter(menu__name=name).order_by("position").values("pk", "name", "url", "parent")
    if not qs:
        raise ValueError(f"Menu '{name}' does not exist!")
    current_item = list(filter(lambda item: item["url"] == context["request"].path, qs))
    if current_item:
        current_item = current_item[0]
    menu_items = []
    for item in qs:
        if item["parent"] is None:
            menu_items.append(item)
        else:
            parent = list(filter(lambda item_parent: item["parent"] == item_parent["pk"], qs))
            if parent:
                if "children" not in parent[0]:
                    parent[0]["children"] = []
                parent[0]["children"].append(item)
    while current_item and True:
        current_item["item_active_tree"] = True
        if current_item["parent"] is None:
            break
        item_active_tree = list(filter(lambda item_parent: item_parent["pk"] == current_item["parent"], qs))[0]
        current_item = item_active_tree

    return {"menu_items": menu_items, "request": context["request"]}
