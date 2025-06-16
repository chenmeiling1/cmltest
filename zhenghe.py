import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime


# 设置页面配置
st.set_page_config(
    page_title="多页面展示",
    page_icon='🎡',
    layout="wide"
)
page = st.sidebar.selectbox("选择页面", ["个人简历", "美食数据", "视频", "数字档案"])

if page == "个人简历":
    st.header('🎨个人简历生成器')
    st.text('使用streamlit创建个性化简历')
    #页面分为两份，比例1:2
    c1, c2 = st.columns([1, 2])
    #个人信息输入
    with c1:
        st.subheader('个人信息表')
        w1=st.text_input('姓名',autocomplete='w1')
        w2=st.text_input('职位',autocomplete='w2')
        w3=st.text_input('电话',autocomplete='w3')
        w4=st.text_input('邮箱',autocomplete='w4')
        w5=st.text_input('出生日期',autocomplete='w5')

        #设置下拉选项框
        w6=st.text('性别')
        # 设置标签为“hidden”
        # 设置水平排列
        Sex=st.radio(
            '请选择性别',
            ['男','女'],
            horizontal=True,
            label_visibility='hidden'
        )
        #单行文本输入
        w7=st.text('学历')
        level = st.selectbox(
            '选择学历',
            ['小学', '初中', '高中', '本科','专科'],
            label_visibility='collapsed'
        )
        #多行文本输入
        w8=st.multiselect(
            '语言能力',
            ['中文', '英语', '日语', '韩语'],
       
          )
        w9=st.multiselect(
            '技能（可多选）',
            ['机器学习', 'HTML', 'Python','Java','神经网络'],
        
            )
        #数字输入组件
        year = st.slider('工作经验', 0, 50, 5)
        gz = st.slider(
        '期望薪资范围（元）',
         5000, 50000, (15000, 30000))

        grjj=st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点')

        w10=st.text('每日最佳联系时间')
        #时间选择器
        time = st.selectbox(
            '选择时间',
            ['18:50', '19:30', '20:20', '21:00','21:30'],
            label_visibility='collapsed'
        )
        #上传文件组件
        upload_file=st.file_uploader('上传个人照片',type='jpg')
        if upload_file is not None:
            bytes_data=upload_file.getvalue()
    #设置信息实时预览
    with c2:
        st.subheader("简历实时预览")
        c1,c2=st.columns(2)
        with c1:
            st.write(w1)
            st.write(upload_file)
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
        t1=st.subheader("个人简历")
        st.write(grjj)
        t2=st.subheader("专业技能")
        st.write(w9)

elif page == "美食数据":
   
    # 定义数据,以便创建数据框
    data = {
        '月份': ['01月', '02月', '03月','04月', '05月'],
        '餐厅': ['星艺会尝不忘', '高峰柠檬鸭', '复记老友粉', '好友缘', '西冷牛排店'],
        '类型': ['中餐', '中餐', '快餐', '自助餐', '西餐'],
        '评分': [4.2, 4.5, 4.0, 4.7, 4.3],
   
        '人均消费(元)': [15, 15, 25, 35, 50],
     
        'latitude': [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        'longitude': [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }

    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5,], name='序号')
    # 将新索引应用到数据框上
    df.index = index

    st.header("门店数据")
    # 使用write()方法展示数据框
    st.write(df)

    dg = pd.DataFrame(
        np.random.randn(1000, 2) / [20, 50] + [22.853838, 108.222177],
        columns=['latitude', 'longitude'])
    # 设置索引列的名称
    df.index.name='序号'


    st.subheader('🥬南宁美食地图')
    st.map(df)

    st.header("⭐餐厅评分")
    st.bar_chart(df, x='餐厅',y='评分')

    data1={
        "月份":["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"],
        "星艺会尝不忘":[15,16,19,12,14,25,18,15,17,28,20,17],
        "高峰柠檬鸭":[45,56,39,62,24,45,78,56,47,38,20,77],
        "复记老友粉":[15,17,20,12,15,25,19,13,18,24,19,27],
        "好友缘":[55,66,49,32,54,75,48,65,47,58,30,67],
        "西冷牛排店":[65,76,59,42,74,85,48,55,87,98,40,67],

        }
    df1 = pd.DataFrame(data1)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,], name='序号')
    # 将新索引应用到数据框上
    df1.index = index

    st.header("🍉不同类型餐厅价格")

    st.line_chart(df1, x='月份')


    data2={
        '时间':['0-2','2-4','4-6','6-8','8-10','10-12','12-14','14-16','16-18','18-20','20-22','22-24',],
        '星艺会尝不忘':[0,0,0,0,8,20,35,20,15,20,10,0],
        '高峰柠檬鸭':[0,0,0,0,10,12,20,20,10, 2,0,0],
        '复记老友粉':[0,0,0,5,5,15,40,30,15,15,10,0],
        '好友缘':[0,0,0,0,3,10,9,30,15,10,10,0],
        '西冷牛排店':[0,0,0,0,6,15,30,20,15,10,0,0],
        }
    df2=pd.DataFrame(data2)
    df2.index = index
    st.header("🕣用餐高峰时段")
    st.area_chart(df2, x='时间')

