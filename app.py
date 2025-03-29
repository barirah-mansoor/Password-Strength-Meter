import streamlit as st

# Custom style for background and text
st.markdown(
    """
    <style>
    .stApp {
        background: rgb(242,236,171);
        background: linear-gradient(90deg, rgba(242,236,171,1) 0%, rgba(156,236,235,1) 59%);
        color: #1F2937;
    }
    h1, h2, h3 {
        color: #4caf50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "❌😂 Weak", "red", "Adding special characters (#$%!*) will make it stronger."
    elif len(password) < 10:
        return "⚡😎 Moderate", "orange", "Making your password longer will improve security."
    else:
        return "✅🤯 Strong", "green", "Nice! Your password looks strong and secure."

st.title("🔒 Easy Password Strength Checker By Barirah Mansoor")
st.write("🎆 Let's check your password strength!")

password = st.text_input("Enter your password HERE 👇:", type="password")

if password:
    strength, color, suggestion = check_password_strength(password)
    st.markdown(
        f"<h2 style='color: {color};'>Password Strength: {strength}</h2>",
        unsafe_allow_html=True
    )
    st.write(f"💡 **Tip:** {suggestion}")