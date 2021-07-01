import streamlit as st
import math
import pandas as pd
from vpython import *


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    st.title("الشكل الخارجي - External shape")
    shape = st.multiselect("Shape ", ["Sphere", "Cube", "Cylinder", "Round nose", "Sharp nose", "Custom"])
    x = [.2, .5, .6, .7, .72, .75, .8, .9, 1, 1.1, 1.2, 1.3, 1.5, 1.7, 2, 3, 4, 5]
    info = {'index': x}
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    # shape drawing format
    html_design = """<div style="height:{}px;width:{}px;background-image:{};border-radius:{}px {}px {}px 
    {}px;border-left:{};border-top:{};border-bottom:{}"></div> """
    size = st.sidebar.slider('Shape Size', 50, 200, 100)
    if "Sphere" in shape:
        for i in range(len(x)):
            if x[i] > 0.722:
                y0.append(2.1 * math.exp(-1.2 * (x[i] + 0.35)) - 8.9 * math.exp(-2.2 * (x[i] + 0.35)) + 0.92)
            else:
                y0.append(0.45 * x[i] * x[i] + 0.424)
        info.update({'Cd_sphere': y0})
        st.markdown(html_design.format(size, size, "radial-gradient(#F8F9F9,#CACFD2 ,#5F6A6A)", size
                                       , size, size, size, 0, 0, 0), unsafe_allow_html=True)

    if "Cube" in shape:
        for i in range(len(x)):
            if x[i] > 1.150:
                y1.append(2.1 * math.exp(-1.16 * (x[i] + 0.35)) - 6.5 * math.exp(-2.23 * (x[i] + 0.35)) + 1.67)
            else:
                y1.append(0.6 * x[i] * x[i] + 1.04)
        info.update({'Cd_cube': y1})
        if len(shape) > 1:
            st.subheader("")
        st.markdown(html_design.format(size, size, "linear-gradient(45deg,#F8F9F9,#CACFD2 ,#5F6A6A)", 0
                                       , 0, 0, 0, 0, 0, 0), unsafe_allow_html=True)

    if "Cylinder" in shape:
        for i in range(len(x)):
            if x[i] > 1:
                y2.append((.8 * math.exp(-1.16 * (x[i] + 0.35)) - 7 * math.exp(-2.23 * (x[i] + 0.35)) + 1.5))
            else:
                y2.append(0.5 * x[i] * x[i] + .75)
        info.update({'Cd_cylinder': y2})
        if len(shape) > 1:
            st.subheader("")
        st.markdown(
            html_design.format(size, size + size / 2, "linear-gradient(0deg,#5F6A6A,#F8F9F9,#CACFD2 ,#5F6A6A)", 5
                               , 5, 5, 5, 0, 0, 0), unsafe_allow_html=True)
    if "Round nose" in shape:
        for i in range(len(x)):
            if x[i] > 1.2:
                y3.append(3 * math.exp(-1.16 * (x[i] + 0.35)) - 10 * math.exp(-2.23 * (x[i] + 0.35)) + .5)
            else:
                y3.append(0.3 * x[i] * x[i] + .2)
        info.update({'Cd_roundN': y3})
        if len(shape) > 1:
            st.subheader("")
        st.markdown(
            html_design.format(size / 2, size + size / 2, "linear-gradient(0deg,#5F6A6A,#F8F9F9,#CACFD2 ,#5F6A6A)", 0
                               , size / 8, size / 8, 0, 0, 0, 0), unsafe_allow_html=True)
    if "Sharp nose" in shape:
        for i in range(len(x)):
            if x[i] > 1.2:
                y4.append(3.2 * math.exp(-1.16 * (x[i] + 0.35)) - 10 * math.exp(-2.23 * (x[i] + 0.35)) + .25)
            else:
                y4.append(0.2 * x[i] * x[i] + .15)
        info.update({'Cd_sharpN': y4})
        if len(shape) > 1:
            st.subheader("")
        st.markdown(
            html_design.format(0, 0, "blue", 0, 0, 0, 0, str(size + size / 2) + "px solid #CACFD2",
                               str(size / 4) + "px solid transparent",
                               str(size / 4) + "px solid transparent"), unsafe_allow_html=True)
    if "Custom" in shape:
        st.subheader("COMING SOON...")
        if len(shape) > 1:
            st.subheader("")
        L1, L2 = st.beta_columns(2)
        with L1:
            bgcolor2 = st.color_picker("Pick a color", "#00FFAA")
            st.markdown("")
            top_left_border = st.number_input('Top Left Border', 0, 50, 10)
            top_right_border = st.number_input('Top Right Border', 0, 50, 10)

        with L2:
            ratio = st.slider("Ratio", 0.5, 2.0, 1.0)
            bottom_left_border = st.number_input('Bottom Left Border', 0, 50, 10)
            bottom_right_border = st.number_input('Bottom Right Border', 0, 50, 10)

        st.markdown(html_design.format(size * ratio, size / ratio, "linear-gradient(white," + str(bgcolor2) + ")",
                                       top_left_border,
                                       top_right_border, bottom_left_border, bottom_right_border, 0, 0, 0),
                    unsafe_allow_html=True)

    if shape:
        df = pd.DataFrame(info).set_index('index')
        st.subheader("Cd vs mach no.")
        st.line_chart(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sphere(pos=vector(0, 0, 0))

    st.set_page_config("Drag Coeff.", ":flags:", 'centered')
    st.title("Drag Coefficient vs Mach No.")
    st.text("0.0.1 (Privet)")
    st.header("التعليمات - Instructions")
    st.markdown("""<div style="text-align: right"><b> :معامل السحب هي كمية تستخدم في حساب مقاومة مائع لحركة جسم فيه, 
    ولها عدة استخدامات  منها</b> </div> <div style="text-align: right"> قوة الهواء المضاد للسيارة - </div> <div 
    style="text-align: right"> مقاومة الهواء للرصاصة اثناء سيرها، وكذلك الصاروخ - </div> 
    ------------------------------------------------------------------------------------------------------------- 
    <div style="text-align: left"> <b>the drag coefficient is used to quantify the drag or resistance of an object in 
    a fluid environment, it has many application such as:</b> </div> <div style="text-align: left"> - Cars air 
    resistance. </div> <div style="text-align: left"> - Bullet or rocket air resistance. </div>""", True)
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
