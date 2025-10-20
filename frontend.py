import requests
import streamlit as st


st.title("Box In")
st.write("Получить или добавить новую коробку")

with st.form("Получение коробок"):
    submit = st.form_submit_button("Получить все коробки")

    if submit:
        try:
            response = requests.get("http://localhost:8000/api/v1/boxes")

            if response.status_code == 200:
                boxes = response.json()

                for box in boxes:
                    with st.container():
                        st.subheader(f"**Имя коробки:** {box["name"]}")
                        st.write(f"**ID:** {box["id"]}")
                        st.write(f"**Описание:** {box["description"]}")
                        st.write(f"**Цена:** {box["price"]} рублей")

                if not boxes:
                    st.info("Коробок не найдено")

            else:
                st.error(f"Ошибка сервера: {response.status_code}")


        except requests.exceptions.ConnectionError:
            st.error("Не удалось подключиться к серверу")

        except Exception as ex:
            st.error(f"Произошла ошибка {ex}")
st.write("---")
with st.form("Создание коробки"):
    name = st.text_input("**Имя коробки:**")
    description = st.text_input("**Описание:**")
    price = st.number_input("**Цена:**")
    submit = st.form_submit_button("Создать коробку")

    if submit:
        data = {"name": name, "description": description, "price": price}
        try:
            response = requests.post("http://localhost:8000/api/v1/boxes", json=data)

            if response.status_code == 200:
                box = response.json()

                st.success("Коробка успешно создана")


                with st.container():
                    st.subheader(f"**Имя коробки:** {box["name"]}")
                    st.write(f"**ID:** {box["id"]}")
                    st.write(f"**Описание:** {box["description"]}")
                    st.write(f"**Цена:** {box["id"]} рублей")

            else:
                st.error(f"Ошибка сервера: {response.status_code}")


        except requests.exceptions.ConnectionError:
            st.error("Не удалось подключиться к серверу")

        except Exception as ex:
            st.error(f"Произошла ошибка {ex}")