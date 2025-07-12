import streamlit as st
import datetime
from PIL import Image
from streamlit_player import st_player
import base64
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Set page title (Must be the first Streamlit command)
st.set_page_config(page_title="Phosphorus Web Book", layout="wide")




# Sidebar Navigation
st.sidebar.title("Phosphorus: From Alchemy to Agriculture")
pages = [
    "Home",
    "About the Element",
    "Discovery & History",
    "X-ray Photoelectron Spectroscopy Database",
    "Atomic Spectra Data",
    "Other Data",
    "Uses",
    "Phosphorus in the Economy",
    "Environment & Phosphorus",
    "Future Prospects",
    "Sources"
]

selected_page = st.sidebar.radio("Hello, What would you like to know today?", pages)

# Display content based on selection
st.title(selected_page)

if selected_page == "Home":
    st.header("Phosphorus: From Alchemy to Agriculture")
    st.divider()
    image = Image.open("images/1.jpg")
    

    st.write("""
        Welcome to the web book on **Phosphorus**, an essential element that has shaped human history, 
        from its mystical discovery by alchemists to its critical role in modern agriculture and industry.

        This resource serves as a comprehensive guide to the **chemistry, history, applications, 
        and environmental impact** of phosphorus.
        """)
    st.image(image,use_container_width=True)
    st.divider()
    st.subheader("About this Web Book")
    st.write("""
        Inspired by **NIST Chemistry WebBook**, this project aims to present structured and 
        accessible data on phosphorus. Our sections cover:
        - **Discovery & History**: How phosphorus was first isolated and studied.
        - **Spectroscopic Data**: X-ray photoelectron and atomic spectra insights.
        - **Uses & Applications**: From fertilizers to high-tech industries.
        - **Economic & Environmental Impact**: The role of phosphorus in global markets and ecosystems.

        Feel free to navigate through the sections using the sidebar!
        """)
    st.divider()

