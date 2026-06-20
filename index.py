import os  # ➕ هذا السطر مضاف لقراءة المنفذ من Render
from flask import Flask, render_template, request

app = Flask(__name__)

company_info = {
    "phone": "07717100200",
    "location_ar": "النجف الأشرف - شارع الحزام الاخضر جهة العدالة  - مقابيل سنتر جبل عامل",
    "location_ku": "نەجەفی ئەشرەف - شەقامی پشتوێنی سەوز، لای عەدالە - بەرامبەر سەنتەری جەبەل عامیل",
    "location_en": "Najaf Al-Ashraf - Green Belt Street, Justice side - opposite Jabal Amel Center",
}

multilingual_data = {
    "ar": {
        "title": "SAMA AL-LUALUA AL-THAHBIA",
        "home": "الرئيسية",
        "products": "أقسام الديكور والمواد",
        "contact": "اتصل بنا",
        "hero_title": "أرقى مواد الديكور المعماري الحديث",
        "hero_sub": "شركة سما اللؤلؤة الذهبية يوفر لكم أحدث صيحات الديكور الداخلي والخارجي بأعلى جودة في العراق.",
        "btn_browse": "تصفح الأقسام والمنتجات",
        "btn_order": "اطلب أو استفسر عبر الواتساب",
        "contact_title": "معلومات الاتصال والزيارة",
        "address_label": "موقع المكتب",
        "phone_label": "رقم الهاتف الفعلي",
        "hours_label": "أوقات العمل",
        "hours_val": "أهلاً وسهلاً بكم في جميع الأوقات",
        "footer_text": "شركة سما اللؤلؤة الذهبية - الفخامة والتميز في عالم الديكور الحديث",
        "all_categories": "كل الأقسام",

        "sections": [
            {
                "id": "waterfalls",
                "title": "الشلالات الداخلية والنافورات",
                "items": [
                    {
                        "name": "شلال جداري مودرن - إضاءة ذكية",
                        "features": "استمع إلى هدير الماء مع شلالات اللؤلؤة الذهبية للديكور شلال داخلي من مادة الفايبر گلاس عالي الكثافة الأبعاد الارتفاع 175 سم  العرض 68 سم",
                        "placeholder": "/static/images/water1.jpg",
                        "note": "سهلة التركيب"
                    },
                    {
                        "name": "شلال جداري مودرن - إضاءة ذكية",
                        "features": "استمع إلى هدير الماء مع شلالات اللؤلؤة الذهبية للديكور شلال داخلي من مادة الفايبر گلاس عالي الكثافة الأبعاد الارتفاع 150 سم  العرض 50 سم",
                        "placeholder": "/static/images/water2.jpg",
                        "note": "سهلة التركيب"
                    },
                    {
                        "name": "شلال جداري مودرن - إضاءة ذكية",
                        "features": "استمع إلى هدير الماء مع شلالات اللؤلؤة الذهبية للديكور شلال داخلي من مادة الفايبر گلاس عالي الكثافة الأبعاد الارتفاع 90 سم  العرض 68 سم",
                        "placeholder": "/static/images/water3.jpg",
                        "note": "سهلة التركيب"
                    },
                    {
                        "name": "شلال جداري مودرن - إضاءة ذكية",
                        "features": "استمع إلى هدير الماء مع شلالات اللؤلؤة الذهبية للديكور شلال داخلي من مادة الفايبر گلاس عالي الكثافة الأبعاد الارتفاع 95 سم  العرض 40 سم",
                        "placeholder": "/static/images/water4.jpg",
                        "note": "سهلة التركيب"
                    }
                ]
            },
            {
                "id": "marble-wood",
                "title": "قسم مواد الديكور",
                "items": [
                    {
                        "name": "بديل الخشب",
                        "features": "حشوه الابواب الخارجيه المقاومه للمياه والحريق والعفن والبكتيريا اسعار مميزه للجمله والمفرد",
                        "placeholder": "/static/images/water5.jpg",
                        "note": "اضغط لمعاينة النقشات الـ 6",
                        "images": [
                            "/static/images/water5.jpg",
                            "/static/images/water6.jpg",
                            "/static/images/water7.jpg",
                            "/static/images/water8.jpg",
                            "/static/images/water9.jpg",
                            "/static/images/water10.jpg"
                        ]
                    },
                    {
                        "name": "مواد الواجهات العازله للبروده والحراره",
                        "features": "تتميز بالجوده العاليه ومواصفات تلائم الاجواء العراقيه اسعار مميزه احصل على خصم 25% الان من كل قوائم الجمله",
                        "placeholder": "/static/images/water11.jpg",
                        "note": "اضغط لمعاينة النقشات الـ 3",
                        "images": [
                            "/static/images/water11.jpg",
                            "/static/images/water12.jpg",
                            "/static/images/water13.jpg"
                        ]
                    },
                    {
                        "name": "بديل خشب",
                        "features": "اكثر من 50 موديل تناسب كافه الاذواق اسعار مميزه وجوده عاليه جدا",
                        "placeholder": "/static/images/water14.jpg",
                        "note": "اضغط لمعاينة النقشات الـ 3",
                        "images": [
                            "/static/images/water14.jpg",
                            "/static/images/water15.jpg",
                            "/static/images/water16.jpg"
                        ]
                    },
                    {
                        "name": "بديل رخام",
                        "features": "بديل رخام الوان وتشكيله جديده",
                        "placeholder": "/static/images/water17.jpg",
                        "note": "اضغط لمعاينة النقشات الـ 3",
                        "images": [
                            "/static/images/water17.jpg",
                            "/static/images/water18.jpg",
                            "/static/images/water19.jpg"
                        ]
                    },
                    {
                        "name": "ورق جدران فاخر",
                        "features": "بديل رخام الوان وتشكيله جديده",
                        "placeholder": "/static/images/water20.jpg",
                        "note": "اضغط لمعاينة النقشات",
                        "images": [
                            "/static/images/water20.jpg"
                        ]
                    }
                ]
            },
            {
                "id": "wallpaper",
                "title": "قسم مواد البناء",
                "items": [
                    {
                        "name": "تحت شعار 'صنع في العراق' صناعة البروفايلات الخاصة بالجبسم بورد بأعلى معايير الجودة والدقة،",
                        "features": "منتج وطني يواكب التطور ويخدم مشاريعكم باحترافية عالية، متانة، ثبات، وتشطيب مثالي يلبي متطلبات منفذي الديكور، اختيارك الأول للثقة والجودة.",
                        "placeholder": "/static/images/water21.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water21.jpg",
                            "/static/images/water22.jpg",
                            "/static/images/water23.jpg",
                            "/static/images/water24.jpg",
                            "/static/images/water25.jpg",
                            "/static/images/water26.jpg",
                            "/static/images/water27.jpg"
                        ]
                    },
                    {
                        "name": "الواح المتحدة",
                        "features": "جوده وامان نتحدى بجودة منتوجنا الاسماء كثيرة قمتها اسم منتوجنا جمله ومفرد مستعدون لتجهيز كافه المشاريع وشركات الديكور اسعارنا مميزه",
                        "placeholder": "/static/images/water28.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water28.jpg",
                            "/static/images/water29.jpg"
                        ]
                    },
                    {
                        "name": "الواح البورد اكس الخارجية",
                        "features": "مقاومة للماء والرطوبة مقاومة للحريق",
                        "placeholder": "/static/images/water30.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water30.jpg",
                            "/static/images/water31.jpg"
                        ]
                    },
                    {
                        "name": "رافعة ألواح جبسية",
                        "features": "تسهل اعمالك سهولة العمل بها تزيد من سرعة الإنجاز ماذا تنتظر",
                        "placeholder": "/static/images/water32.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water32.jpg",
                            "/static/images/water33.jpg"
                        ]
                    },
                    {
                        "name": "صوف صخري من شركة كناوف الألمانية",
                        "features": "مادة التصنيع: يُصنع من صخور البازلت الطبيعية المعاد صهرها. الموصلية الحرارية: منخفضة جدًا بحدود 0.034 – 0.040 W/m·K مقاومة النار: غير قابل للاشتعال (تصنيف A1). يتحمل درجات حرارة تصل إلى1000°C قدرة عالية على امتصاص الصوت مقاوم للرطوبة والعفن والفطريات",
                        "placeholder": "/static/images/water34.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water34.jpg",
                            "/static/images/water35.jpg",
                            "/static/images/water36.jpg"
                        ]
                    },
                    {
                        "name": "ساتين طلية نهائية",
                        "features": "من ماركة KNAUF الألمانية صنع في تركيا",
                        "placeholder": "/static/images/water37.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water37.jpg"
                        ]
                    },
                    {
                        "name": "معجون ابيضّ ناعم مقاوم للماء",
                        "features": "للاستعمال الخارجي من شركة جدار",
                        "placeholder": "/static/images/water38.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water38.jpg"
                        ]
                    },
                    {
                        "name": "ورق ذهب",
                        "features": "إيطالي جودة عالية",
                        "placeholder": "/static/images/water39.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water39.jpg"
                        ]
                    },
                    {
                        "name": "تيب جوين نوع ABA",
                        "features": "استيراد خاص ذو مواصفات عالمية عالية الجودة العرض 5 سم الطول 90 متر ذو لاصق قوي جداً",
                        "placeholder": "/static/images/water40.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water40.jpg"
                        ]
                    },
                    {
                        "name": "تيب جوين نوع متحدة سعودي",
                        "features": "العرض 5 سم الطول 90 متر ذو لاصق قوي جداً",
                        "placeholder": "/static/images/water41.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water41.jpg"
                        ]
                    },
                    {
                        "name": "گبان ليزري من BOSCH",
                        "features": "أربع خطوط المدى 50 متر",
                        "placeholder": "/static/images/water42.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water42.jpg",
                            "/static/images/water43.jpg",
                            "/static/images/water44.jpg"
                        ]
                    },
                    {
                        "name": "گبان ليزري ماركة DEWALT ليزر احمر",
                        "features": "ذو مدى طويل يصل إلى 50 متر",
                        "placeholder": "/static/images/water45.jpg",
                        "note": "اضغط لمعاينة",
                        "images": [
                            "/static/images/water45.jpg",
                            "/static/images/water46.jpg"
                        ]
                    }
                ]
            }
        ]
    },

    "ku": {
        "title": "SAMA AL-LUALUA AL-THAHBIA",
        "home": "سەرەکی",
        "products": "بەشەکانی دیکۆر و کەرەستەکان",
        "contact": "پەیوەندیمان پێوە بکە",
        "hero_title": "ناوازەترین کەرەستەکانی دیکۆری تەلارسازی هاوچەرخ",
        "hero_sub": "کۆمپانیای سەما اللؤلؤة الذهبية نوێترین مۆدێلەکانی دیکۆری ناوخۆیی و دەرەکی بە بەرزترین کوالیتی لە عێراق بۆ دابین دەکات.",
        "btn_browse": "گەڕان لە بەشەکان و بەرهەمەکان",
        "btn_order": "داواکردن یان پرسیارکردن لەڕێگەی واتسئەپەوە",
        "contact_title": "زانیاری پەیوەندی و سەردانکردن",
        "address_label": "شوێنی نووسینگە",
        "phone_label": "ژمارەی تەلەفۆنی ڕاستەقینە",
        "hours_label": "کاتەکانی کارکردن",
        "hours_val": "بەخێرهاتنتان دەکەین لە هەموو کاتێکدا",
        "footer_text": "کۆمپانیای سەما اللؤلؤة الذهبية - ڕازاوەیی و ناوازەیی لە جیهانی دیکۆری هاوچەرخدا",
        "all_categories": "هەموو بەشەکان",

        "sections": [
            {
                "id": "waterfalls",
                "title": "شەلالەکانی ناوخۆ و نافورەکان",
                "items": [
                    {
                        "name": "شەلالی دیواری مۆدێرن - ڕووناکی زیرەک",
                        "features": "گوێ لە خوڕەی ئاو بگرە لەگەڵ شەلالەکانی مرواری زێڕین بۆ دیکۆر، شەلالی ناوخۆیی لە ماددەی فایبەرگلاسی چڕی بەرز، ڕەهەندەکان: بەرزی ١٧٥ سم، پانی ٦٨ سم",
                        "placeholder": "/static/images/water1.jpg",
                        "note": "ئاسانە بۆ بەستن"
                    },
                    {
                        "name": "شەلالی دیواری مۆدێرن - ڕووناکی زیرەک",
                        "features": "گوێ لە خوڕەی ئاو بگرە لەگەڵ شەلالەکانی مرواری زێڕین بۆ دیکۆر، شەلالی ناوخۆیی لە ماددەی فایبەرگلاسی چڕی بەرز، ڕەهەندەکان: بەرزی ١٥٠ سم، پانی ٥٠ سم",
                        "placeholder": "/static/images/water2.jpg",
                        "note": "ئاسانە بۆ بەستن"
                    },
                    {
                        "name": "شەلالی دیواری مۆدێرن - ڕووناکی زیرەک",
                        "features": "گوێ لە خوڕەی ئاو بگرە لەگەڵ شەلالەکانی مرواری زێڕین بۆ دیکۆر، شەلالی ناوخۆیی لە ماددەی فایبەرگلاسی چڕی بەرز، ڕەهەندەکان: بەرزی ٩٠ سم، پانی ٦٨ سم",
                        "placeholder": "/static/images/water3.jpg",
                        "note": "ئاسانە بۆ بەستن"
                    },
                    {
                        "name": "شەلالی دیواری مۆدێرن - ڕووناکی زیرەک",
                        "features": "گوێ لە خوڕەی ئاو بگرە لەگەڵ شەلالەکانی مرواری زێڕین بۆ دیکۆر، شەلالی ناوخۆیی لە ماددەی فایبەرگلاسی چڕی بەرز، ڕەهەندەکان: بەرزی ٩٥ سم، پانی ٤٠ سم",
                        "placeholder": "/static/images/water4.jpg",
                        "note": "ئاسانە بۆ بەستن"
                    }
                ]
            },
            {
                "id": "marble-wood",
                "title": "بەشی کەرەستەکانی دیکۆر",
                "items": [
                    {
                        "name": "جێگری دار",
                        "features": "پڕکەرەوەی دەرگا دەرەکییەکان، دژە ئاو، دژە ئاگر، دژە قەوزە و بەکتریا، نرخێکی تایبەت بۆ کۆمەڵ و تاک",
                        "placeholder": "/static/images/water5.jpg",
                        "note": "کلیک بکە بۆ بینینی ٦ نەخشەکە",
                        "images": [
                            "/static/images/water5.jpg",
                            "/static/images/water6.jpg",
                            "/static/images/water7.jpg",
                            "/static/images/water8.jpg",
                            "/static/images/water9.jpg",
                            "/static/images/water10.jpg"
                        ]
                    },
                    {
                        "name": "کەرەستەی دیواری ئیزۆلاسیۆنی سارد و گەرم",
                        "features": "بە کوالیتیی بەرز و تایبەتمەندییەکانی گونجاو بۆ کەشوهەوای عێراق، نرخی تایبەت، ئێستا ٢٥٪ داشکاندن لە هەموو لیستی کۆمەڵەوە بەدەست بهێنە",
                        "placeholder": "/static/images/water11.jpg",
                        "note": "کلیک بکە بۆ بینینی ٣ نەخشەکە",
                        "images": [
                            "/static/images/water11.jpg",
                            "/static/images/water12.jpg",
                            "/static/images/water13.jpg"
                        ]
                    },
                    {
                        "name": "جێگری دار",
                        "features": "زیاتر لە ٥٠ مۆدێل کە گونجاوە بۆ هەموو تامەکان، نرخی تایبەت و کوالیتیی زۆر بەرز",
                        "placeholder": "/static/images/water14.jpg",
                        "note": "کلیک بکە بۆ بینینی ٣ نەخشەکە",
                        "images": [
                            "/static/images/water14.jpg",
                            "/static/images/water15.jpg",
                            "/static/images/water16.jpg"
                        ]
                    },
                    {
                        "name": "جێگری مەرمەر",
                        "features": "جێگری مەرمەر بە ڕەنگ و شێوەی نوێ",
                        "placeholder": "/static/images/water17.jpg",
                        "note": "کلیک بکە بۆ بینینی ٣ نەخشەکە",
                        "images": [
                            "/static/images/water17.jpg",
                            "/static/images/water18.jpg",
                            "/static/images/water19.jpg"
                        ]
                    },
                    {
                        "name": "کاغەزی دیواری لوکس",
                        "features": "جێگری مەرمەر بە ڕەنگ و شێوەی نوێ",
                        "placeholder": "/static/images/water20.jpg",
                        "note": "کلیک بکە بۆ بینینی نەخشەکان",
                        "images": [
                            "/static/images/water20.jpg"
                        ]
                    }
                ]
            },
            {
                "id": "wallpaper",
                "title": "بەشی کەرەستەکانی بیناسازی",
                "items": [
                    {
                        "name": "بە دروشمی 'دروستکراوی عێراق' دروستکردنی پڕۆفایلەکانی جیبسم بۆرد بە بەرزترین پێوەرەکانی کوالیتی و وردی،",
                        "features": "بەرهەمێکی نیشتمانی کە هاوکاتە لەگەڵ پێشکەوتن و خزمەت بە پرۆژەکانتان دەکات بە پیشەیییەکی بەرز، بەهێزی، جێگیری، و تەواوکارییەکی نموونەیی کە پێداویستییەکانی جێبەجێکەرانی دیکۆر دابین دەکات، هەڵبژاردنی یەکەم بۆ متمانە و کوالیتی.",
                        "placeholder": "/static/images/water21.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water21.jpg",
                            "/static/images/water22.jpg",
                            "/static/images/water23.jpg",
                            "/static/images/water24.jpg",
                            "/static/images/water25.jpg",
                            "/static/images/water26.jpg",
                            "/static/images/water27.jpg"
                        ]
                    },
                    {
                        "name": "تەختەکانی یەکگرتوو",
                        "features": "کوالیتی و ئاسایش، ئێمە بە کوالیتیی بەرهەمەکەمان دەنگۆ دەکەین، ناوەکان زۆرن، بەرزترینی ناوی بەرهەمەکەمانە، بە کۆمەڵ و تاک، ئامادەین بۆ دابینکردنی هەموو پرۆژەکان و کۆمپانیاکانی دیکۆر، نرخەکەمان تایبەتن.",
                        "placeholder": "/static/images/water28.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water28.jpg",
                            "/static/images/water29.jpg"
                        ]
                    },
                    {
                        "name": "تەختەکانی بۆرد ئێکس دەرەکی",
                        "features": "دژە ئاو و شێ، دژە ئاگر",
                        "placeholder": "/static/images/water30.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water30.jpg",
                            "/static/images/water31.jpg"
                        ]
                    },
                    {
                        "name": "هەڵگرتەنی تەختەکانی گەچ",
                        "features": "کاری تۆ ئاسان دەکات، ئاسانی کارکردن لەگەڵی، خێرایی جێبەجێکردن زیاد دەکات، چاوەڕوانی چی دەکەیت؟",
                        "placeholder": "/static/images/water32.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water32.jpg",
                            "/static/images/water33.jpg"
                        ]
                    },
                    {
                        "name": "لووفی بەردیی لە کۆمپانیای KNAUF ئەڵمانی",
                        "features": "ماددەی دروستکردن: لە بەردی بازەلتی سروشتییەوە دروست دەکرێت کە دووبارە توێ دەکرێتەوە. گەیاندنی گەرمی: زۆر نزم لە نێوان ٠.٠٣٤ – ٠.٠٤٠ وات/مەتر·کێلوین. بەرگری لە ئاگر: ناسوتێنرێت (پۆلێنی A1). بەرگەی پلەی گەرمی تا ١٠٠٠ پلەی سەدی دەگرێت. توانای بەرزی هەڵمژینی دەنگ. بەرگری لە شێ، قەوزە و کەڕوو.",
                        "placeholder": "/static/images/water34.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water34.jpg",
                            "/static/images/water35.jpg",
                            "/static/images/water36.jpg"
                        ]
                    },
                    {
                        "name": "ساتینی پۆلەشکردنی کۆتایی",
                        "features": "لە مارکەی KNAUF ئەڵمانی، دروستکراوە لە تورکیا",
                        "placeholder": "/static/images/water37.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water37.jpg"
                        ]
                    },
                    {
                        "name": "سوچی سپیی نەرمی دژە ئاو",
                        "features": "بۆ بەکارهێنانی دەرەکی لە کۆمپانیای جیدار",
                        "placeholder": "/static/images/water38.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water38.jpg"
                        ]
                    },
                    {
                        "name": "کاغەزی زێڕ",
                        "features": "ئیتالی، کوالیتیی بەرز",
                        "placeholder": "/static/images/water39.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water39.jpg"
                        ]
                    },
                    {
                        "name": "تیپ جۆین جۆری ABA",
                        "features": "هاوردەی تایبەت خاوەنی تایبەتمەندییەکی جیهانیی بەرز، پانی ٥ سم، درێژی ٩٠ مەتر، چەسپاوێکی زۆر بەهێز",
                        "placeholder": "/static/images/water40.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water40.jpg"
                        ]
                    },
                    {
                        "name": "تیپ جۆین جۆری یەکگرتووی سعودی",
                        "features": "پانی ٥ سم، درێژی ٩٠ مەتر، چەسپاوێکی زۆر بەهێز",
                        "placeholder": "/static/images/water41.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water41.jpg"
                        ]
                    },
                    {
                        "name": "گپانی لێزەری لە BOSCH",
                        "features": "چوار هێڵ، مەودا ٥٠ مەتر",
                        "placeholder": "/static/images/water42.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water42.jpg",
                            "/static/images/water43.jpg",
                            "/static/images/water44.jpg"
                        ]
                    },
                    {
                        "name": "گپانی لێزەری مارکەی DEWALT لێزەری سوور",
                        "features": "مەودای درێژ تا ٥٠ مەتر",
                        "placeholder": "/static/images/water45.jpg",
                        "note": "کلیک بکە بۆ بینین",
                        "images": [
                            "/static/images/water45.jpg",
                            "/static/images/water46.jpg"
                        ]
                    }
                ]
            }
        ]
    },

    "en": {
        "title": "SAMA AL-LUALUA AL-THAHBIA",
        "home": "Home",
        "products": "Decor Sections & Materials",
        "contact": "Contact Us",
        "hero_title": "The Finest Modern Architectural Decoration Materials",
        "hero_sub": "Sama Al-Lualua Al-Thahbia Company provides you with the latest interior and exterior decoration trends with the highest quality in Iraq.",
        "btn_browse": "Browse Sections & Products",
        "btn_order": "Order or Inquire via WhatsApp",
        "contact_title": "Contact & Visit Information",
        "address_label": "Office Location",
        "phone_label": "Actual Phone Number",
        "hours_label": "Working Hours",
        "hours_val": "Welcome at All Times",
        "footer_text": "Sama Al-Lualua Al-Thahbia Company - Luxury and Excellence in the World of Modern Decoration",
        "all_categories": "All Sections",

        "sections": [
            {
                "id": "waterfalls",
                "title": "Indoor Waterfalls & Fountains",
                "items": [
                    {
                        "name": "Modern Wall Waterfall - Smart Lighting",
                        "features": "Listen to the roar of water with Golden Pearl waterfalls for decor. Indoor waterfall made of high-density fiberglass. Dimensions: Height 175 cm, Width 68 cm.",
                        "placeholder": "/static/images/water1.jpg",
                        "note": "Easy to install"
                    },
                    {
                        "name": "Modern Wall Waterfall - Smart Lighting",
                        "features": "Listen to the roar of water with Golden Pearl waterfalls for decor. Indoor waterfall made of high-density fiberglass. Dimensions: Height 150 cm, Width 50 cm.",
                        "placeholder": "/static/images/water2.jpg",
                        "note": "Easy to install"
                    },
                    {
                        "name": "Modern Wall Waterfall - Smart Lighting",
                        "features": "Listen to the roar of water with Golden Pearl waterfalls for decor. Indoor waterfall made of high-density fiberglass. Dimensions: Height 90 cm, Width 68 cm.",
                        "placeholder": "/static/images/water3.jpg",
                        "note": "Easy to install"
                    },
                    {
                        "name": "Modern Wall Waterfall - Smart Lighting",
                        "features": "Listen to the roar of water with Golden Pearl waterfalls for decor. Indoor waterfall made of high-density fiberglass. Dimensions: Height 95 cm, Width 40 cm.",
                        "placeholder": "/static/images/water4.jpg",
                        "note": "Easy to install"
                    }
                ]
            },
            {
                "id": "marble-wood",
                "title": "Decor Materials Section",
                "items": [
                    {
                        "name": "Wood Alternative",
                        "features": "Infill for exterior doors, resistant to water, fire, mold, and bacteria. Special prices for wholesale and retail.",
                        "placeholder": "/static/images/water5.jpg",
                        "note": "Click to preview the 6 textures",
                        "images": [
                            "/static/images/water5.jpg",
                            "/static/images/water6.jpg",
                            "/static/images/water7.jpg",
                            "/static/images/water8.jpg",
                            "/static/images/water9.jpg",
                            "/static/images/water10.jpg"
                        ]
                    },
                    {
                        "name": "Insulated Facade Materials (Heat & Cold)",
                        "features": "Distinguished by high quality and specifications suitable for the Iraqi climate. Special prices — get 25% off all wholesale lists now.",
                        "placeholder": "/static/images/water11.jpg",
                        "note": "Click to preview the 3 textures",
                        "images": [
                            "/static/images/water11.jpg",
                            "/static/images/water12.jpg",
                            "/static/images/water13.jpg"
                        ]
                    },
                    {
                        "name": "Wood Alternative",
                        "features": "More than 50 models to suit all tastes, special prices and very high quality.",
                        "placeholder": "/static/images/water14.jpg",
                        "note": "Click to preview the 3 textures",
                        "images": [
                            "/static/images/water14.jpg",
                            "/static/images/water15.jpg",
                            "/static/images/water16.jpg"
                        ]
                    },
                    {
                        "name": "Marble Alternative",
                        "features": "Marble alternative with new colors and patterns.",
                        "placeholder": "/static/images/water17.jpg",
                        "note": "Click to preview the 3 textures",
                        "images": [
                            "/static/images/water17.jpg",
                            "/static/images/water18.jpg",
                            "/static/images/water19.jpg"
                        ]
                    },
                    {
                        "name": "Luxury Wallpaper",
                        "features": "Marble alternative with new colors and patterns.",
                        "placeholder": "/static/images/water20.jpg",
                        "note": "Click to preview textures",
                        "images": [
                            "/static/images/water20.jpg"
                        ]
                    }
                ]
            },
            {
                "id": "wallpaper",
                "title": "Building Materials Section",
                "items": [
                    {
                        "name": "Under the slogan 'Made in Iraq' - manufacturing gypsum board profiles with the highest quality and precision standards,",
                        "features": "A national product that keeps pace with development and serves your projects with high professionalism, durability, stability, and perfect finishing that meets the needs of decor executors. Your first choice for trust and quality.",
                        "placeholder": "/static/images/water21.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water21.jpg",
                            "/static/images/water22.jpg",
                            "/static/images/water23.jpg",
                            "/static/images/water24.jpg",
                            "/static/images/water25.jpg",
                            "/static/images/water26.jpg",
                            "/static/images/water27.jpg"
                        ]
                    },
                    {
                        "name": "United Boards",
                        "features": "Quality and safety, we challenge with the quality of our product. Many names, the highest is our product name. Wholesale and retail, ready to supply all projects and decor companies. Our prices are special.",
                        "placeholder": "/static/images/water28.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water28.jpg",
                            "/static/images/water29.jpg"
                        ]
                    },
                    {
                        "name": "Exterior Board X Sheets",
                        "features": "Water and moisture resistant, fire resistant.",
                        "placeholder": "/static/images/water30.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water30.jpg",
                            "/static/images/water31.jpg"
                        ]
                    },
                    {
                        "name": "Gypsum Board Lift",
                        "features": "Makes your work easier, easy to operate, increases speed of accomplishment. What are you waiting for?",
                        "placeholder": "/static/images/water32.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water32.jpg",
                            "/static/images/water33.jpg"
                        ]
                    },
                    {
                        "name": "Rock wool from Knauf Germany",
                        "features": "Material: Made from natural basalt rocks re-melted. Thermal conductivity: very low at 0.034 – 0.040 W/m·K. Fire resistance: non-combustible (A1 rating). Withstands temperatures up to 1000°C. High sound absorption capacity. Resistant to moisture, mold, and fungi.",
                        "placeholder": "/static/images/water34.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water34.jpg",
                            "/static/images/water35.jpg",
                            "/static/images/water36.jpg"
                        ]
                    },
                    {
                        "name": "Satin Finish Coating",
                        "features": "From Knauf Germany, made in Turkey.",
                        "placeholder": "/static/images/water37.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water37.jpg"
                        ]
                    },
                    {
                        "name": "Smooth White Waterproof Putty",
                        "features": "For exterior use from Jidar Company.",
                        "placeholder": "/static/images/water38.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water38.jpg"
                        ]
                    },
                    {
                        "name": "Gold Leaf",
                        "features": "Italian, high quality.",
                        "placeholder": "/static/images/water39.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water39.jpg"
                        ]
                    },
                    {
                        "name": "Tape Joint Type ABA",
                        "features": "Special import with high global specifications, width 5 cm, length 90 m, very strong adhesive.",
                        "placeholder": "/static/images/water40.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water40.jpg"
                        ]
                    },
                    {
                        "name": "Tape Joint Type United Saudi",
                        "features": "Width 5 cm, length 90 m, very strong adhesive.",
                        "placeholder": "/static/images/water41.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water41.jpg"
                        ]
                    },
                    {
                        "name": "Laser Level from BOSCH",
                        "features": "Four lines, range 50 m.",
                        "placeholder": "/static/images/water42.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water42.jpg",
                            "/static/images/water43.jpg",
                            "/static/images/water44.jpg"
                        ]
                    },
                    {
                        "name": "Laser Level DEWALT Red Laser",
                        "features": "Long range up to 50 m.",
                        "placeholder": "/static/images/water45.jpg",
                        "note": "Click to preview",
                        "images": [
                            "/static/images/water45.jpg",
                            "/static/images/water46.jpg"
                        ]
                    }
                ]
            }
        ]
    }
}

@app.route('/')
def home():
    lang = request.args.get('lang', 'ar')
    if lang not in multilingual_data:
        lang = 'ar'

    direction = 'rtl' if lang in ['ar', 'ku'] else 'ltr'

    return render_template('index.html', lang=lang, dir=direction, content=multilingual_data[lang], info=company_info)

# ➕ التعديل النهائي هنا (تم إضافة os وقراءة المنفذ)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)