import pandas as pd
from preproccess import preprocess_input
from usoModelo import load_model, predict
import os

def main():
    filesPath = "."
    selected_model = "3_mas_importantes"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    min_vals = pd.read_csv(os.path.join(BASE_DIR, "Scaler", "min_values.csv"), index_col=0).squeeze()
    max_vals = pd.read_csv(os.path.join(BASE_DIR, "Scaler", "max_values.csv"), index_col=0).squeeze()
    expected_features = list(pd.read_csv(os.path.join(BASE_DIR, "SelectedColumns", f"{selected_model}.csv"))['column_name'])
    categorical_columns = []  # Del formulario se escriben las que sean categoricas


    input = pd.DataFrame([{
        "total_rec_prncp": 0.1457,  
        "funded_amnt": 0.1333, 
        "total_pymnt_inv": -0.2496
    }]) ## acá se pone la información del formulario

    processed = preprocess_input(input,  min_vals, max_vals, categorical_columns, expected_features)

    model, device = load_model(path=os.path.join(BASE_DIR, "Models", f"best_model_for_{selected_model}.pth"), 
                               input_size=3)

    predictionDict = predict(processed, model, device)

    print(predictionDict["probabilities"], predictionDict["predictions"], sep = "\n")


if __name__ == "__main__":
    main()