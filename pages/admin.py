from django.contrib import admin
from .models import Banner, Testimonial, USP, TeamMember, FAQ, ContactInquiry

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'cta_text', 'order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'product', 'is_featured', 'created_at')
    list_filter = ('rating', 'is_featured')
    search_fields = ('customer_name', 'review_text')
    ordering = ('-created_at',)

@admin.register(USP)
class USPAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    ordering = ('order',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order')
    list_filter = ('category',)
    ordering = ('order',)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)
