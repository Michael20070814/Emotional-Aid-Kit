import streamlit as st
import snownlp as sn

st.set_page_config(
    page_title="Your personal emotional aid kit💊",
    page_icon="❤️",
    layout="centered"
)

st.title("Hi, Baby!")
st.write("I'm your emotional analysis assistant. Although he is straightforward, he understand you well.")
st.write("Tell me your story, and I'll help you.")

user_input = st.text_area("Enter your story here")

if "痛" in user_input or "不想理你" in user_input:
    st.error("You are sad!😭 Launch the first level of the emotional aid kit! 🏥")
    st.progress(100)
    st.markdown("> **Sorry. Although I don't know what had happened, what makes you sad is the fault of the world!(also my faults)**")
    st.markdown("> **But don't worry, I'm here to help you!**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎟️ Exchange a anger-free ticket!"):
            st.toast("You have successfully exchanged a anger-free ticket! Screenshot it and send it to me! Making a difference instantly! 🌟")
    with col2:
        if st.button("📞 Call me!"):
            st.toast("Calling me....(Although I can only display the row of the emoji, but you can call me! 📞")

# Initialize session state for persisting analysis results
if "score" not in st.session_state:
    st.session_state.score = None

if st.button("Send to your protector!"):
    if not user_input:
        st.warning("You still input nothing! Are you angry?🥺")
    else:
        s = sn.SnowNLP(user_input)
        st.session_state.score = s.sentiments

# Display results if we have a score (persists across reruns)
if st.session_state.score is not None:
    score = st.session_state.score
    if score > 0.6:
        st.success(f"Examine result: {int(score * 100)} scores. You are happy! 🎉")
        st.balloons()
    elif score < 0.4:
        st.error(f"Examine result: {int(score * 100)} scores. You are sad!😭 Launch the first level of the emotional aid kit! 🏥")
        st.progress(100)
        st.markdown("> **Sorry. Although I don't know what had happened, what makes you sad is the fault of the world!(also my faults)**")
        st.markdown("> **But don't worry, I'm here to help you!**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎟️ Exchange a anger-free ticket!"):
                st.toast("You have successfully exchanged a anger-free ticket! Screenshot it and send it to me! Making a difference instantly! 🌟")
        with col2:
            if st.button("📞 Call me!"):
                st.toast("Calling me....(Although I can only display the row of the emoji, but you can call me! 📞")
    else:
        st.warning(f"Examine result: {int(score * 100)} scores. You are neutral! 😐")
        st.write("Hug you. Whatever it happens, we are together! 🥰")
        st.write("Advice: go to drink a milk tea! 🥤, or go to listen to a song! 🎵")
