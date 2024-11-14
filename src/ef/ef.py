import click
from ef.cli.evaluate import evaluate, evaluate_two, evaluatep
from ef.cli.visualize import visualize
from ef.cli.plausibility import plausibility
from ef.cli.embed import embed
from ef.cli.embed_bucc import embed_bucc
from ef.cli.sae import sae
from ef.cli.pca import pca
from ef.cli.svd import svd
from ef.cli.svd_bucc import svd_bucc
from ef.cli.lda import lda
from ef.cli.lda_bucc import lda_bucc
from ef.cli.translate import translate
from ef.cli.run_mteb import run_mteb


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

main.add_command(visualize)

main.add_command(plausibility)

main.add_command(embed)
main.add_command(embed_bucc)
main.add_command(sae)
main.add_command(pca)
main.add_command(svd)
main.add_command(svd_bucc)
main.add_command(lda)
main.add_command(lda_bucc)

main.add_command(translate)

main.add_command(run_mteb)


if __name__ == "__main__":
    main()