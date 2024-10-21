import click
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, regularizers, Model, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError


def build_sparse_autoencoder(input_dim, latent_dim, l1_penalty=1e-5):
    # Input layer
    inputs = Input(shape=(input_dim,))
    
    # Encoder: Apply sparsity through L1 regularization
    encoded = layers.Dense(latent_dim, activation='relu', 
                           activity_regularizer=regularizers.l1(l1_penalty))(inputs)
    
    # Decoder: Reconstruct the original dense embeddings
    decoded = layers.Dense(input_dim, activation='sigmoid')(encoded)
    
    # Build autoencoder model
    autoencoder = Model(inputs, decoded)
    
    # Build separate encoder model
    encoder = Model(inputs, encoded)
    
    return autoencoder, encoder


def train_autoencoder(dense_vectors, latent_dim=10000, l1_penalty=1e-5, 
                      learning_rate=0.001, epochs=50, batch_size=128, validation_split=0.2):
    
    input_dim = dense_vectors.shape[1]  # Dimension of the dense embeddings
    
    # Build the sparse autoencoder and encoder
    autoencoder, encoder = build_sparse_autoencoder(input_dim, latent_dim, l1_penalty)
    
    # Compile the model
    autoencoder.compile(optimizer=Adam(learning_rate=learning_rate), 
                        loss=MeanSquaredError())
    
    # Train the autoencoder
    history = autoencoder.fit(dense_vectors, dense_vectors,  # Input and target are the same for autoencoders
                              epochs=epochs,
                              batch_size=batch_size,
                              validation_split=validation_split,
                              verbose=1)
    
    # Return the trained autoencoder, encoder, and training history
    return autoencoder, encoder, history


@click.command()
@click.argument("method", type=click.Choice(['train', 'evaluate']))
def sae(method: str):
    """
    Train and infer a Sparse Autoencoder.
    """
    click.echo('Training and evaluating a Sparse Autoencoder')

    # Hyperparameters
    latent_dim = 10000       # Dimensionality of the sparse latent space
    l1_penalty = 1e-5        # L1 regularization strength
    learning_rate = 0.001    # Learning rate
    epochs = 5              # Number of training epochs
    batch_size = 128         # Batch size

    # Model path
    model_path = 'encoder_model.h5'

    if method == 'train':
        # Load dense vectors
        dense_vectors = np.random.rand(10000, 512)  # Example data: 10000 samples of 512-dimensional vectors

        # Train the autoencoder
        _, encoder, history = train_autoencoder(
            dense_vectors=dense_vectors,
            latent_dim=latent_dim, 
            l1_penalty=l1_penalty, 
            learning_rate=learning_rate, 
            epochs=epochs,
            batch_size=batch_size
        )

        # Print training history
        click.echo(f'History:\n{history.history}')

        # Save the encoder model
        tf.keras.saving.save_model(encoder, model_path)

    elif method == 'evaluate':
        # Load the encoder model
        encoder = tf.keras.models.load_model(model_path)

        # Load dense vectors
        dense_vectors = np.random.rand(10000, 512)

        # Generate sparse vectors from your dense embeddings
        sparse_vectors = encoder.predict(dense_vectors)

        # Save sparse vectors or use them for retrieval
        print(sparse_vectors.shape)

    else:
        click.echo('Invalid method. Choose between "train" and "evaluate".')
