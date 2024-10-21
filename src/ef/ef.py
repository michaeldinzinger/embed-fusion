import click
from ef.cli.evaluate import evaluate, evaluate_two, evaluatep
from ef.cli.sae import sae


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

main.add_command(sae)


if __name__ == "__main__":
    main()