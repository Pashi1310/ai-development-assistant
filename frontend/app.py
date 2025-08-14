import streamlit as st

st.set_page_config(page_title="AI Dev Assistant", page_icon="🤖")

st.title("🤖 AI Development Assistant")
st.write("Welcome to your AI Development Assistant!")

# Sidebar
with st.sidebar:
    st.header("Tools")
    tool = st.selectbox("Choose:", ["Code Analyzer", "Generator"])

if tool == "Code Analyzer":
    st.header("📊 Code Analyzer")
    code = st.text_area("Enter your code:", height=200)
    
    if st.button("Analyze"):
        if code:
            st.success("✅ Analysis complete!")
            st.metric("Lines", len(code.split('\n')))
        else:
            st.error("Please enter code!")

else:
    st.header("⚡ Code Generator")
    desc = st.text_input("Describe what you want:")
    if st.button("Generate"):
        if desc:
            st.code("def example():\n    return 'Generated code'")
        else:
            st.error("Please describe your request!")
