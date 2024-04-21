import mlflow

if __name__ == "__main__":
    # create a new mlflow experiment
    experiment_id = mlflow.create_experiment(
        name="mlflow_by_rabii",
        artifact_location="mlflow_by_rabii_artifacts",
        tags={"env": "dev", "version": "1.0.0"},
    )

    print(experiment_id)