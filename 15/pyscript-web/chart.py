# data.py
import altair as alt

def get_chart(cars):
    return (alt.Chart(cars).mark_circle(size=60).encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin',
            tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
        ))