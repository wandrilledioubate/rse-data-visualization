import streamlit as st

def display_footer():
    footer_html = """
        <style>
            .footer {
                padding-top: 20px;
                bottom: 0;
                left: 0;
                right: 0;
                padding_bottom: Opx;
                margin_top: 15px;
                position: fixed;
                text-align: center;
                background-color: #0E1116;
            }
            .link {
                color: #3333cc;
                text-decoration: none;
            }
        </style>
        <div class="footer">
            <p>Let's chat with me on <a class="link" href="https://www.linkedin.com/in/wandrilledioubate/" target="_blank">LinkedIn</a> |  📧 : <a class="link" href="mailto:wandrille.dioubate@efrei.net">Email</a>  |  🧑‍💻 : <a class="link" href="https://github.com/wandrilledioubate" target="_blank">Github</a>  | 📞 : (+33) 6 44 39 37 66 </p>
            <p>Code with ❤️ by Wandrille (Data Engineering 1️⃣)</p>
        </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)