elif page == "视频":
    st.title("🌳streamlit视频播放器")
    st.text('点击下方视频封面选择要播放的视频')
    st.header('视频播放')


    # 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 读取视频数据
    video_obj=[{
            'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title': '兔子和蝴蝶'
    },     {
            'url': 'https://www.w3schools.com/html/movie.mp4',
            'title': '熊'
    },     {
            'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
            'title': '人'
    }]
    st.video(video_obj[st.session_state['ind']]['url'])

    # 显示按钮
    def prevVideo():
        # 点击上一个按钮要做的事
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(video_obj)

    def nextVideo():
        # 点击下一个按钮要做的事
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(video_obj)

    c1, c2 = st.columns(2)

    with c1:
        st.button('上一个', on_click=prevVideo,use_container_width=True)

    with c2:
        st.button('下一个', on_click=nextVideo, use_container_width=True)

    def my_format_func(option):
        return f'{option}'

    st.header("兔子和蝴蝶")
    # 创建一个文本，介绍一下第一个视频
    st.text('描述：可爱的大兔子和美丽的蝴蝶')
    st.text('时长：0:10 | 分类:动画片段')
    st.subheader("视频库")
    st.text('点击图片选择视频')
    name = st.selectbox('按分类筛选：', ['动画片段', '动物世界', '电影片段'], format_func=my_format_func, index=2)
    # 根据返回值不同，选择不同的特色回答
    # 同时应注意返回值不受自定义my_format_func
    if name == '动画片段':
        st.video('https://www.w3school.com.cn/example/html5/mov_bbb.mp4')
        st.write('**兔子和蝴蝶**')
    elif name == '动物世界':
        st.video('https://www.w3schools.com/html/movie.mp4')
        st.write('**熊**')
    else:
        st.video('https://media.w3.org/2010/05/sintel/trailer.mp4')
        st.write('**人**')

else:
    #创建一个标题展示元素，内容是emjio,符号，中文
    st.title('🕶学生 李华-数字档案')
    #标题格式
    st.markdown('#### 🔑基础信息')
    st.markdown('学生ID:NUM-2025-001')
    st.markdown('注册时间：<span style="color:green">2025-10-01 08:30</span>|精神状态：✅正常', unsafe_allow_html=True)
    st.markdown('当前教室：<span style="color:green">实训楼301</span>|安全等级：<span style="color:green">绝密</span>', unsafe_allow_html=True)
    st.subheader('📊 技能矩阵')
    # 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="95%", delta="2%")
    c2.metric(label="Python", value="87%", delta="-1%")
    c3.metric(label="Java", value="68%", delta="-10%")
    st.header("Streamlit课程进度")
    progress_text_1="Streamlit课程进度"
    my_bar=st.progress(0.3,text=progress_text_1)

    st.subheader('📝任务日志')
    # 定义数据,以便创建数据框
    data={
        '日期':['2025-10-01','2025-10-05','2025-10-12'],
        '任务':['学生数字档案','课程管理系统','数据图表展示'],
        '状态':['✅完成','🕒进行中','❌未完成'],
        '难度':["★★☆☆☆","★☆☆☆☆","★★★☆☆"],
}
    # 定义数据框所用的索引
    index=pd.Series([0,1,2])
    # 根据上面创建的data和index，创建数据框
    df=pd.DataFrame(data,index=index)
    st.write(df)
       
    st.subheader('🔐最新代码成果')
    # 创建要显示的Python代码块的内容
    python_code = '''
    def matrix-breach():
        while True:
            if detact_vulnerability():
                exploit()
                return "ACCESS GRANTED"
            else:
                stealth_evade()


    '''
    # 创建一个代码块，用于展示python_code的内容
    # 并设置language为None，即该代码块无语法高亮
    st.code(python_code, language=None)
    st.markdown('<span style="color:green">>>SYSTEM MESSAGE:</span>下一个任务目标已解锁...', unsafe_allow_html=True)
    st.markdown('<span style="color:green">>>TARGET:</span>课程管理系统', unsafe_allow_html=True)
    st.markdown('<span style="color:green">>>COUNTDOWN:</span>2025-06-05 11:10:50', unsafe_allow_html=True)
    st.markdown('系统状态：在线 连线状态：已加密')
