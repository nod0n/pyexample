from externalcode1 import bestmodelever


def forward(*args, **kwargs):
    # They just got the best model, so we use it here
    bestmodelever.forward(*args, **kwargs)

    print("Main function in pyexample.models.model is done.")
