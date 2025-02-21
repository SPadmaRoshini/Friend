import streamlit as st

# Set page title and icon
st.set_page_config(page_title="I Love You", page_icon="❤️")


# CSS for styling, animations, and effects
page_bg = """
<style>
body {
    background: linear-gradient(to bottom, #ffdde1, #ee9ca7); /* Soft pink gradient */
    overflow: hidden; /* Prevents scrollbars */
}

.stApp {
    background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    padding: 50px;
    border: 40px solid transparent;
    border-image: url("static/images/heart.png") 30 round; /* Heart border effect */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    position: relative;
}

/* Falling flowers animation */
@keyframes fall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
    50% { transform: translateY(50vh) rotate(180deg); opacity: 0.8; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}

.falling-flower {
    position: absolute;
    font-size: 35px;
    animation: fall 6s infinite;
}

.flower1 { left: 10%; animation-delay: 0s; }
.flower2 { left: 30%; animation-delay: 0s; }
.flower3 { left: 50%; animation-delay: 0s; }
.flower4 { left: 70%; animation-delay: 0s; }
.flower5 { left: 90%; animation-delay: 0s; }

/* Twinkling hearts effect */
@keyframes twinkle {
    0% { opacity: 0.5; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
    100% { opacity: 0.5; transform: scale(1); }
}

.twinkling-heart {
    position: absolute;
    color: #D1001C;
    font-size: 25px;
    animation: twinkle 2s infinite;
}

/* Random positions for twinkling hearts */
.twinkle1 { top: 20%; left: 20%; animation-delay: 0s; }
.twinkle2 { top: 40%; left: 40%; animation-delay: 0s; }
.twinkle3 { top: 60%; left: 60%; animation-delay: 0s; }
.twinkle4 { top: 80%; left: 80%; animation-delay: 0s; }
/* Gradient red text */
.gradient-text {
    background: linear-gradient(to right, #8B0000, #FF0000, #FF6347); /* Dark Red → Bright Red → Soft Red */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    font-size: 50px;
    text-align: center;
    display: inline-block;
}

/* Pulsating text effect for "I Love You" */
@keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.2); opacity: 0.8; }
    100% { transform: scale(1); opacity: 1; }
}

.pulsating-text {
    animation: pulse 2s infinite;
}

/* Fade-in effect for text */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.text-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
    animation: fadeIn 2s ease-in-out;
}
</style>
"""

# Apply the background styling
st.markdown(page_bg, unsafe_allow_html=True)

# Falling flowers (HTML elements)
st.markdown(
    """
    <div class="falling-flower flower1">🌸</div>
    <div class="falling-flower flower2">🌺</div>
    <div class="falling-flower flower3">🌸</div>
    <div class="falling-flower flower4">🌺</div>
    <div class="falling-flower flower5">🌸</div>

    <div class="twinkling-heart twinkle1">💖</div>
    <div class="twinkling-heart twinkle2">💖</div>
    <div class="twinkling-heart twinkle3">💖</div>
    <div class="twinkling-heart twinkle4">💖</div>
    """,
    unsafe_allow_html=True
)

# Main content with adjusted alignment and animations
st.markdown(
    """
    <div class="text-container">
        <h1 class="gradient-text pulsating-text">This is a special place filled with love</h1>
        <h2 class="gradient-text pulsating-text">I Love You ❤️! And I hope You can be Happy Forever~</h2>
        <h2 class="gradient-text">This may not be much, but I created this to let you know that for as long as possible I will always be there with you. Even Though our first meeting was a bit strange you stuck around me for a long time, to be honest I thought that our interaction was going to be fleeting one just like all the other interactions I had with the other players, but well we have are seeing how that's going....So what I'm trying to say is never doubt the fact I want to be your friend, I want be your best friend despite all your flaws and I hope you will consider me as your best friend even with my flaws.</h2>
    </div>
    """,
    unsafe_allow_html=True
)
