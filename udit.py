import streamlit as st

def calculate_dowry(age, profession, salary, education, residence, country):
    # Example dowry calculation logic (you can adjust these values as per your requirements)
    dowry_amount = 0

    # Age factor
    if age == "18-25":
        dowry_amount += 50000
    elif age == "26-30":
        dowry_amount += 100000
    elif age == "31-35":
        dowry_amount += 150000
    elif age == "36-40":
        dowry_amount += 200000
    else:
        dowry_amount += 250000

    # Profession factor
    profession_values = {
        "Entrepreneur": 200000,
        "Engineer": 150000,
        "Doctor": 250000,
        "Investment Banker": 300000,
        "Brand Manager": 180000,
        "Product Manager": 220000,
        "Content Creator": 120000,
        "Others": 100000
    }
    dowry_amount += profession_values.get(profession, 0)

    # Salary factor
    salary_amount = int(salary) * 10  # Example logic: multiplying salary by 10
    dowry_amount += salary_amount

    # Education factor
    education_values = {
        "High School": 50000,
        "12th Pass": 100000,
        "Graduation": 150000,
        "Post Graduation": 200000
    }
    dowry_amount += education_values.get(education, 0)

    # Residence factor
    residence_values = {
        "Rented House": 50000,
        "Self House": 150000,
        "Father's House": 100000
    }
    dowry_amount += residence_values.get(residence, 0)

    # Country factor
    country_values = {
        "India": 50000,
        "Abroad": 200000
    }
    dowry_amount += country_values.get(country, 0)

    return dowry_amount

def main():
    st.set_page_config(page_title="Dowry Calculator", page_icon=":moneybag:", layout="centered")
    
    st.title("💰 Dowry Calculator")
    
    st.markdown("### Fill in the details below to calculate the dowry(Dahej) amount:")
    
    age_options = ["18-25", "26-30", "31-35", "36-40", "41+"]
    profession_options = ["Entrepreneur", "Engineer", "Doctor", "Investment Banker", "Brand Manager", "Product Manager", "Content Creator", "Others"]
    education_options = ["High School", "12th Pass", "Graduation", "Post Graduation"]
    residence_options = ["Rented House", "Self House", "Father's House"]
    country_options = ["India", "Abroad"]

    st.subheader("Personal Information")
    age = st.selectbox("Age:", age_options)
    profession = st.selectbox("Profession:", profession_options)

    st.subheader("Financial Information")
    salary = st.text_input("Monthly Salary (₹):")

    st.subheader("Educational Information")
    education = st.selectbox("Education:", education_options)

    st.subheader("Residential Information")
    residence = st.selectbox("Residence:", residence_options)

    st.subheader("Location Information")
    country = st.selectbox("Country:", country_options)

    if st.button("💡 Calculate Now"):
        try:
            dowry_amount = calculate_dowry(age, profession, salary, education, residence, country)
            st.success(f"💸 Dowry Amount: ₹{dowry_amount}")

            # Display video pop-up after calculation
            st.video("https://www.youtube.com/watch?v=ffOZ4wXrWSo&ab_channel=MemeMandirShorts")
            st.markdown("Follow on Instagram @skeletordork ")
        except ValueError:
            st.error("Please enter a valid salary amount.")

    st.markdown("---")
    st.markdown("### About")
    st.info("This application is designed to calculate a theoretical dowry amount based on various personal, financial, educational, residential, and locational factors. Please note that dowry is illegal and unethical, and this tool is purely for educational and informational purposes.")

if __name__ == "__main__":
    main()
