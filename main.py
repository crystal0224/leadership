import streamlit as st
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title="고민 해결사", page_icon=":sunglasses:")

st.markdown("""
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #333; /* Dark gray color */
        padding: 10px;
        border-radius: 10px;
    }
    .description-box {
        background-color: #f0f0f0; /* Light gray background */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the header
st.markdown('<div class="header">🏆 다른 팀장 고민해결 도와주기 🏆 </div>', unsafe_allow_html=True)

st.markdown("""
    <div class="description-box">
        <p> How to use </br> 1. 좌측에서 조언을 제공할 팀장의 연차를 선택해주세요. </br> 2. [고민 확인]버튼을 누르면 아래에 고민 내용과 조언 작성창이 뜹니다. </br> 3. 다시 한번 [고민 확인]버튼을 누르면 새로운 고민이 나옵니다 </br> </p>
    </div>
    """, unsafe_allow_html=True)

# Load Excel file into DataFrame
df = pd.read_excel("painpoint2.xlsx")

# Define experience level options
seniority_options = ['저연차 팀장', '중간연차 팀장', '고연차 팀장']

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('URL_TO_YOUR_BACKGROUND_IMAGE');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

st.sidebar.markdown("#\n" * 5) 
# Add radio button to select experience level
st.sidebar.subheader("조언해줄 연차 선택하기:")
selected_experience = st.sidebar.radio(" ", seniority_options)
submit_button_left = st.sidebar.button("고민 확인")
# Initialize session state for button click
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

# Modify the button click to update session state
if submit_button_left:
    st.session_state['button_clicked'] = True

# Display random rows based on selected experience level
if submit_button_left:
    st.subheader("선택된 고민은?")
    selected_row = df[selected_experience].sample(n=1)
    with st.expander("고민 내용보기", expanded=True):
        for column_name, cell_value in selected_row.items():
            st.markdown(f"{cell_value}")

    # Add advice section
    st.subheader("고민 조언해주기")
    st.write("다른 팀장님들의 고민에 대해 조언해주시겠어요?")
    advice = st.text_area(" ", height=100)
    submit_button_right = st.button("조언 제출하기")

    if submit_button_right:
        # TODO: Perform the task of saving the input advice
        st.write("조언이 제출되었습니다 : )")