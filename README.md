# 🦙 Llama Mahalliy Chat Interfeysi

Llama AI yordamida mahalliy chat interfeysi. Bu loyiha Streamlit va mahalliy Llama modellarini ishlatadi.

## 🚀 Loyihani ishga tushirish

### Talablar

- Python 3.8 yoki undan yuqori
- Kamida 16GB RAM (32GB tavsiya etiladi)
- NVIDIA GPU CUDA qo'llab-quvvatlash bilan (ixtiyoriy, tezroq natija uchun)
- Git va Make (llama.cpp uchun)

### O'rnatish

1. **Loyihani klonlash**
   ```bash
   git clone https://github.com/mustafoyev202/Llama_Chatbot
   cd Llama
   ```

2. **Kerakli kutubxonalarni o'rnatish**
   ```bash
   pip install -r requirements.txt
   ```

3. **llama.cpp yuklab olish va o'rnatish**
   ```bash
   git clone https://github.com/ggerganov/llama.cpp.git
   cd llama.cpp
   make
   cd ..
   ```

4. **Model yuklab olish**
   ```bash
   python download.py
   ```

5. **Ilovani ishga tushirish**
   ```bash
   streamlit run app.py
   ```

Ilova `http://localhost:8501` manzilida ochiladi.

## 🤖 Qaysi model tanlangan va nima uchun

### Llama 4 Scout 17B Modeli

**Nima uchun tanlangan:**
- **Yuqori sifatli natijalar**: 17B parametrli model katta hajmdagi ma'lumotlar asosida o'qitilgan
- **Tezkor ishlash**: Optimallashtirilgan arxitektura tufayli tez javob beradi
- **Mahalliy ishlash**: Internetga bog'liq emas, xavfsizlik ta'minlanadi
- **Ko'p tilli qo'llab-quvvatlash**: O'zbek tilini ham yaxshi tushunadi
- **Xavfsizlik**: Barcha ma'lumotlar mahalliy kompyuteringizda saqlanadi

**Texnik xususiyatlar:**
- **Parametrlar soni**: 17 milliard
- **Kontekst o'lchami**: 16,384 token
- **Kvantlash**: IQ2_XXS (yuqori siqish)
- **Hajmi**: ~2.5GB
- **Ishlash tezligi**: GPU bilan 10-20 token/s, CPU bilan 2-5 token/s

### Model tanlash sabablari

1. **Sifat va tezlik balansi**: 17B model katta hajmdagi ma'lumotlar asosida o'qitilgan, lekin optimallashtirilgan
2. **Mahalliy ishlash**: Internetga bog'liq emas, ma'lumotlar xavfsizligi ta'minlanadi
3. **O'zbek tilini qo'llab-quvvatlash**: Ko'p tilli model sifatida o'zbek tilini ham yaxshi tushunadi
4. **Tezkor natija**: Optimallashtirilgan arxitektura tufayli tez javob beradi
5. **Xavfsizlik**: API kalitlariga ehtiyoj yo'q, barcha ma'lumotlar mahalliy

## 💬 Suhbat namunalari

### Namuna 1: Dasturlash haqida

**Foydalanuvchi:** Python dasturlash tilini o'rganishni boshlash uchun qanday maslahat berasiz?

**Llama:** Python dasturlash tilini o'rganish uchun quyidagi bosqichlarni tavsiya qilaman:

1. **Asosiy tushunchalar**: O'zgaruvchilar, ma'lumotlar turlari, operatorlar
2. **Kontrollar**: if/else, for/while tsikllari
3. **Funksiyalar**: Parametrlar, qaytarish qiymatlari
4. **Ro'yxatlar va lug'atlar**: Ma'lumotlar strukturasi
5. **Fayllar bilan ishlash**: O'qish va yozish
6. **Xatolarni boshqarish**: try/except bloklari

Boshlash uchun oddiy loyihalar: kalkulyator, ro'yxat boshqaruvchisi, o'yinlar.

### Namuna 2: Sun'iy intellekt haqida

