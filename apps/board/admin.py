from django.contrib import admin
from board.models import ImageBoard
from django.utils.html import mark_safe

class ImageBoardAdmin(admin.ModelAdmin):
    fields = ["room", "display_image"]
    readonly_fields = ["room", "display_image"]

    def display_image(self, obj):
        if obj.image:
            print(obj.image.url)
            return self.get_image_html(obj.image.url)
        else:
            return 'No image'

    display_image.short_description = 'Image'
    display_image.allow_tags = True

    @staticmethod
    def get_image_html(url):
        return mark_safe(f'<img src="{url}" width="200px" height="100px">')


admin.site.register(ImageBoard, ImageBoardAdmin)
