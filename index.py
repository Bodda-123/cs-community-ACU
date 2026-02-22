import os
import sys

# 1) حدد المسار المطلق للمجلد الحالي ومجلد المشروع
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Sky_Hub_Project')

# 2) أضف مجلد المشروع إلى مسارات البحث الخاصة بـ Python
# نستخدم insert(0) لضمان أن يكون مجلدك هو الأولوية الأولى
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# 3) استيراد تطبيق Flask الحقيقي
try:
    # نحاول الاستيراد المباشر لأن المجلد مضاف لـ sys.path
    from app import app as application
except ImportError:
    # محاولة بديلة في حال فشل الاستيراد الأول
    sys.path.append(BASE_DIR)
    from Sky_Hub_Project.app import app as application

# 4) ضبط مسارات التنسيقات والقوالب
application.template_folder = os.path.join(PROJECT_DIR, 'templates')
application.static_folder = os.path.join(PROJECT_DIR, 'static')

# التأكد من وجود مجلد الرفع في مسار الإنتاج
UPLOAD_ROOT = os.path.join(application.static_folder, 'uploads')
os.makedirs(os.path.join(UPLOAD_ROOT, 'profile_pics'), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_ROOT, 'cv'), exist_ok=True)

# 5) إنشاء جداول قاعدة البيانات تلقائياً إذا لم تكن موجودة
with application.app_context():
    from models import db
    db.create_all()
    print("Database tables initialized successfully!")

app = application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # تم إيقاف وضع التصحيح للإنتاج
    app.run(host="0.0.0.0", port=port, debug=False)
