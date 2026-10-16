import streamlit as st
import openai

# إعدادات الصفحة
st.set_page_config(page_title="PivotAI - مستقبل المهنة", page_icon="🚀")

# تصميم الواجهة
st.title("🚀 PivotAI")
st.subheader("اكتشف كيف تنجو من ثورة الذكاء الاصطناعي في 2027")

# إدخال مفتاح API في القائمة الجانبية
api_key = st.sidebar.text_input("أدخل مفتاح OpenAI API الخاص بك", type="password")

job = st.text_input("ما هي وظيفتك الحالية؟", placeholder="مثلاً: محاسب مالي")
skills = st.text_area("ما هي مهاراتك الحالية؟", placeholder="مثلاً: إكسل، تحليل بيانات، لغة إنجليزية...")

if st.button("حلل مستقبلي المهني الآن"):
    if not api_key:
        st.error("من فضلك أدخل مفتاح API في القائمة الجانبية أولاً!")
    elif not job or not skills:
        st.warning("من فضلك املأ جميع الخانات.")
    else:
        try:
            openai.api_key = api_key
            with st.spinner('جاري تحليل سوق العمل لعام 2027...'):
                prompt = f"أنت خبير مهني لعام 2027. المستخدم يعمل كـ {job} ومهاراته هي {skills}. أعطه نسبة خطورة استبداله بالذكاء الاصطناعي، ووظيفة بديلة مقترحة، وخطة تعلم من 3 خطوات. اجعل الإجابة باللغة العربية وبتنسيق جميل ومنظم باستخدام النقاط."
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", 
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
                
                st.success("تم التحليل بنجاح!")
                st.markdown("### 📊 النتيجة:")
                st.write(result)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")

st.markdown("---")
st.caption("تم التطوير بواسطة PivotAI © 2024")
