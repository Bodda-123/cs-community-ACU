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
    
    # التأكد من وجود صورة البروفايل الافتراضية
    default_avatar_path = os.path.join(UPLOAD_ROOT, 'profile_pics', 'default_profile.png')
    if not os.path.exists(default_avatar_path):
        try:
            from create_default_avatar import make_with_pillow
            make_with_pillow()
        except Exception as e:
            print(f"Warning: Could not create default avatar: {e}")
            
    # جعل المستخدم صاحب البريد الإلكتروني أدمن للتجربة
    from models import User
    admin_user = User.query.filter_by(email="abdelrahmanaboalsouad@gmail.com").first()
    if admin_user and not admin_user.is_admin:
        admin_user.is_admin = True
        db.session.commit()
        print(f"User {admin_user.email} promoted to Admin.")
            
    print("Application initialized successfully!")

app = application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # تم إيقاف وضع التصحيح للإنتاج
    app.run(host="0.0.0.0", port=port, debug=False)
