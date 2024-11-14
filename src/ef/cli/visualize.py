import click
import matplotlib.pyplot as plt
import seaborn as sns
from ef.config import *
from ef.utils import *


@click.command()
def visualize():
    """
    Visualize the data.
    """
    # Load results file
    df_results = pd.read_csv(os.path.join(RESULTS_FOLDER, RESULTS_CONCAT_FILE))

    df_plot_dict_tasks = {}
    rankings = {}
    for _, row in df_results.iterrows():
        task_name = row['task_name']
        combined_model_name = row['combined_model_name']
        if '___' in combined_model_name:
            model1, model2 = combined_model_name.split('___')
        else:
            model1 = combined_model_name
            model2 = combined_model_name
        if task_name not in df_plot_dict_tasks:
            df_plot_dict_tasks[task_name] = {}
        if task_name not in rankings:
            rankings[task_name] = {}
        if model1 not in df_plot_dict_tasks[task_name]:
            df_plot_dict_tasks[task_name][model1] = {}
        if model2 not in df_plot_dict_tasks[task_name]:
            df_plot_dict_tasks[task_name][model2] = {}
        df_plot_dict_tasks[task_name][model1][model2] = row['NDCG@10']
        df_plot_dict_tasks[task_name][model2][model1] = row['NDCG@10']
        if model1 == model2:
            rankings[task_name][model1] = row['NDCG@10']

    # Give me a list of ranked models for each task
    df_plot_tasks = {}
    for task_name in df_plot_dict_tasks:
        ranked_models = sorted(rankings[task_name], key=rankings[task_name].get, reverse=True)

        df_plot_list = []
        for i, model1 in enumerate(ranked_models):
            for j, model2 in enumerate(ranked_models):
                if i > j:
                    df_plot_list.append((model1, model2, 0))
                else:
                    value = df_plot_dict_tasks[task_name][model1][model2] * 100
                    df_plot_list.append((model1, model2, value))
        df_plot_tasks[task_name] = pd.DataFrame(df_plot_list, columns=['Model1', 'Model2', 'NDCG@10'])

    for task_name in df_plot_tasks:
        click.echo(f'Task: {task_name}')

        # Create DataFrame
        df_plot = df_plot_tasks[task_name]
        df_plot_pivot = df_plot.pivot(index='Model1', columns='Model2', values='NDCG@10')
        ranked_models = sorted(rankings[task_name], key=rankings[task_name].get, reverse=True)
        df_plot_pivot_sorted = df_plot_pivot.reindex(index=ranked_models, columns=ranked_models)

        plt.figure(figsize=(10, 7))

        plt.title(f'NDCG@10 Heatmap for {task_name}')

        # Create Heatmap
        sns.heatmap(df_plot_pivot_sorted, annot=True, fmt='.2f')
        
        plt.xlabel('')
        plt.ylabel('')

        plt.tight_layout()
        plt.savefig(f'heatmap_{task_name}.png')