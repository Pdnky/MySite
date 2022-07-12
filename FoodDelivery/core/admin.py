from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

admin.site.register(get_user_model())
admin.site.register(Reviews)
admin.site.register(Category)


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]



class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

# Register your models here.
