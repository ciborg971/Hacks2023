import streamlit as st


st.markdown("# CV Creation")
st.sidebar.markdown("# Create my CV")

if "CV" not in st.session_state : 
    st.write("Connect to your wallet first")

else :
    def write_cv_sidebar():
        st.sidebar.write("## Diploma")
        for i in st.session_state["CV"]["School"]:
            st.sidebar.write("#### " + i["name"] + " - " + i["specialty"])

        st.sidebar.write("## Exp Pro")
        for i in st.session_state["CV"]["Exp"]:
            st.sidebar.write("#### " + i["name"] + " - " + i["Job"])

        st.sidebar.write("## Certification")
        for i in st.session_state["CV"]["Cert"]:
            st.sidebar.write("#### " + i["job"])


    write_cv_sidebar()
    if st.session_state["CV"]["Page"] == 0 :
        st.write("## Enter School name")

        with st.form(key='school', clear_on_submit=True):
            name = st.text_input("School")
            specialty = st.text_input("Specialty")
            col1, col2 = st.columns(2)
            with col1:
                start = st.date_input("Start")
            with col2:
                end = st.date_input("End")
            field = st.multiselect("Field studied", ["Marketing", "Computer Science", "C", "C++", "Rust", "Blockchain", "PHP", "Tezos", "Web", "Javascript", "Android", "IOS"])
            uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
                #st.write(bytes_data)

            submitted = st.form_submit_button("Add Formation")
            if submitted:
                tmp = dict()
                tmp = {"name": name,
                    "start": start,
                    "specialty": specialty,
                    "end": end,
                    "field" : field
                    }
                tmp2 = []

                for uploaded_file in uploaded_files:
                    bytes_data = uploaded_file.read()
                    #st.write("filename:", uploaded_file.name)
                    tmp2.append({ "name" : uploaded_file.name, "data": bytes_data})
                tmp["Upload"] = tmp2
                st.session_state["CV"]["School"].append(tmp)
                st.experimental_rerun()

        col1, col2 = st.columns(2)
        with col2:
            if st.button('Experience Pro') :
                st.session_state["CV"]["Page"] = 1 
                st.experimental_rerun()
            
    if st.session_state["CV"]["Page"] == 1 :
        st.write("## Enter Professionnal Experience")

        with st.form(key='pro', clear_on_submit=True):
            name = st.text_input("Company Name")
            job = st.text_input("Job Name")
            col1, col2 = st.columns(2)
            with col1:
                start = st.date_input("Start")
            with col2:
                end = st.date_input("End")
            field = st.multiselect("Field studied", ["Marketing", "Computer Science", "C", "C++", "Rust", "Blockchain", "PHP", "Tezos", "Web", "Javascript", "Android", "IOS"])
            submitted = st.form_submit_button("Add Experience")
            if submitted:
                st.session_state["CV"]["Exp"].append({
                    "name": name,
                    "start": start,
                    "Job": job,
                    "end": end,
                    "field" : field
                })
                st.experimental_rerun()
        col1, col2 = st.columns(2)
        with col1:
            if st.button('School') :
                st.session_state["CV"]["Page"] = 0 
                st.experimental_rerun()
        with col2:
            if st.button('Certification') :
                st.session_state["CV"]["Page"] = 2
                st.experimental_rerun()


    if st.session_state["CV"]["Page"] == 2 :
        st.write("## Enter Certification")

        with st.form(key='cert', clear_on_submit=True):
            name = st.text_input("Certifying company")
            job = st.text_input("Certification name")
            field = st.multiselect("Field studied", ["Marketing", "Computer Science", "C", "C++", "Rust", "Blockchain", "PHP", "Tezos", "Web", "Javascript", "Android", "IOS"])
            uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
            submitted = st.form_submit_button("Add Certification")
            if submitted:
                tmp = { "name": name, "job": job, "field" : field }
                tmp2 = []
                for uploaded_file in uploaded_files:
                    bytes_data = uploaded_file.read()
                    #st.write("filename:", uploaded_file.name)
                    #st.session_state["CV"]["Cert"]["Upload"].append({ "name" : uploaded_file.name, "data": bytes_data})
                    tmp2.append({"name" : uploaded_file.name, "data" : bytes_data})
                tmp["Upload"] = tmp2
                st.session_state["CV"]["Cert"].append(tmp)
                st.experimental_rerun()
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Experience Pro') :
                st.session_state["CV"]["Page"] = 1 
                st.experimental_rerun()
        with col2:
            if st.button('Validate') :
                st.session_state["CV"]["State"] = "Filled" 
                st.balloons()

    #st.sidebar.write("## Experience Pro")
    # Nom de l'entreprise, poste, date début, date de fin, compétences
    #st.sidebar.write("## Certification")