elif selected_page == "About the Element":
    st.divider()

    st.markdown("### <u>Chemical Properties</u>", unsafe_allow_html=True)
    table_html = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid white;
            padding: 10px;
            text-align: left;
        }
        th {
            display: none;
        }
    </style>
    <table>
        <tr><td><b>Formula</b></td><td>P</td></tr>
        <tr><td><b>Molecular Weight</b></td><td>30.973762</td></tr>
        <tr><td><b>Atomic Number</b></td><td>15</td></tr>
        <tr><td><b>Classification</b></td><td>Pnictogen, Non-metal</td></tr>
        <tr><td><b>Electronic Configuration</b></td><td>1s² 2s² 2p⁶ 3s² 3p³</td></tr>
        <tr><td><b>Group</b></td><td>15</td></tr>
        <tr><td><b>Period</b></td><td>3</td></tr>
        <tr><td><b>Common Oxidation States</b></td><td>+5, +3, -3</td></tr>
        <tr><td><b>Key Isotope</b></td><td>³¹P</td></tr>
        <tr><td><b>State at 20°C</b></td><td>Solid</td></tr>
    </table>
    """

    # Display table
    st.markdown(table_html, unsafe_allow_html=True)

    image = Image.open("images/9.jpg")

    # Convert image to base64
    def image_to_base64(image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")  # Save image as PNG in memory
        return base64.b64encode(buffered.getvalue()).decode()

    # Get base64 string
    image_base64 = image_to_base64(image)

    # Display image using markdown to ensure full width
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" style="width: 100vw; height: auto; border-radius: 0px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #FFB6C1; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
            ">
                <h2 style="color: #AA336A;">DID YOU KNOW?</h2>
                <hr style="border: 2px solid #AA336A; width: 50%; margin: 10px auto;"> 
                <p style="color: #AA336A; font-size: 18px;">
                    <b>Violet phosphorus is a semiconducting allotrope of phosphorus with a layered crystalline structure, exhibiting unique electronic and optoelectronic properties, and is considered the most stable form of phosphorus</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()

    st.markdown("### <u>Allotropes of Phosphorous</u>", unsafe_allow_html=True)
        
    def image_to_base64(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except FileNotFoundError:
            return None
    
    
    phosphorus_data = {
    "White Phosphorus": {
        "Name": "White Phosphorous",
        "Structure": "Discrete P₄ tetrahedra",
        "Diagram": "images/6.jpg",
        "Colour": "White or yellow",
        "Melting Point": "~44°C (317 K)",
        "Stability": "Least stable, highly reactive",
        "Reactivity": "Highly reactive, ignites spontaneously in air",
        "Solubility": "Insoluble in water, soluble in carbon disulfide",
        "Electrical Conductivity": "Non-conductive",
        "Common Uses": "Fertilisers, pesticides, explosives, rat poison",
    },
    "Black Phosphorus": {
        "Name": "Black Phosphorous",
        "Structure": "Corrugated sheets, flaky crystals",
        "Diagram": "images/7.jpg",
        "Colour": "Black",
        "Melting Point": "~44°C (317 K)",
        "Stability": "Most stable of all allotropes",
        "Reactivity": "Inert, does not ignite in air up to 673 K",
        "Solubility": "Insoluble in water, carbon disulfide",
        "Electrical Conductivity": "Conductive",
        "Common Uses": "Biomedical applications, photothermal therapy",
    },
    "Red Phosphorus": {
        "Name": "Red Phosphorous",
        "Structure": "Polymeric chains of P₄ tetrahedra",
        "Diagram": "images/8.jpg",
        "Colour": "Iron-grey",
        "Melting Point": "860 K",
        "Stability": "More stable than white phosphorus",
        "Reactivity": "Less reactive, does not ignite in air",
        "Solubility": "Insoluble in water and carbon disulfide",
        "Electrical Conductivity": "Non-conductive",
        "Common Uses": "Matchsticks, flame retardants, smoke devices",
    },
    }

    # Convert images to Base64 and update dictionary
    for allotrope in phosphorus_data:
        img_base64 = image_to_base64(phosphorus_data[allotrope]["Diagram"])
        if img_base64:
            phosphorus_data[allotrope]["Diagram"] = f'<img src="data:image/png;base64,{img_base64}" width="100">'
        else:
            phosphorus_data[allotrope]["Diagram"] = "Image not found"

    options = list(phosphorus_data.keys())
    st.write("Select Phosphorus Allotropes for Comparison:")
    selection = st.segmented_control(" ", options, selection_mode="multi")

    # Display table if any selection is made
    if selection:
        selected_data = {key: phosphorus_data[key] for key in selection}

        # Convert to DataFrame
        df = pd.DataFrame(selected_data).rename_axis("Property").reset_index()

        # Display table with embedded images
        st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

    st.divider()
    st.markdown("### <u>Phase Diagram</u>", unsafe_allow_html=True)
    phase = Image.open(r"images/phase.png")
    st.image(phase, use_container_width=True)
    st.divider()
    st.markdown("### <u>IUPAC Identifiers & Registry Information</u>", unsafe_allow_html=True)
    st.write("IUPAC Standard InChI: InChI=1S/P")
    st.write("IUPAC Standard InChIKey: OAICVXFJPJFONN-UHFFFAOYSA-N")
    st.write("CAS Registry Number: 7723-14-0")
    st.divider()

elif selected_page == "Discovery & History":
    st.divider()
    # GUESSING THE DATE-----------------
    @st.dialog(" Can you guess the year in which phosphorous was discovered?")
    def guess_year_dialog():
            st.write("Take a guess! In which year was phosphorus discovered?")

            # Input for guessing the year
            guess = st.number_input("Enter a year:", min_value=1000, max_value=2025, value=1800, step=1)

            # Submit button
            if st.button("Submit Guess"):
                if guess == 1669:
                    st.success("Correct! Phosphorus was discovered in 1669 by Hennig Brand.")
                else:
                    st.error(f"Oops! {int(guess)} is incorrect. Try again or check the correct answer below.")

            # Reveal correct answer
            if st.button("Reveal Correct Answer"):
                st.info("Phosphorus was discovered in **1669** by **Hennig Brand**, a German alchemist.")

        # Ask user if they want to guess
    if st.button("TEST YOUR KNOWLEDGE: Do you think you can guess the discovery year of Phosphorous?"):
            guess_year_dialog()


    
    st_player('https://www.youtube.com/watch?v=b5bXTAqep6s')
    st.header("The Discovery of Phosphorus", divider="gray")
    st.markdown("### <u>A Curious Accident</u>", unsafe_allow_html=True)
    st.write(
        "In 1669, a German alchemist named **Hennig Brand** was obsessed with finding the "
        "**Philosopher’s Stone**, a legendary substance that could turn metals into gold. "
        "Alchemy at the time was a mix of science and superstition, and Brand believed that "
        "human urine, rich in mysterious substances, might hold the secret."
    )

    image = Image.open("images/2.jpg")

    # Convert image to base64
    def image_to_base64(image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")  # Save image as PNG in memory
        return base64.b64encode(buffered.getvalue()).decode()

    # Get base64 string
    image_base64 = image_to_base64(image)

    # Display image using markdown to ensure full width
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" style="width: 100vw; height: auto; border-radius: 0px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "So, he **collected gallons of urine**, let it rot for days, and boiled it down to a thick paste. "
        "He then heated this paste until it glowed and, to his amazement, a strange, waxy substance appeared. "
        "It **glowed eerily in the dark**—something never seen before. "
        "This was **phosphorus**, though Brand had no idea of its true significance."
    )

    st.divider()
    st.markdown("### <u>Phosphorus in History</u>", unsafe_allow_html=True)
    st.write(
        "Over time, scientists realized phosphorus was not a magical substance but a crucial element for life. "
        "By the 18th century, it became famous for its **ability to catch fire**, leading to its use in early **matches**."
    )

    st.write(
        "In the 19th and 20th centuries, phosphorus took on a darker role. It was used in **weapons** like incendiary bombs "
        "during wars. But its most important use came in **agriculture**, where farmers learned that phosphorus was essential "
        "for plant growth, leading to the development of **fertilizers** that revolutionized food production."
    )
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #FFB6C1; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
            ">
                <h2 style="color: #AA336A;">DID YOU KNOW?</h2>
                <hr style="border: 2px solid #AA336A; width: 50%; margin: 10px auto;"> 
                <p style="color: #AA336A; font-size: 18px;">
                    <b>In 1669, German alchemist <b>Hennig Brand</b> boiled 50 buckets of urine 
                    while searching for gold—only to find a <b>glowing, waxy substance</b> instead.</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()
    st.markdown("### <u>The Element of Life and Destruction</u>", unsafe_allow_html=True)
    st.write(
        "Phosphorus is strange—it can **glow in the dark, burn intensely, sustain life, or destroy it**. "
        "Today, it's essential for **DNA, bones, and energy in cells (ATP)**. "
        "Ironically, in his quest for gold, Brand had actually discovered something far more valuable—the building block of life itself."
    )

# -----------------------------------------------------------------------------------------------------------------------------------


elif selected_page == "Other Data":
    option = st.selectbox(
    "Select an option:",
    [
        "Gas phase thermochemistry data",
        "Condensed phase thermochemistry data",
        "Phase change data",
        "Reaction thermochemistry data",
        "Gas phase ion energetics data",
        "Ion clustering data"
    ]
    )
    st.divider()
    
    if option == "Gas phase thermochemistry data":

        J_to_cal = 0.239006
        kJ_to_kcal = 0.239006
        use_calories = st.checkbox("Show values in calorie-based units")
        def convert_value(value, factor):
                """Converts value and its uncertainty while preserving format."""
                match = re.match(r"([-+]?\d*\.?\d+)\s*±\s*([-+]?\d*\.?\d+)", value)
                if match:
                    main_value, uncertainty = map(float, match.groups())
                    return f"{main_value * factor:.4f} ± {uncertainty * factor:.4f}"
                else:
                    try:
                        return f"{float(value) * factor:.4f}"
                    except ValueError:
                        return value  # Return as is if conversion fails
        
        data = {
            "Quantity": [
                "ΔfH°gas", "ΔfH°gas", "S°gas,1 bar", "S°gas,1 bar"
            ],
            "Value": [
                "316.5 ± 1.0", "316.39", "163.199 ± 0.003", "163.20"
            ],
            "Units": [
                "kJ/mol", "kJ/mol", "J/mol*K", "J/mol*K"
            ]
        }

        if use_calories:
            data["Value"] = [convert_value(v, kJ_to_kcal) if "kJ" in u else convert_value(v, J_to_cal) for v, u in zip(data["Value"], data["Units"])]
            data["Units"] = ["kcal/mol" if "kJ" in u else "cal/mol*K" for u in data["Units"]]

        df = pd.DataFrame(data)
        st.markdown("### <u>Thermodynamic Properties Table</u>", unsafe_allow_html=True)
    
        st.caption("These values are calculated by 2 different methods.")
        st.dataframe(df, hide_index=True)
        st.divider()

        st.markdown("### <u>Gas Phase Heat Capacity (Shomate Equation)</u>", unsafe_allow_html=True)
        st.latex(r"""
            C_p^\circ = A + B*t + C*t^2 + D*t^3 + \frac{E}{t^2}
        """)
        st.latex(r"""
            H^\circ - H^\circ_{298.15} = A*t + \frac{B*t^2}{2} + \frac{C*t^3}{3} + \frac{D*t^4}{4} - \frac{E}{t} + F - H
        """)
        st.latex(r"""
            S^\circ = A\ln(t) + B*t + \frac{C*t^2}{2} + \frac{D*t^3}{3} - \frac{E}{(2*t^2)} + G
        """)

        st.write("#### Explanation of Variables")
        st.write("- $C_p$ = heat capacity (J/mol*K)")
        st.write("- $H^\circ$ = standard enthalpy (kJ/mol)")
        st.write("- $S^\circ$ = standard entropy (J/mol*K)")
        st.write("- $t$ = temperature (K) / 1000")
        data_constants = {
            "Temperature Range (K)": ["1180.008 - 2200", "2200 - 6000"],
            "A": [20.44403, -2.107549],
            "B": [1.051745, 9.311953],
            "C": [-1.098514, -0.557522],
            "D": [0.377924, -0.020498],
            "E": [0.010645, 29.30064],
            "F": [310.2930, 353.6459],
            "G": [187.7302, 190.4707],
            "H": [316.3903, 316.3903]
        }
        
        if use_calories:
            for key in ["A", "B", "C", "D", "E", "G"]:
                data_constants[key] = [v * J_to_cal for v in data_constants[key]]
            for key in ["F", "H"]:
                data_constants[key] = [v * kJ_to_kcal for v in data_constants[key]]
        df_constants = pd.DataFrame(data_constants)
        st.write("#### Shomate Equation Constants")
        st.dataframe(df_constants, hide_index=True)
        st.divider()

        st.markdown("### <u>Calculate Properties Based on Temperature</u>", unsafe_allow_html=True)
        temp = st.number_input("Enter Temperature (K) between 1180.008 and 6000:", min_value=1180.008, max_value=6000.0, step=0.1)

        if temp:
            t = temp / 1000  
            if temp <= 2200:
                idx = 0  # Use first set of constants
            else:
                idx = 1  # Use second set of constants
            
            A = data_constants["A"][idx]
            B = data_constants["B"][idx]
            C = data_constants["C"][idx]
            D = data_constants["D"][idx]
            E = data_constants["E"][idx]
            F = data_constants["F"][idx]
            G = data_constants["G"][idx]
            H = data_constants["H"][idx]
            
            # Compute values
            Cp = A + B*t + C*t**2 + D*t**3 + E/t**2
            H_val = A*t + (B*t**2)/2 + (C*t**3)/3 + (D*t**4)/4 - E/t + F - H
            S_val = A*np.log(t) + B*t + (C*t**2)/2 + (D*t**3)/3 - E/(2*t**2) + G
            

            st.write(f"**Computed Properties at** {temp} K")
            st.write(f"**Heat Capacity (Cₚ):**  {Cp:.3f} {'cal/mol*K' if use_calories else 'J/mol*K'}")
            st.write(f"**Enthalpy (H° - H°₂₉₈.₁₅):**  {H_val:.3f} {'kcal/mol' if use_calories else 'kJ/mol'}")
            st.write(f"**Entropy (S°):**  {S_val:.3f} {'cal/mol*K' if use_calories else 'J/mol*K'}")
            st.divider()

    
        st.markdown("### <u>Variation of Cₚ with Temperature</u>", unsafe_allow_html=True)
        temperatures = np.linspace(1180.008, 6000, 100)
        Cp_values = []
        for T in temperatures:
            t_temp = T / 1000
            if T <= 2200:
                idx_temp = 0
            else:
                idx_temp = 1
            A_temp = data_constants["A"][idx_temp]
            B_temp = data_constants["B"][idx_temp]
            C_temp = data_constants["C"][idx_temp]
            D_temp = data_constants["D"][idx_temp]
            E_temp = data_constants["E"][idx_temp]
            Cp_temp = A_temp + B_temp*t_temp + C_temp*t_temp**2 + D_temp*t_temp**3 + E_temp/t_temp**2
            # if use_calories:
            #     Cp_temp *= J_to_cal 
            Cp_values.append(Cp_temp)
        
        df_plot = pd.DataFrame({
            "Temperature (K)": temperatures,
            "Heat Capacity":[cp for cp in Cp_values]
        })

        y_label = "Heat Capacity (cal/mol*K)" if use_calories else "Heat Capacity (J/mol*K)"
        st.markdown(f"**X-axis:** Temperature (K)  |  **Y-axis:** {y_label}")
        st.line_chart(
            df_plot.set_index("Temperature (K)"),
            use_container_width=True
        )
    # -----------------------------------------------

    elif option =="Condensed phase thermochemistry data":
        J_to_cal = 0.239006
        kJ_to_kcal = 0.239006
        use_calories = st.checkbox("Show values in calorie-based units")
        def convert_value(value, factor):
                """Converts value and its uncertainty while preserving format."""
                match = re.match(r"([-+]?\d*\.?\d+)\s*±\s*([-+]?\d*\.?\d+)", value)
                if match:
                    main_value, uncertainty = map(float, match.groups())
                    return f"{main_value * factor:.4f} ± {uncertainty * factor:.4f}"
                else:
                    try:
                        return f"{float(value) * factor:.4f}"
                    except ValueError:
                        return value  # Return as is if conversion fails
        
        data = {
            "Quantity": [
                "ΔfH° liquid", "S° liquid, 1 bar", "ΔfH° solid", "S° solid, 1 bar"
            ],
            "Value": [
                "0.62", "43.01", "-17.46", "41.09 ± 0.25"
            ],
            "Units": [
                "kJ/mol", "J/mol*K", "kJ/mol", "J/mol*K"
            ]
        }

        df = pd.DataFrame(data)
        if use_calories:
            df["Value"] = [
                convert_value(val, kJ_to_kcal if unit.startswith("kJ") else J_to_cal)
                for val, unit in zip(df["Value"], df["Units"])
            ]
            df["Units"] = [unit.replace("J", "cal") for unit in df["Units"]]
                           
        st.markdown("### <u>Thermodynamic Properties Table</u>", unsafe_allow_html=True)
        st.caption("Experimental values for different phases.")
        st.dataframe(df, hide_index=True)
        st.divider()
        option2 = st.selectbox(
            "Choose the condensed phase:",
            [
                "Liquid phase",
                "Solid Phase"
            ]
            )
        if option2=="Liquid phase":
            st.markdown("### <u>Liquid Phase Heat Capacity (Shomate Equation)</u>", unsafe_allow_html=True)
            st.latex(r"""
                C_p^\circ = A + B*t + C*t^2 + D*t^3 + \frac{E}{t^2}
            """)
            st.latex(r"""
                H^\circ - H^\circ_{298.15} = A*t + \frac{B*t^2}{2} + \frac{C*t^3}{3} + \frac{D*t^4}{4} - \frac{E}{t} + F - H
            """)
            st.latex(r"""
                S^\circ = A\ln(t) + B*t + \frac{C*t^2}{2} + \frac{D*t^3}{3} - \frac{E}{(2*t^2)} + G
            """)

            st.write("#### Explanation of Variables")
            st.write("- $C_p^\circ$ = heat capacity (J/mol*K)")
            st.write("- $H^\circ$ = standard enthalpy (kJ/mol)")
            st.write("- $S^\circ$ = standard entropy (J/mol*K)")
            st.write("- $t$ = temperature (K) / 1000")
            st.divider()
            data_constants = {
                "Parameter": ["Temperature (K)", "A", "B", "C", "D", "E", "F", "G", "H"],
                "Value": [
                    "317.3 to 1180.008",  # Keep this as a string
                    26.32602,
                    1.041373e-10,  # Convert scientific notation strings to floats
                    -6.121360e-11,
                    1.094033e-11,
                    2.995196e-12,
                    -7.234262,
                    74.86891,
                    0.615002
                ]
            }

            if use_calories:
                for key, index in zip(["A", "B", "C", "D", "E", "G"], [1, 2, 3, 4, 5, 7]):  # Matching indices
                    data_constants["Value"][index] *= J_to_cal  # Corrected dictionary access

                for key, index in zip(["F", "H"], [6, 8]):  # Matching indices
                    data_constants["Value"][index] *= kJ_to_kcal
            df_constants = pd.DataFrame(data_constants)
            st.write("#### Shomate Equation Constants")
            st.dataframe(df_constants, hide_index=True)
            st.divider()

            constant_keys = ["A", "B", "C", "D", "E", "F", "G", "H"]
            constants = {key: data_constants["Value"][index] for key, index in zip(constant_keys, range(1, 9))}
            st.markdown("### <u>Calculate Properties Based on Temperature</u>", unsafe_allow_html=True)
            temp = st.number_input("Enter Temperature (K) between 317.3 and 1180.008:", min_value=317.3, max_value=1180.008, step=0.1)

            if temp:
                t = temp / 1000
                
                # Compute values
                Cp = constants["A"] + constants["B"]*t + constants["C"]*t**2 + constants["D"]*t**3 + constants["E"] / t**2
                H_val = (constants["A"] * t + (constants["B"] * t**2) / 2 + (constants["C"] * t**3) / 3 +
                        (constants["D"] * t**4) / 4 - constants["E"] / t + constants["F"] - constants["H"])
                S_val = (constants["A"] * np.log(t) + constants["B"] * t + (constants["C"] * t**2) / 2 +
                        (constants["D"] * t**3) / 3 - constants["E"] / (2 * t**2) + constants["G"])
                
                # if use_calories:
                #     Cp *= J_to_cal
                #     H_val *= J_to_cal
                #     S_val *= J_to_cal
                
                st.write(f"**Heat Capacity (Cₚ):**  {Cp:.3f} {'cal/mol*K' if use_calories else 'J/mol*K'}")
                st.write(f"**Enthalpy (H° - H°₂₉₈.₁₅):**  {H_val:.3f} {'kcal/mol' if use_calories else 'kJ/mol'}")
                st.write(f"**Entropy (S°):**  {S_val:.3f} {'cal/mol*K' if use_calories else 'J/mol*K'}")
                st.divider()

                st.markdown("### <u>Variation of Cₚ with Temperature</u>", unsafe_allow_html=True)
                temperatures = np.linspace(317.3, 1180.008, 100)
                Cp_values = []
                
                for T in temperatures:
                    t_temp = T / 1000
                    Cp_temp = (constants["A"] + constants["B"]*t_temp + constants["C"]*t_temp**2 +
                            constants["D"]*t_temp**3 + constants["E"] / t_temp**2)
                    
                    
                    Cp_values.append(Cp_temp)
                
                df_plot = pd.DataFrame({
                    "Temperature (K)": temperatures,
                    "Heat Capacity": Cp_values
                })
                
                y_label = "Heat Capacity (cal/mol*K)" if use_calories else "Heat Capacity (J/mol*K)"
                st.markdown(f"**X-axis:** Temperature (K)  |  **Y-axis:** {y_label}")
                st.line_chart(df_plot.set_index("Temperature (K)"), use_container_width=True)
            st.divider()

        if option2 == "Solid Phase":
            st.markdown("### <u>Solid Phase Heat Capacity (Shomate Equation)</u>", unsafe_allow_html=True)
            st.latex(r"""
                C_p^\circ = A + B*t + C*t^2 + D*t^3 + \frac{E}{t^2}
            """)
            st.latex(r"""
                H^\circ - H^\circ_{298.15} = A*t + \frac{B*t^2}{2} + \frac{C*t^3}{3} + \frac{D*t^4}{4} - \frac{E}{t} + F - H
            """)
            st.latex(r"""
                S^\circ = A\ln(t) + B*t + \frac{C*t^2}{2} + \frac{D*t^3}{3} - \frac{E}{(2*t^2)} + G
            """)

            st.write("#### Explanation of Variables")
            st.write("- $C_p^\circ$ = heat capacity (J/mol*K)")
            st.write("- $H^\circ$ = standard enthalpy (kJ/mol)")
            st.write("- $S^\circ$ = standard entropy (J/mol*K)")
            st.write("- $t$ = temperature (K) / 1000")
            st.divider()
            solid_phase_constants = {
                "Phase": ["Red, V Phase", "White Phase", "Red, IV Phase", "Black Phase"],
                "Temperature Range (K)": ["298 to 317.3", "298 to 317.3", "298 to 317.3", "298 to 317.3"],
                "A": [24.32214, 16.45576, 28.04226, 28.38677],
                "B": [-1.809807, 43.28892, -18.96093, -19.14360],
                "C": [7.486431, -58.73876, 36.61209, 36.82476],
                "D": [3.147950, 25.60646, -13.81611, -13.89983],
                "E": [-0.296815, -0.086728, -0.357001, -0.358810],
                "F": [-25.70876, -6.657121, -21.45191, -21.96617],
                "G": [50.77995, 49.97160, 59.26845, 59.11033],
                "H": [-17.46004, 0.000000, -12.43903, -12.85103]
            }

            if use_calories:
                for key in ["A", "B", "C", "D", "E", "G"]:
                    solid_phase_constants[key] = [v * J_to_cal for v in solid_phase_constants[key]]
                for key in ["F", "H"]:
                    solid_phase_constants[key] = [v * kJ_to_kcal for v in solid_phase_constants[key]]
            
            df_solid_constants = pd.DataFrame(solid_phase_constants)

            # Display constants in Streamlit
            st.write("#### Shomate Equation Constants for Solid Phases")
            st.dataframe(df_solid_constants, hide_index=True)
            st.divider()
            st.markdown("### <u>Calculate Properties Based on Temperature</u>", unsafe_allow_html=True)
            temp = st.number_input("Enter Temperature (K) between 298 and 317.3:", min_value=298.0, max_value=317.3, step=0.1)

            if temp:
                t = temp / 1000  # Convert temperature to required scale

                computed_values = []
                for idx, phase in enumerate(df_solid_constants["Phase"]):
                    A, B, C, D, E, F, G, H = df_solid_constants.loc[idx, ["A", "B", "C", "D", "E", "F", "G", "H"]]

                    # Compute properties
                    Cp = A + B*t + C*t**2 + D*t**3 + E/t**2
                    H_val = A*t + (B*t**2)/2 + (C*t**3)/3 + (D*t**4)/4 - E/t + F - H
                    S_val = A*np.log(t) + B*t + (C*t**2)/2 + (D*t**3)/3 - E/(2*t**2) + G

                    computed_values.append([phase, Cp, H_val, S_val])

                # Create DataFrame for calculated values
                df_computed = pd.DataFrame(computed_values, columns=[
                    "Phase", 
                    f"Heat Capacity ({'cal/mol*K' if use_calories else 'J/mol*K'})", 
                    f"Enthalpy ({'kCal/mol' if use_calories else 'kJ/mol'})", 
                    f"Entropy ({'cal/mol*K' if use_calories else 'J/mol*K'})"
                ])
                st.dataframe(df_computed, hide_index=True)
                st.divider()

            # Variation of Cp with Temperature for all phases
            st.markdown("### <u>Variation of Cₚ with Temperature for All Phases</u>", unsafe_allow_html=True)

            temperatures = np.linspace(298, 317.3, 100)
            plt.figure(figsize=(8, 5))

            # Compute Cp for each phase and plot
            for idx, phase in enumerate(df_solid_constants["Phase"]):
                A, B, C, D, E = df_solid_constants.loc[idx, ["A", "B", "C", "D", "E"]]
                
                Cp_values = [A + B*(T/1000) + C*(T/1000)**2 + D*(T/1000)**3 + E/(T/1000)**2 for T in temperatures]
                plt.plot(temperatures, Cp_values, label=phase)

            # Customize plot
            plt.xlabel("Temperature (K)")
            plt.ylabel(f"Heat Capacity ({'cal/mol*K' if use_calories else 'J/mol*K'})")
            plt.title("Heat Capacity Variation for Solid Phases")
            plt.legend()
            plt.grid(True)

            # Display plot in Streamlit
            st.pyplot(plt)
            st.divider()
    # -----------------------------------------------

    elif option == "Phase change data":
        st.write("### Phase change data")
        data = {
            "Quantity": ["T(boil)", "T(triple)", "T(triple)"], 
            "Value": ["550.", "870.", "317.3"],
            "Units": ["K", "K", "K"],
            "Comment": [
                "Uncertainty assigned by TRC = 3. K; TRC",
                "Uncertainty assigned by TRC = 0.6 K; TRC",
                "Metastable crystal phase; Uncertainty assigned by TRC = 0.06 K; TRC"
            ]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)
        st.divider()
        st.markdown("### <u>Antoine Equation for Vapor Pressure</u>", unsafe_allow_html=True)
        st.latex(r"\log_{10}(P) = A - \frac{B}{T + C}")
        st.write("Where:")
        st.latex(r"P = \text{vapor pressure (atm)}")
        st.latex(r"T = \text{temperature (K)}")
        A, B, C = 5.03591, 2819.239, 6.399
        data = {
            "Temperature (K)": ["349.8 to 553."],
            "A": [A],
            "B": [B],
            "C": [C]
        }
        df = pd.DataFrame(data)
        st.write("### Antoine Equation Constants Table")
        st.dataframe(df, hide_index=True)
        option = st.segmented_control("What do you want to calculate?", ["P from T", "T from P"])

        if option == "P from T":
            T = st.number_input("Enter Temperature (K):", min_value=349.8, max_value=553.0, step=0.1)

            if T:
                P = 10 ** (A - (B / (T + C)))  # Antoine equation
                st.write(f"**Vapor Pressure (P):** {P:.5f} atm")

        elif option == "T from P":
            P = st.number_input("Enter Vapor Pressure (atm):", min_value=0.001, step=0.001)

            if P > 0:
                T = (B / (A - np.log10(P))) - C  # Rearranged Antoine equation
                if 349.8 <= T <= 553.0:
                    st.write(f"**Temperature (T):** {T:.2f} K")
                else:
                    st.write("⚠️ Temperature is out of the valid range (349.8 - 553.0 K).")
        st.divider()
        st.markdown("### <u> Vapor Pressure vs. Temperature Graph </u>", unsafe_allow_html=True)

        T_values = np.linspace(349.8, 553.0, 100)
        P_values = [10 ** (A - (B / (T + C))) for T in T_values]
        df_plot = pd.DataFrame({
            "Vapor Pressure (atm)": P_values,
            "Temperature (K)": T_values,
            
        })
        st.markdown("**X-axis:** Temperature (K)  |  **Y-axis:** Vapor Pressure (atm)")
        st.line_chart(df_plot.set_index("Temperature (K)"), use_container_width=True)
     # -----------------------------------------------
    # -----------------------------------------------

    elif option == "Reaction thermochemistry data":  
        J_to_cal = 0.239006
        kJ_to_kcal = 0.239006
        use_calories = st.checkbox("Show values in calorie-based units")
        st.write("### Individual Reactions:")
        reactions = [
            "HP⁻ + P₂ → HP⁻",
            "P₂H⁻ + P → P₂H⁻",
            "OP⁻ + P₂ → OP⁻",
            "P₂O⁻ + P → P₂O⁻"
        ]
        for rxn in reactions:
            st.latex(rxn)
        st.divider()
        def convert_value(value, factor):
            """Converts value and its uncertainty while preserving format."""
            match = re.match(r"([-+]?\d*\.?\d+)\s*±\s*([-+]?\d*\.?\d+)", value)
            if match:
                main_value, uncertainty = map(float, match.groups())
                return f"{main_value * factor:.4f} ± {uncertainty * factor:.4f}"
            else:
                try:
                    return f"{float(value) * factor:.4f}"
                except ValueError:
                    return value
        enthalpy_key = "Enthalpy Change (ΔrH°) [Kcal/mol]" if use_calories else "Enthalpy Change (ΔrH°) [kJ/mol]"

        data = {
            "Reaction": [
                "HP⁻ + P₂ → HP⁻",
                "P₂H⁻ + P → P₂H⁻",
                "OP⁻ + P₂ → OP⁻",
                "P₂O⁻ + P → P₂O⁻"
            ],
            enthalpy_key: [
                "325 ± 35", "354 ± 21", "558.0 ± 3.5", "229.3 ± 3.3"
            ],
            "Reference": [
                "Ervin and Lineberger, 2005", "Jones, Ganteför, et al., 1995",
                "Zittel and Lineberger, 1976", "Snodgrass, Coe, et al., 1985"
            ],
            "Comments": [
                "gas phase", "gas phase; Vertical Detachment Energy: 1.68±0.05 eV",
                "gas phase", "gas phase"
            ]
        }
        if use_calories:
            data[enthalpy_key] = [convert_value(v, kJ_to_kcal) for v in data[enthalpy_key]]

        df = pd.DataFrame(data)
        st.dataframe(df)
    # -----------------------------------------------

    elif option==  "Gas phase ion energetics data":
        J_to_cal = 0.239006
        kJ_to_kcal = 0.239006
        use_calories = st.checkbox("Show values in calorie-based units")
        def convert_value(value, factor):
            """Converts numerical values while preserving format."""
            try:
                return round(float(value) * factor, 4)
            except ValueError:
                return value 

        #table 1
        data1 = {
            "Quantity": ["IE (evaluated)", "Proton affinity (review)", "Gas basicity"],
            "Value": [10.48669, 626.8, 604.8],
            "Units": ["eV", "kcal/mol" if use_calories else "kJ/mol", "kcal/mol" if use_calories else "kJ/mol"],
            "Reference": ["N/A", "Hunter and Lias, 1998", "Hunter and Lias, 1998"]
        }

        if use_calories:
            data1["Value"][1] = convert_value(data1["Value"][1], kJ_to_kcal)
            data1["Value"][2] = convert_value(data1["Value"][2], kJ_to_kcal)
            
        df1 = pd.DataFrame(data1)
        st.table(df1)
        st.divider()
        #table 2
        st.write("### Electron Affinity Determinations:")
        data2 = {
            "EA (eV)": [
                "0.746609 ± 0.000009", "0.746679 ± 0.000062", "0.74640 ± 0.00040",
                "0.750 ± 0.050", "0.74676 ± 0.00040", "0.772 ± 0.052"
            ],
            "Reference": [
                "Pelaez, Blondel, et al., 2011", "Andersson, Lindahl, et al., 2007",
                "Slater and Linberger, 1977", "Jones, Ganteför, et al., 1995",
                "Feldmann, 1976", "Bennett, Margrave, et al., 1974"
            ]
        }
        df2 = pd.DataFrame(data2)
        st.table(df2)
        st.divider()

        #table 3
        st.write("### Ionization Energy Determinations:")
        data3 = {
            "IE (eV)": ["10.48669", "10.49", "10.48669"],
            "Reference": ["Lide, 1992", "Kelly, 1987", "Moore, 1970"]
        }
        df3 = pd.DataFrame(data3)
        st.table(df3) 
        st.divider()       
    # -----------------------------------------------

    elif option== "Ion clustering data":
    
        kJ_to_kcal = 0.239006
        use_calories = st.checkbox("Show values in calorie-based units")
        st.write("### Clustering Reactions:")
        def convert_value(value, factor):
            """Converts numerical values while preserving format."""
            try:
                return round(float(value) * factor, 4)
            except ValueError:
                return value  # If conversion fails, return original

        st.latex(r"( \text{HP}^- \cdot P_2 ) + P \rightarrow \text{HP}^-")
        data1 = {
            "Quantity": ["ΔrH°", "ΔrH°"],
            "Value": ["325. ± 35.", "325. ± 34."],
            "Units": ["kcal/mol" if use_calories else "kJ/mol"] * 2,
            "Reference": ["Ervin and Lineberger, 2005", "Zittel and Lineberger, 1976"],
            "Comment": ["gas phase", "gas phase"]
        }

        if use_calories:
            data1["Value"][0] = f"{convert_value(325, kJ_to_kcal)} ± {convert_value(35, kJ_to_kcal)}"
            data1["Value"][1] = f"{convert_value(325, kJ_to_kcal)} ± {convert_value(34, kJ_to_kcal)}"

        df1 = pd.DataFrame(data1)
        st.table(df1)
        st.divider()
        st.latex(r"( \text{OP}^- \cdot P_2 ) + P \rightarrow \text{OP}^-")
        data2 = {
            "Quantity": ["ΔrH°"],
            "Value": ["558.0 ± 3.5"],
            "Units": ["kcal/mol" if use_calories else "kJ/mol"],
            "Reference": ["Zittel and Lineberger, 1976"],
            "Comment": ["gas phase"]
        }
        
        if use_calories:
            data2["Value"][0] = f"{convert_value(558, kJ_to_kcal)} ± {convert_value(3.5, kJ_to_kcal)}"

        df2 = pd.DataFrame(data2)
        st.table(df2)

elif selected_page == "Atomic Spectra Data":
    popover = st.popover("Filter")
    line = popover.checkbox("Line Holdings", True)
    level = popover.checkbox("Level Holdings", True)
    ground = popover.checkbox("Ground States & Ionization Energies", True)

    if line:
        st.write("### Line Holdings:")
        data = {
            "Ion": [
                "P I", "P II", "P III", "P IV", "P V", "P VI", "P VII", "P VIII",
                "P IX", "P X", "P XI", "P XII", "P XIII", "P XV"
            ],
            "No. of lines": [258, 100, 70, 129, 48, 5, 3, 20, 47, 26, 18, 16, 45, 137],
            "Lines with transition probabilities": [132, 73, 23, 78, 30, 5, 3, 20, 47, 26, 18, 16, 14, 137],
            "Lines with level designations": [133, 73, 23, 78, 30, 5, 3, 20, 47, 26, 18, 16, 45, 137]
        }
        df = pd.DataFrame(data)
        total_row = pd.DataFrame({
            "Ion": ["**Total**"],
            "No. of lines": [df["No. of lines"].sum()],
            "Lines with transition probabilities": [df["Lines with transition probabilities"].sum()],
            "Lines with level designations": [df["Lines with level designations"].sum()]
        })

        df = pd.concat([df, total_row], ignore_index=True)

        st.table(df.set_index("Ion"))
        st.divider()

    if level:
        st.write("### Level Holdings:")
        data = {
            "Ion": [
                "P I", "P II", "P III", "P IV", "P V",
                "P VI", "P VII", "P VIII", "P IX", "P X",
                "P XI", "P XII", "P XIII", "P XIV", "P XV"
            ],
            "No. of levels": [289, 162, 129, 211, 68, 60, 62, 65, 48, 58, 49, 61, 36, 111, 128]
        }
        df = pd.DataFrame(data)
        total_row = pd.DataFrame({
            "Ion": ["**Total for P:**"],
            "No. of levels": [df["No. of levels"].sum()]  # Sum levels dynamically
        })
        df = pd.concat([df, total_row], ignore_index=True)
        st.table(df.set_index("Ion"))
        st.divider()

    if ground:
        st.write("### Ground States & Ionization Energies:")
        data = {
            "At. Num.": [15] * 14,
            "El. name": ["Phosphorus"] * 14,
            "Isoel. Seq.": ["P", "Si", "Al", "Mg", "Na", "Ne", "F", "O", "N", "C", "B", "Be", "Li", "He"],
            "Ground Shells": [
                "[Ne]3s²3p³", "[Ne]3s²3p²", "[Ne]3s²3p", "[Ne]3s²", "[Ne]3s",
                "1s²2s²2p⁶", "1s²2s²2p⁵", "1s²2s²2p⁴", "1s²2s²2p³", "1s²2s²2p²",
                "1s²2s²2p", "1s²2s²", "1s²2s", "1s²"
            ],
            "Ground Level": [
                "⁴S°₃/₂", "³P₀", "²P°₁/₂", "¹S₀", "²S₁/₂", 
                "¹S₀", "²P°₃/₂", "³P₂", "⁴S°₃/₂", "³P₀", 
                "²P°₁/₂", "¹S₀", "²S₁/₂", "¹S₀"
            ],
            "Ionization Energy (eV)": [
                10.486686, 19.76949, 30.20264, 51.44387, 65.02511, 
                220.430, 263.57, 309.60, 372.31, 424.40, 
                479.44, 560.62, 611.741, 2816.90868
            ],
            "Uncertainty (eV)": [
                0.000015, 0.00004, 0.00009, 0.00012, 0.00012, 
                0.005, 0.06, 0.10, 0.21, 0.09, 
                0.05, 0.10, 0.007, 0.00019
            ],
            "References": [
                "L5148", "L11770", "L7147", "L7147", "L7147, L2613",
                "L11770", "L7147", "L7147", "L11770", "L11770",
                "L11770", "L11770", "L16264c99", "L21139"
            ]
        }

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Display table
        st.table(df)
        st.info("**[Ne] = 1s²2s²2p⁶**")
        st.divider()

elif selected_page == "X-ray Photoelectron Spectroscopy Database":
    option3 = ["White Phosphorus", "Red Phosphorus", "Black Phosphorus"]
    selected_option3 = st.radio("Choose one:", option3)
    if selected_option3=="Black Phosphorus":
        data = {
                "Spectral Line": ["1s", "2p₃/₂", "2s", "AP-2p, KL₂₃L₂₃(¹D)", "KL₂₃L₂₃(¹D)"],
                "Energy (eV)": [2143.80, 130.25, 187.85, 1987.30, 1857.05]
            }
        df = pd.DataFrame(data)
        st.dataframe(df)

    elif selected_option3=="Red Phosphorus":
        data_red_phosphorus = {
            "Spectral Line": ["1s", "2p₃/₂", "2p₃/₂", "2s", "AP-2p, KL₂₃L₂₃(¹D)", "KL₂₃L₂₃(¹D)"],
            "Energy (eV)": [2144.00, 130.90, 130.45, 188.05, 1986.75, 1856.30]
        }
        df_red = pd.DataFrame(data_red_phosphorus)
        st.dataframe(df_red)
    elif selected_option3=="White Phosphorus":
        data = {
            "Spectral Line": [
                "1s", "2p₃/₂", "2p₁/₂", "2p₃/₂", "2s", "KL₂₃L₂₃(¹D)", 
                "AP-2p, KL₂₃L₂₃(¹D)", "DS-2p", "SA-KL₁L₁(¹S)", "SA-KL₁L₂₃(¹P)", 
                "SA-KL₁L₂₃(³P)", "SA-KL₂₃L₂₃(¹S)"
            ],
            "Energy (eV)": [
                2145.00, 130.50, 130.30, 129.80, 188.00, 1857.50, 
                1988.00, 0.85, -115.50, -65.00, -46.00, -7.50
            ]
        }
        df = pd.DataFrame(data)
        st.dataframe(df)

elif selected_page =="Uses":
    st.divider()
    image_path = r"images/uses.png"
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
    st.divider()

    st.header("1. Agriculture")
    col1, col2 = st.columns(2)

    with col1:
        image1 = Image.open(r"images/fertilizer.jpg")
        st.image(image1, use_container_width=True)

    with col2:
        st.markdown("""
        Phosphorus is a vital nutrient in agriculture, primarily used in fertilizers to enhance crop growth and soil fertility. 
        It plays a crucial role in **energy transfer (ATP), root development, and flowering**. Phosphorus-based fertilizers such as 
        **superphosphate, triple superphosphate (TSP), diammonium phosphate (DAP), monoammonium phosphate (MAP), and rock phosphate** 
        are commonly used to improve yields. These fertilizers provide essential nutrients that support strong root systems, enhance 
        flowering and seed production, and improve plant resistance to diseases and environmental stress. However, excessive use can 
        lead to **soil imbalance and water pollution through eutrophication**. To ensure sustainable agriculture, farmers are encouraged 
        to adopt **precision farming techniques and controlled-release fertilizers**, optimizing phosphorus use while maintaining 
        long-term soil health.
        """)

    st.divider()

    # Animal Feed Supplements Section
    st.header("2. Animal Feed Supplements")
    col1, col2 = st.columns(2)

    with col2:
        image2 = Image.open(r"images/animal.jpg")
        st.image(image2, use_container_width=True)

    with col1:
        st.markdown("""
        Phosphorus is a crucial mineral in animal nutrition, essential for **bone formation, energy metabolism, and overall growth**. 
        It plays a key role in **DNA synthesis, enzyme activation, and maintaining acid-base balance** in livestock. To meet dietary 
        requirements, phosphorus is often added to animal feed in the form of supplements such as **dicalcium phosphate (DCP) and 
        monocalcium phosphate (MCP)**. These supplements enhance **skeletal strength, improve reproductive performance, and support 
        muscle development** in poultry, cattle, and swine. However, excessive phosphorus intake can lead to **environmental concerns**, 
        such as water pollution from animal waste runoff. Therefore, balanced supplementation and efficient phosphorus utilization 
        strategies are essential to promote animal health while minimizing ecological impact.
        """)

    st.divider()

    # Detergents and Cleaning Products Section
    st.header("3. Detergents and Cleaning Products")
    col1, col2 = st.columns(2)

    with col1:
        image3 = Image.open(r"images/detergenet.jpeg")
        st.image(image3, use_container_width=True)

    with col2:
        st.markdown("""
        Phosphorus compounds, particularly **phosphates**, are widely used in **detergents and cleaning products** due to their 
        ability to **soften water and enhance cleaning efficiency**. Phosphates help **break down grease, remove stains, and prevent 
        dirt from redepositing** on clothes or surfaces. They are especially useful in laundry and dishwashing detergents. However, 
        excessive phosphorus runoff from wastewater can lead to **eutrophication**, causing harmful algal blooms in water bodies. 
        To address this, many regions have implemented **restrictions on phosphate-based detergents**, promoting the use of 
        environmentally friendly alternatives.
        """)

    st.divider()

    # Food and Drink Additives Section
    st.header("4. Food and Drink Additives")
    col1, col2 = st.columns(2)

    with col2:
        image4 = Image.open(r"images/food.jpg")
        st.image(image4, use_container_width=True)

    with col1:
        st.markdown("""
        Phosphorus is a key ingredient in many **food and drink additives**, where it serves as a **preservative, acidity regulator, 
        and texture enhancer**. **Phosphates** are commonly added to processed meats, dairy products, and carbonated beverages to 
        **maintain freshness, improve texture, and extend shelf life**. They also play a role in **enhancing the baking properties 
        of flour and stabilizing emulsions in processed foods**. While phosphorus is essential for human health, excessive intake 
        from processed foods has raised concerns about **potential health risks, such as kidney disease and cardiovascular issues**, 
        prompting discussions on dietary balance.
        """)

    st.divider()

    # Uses in Metal Production Section
    st.header("5. Uses in Metal Production")
    col1, col2 = st.columns(2)

    with col1:
        image5 = Image.open(r"images/metal.jpeg")
        st.image(image5, use_container_width=True)

    with col2:
        st.markdown("""
        Phosphorus is used in **metal production**, particularly in the **steel and aluminum industries**, to improve mechanical 
        properties. In steelmaking, **phosphorus is added to enhance strength, hardness, and corrosion resistance**, making it 
        essential for manufacturing **automobile parts, structural components, and high-strength alloys**. However, excessive 
        phosphorus in steel can lead to **brittleness**, so its concentration must be carefully controlled. Additionally, 
        phosphorus-based chemicals are used in metal surface treatments, such as **phosphating**, to **prevent rust and improve 
        paint adhesion** in industrial applications.
        """)

    st.divider()

    # Water Treatment Section
    st.header("6. Water Treatment")
    col1, col2 = st.columns(2)

    with col2:
        image6 = Image.open(r"images/water.jpeg")
        st.image(image6, use_container_width=True)

    with col1:
        st.markdown("""
        Phosphorus compounds play a crucial role in **water treatment processes**, particularly in **corrosion control and 
        wastewater management**. **Phosphates** are added to municipal water supplies to prevent **pipe corrosion and reduce 
        lead contamination**. In wastewater treatment, phosphorus removal techniques are used to **minimize nutrient pollution** 
        and prevent **eutrophication** in natural water bodies. While phosphorus is essential for life, controlling its levels 
        in water systems is crucial for maintaining environmental balance and protecting aquatic ecosystems.
        """)

    st.divider()

    # Specialized Fertilizers Section
    st.header("7. Specialized Fertilizers")
    col1, col2 = st.columns(2)

    with col1:
        image7 = Image.open(r"images/special.jpeg")
        st.image(image7, use_container_width=True)

    with col2:
        st.markdown("""
        Besides conventional phosphorus fertilizers, **specialized fertilizers** are formulated for **specific crops, soil 
        conditions, and precision agriculture techniques**. These include **slow-release phosphorus fertilizers, biofertilizers, 
        and customized blends** tailored to optimize nutrient uptake and **minimize environmental impact**. Advances in 
        fertilizer technology are helping farmers achieve **higher efficiency while reducing phosphorus runoff**, ensuring 
        **sustainable agricultural practices**.
        """)

    st.divider()

    # Toothpaste Section
    st.header("8. Toothpaste")
    col1, col2 = st.columns(2)

    with col2:
        image8 = Image.open(r"images/toothpaste.jpeg")
        st.image(image8, use_container_width=True)

    with col1:
        st.markdown("""
        Phosphorus compounds, particularly **calcium phosphate and dicalcium phosphate**, are key ingredients in **toothpaste**, 
        where they help **strengthen enamel and prevent cavities**. These compounds act as **abrasives** that aid in the removal 
        of plaque while **promoting remineralization** of teeth. Phosphates also help in maintaining the **pH balance** of 
        toothpaste, ensuring effective cleaning without damaging the enamel.
        """)

    st.divider()

    # Other Uses Section
    st.header("9. Other Uses")
    col1, col2 = st.columns(2)

    with col1:
        image9 = Image.open(r"images/fireworks.jpeg")
        st.image(image9, use_container_width=True)

    with col2:
        st.markdown("""
        Phosphorus finds applications in **numerous other industries**, including **fireworks, matches, pharmaceuticals, 
        and electronics**. **Red phosphorus** is commonly used in the production of **safety matches and flame retardants**, 
        while **phosphorus compounds** are essential in making **lithium-ion batteries and LED lighting**. As research continues, 
        new and innovative uses for phosphorus are emerging in modern technology and sustainable development.
        """)

    st.divider()

elif selected_page == "Phosphorus in the Economy":
    st.divider()
    st.write("Phosphorus plays a crucial role in global agriculture and industry, influencing food security, trade, and environmental policies. Its limited supply, concentrated in a few countries, has led to economic dependencies, price fluctuations, and regulatory interventions to manage its use and environmental effects.")
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #FFB6C1; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
            ">
                <h2 style="color: #AA336A;">DID YOU KNOW?</h2>
                <hr style="border: 2px solid #AA336A; width: 50%; margin: 10px auto;"> 
                <p style="color: #AA336A; font-size: 18px;">
                    <b>Around 90% of mined phosphorus is used to make fertilizers that boost crop yields. Countries with large phosphate reserves, like Morocco, China, and the U.S., have significant control over the phosphorus supply, making it a critical element in the global economy.</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()
    st.markdown("## <u>Phosphorus in Agriculture and Food Security </u>", unsafe_allow_html=True)
    st.write("Phosphorus-based fertilizers are essential for maintaining soil fertility and ensuring high crop yields. Countries with high agricultural output, such as the U.S., China, and India, heavily rely on phosphate fertilizers. The rising cost of phosphorus-based fertilizers due to supply chain disruptions has led to government subsidies and incentives in some regions to support farmers. However, inefficient use and over-application have caused environmental concerns, prompting stricter regulations on phosphorus management.")
    st.divider()
    st.markdown("## <u>Bans and Restrictions on Phosphorus Use </u>", unsafe_allow_html=True)
    st.subheader("1.Detergents and Cleaning Products")
    st.write("Many countries, including the U.S., Canada, and members of the European Union, have banned or restricted phosphorus in household and industrial detergents. This was done to reduce water pollution and prevent eutrophication in lakes and rivers. The bans have led to the development of phosphate-free detergents.")
    st.subheader("2.Agricultural Runoff Regulations")
    st.write("In response to rising phosphorus pollution, certain regions have imposed restrictions on fertilizer use. For example, the European Union has introduced regulations on phosphorus application rates in agriculture, and some U.S. states, such as Minnesota and Wisconsin, have restricted phosphorus-based lawn fertilizers to limit water contamination.")
    st.subheader("3.Phosphorus Recycling Initiatives")
    st.write("Some countries, such as Germany and Sweden, have implemented policies to encourage phosphorus recovery from wastewater and agricultural runoff. Technologies such as struvite precipitation and bio-based phosphorus recycling are gaining traction as part of circular economy strategies.")
    image = Image.open(r"images/ban.jpg")
    st.image(image, use_container_width=True)
    st.divider()
    st.markdown("## <u>Economic Instruments and Incentives </u>", unsafe_allow_html=True)
    st.write("Governments and international organizations are increasingly adopting economic tools to manage phosphorus sustainably:")
    st.subheader("1.Subsidies for Sustainable Fertilizers")
    st.write("Several governments provide financial incentives for using controlled-release and organic phosphorus fertilizers to reduce runoff and increase efficiency.")
    st.subheader("2.Emissions Trading for Phosphorus Pollution")
    st.write("Some regions have proposed market-based mechanisms where industries and farms trade phosphorus emissions permits to encourage efficient use and reduce environmental impact.")
    st.subheader("3.Investment in Phosphorus Recycling")
    st.write("Countries like Japan and the Netherlands are investing in technologies to extract phosphorus from wastewater and sewage sludge, reducing dependency on imported phosphate rock.")
    st.divider()
    st.markdown("## <u>Conclusion</u>", unsafe_allow_html=True)
    st.write("Phosphorus remains a critical element in agriculture and industry, with significant economic and environmental implications. While bans and restrictions have helped mitigate its negative effects, global efforts are needed to enhance phosphorus efficiency, invest in recycling technologies, and create policies that balance agricultural productivity with environmental sustainability.")
    st.divider()

elif selected_page == "Environment & Phosphorus":
    st.divider()
    st.markdown("### <u> Sources of Phosphorus Pollution</u>", unsafe_allow_html=True)
    st.write("1. **Agricultural Runoff**: Fertilizers contribute to 38% of phosphorus pollution in water bodies.")
    st.write("2. **Industrial Waste**: Mining and chemical industries add 8% to phosphorus emissions.")
    st.write("3. **Urban Wastewater**: Domestic sewage and detergents account for 12% of phosphorus pollution.")
    st.divider()
    st.markdown("### <u>Phosphorus Use and Runoff Trends </u>", unsafe_allow_html=True)
    years = np.arange(2000, 2030, 5)
    phosphorus_use = [36, 40, 45, 51, 58, 65]
    pollution_index = [50, 60, 75, 90, 110, 130]

    data = pd.DataFrame({
        "Year": years,
        "Phosphorus Use (Million Metric Tons)": phosphorus_use,
        "Water Pollution Index": pollution_index
    })

    st.line_chart(data.set_index("Year"))
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #FFB6C1; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
            ">
                <h2 style="color: #AA336A;">DID YOU KNOW?</h2>
                <hr style="border: 2px solid #AA336A; width: 50%; margin: 10px auto;"> 
                <p style="color: #AA336A; font-size: 18px;">
                    <b>While phosphorus is essential for plant growth and used in fertilizers, excessive phosphorus runoff into water bodies causes eutrophication—leading to harmful algal blooms, oxygen depletion, and dead zones in lakes and oceans. This disrupts aquatic ecosystems and can harm marine life. </b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()
    st.markdown("### <u>Environmental Effects of Excess Phosphorus </u>", unsafe_allow_html=True)
    st.write("1. **Eutrophication**: High phosphorus levels in water bodies lead to algal blooms, which deplete oxygen levels and cause aquatic dead zones.\n - Example: The Gulf of Mexico dead zone expanded to **16,400 sq. km in 2023**, mainly due to phosphorus runoff.")
    st.write("2. **Water Quality Degradation**: Algal blooms increase water toxicity, affecting drinking water supply.\n - The cost of water treatment due to algal blooms is estimated at **$4.6 billion annually** in the U.S.")
    st.write("3. **Biodiversity Loss**: Oxygen-deprived zones lead to the collapse of fish populations, affecting fisheries.")
    st.divider()
    
elif selected_page == "Future Prospects":
    st.divider()
    st.write("Phosphorus is an essential element with widespread applications in agriculture, industry, and energy. However, its future availability and sustainability pose significant challenges and opportunities.")
    st.divider()
    st.markdown("### <u> 1. Growing Demand in Agriculture</u>", unsafe_allow_html=True)
    st.write("- Phosphorus is a key nutrient for plant growth and a major component of fertilizers.")
    st.write("- With increasing global food demand, phosphorus consumption is expected to rise, putting pressure on natural phosphate reserves.")
    st.divider()
    st.markdown("### <u>2. Phosphate Rock Depletion </u>", unsafe_allow_html=True)
    st.write("- Phosphorus is mainly obtained from phosphate rock, which is a **finite resource**.")
    st.write("- Some studies suggest that **high-quality phosphate reserves may be depleted within 50-100 years**.")
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #FFB6C1; 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center;
            ">
                <h2 style="color: #AA336A;">DID YOU KNOW?</h2>
                <hr style="border: 2px solid #AA336A; width: 50%; margin: 10px auto;"> 
                <p style="color: #AA336A; font-size: 18px;">
                    <b>Phosphorus might power the future of electric vehicles! Researchers are developing lithium iron phosphate (LFP) batteries, which use phosphorus and are safer, longer-lasting, and more sustainable than traditional lithium-ion batteries. These batteries are already used in Tesla's entry-level models and could dominate the EV market in the future!</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()
    st.markdown("### <u>3. Sustainable Phosphorus Management </u>", unsafe_allow_html=True)
    st.write("- Recycling phosphorus from wastewater, agricultural runoff, and food waste is gaining attention.")
    st.write("- Technologies like **struvite precipitation** (recovering phosphorus from wastewater) and bio-based fertilizers offer sustainable alternatives.")
    st.divider()
    st.markdown("### <u>4. Environmental Regulations & Circular Economy </u>", unsafe_allow_html=True)
    st.write("- Governments are implementing policies to reduce phosphorus pollution, such as limiting fertilizer runoff.")
    st.write("- Circular economy approaches, like recovering phosphorus from sewage sludge and animal manure, are being explored.")
    st.divider()
    st.markdown("### <u>5. Innovation in Fertilizer Technology </u>", unsafe_allow_html=True)
    st.write("- Researchers are developing **slow-release and precision fertilizers** to improve efficiency and reduce waste.")
    st.write("- **Microbial biofertilizers** (using phosphorus-solubilizing bacteria) could enhance phosphorus availability in soil.")
    st.divider()
    st.markdown("### <u>6. Phosphorus in Energy & Industry </u>", unsafe_allow_html=True)
    st.write("- Phosphorus is used in **lithium iron phosphate (LFP) batteries**, which are gaining popularity in **electric vehicles and renewable energy storage**.")
    st.write("- It is also essential in semiconductor production, flame retardants, and metal refining.")
    st.divider()
    st.markdown("### <u>Conclusion </u>", unsafe_allow_html=True)
    st.write("Phosphorus will remain **critical for agriculture, industry, and energy storage** in the future. Sustainable management strategies, innovative recovery methods, and regulatory policies will be key to balancing demand while mitigating environmental risks.")

elif selected_page == "Sources":
    st.divider()
    st.markdown("[NIST WebBook - Phosphorus Data](https://webbook.nist.gov/cgi/inchi?ID=C7723140&Units=SI&Mask=20)")
    st.markdown("[NIST XPS Spectral Data](https://srdata.nist.gov/xps/SpectralByCompdDd/3164)")
    st.markdown("[RSC Periodic Table - Phosphorus](https://periodic-table.rsc.org/element/15/phosphorus)")
    st.markdown("[Lithium Iron Phosphate (LFP) Battery Market Report](https://www.globenewswire.com/news-release/2024/05/08/2877971/0/en/Lithium-Iron-Phosphate-Battery-Market-Surges-to-USD-51-5-Billion-by-2031-Propelled-by-19-4-CAGR-Verified-Market-Research.html)")
    st.markdown("[Wikipedia - Applications of Phosphorus](https://en.wikipedia.org/wiki/Phosphorus#Other_applications)")
    st.markdown("[NIH Fact Sheet on Phosphorus](https://ods.od.nih.gov/factsheets/Phosphorus-HealthProfessional/#:~:text=Phosphorus%2C%20an%20essential%20mineral%2C%20is,%2C%20and%20RNA%20%5B1%5D.)")
    st.caption("..and more")
    st.divider()

# [theme]
# base="light"
# primaryColor="#fe97ac"
# secondaryBackgroundColor="#fff400"
