import streamlit as st
from webui_pages.utils import *
from streamlit_option_menu import option_menu
import webui_pages.dialogue.dialogue as dialogue
from webui_pages.dialogue.dialogue import dialogue_page, chat_box
from webui_pages.dialogue import dialogue
from webui_pages.knowledge_base.knowledge_base import knowledge_base_page
import os
import sys
from configs import VERSION
from server.utils import api_address
# from configs.prompt_config import Excel_path, save_path

api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv

    st.set_page_config(
        "Langchain-Chatchat WebUI",
        os.path.join("img", "zhihuikeyanjiaoxue.png"),
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
            'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            'About': f"""欢迎使用 智慧科研教学辅助平台 WebUI {VERSION}！"""
        }
    )

    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        "知识库管理": {
            "icon": "hdd-stack",
            "func": knowledge_base_page,
        },
}
    with st.sidebar:
            st.image(
                os.path.join(
                    "img",
                    "logo-zhihuikeyanjiaoxue.png"
                ),
                use_column_width=True
            )
            st.caption(
                f"""<p align="right">当前版本：{VERSION}</p>""",
                unsafe_allow_html=True,
            )
            options = list(pages)
            icons = [x["icon"] for x in pages.values()]

            default_index = 0
            selected_page = option_menu(
                "",
                options=options,
                icons=icons,
                # menu_icon="chat-quote",
                default_index=default_index,
            )
            # file_uploader = st.file_uploader("选择本地文件",type=["csv","txt","xlsx"])
            # if file_uploader is not None:
            #     local_path = "/home/root1/wcc/Langchain-Chatchat/save_excel"
            #     os.makedirs(local_path,exist_ok=True)
            #     filename = file_uploader.name
                
            #     dialogue.NAME_EXCEL = filename
            #     with open(os.path.join(local_path, filename),"wb") as f:
            #         f.write(file_uploader.read())
            #     st.success(f"文件成功保存到 {local_path}/{filename} ")
                
            #     Excel_path = os.path.join(local_path, filename)
            #     last_dot_index = Excel_path.rfind(".")
            #     #如果找到了点，截取文件名
            #     if last_dot_index != -1:
            #         file_name_without_extension = Excel_path[:last_dot_index]
            #     else:
            #         # 如果没有找到点，整个字符串都是文件名
            #         file_name_without_extension = Excel_path
            #     save_path = file_name_without_extension + ".png"
    if selected_page in pages:
        pages[selected_page]["func"](api=api, is_lite=is_lite)
