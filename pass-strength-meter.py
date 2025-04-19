import streamlit as st
import random

st.title("Password Strength Meter")
st.write("Type your password and know its strength and make it stronger")
pass_input = st.text_input("Type Your Password Here")
if pass_input:
    pass_input_length = len(pass_input)
    has_upper = False
    has_lower = False
    has_non_alphnum = False
    has_number = False
    score = "very weak"

    if pass_input_length < 8:
        st.error("Password should be at least 8 characters.")
    elif pass_input_length >= 8:
        score = "weak"
        for char in pass_input:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif not char.isalnum():
                has_non_alphnum = True
            elif char.isdigit():
                has_number = True

        if not has_upper:
            st.error("Password must contain at least one uppercase letter.")
        elif not has_lower:
            st.error("Password must contain at least one lowercase letter.")
        elif not has_non_alphnum:
            st.error("Password must contain at least one symbol (non-alphanumeric character).")
            score = "moderate"
        elif not has_number:
            st.error("Password must contain a number.")
            score = "strong"
        else:
            st.success("Its a Perfect Password")
            score = "very strong"
        if score == "weak":
            st.error(f"Your Score: {score}")
        elif score == "very weak":
            st.warning(f"Your Score: {score}")
        elif score == "moderate":
            st.info(f"Your Score: {score}")
        elif score == "strong":
            st.success(f"Your Score: {score}")
        elif score == "very strong":
            st.success(f"Your Score: {score}")
numbers = [2890, 2390, 7809, 6758, 102, 3234]
symbols = ["@", "#","$","%","^","&", "*", "(", ")", "_", "-", "=", "+"]
texts = ["tjsdfi", "huhghjhj", "yuijkijm", "tyuiojk", "uijkjmk", "qwertty"]
def suggest():
    if pass_input:
        suggestions = f"{pass_input}{random.choice(symbols)}{random.choice(numbers)}" 
        return suggestions
    else:
        suggestions = f"{random.choice(texts)}{random.choice(symbols)}{random.choice(numbers)}"
        return suggestions
st.code(suggest())
st.code(suggest())
st.code(suggest())
st.code(suggest())
