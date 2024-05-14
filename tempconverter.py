import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

# Streamlit app
def main():
    st.title("Temperature Converter")

    # User input
    temperature = st.number_input("Enter temperature:", value=0.0)
    input_unit = st.selectbox("Select input unit:", ("Celsius", "Fahrenheit", "Kelvin"))
    output_unit = st.selectbox("Select output unit:", ("Celsius", "Fahrenheit", "Kelvin"))

    # Conversion and result
    if input_unit == output_unit:
        st.write("Please select different input and output units.")
    else:
        result = 0.0
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(temperature)
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = fahrenheit_to_celsius(temperature)
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = celsius_to_kelvin(temperature)
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = kelvin_to_celsius(temperature)
        else:
            st.write("Conversion not supported.")

        st.write(f"{temperature} {input_unit} is {result:.2f} {output_unit}")

if __name__ == "__main__":
    main()

