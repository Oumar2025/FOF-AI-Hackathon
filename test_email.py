from services.notification_service import NotificationService

success = NotificationService.send_email(
    subject="FOF-AI Test Email",
    message="""
Hello,

This is a test email from FOF-AI.

If you received this message, the email notification system is working correctly.

Regards,
FOF-AI Business Intelligence Assistant
"""
)

if success:
    print("✅ Email sent successfully!")
else:
    print("❌ Failed to send email.")