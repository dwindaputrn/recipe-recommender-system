# Importing modules
import pickle # For loading model
import streamlit as st # For web app
import pandas as pd
import difflib

#page config
st.set_page_config(
    page_title="Recipes Recommendation by Epiktetus",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Loading data frame
recipes_dict = pickle.load(open('recipes_dict.pkl', 'rb'))
recipes_data = pd.DataFrame(recipes_dict)

# Loading similarity file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Main heading
st.markdown("<h1 style='text-align: center; color: black;'>RECIPE RECOMMENDATION</h1>", unsafe_allow_html=True)

input_ingredient = st.text_input('Input ingredients that you have :')



def recommend(recipe):
    # creating a list with all the recipe names given in the dataset
    list_of_all_recipe = recipes_data['recipe_name'].tolist()

    # finding the close match for the recipe given by the user
    find_close_match = difflib.get_close_matches(input_ingredient, list_of_all_recipe, 3, 0.1)
    close_match = find_close_match[0]

    # finding the index of the recipe with ingredient
    index_of_the_recipe = recipes_data[recipes_data.recipe_name == close_match]['index'].values[0]

    # getting a list of similar recipe
    similarity_score = list(enumerate(similarity[index_of_the_recipe]))
    len(similarity_score)

    # sorting the recipe based on their similarity score
    sorted_similar_recipe = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    index = recipe[0]
    image = []
    recipe_name = []
    ingredient = []
    Cooking_Method = []
    for i in sorted_similar_recipe:
        try:
            image.append(recipes_data.iloc[i[0]].image)
            recipe_name.append(recipes_data.iloc[i[0]].recipe_name)
            ingredient.append(recipes_data.iloc[i[0]].ingredient)
            Cooking_Method.append(recipes_data.iloc[i[0]].Cooking_Method)
        except:
            pass
    return image, recipe_name, ingredient, Cooking_Method

if st.button('Search'):
    image,recipe_name,ingredient,Cooking_Method = recommend(input_ingredient)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[0], width=200, caption=recipe_name[0])
        with col2:
            st.subheader(recipe_name[0])
            with st.expander("Ingredients"):
                st.write(ingredient[0])
            with st.expander("Cooking Method"):
                st.write(Cooking_Method[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[1], width=200, caption=recipe_name[1])
        with col2:
            st.subheader(recipe_name[1])
            with st.expander("Ingredients"):
                st.write(ingredient[1])
            with st.expander("Cooking Method"):
                st.write(Cooking_Method[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[2], width=200, caption=recipe_name[2])
        with col2:
            st.subheader(recipe_name[2])
            with st.expander("Ingredients"):
                st.write(ingredient[2])
            with st.expander("Cooking Method"):
                st.write(Cooking_Method[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[3], width=200, caption=recipe_name[3])
        with col2:
            st.subheader(recipe_name[3])
            with st.expander("Ingredients"):
                st.write(ingredient[3])
            with st.expander("Cooking Method"):
                st.write(Cooking_Method[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[4], width=200, caption=recipe_name[4])
        with col2:
            st.subheader(recipe_name[4])
            with st.expander("Ingredients"):
                st.write(ingredient[4])
            with st.expander("Cooking Method"):
                st.write(Cooking_Method[4])

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)