**Foydalanuvchi:** Sun'iy intellekt kelajakda qanday ta'sir qiladi?

**Llama:** Sun'iy intellekt kelajakda quyidagi sohalarga ta'sir qiladi:

**Ijobiy ta'sirlar:**
- Avtomatlashtirilgan ishlar va samaradorlik oshishi
- Tibbiyotda aniq tashxis va davolash
- Ta'limda shaxsiylashtirilgan o'qitish
- Ilmiy tadqiqotlarda yangi kashfiyotlar

**Ehtiyotkorlik:**
- Ish o'rinlari o'zgarishi va yangi kasblar paydo bo'lishi
- Ma'lumotlar xavfsizligi va shaxsiy hayot himoyasi
- AI tizimlarining adolatli va halol ishlashi

Muhimi - AI insoniyat manfaatlari uchun ishlatilishi kerak.

## 🛠️ Texnik ma'lumotlar

### Loyiha strukturasi
```
Llama/
├── app.py                 # Asosiy Streamlit ilovasi
├── download.py            # Model yuklab olish skripti
├── requirements.txt       # Kerakli kutubxonalar
├── config.py              # Sozlamalar
├── utils.py               # Yordamchi funksiyalar
├── README.md              # Bu fayl
├── .gitignore             # Git ignore qoidalari
├── LICENSE                # Litsenziya
├── setup.py               # O'rnatish skripti
├── Makefile               # Loyiha boshqaruvi
├── scripts/               # Qo'shimcha skriptlar
│   ├── setup.py          # Avtomatik o'rnatish
│   └── check_system.py   # Tizim tekshiruvi
└── llama_models/          # Yuklab olingan modellar
    └── Llama-4-Scout-17B/
        └── Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf
```

### Ishlatilgan texnologiyalar
- **Streamlit**: Web interfeys uchun
- **llama.cpp**: Mahalliy model ishlashi uchun
- **Python**: Asosiy dasturlash tili
- **Hugging Face**: Model yuklab olish uchun

## ⚙️ Sozlamalar

### Model parametrlari
- **Temperature**: 0.6 (tasodifiylik darajasi)
- **Top-p**: 0.9 (nukleus namunalash)
- **Context size**: 16384 token
- **Threads**: 16 (CPU yadrolari)

### GPU sozlamalari
- **GPU layers**: 99 (GPU'da ishlaydigan qatlamlar)
- **GPU acceleration**: Mavjud bo'lsa avtomatik yoqiladi

## 🐛 Muammolarni hal qilish

### Keng tarqalgan muammolar

1. **Xotira yetishmovchiligi**
   - RAM'ni kamaytiring: `--ctx-size 8192`
   - Kichikroq model ishlating
   - GPU'ni yoqing

2. **Sekin ishlash**
   - GPU acceleration yoqing
   - Threads sonini oshiring
   - SSD disk ishlating

3. **Model yuklanmagan**
   - Internet aloqasini tekshiring
   - Disk joyini tekshiring (5GB kerak)
   - `python download.py` qayta ishga tushiring

### Ishlash tezligini oshirish

- **SSD disk ishlating**: Model yuklash tezroq bo'ladi
- **GPU acceleration yoqing**: 10-20 barobar tezroq
- **Threads sonini optimallashtiring**: CPU yadrolari soniga qarab
- **Kichikroq kontekst ishlating**: Xotira tejaydi

## 🤝 Hissa qo'shish

1. Loyihani fork qiling
2. Yangi branch yarating
3. O'zgarishlarni qiling
4. Pull request yuboring

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.

## 📞 Yordam

Savollar yoki muammolar bo'lsa, GitHub'da issue oching.

## 🙏 Minnatdorchilik

- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Samarali mahalliy ishlash uchun
- [Streamlit](https://streamlit.io/) - Web interfeys uchun
- [Hugging Face](https://huggingface.co/) - Model hosting uchun
- [Unsloth](https://github.com/unslothai) - Optimallashtirilgan model uchun 
