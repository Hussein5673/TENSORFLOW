import numpy as np
import tensorflow as tf

def train_model():
    
    n_bedrooms = np.array([1, 2, 3, 4, 5, 6], dtype=float)
    price_in_hundreds_of_thousands = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
    
    
    model = tf.keras.Sequential([ 
        tf.keras.Input(shape=(1,)),
        tf.keras.layers.Dense(units=1)
    ]) 
    
    model.compile(optimizer='sgd', loss='mse')

    
    model.fit(n_bedrooms, price_in_hundreds_of_thousands, epochs=500)
    
   
    return model


trained_model = train_model()


new_n_bedrooms = np.array([7.0])
predicted_price = trained_model.predict(new_n_bedrooms, verbose=False).item()
print(f"Your model predicted a price of {predicted_price:.2f} hundreds of thousands of dollars for a {int(new_n_bedrooms.item())} bedrooms house")
