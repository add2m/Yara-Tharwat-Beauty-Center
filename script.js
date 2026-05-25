// كود لقراءة الصفحة المطلوبة من الرابط وعرضها في التاب الجديدة
const urlParams = new URLSearchParams(window.location.search);
const pageParam = urlParams.get('p');

if (pageParam) {
    window.addEventListener('DOMContentLoaded', () => {
        const targetPage = document.getElementById(`${pageParam}-page`);
        if (targetPage) {
            // إخفاء الصفحة الرئيسية أولاً
            document.getElementById('home-page').classList.remove('active');
            // إظهار الصفحة المطلوبة في التاب الجديدة
            targetPage.classList.add('active');
        }
    });
}

// ثوابت السنتر الأساسية
const WA_NUM = "201055901090";

// 1. دالة التحقق من مواعيد العمل (من الساعة 1 ظهراً حتى 10 مساءً بتوقيت مصر GMT+3)
function updateCenterStatus() {
    const badge = document.getElementById("status-badge");
    
    // الحصول على الوقت الحالي بالتوقيت المحلي وحسابه لتوقيت مصر
    const now = new Date();
    const utcHour = now.getUTCHours();
    const egyptHour = (utcHour + 3) % 24; // توقيت مصر GMT +3

    // إذا كانت الساعة بين 13 (1 ظهراً) و 22 (10 مساءً)
    if (egyptHour >= 13 && egyptHour < 22) {
        badge.innerHTML = "🟢 نتشرف بكم الآن";
        badge.className = "status-badge status-open";
    } else {
        badge.innerHTML = "🔴 السنتر مغلق حالياً";
        badge.className = "status-badge status-closed";
    }
}

// 2. تفعيل لينك مشاركة الواتساب بالرسالة المخصصة
function setupShareButton() {
    const shareText = "شوفت بيوتي سنتر يارا ثروت وعجبني شغله ادخلي شوفيه انتي كمان اللينك ده";
    const currentUrl = window.location.href;
    const fullShareUrl = `https://wa.me/?text=${encodeURIComponent(shareText)} ${encodeURIComponent(currentUrl)}`;
    document.getElementById("share-wa").href = fullShareUrl;
}

// 3. دالة التنقل الذكي بين السكاشن (بدل الـ Query Params القديم)
function navigateTo(pageId) {
    // إخفاء كل السكاشن
    document.querySelectorAll('.page-section').forEach(section => {
        section.classList.remove('active');
    });
    // إظهار السكشن المطلوب
    document.getElementById(pageId).classList.add('active');
    // سكرول لأعلى الصفحة سلاسة
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 4. تجميع بيانات الحجز وإرسالها للواتساب مباشرة
function sendBooking() {
    const name = document.getElementById("b_name").value.trim();
    const age = document.getElementById("b_age").value.trim();
    const phone = document.getElementById("b_phone").value.trim();
    const service = document.getElementById("b_service").value;
    const notes = document.getElementById("b_notes").value.trim();

    if (!name || !phone) {
        alert("⚠️ يرجى كتابة الاسم ورقم الهاتف لتفعيل إرسال الحجز");
        return;
    }

    const msg = `✨ حجز جديد ✨\n----------------------------------\n👤 الاسم: ${name}\n🎂 السن: ${age}\n📱 الهاتف: ${phone}\n💄 الخدمة: ${service}\n📝 ملاحظات: ${notes}`;
    const finalWaUrl = `https://wa.me/${WA_NUM}?text=${encodeURIComponent(msg)}`;
    
    // فتح رابط الواتساب في نافذة جديدة
    window.open(finalWaUrl, '_blank');
}

// 5. نظام إضافة الآراء (حفظ محلي مؤقت في المتصفح LocalStorage)
function addReview() {
    const name = document.getElementById("rev_name").value.trim();
    const text = document.getElementById("rev_text").value.trim();

    if (!name || !text) {
        alert("⚠️ يرجى ملء الاسم ونص الرأي أولاً");
        return;
    }

    const reviewList = document.getElementById("reviews-list");
    
    // إنشاء كارت الرأي الجديد
    const newCard = document.createElement("div");
    newCard.className = "review-card";
    newCard.innerHTML = `"${text}"<br><small style="color:#D4AF37;">— ${name}</small>`;
    
    // إضافته في البداية فوق الآراء القديمة
    reviewList.insertBefore(newCard, reviewList.firstChild);

    // تنظيف الحقول
    document.getElementById("rev_name").value = "";
    document.getElementById("rev_text").value = "";
    alert("شكراً لثقتك! تم النشر.");
}

// 6. التعامل مع السايدبار في الموبايل (فتح وقفل)
document.getElementById("sidebarToggle").addEventListener("click", () => {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("open");
});

// تشغيل الدوال عند تحميل الصفحة فوراً
window.onload = () => {
    updateCenterStatus();
    setupShareButton();
    // تحديث الحالة كل دقيقة عشان لو المواعيد اتغيرت والموقع مفتوح
    setInterval(updateCenterStatus, 60000); 
};