import streamlit as st
import random
import time
from generate_for_app import main as generate
from module import GPT2LMHeadModel
import opencc

with st.sidebar:
    st.title("Punchline 筆記本")
    t = st.text_area(label=" ", height=400, label_visibility="collapsed")
    col1, col2 = st.columns([1,1])
    with col2:
        if st.button("儲存", use_container_width=True):
            st.write("儲存成功！")

st.title(":slot_machine: Punchline 製造機 **ft. DeepRapper**")

st.markdown(
    """
<style>
    .st-emotion-cache-janbn0 {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)

option = st.selectbox(
    '你想選擇哪個歌手的風格？',
    ('Gummy B', 'Leo王', 'MC HotDog', 'wannasleep', '熊仔', '瘦子', '蛋堡', '頑童', '高爾宣'))

print(option)
model = GPT2LMHeadModel.from_pretrained(f'model/adl-final model/{option}')
converter = opencc.OpenCC('s2t.json')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("請輸入你的第一句歌詞"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        lines = generate(prompt, model)
        traditional_lines = []
        for line in lines:
            line = converter.convert(line)
            traditional_lines.append(line)
        # result = '\n'.join(traditional_lines)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        time.sleep(1)
        message_placeholder = st.empty()
        full_response = ""
        line = "歡迎來到 Punchline 製造機！你也可以成為韻腳無限總裁~"
        assistant_response = '*'.join(list(line))
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split('*'):
            full_response += chunk
            time.sleep(0.1)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})        
else:
    try:
        with st.chat_message("assistant"):
        
            fully_response = ""
            for line in traditional_lines:
                time.sleep(0.1)
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = '*'.join(list(line))
                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split('*'):
                    full_response += chunk
                    time.sleep(0.1)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                fully_response += full_response + '\n\n'
            st.session_state.messages.append({"role": "assistant", "content": fully_response})
    except:
        pass
        