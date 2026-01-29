import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Variable declaration
bio_text = ""
datafile = pd.read_csv('MatriarchData.csv')

st.set_page_config(
    page_title="Stella Research",  # This is the text in the browser tab
    page_icon="https://img.freepik.com/premium-psd/model-spaceship-with-space-ship-it_911060-119752.jpg",                     # This is the icon (can be an emoji or file path)
    layout="wide"                       # Optional: Makes the content stretch to full width
)

with st.sidebar:
    st.title("Christoffel Schoeman") 
    st.write("**Role:** Stellar Vehicle Design and Robotic analysis")
    st.write("**Current Qualificaition:** Honours in Physics")
    
    st.divider()
    
    # Navigation
    page = st.radio("Models and Data:", ["Home","Bio-Molecular Integrity", "Robotic Telemetry"])
if page == "Bio-Molecular Integrity":
    st.header('Bio-Molecular Integrity')
    
if page == "Home":
    
    st.title("Astrophysics research at the Stella Montis Development,Research and Preservation facility")
    st.image(
        "https://i.redd.it/new-images-from-the-nexon-site-v0-j7t346wc94vf1.png?width=1920&format=png&auto=webp&s=854b834b36261c6ec3328c678796bebfa673b0c7",
        caption="Stella Montis preservation and research facility"
    )
    intro_text = """
    Here at Stella Montis, we specialise in the development of stellar vehicles capable of holding thousands of individuals
    in journeys across the stars. 

    My specialisation lies in designing vessels that allow for near light-speed travel while maintaining bio-molecular 
    structures of living tissue, as well as data analysis of robotic creations specialised in collection of various 
    valuable substances and extermination of hostile fauna on Earth-like celestial bodies.
    """
    st.write(intro_text)

if page == "Bio-Molecular Integrity":
    st.image(
        "https://pbs.twimg.com/media/D5qPhpqW4AEgmGl.jpg",
        caption = "Exodus Maroon: Colony ship"
        )
    bio_text = """
    Careful relativistic research has shown that organic material degrades as 
    the specimen approaches the speed of light. 
    
    Thus, at v (velocity) = 0, an organism is at 100% integrity, but as they approach light speed
    their integrity degrades. This can be described mathematically by the Lorenzts factor, with I being the 
    biological integrity at certain speeds.
    """
    st.write(bio_text)
    st.latex(r"I = I_0 \sqrt{1-\frac{v^2}{c^2}}")
    st.write(
        """
        The following is graphical represtations of how the changing speed impacts the integrity of the 
        organism.
        """
        )
    
    st.write("Use this slider to change the fractional speed")
    v = st.slider("Target Velocity (Fraction of c)", 0.0, 0.999, 0.5)
    
    integrity = 100*(np.sqrt(1-v**2))
    vPlot = np.linspace(0, 0.99, 100)
    iPlot = 100*(np.sqrt(1-vPlot**2))
    fig,ax = plt.subplots()
    
    ax.plot(vPlot, iPlot, label = 'Integrity')
    ax.plot(v,integrity,'ro')
    ax.set_xlabel("Fractional speed of light (c)")
    ax.set_ylabel("Integrity of biological matter (I)")
    ax.grid()
    st.pyplot(fig)

if page == "Robotic Telemetry":
    
    st.image(
        "https://arcraiders.wiki/w/images/thumb/4/49/ARC_Matriarch.png/348px-ARC_Matriarch.png.webp",
        caption = "Matriarch model, designed for securing and forifying large sections of area"
        )
    st.write(
        """
        This analysis of robotic performance focuses primarily on the robot model
        called "Matriarch" and its orbtial descent procedure. This holds telemetry based on
        shield integrity during descent, core temperature during descent and seismic activity measured on planetoid
        surface as descent proceeds.
        """
        )
    
    st.dataframe(datafile)
    st.write("The table above documents key measurements of matriarch orbital descent.")
    altitude = datafile['altitude_m']
    temp = datafile['core_temp_k']
    shield = datafile['shield_integrity']
    
    fig1,ax = plt.subplots()
    ax.plot(altitude, temp)
    ax.invert_xaxis()
    ax.set_xlabel('Altitude (m)')
    ax.set_ylabel('Core temperature (K)')
    ax.grid()
    st.pyplot(fig1)
    st.caption('Figure 1: Line graph showing change in temperature during Matriarch Orbital Descent')
    
    st.write(
        """
        This graph demonstrates temperature readings within the core of the Matriarch. Given the material used to
        make this model, it should be able to withstand multiple orbit descents if it can be retrieved
        from planetoid surface, allowing for reusing of models more readily.
        """
        )
    
    fig2,ax = plt.subplots()
    ax.plot(altitude, shield, color = 'red',drawstyle = 'steps-post')
    ax.fill_between(altitude,shield,alpha = 0.3, step = 'post', color = 'red')
    ax.invert_xaxis()
    ax.set_xlabel('Altitude (m)')
    ax.set_ylabel('Shield integrity (%)')
    ax.grid()
    st.pyplot(fig2)
    
    st.caption('Figure 2: Shield integrity during descent')
    st.write(
        """
        While shield integrity is at 75% upon landing, this does pose risks to this model if the planets surface
        is deemed dangerous. Missing 25% of shields upon landing can lead to potential mission failures in severe cases.
        Better shield generates or any different approaches must be considered before full implimentation.
        """
        )
    
    
    
    
    