import click
from ef.cli.evaluate import evaluate, evaluate_two, evaluatep


@click.group()
def main():
    """
    ChunkEval

    Experiments on embeddings of web text chunks.
    """
    pass


main.add_command(evaluate)
main.add_command(evaluate_two)
main.add_command(evaluatep)


if __name__ == "__main__":
    main()