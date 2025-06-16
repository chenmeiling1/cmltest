import streamlit as st
import pandas as pd

# 设置页面配置
st.set_page_config(
    page_title="个人简历",
    page_icon='📄',
    layout="wide"
)
st.header('🎨个人简历生成器')
st.text('使用streamlit创建个性化简历')
c1, c2 = st.columns([1, 2])
with c1:
    st.subheader('个人信息表')
    w1=st.text_input('姓名',autocomplete='w1')
    w2=st.text_input('职位',autocomplete='w2')
    w3=st.text_input('电话',autocomplete='w3')
    w4=st.text_input('邮箱',autocomplete='w4')
    w5=st.text_input('出生日期',autocomplete='w5')


    w6=st.text('性别')
    # 设置标签为“hidden”
    # 设置水平排列
    Sex=st.radio(
        '请选择性别',
        ['男','女'],
        horizontal=True,
        label_visibility='hidden'
    )
    w7=st.text('学历')
    level = st.selectbox(
        '选择学历',
        ['小学', '初中', '高中', '本科','专科'],
        label_visibility='collapsed'
    )

    w8=st.multiselect(
        '语言能力',
        ['中文', '英语', '日语', '韩语'],
       
      )
    
    w9=st.multiselect(
        '技能（可多选）',
        ['机器学习', 'HTML', 'Python','Java','神经网络'],
        
        )
    year = st.slider('工作经验', 0, 50, 5)
    gz = st.slider(
    '期望薪资范围（元）',
    5000, 50000, (15000, 30000))

    st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点')

    w10=st.text('每日最佳联系时间')
    time = st.selectbox(
        '选择时间',
        ['18:50', '19:30', '20:20', '21:00','21:30'],
        label_visibility='collapsed'
    )    


with c2:
    st.subheader("简历实时预览")
    c1,c2=st.columns(2)
    with c1:
        st.write(w1)
        st.write("职位:",w2)
        st.write("电话:",w3)
        st.write("邮箱:",w4)
        st.write("出生日期:",w5)
        
    with c2:
        st.write("性别:",Sex)
        st.write("学历:",level)
        #st.write("语言能力:",w8)
        st.write("工作经验:",year)
        st.write("期望薪资:",gz)
        st.write("每日最佳联系时间:",time)
        st.write("语言能力:",w8)





