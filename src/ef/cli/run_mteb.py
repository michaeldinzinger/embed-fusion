import click
import mteb
from ef.config import *
from ef.globals import *
from ef.utils import *


class RetrievalModel():
    # Refer to the code of DRESModel for the methods to overwrite
    def __init__(self, pretrained_model_name: str, **kwargs):
        self.pretrained_model_name = pretrained_model_name
        self.encoder = AutoModel.from_pretrained(pretrained_model_name, trust_remote_code=True)
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name, trust_remote_code=True)
        self.gpu_count = torch.cuda.device_count()
        self.batch_size = BATCH_SIZE

        self.query_instruction = 'Represent this sentence for searching relevant passages: {}'
        self.document_instruction = '{}'
        self.pool_type = 'cls'
        self.max_length = 512

        self.encoder.cuda()
        self.encoder.eval()

    def encode_queries(self, queries: List[str], **kwargs) -> np.ndarray:
        input_texts = [self.query_instruction.format(q) for q in queries]
        return self._do_encode(input_texts)

    def encode_corpus(self, corpus: List[Dict[str, str]], **kwargs) -> np.ndarray:
        input_texts = [self.document_instruction.format('{} {}'.format(d.get('title', ''), d['text']).strip()) for d in corpus]
        return self._do_encode(input_texts)

    @torch.no_grad()
    def _do_encode(self, input_texts: List[str]) -> np.ndarray:
        dataset: Dataset = Dataset.from_dict({'contents': input_texts})
        dataset.set_transform(partial(transform_func, self.tokenizer, self.max_length))

        data_collator = DataCollatorWithPadding(self.tokenizer, pad_to_multiple_of=8)
        data_loader = DataLoader(
            dataset,
            batch_size=self.batch_size * self.gpu_count,
            shuffle=False,
            drop_last=False,
            num_workers=4,
            collate_fn=data_collator,
            pin_memory=True)

        encoded_embeds = []
        for batch_dict in tqdm(data_loader, desc='encoding', mininterval=10):
            batch_dict = move_to_cuda(batch_dict)

            with torch.amp.autocast('cuda'):
                outputs = self.encoder(**batch_dict)
                encoded_embeds.append(outputs.cpu().numpy())

        return np.concatenate(encoded_embeds, axis=0)


@click.command()
def run_mteb():
    """
    Run MTEB evaluation.
    """
    click.echo('Run MTEB evaluation')

    # 'SciFact'
    # tasks = mteb.get_tasks(tasks=['ArguAna', 'ClimateFEVER', 'CQADupstackTexRetrieval', 'DBPedia', 'FEVER', 'FiQA2018', 'HotpotQA', 'MSMARCO', 'NFCorpus', 'NQ', 'QuoraRetrieval', 'SCIDOCS', 'Touche2020', 'TRECCOVID'])
    tasks = mteb.get_tasks(tasks=[
        'CQADupstackAndroidRetrieval',
        'CQADupstackEnglishRetrieval',
        'CQADupstackGamingRetrieval',
        'CQADupstackGisRetrieval',
        'CQADupstackMathematicaRetrieval',
        'CQADupstackPhysicsRetrieval',
        'CQADupstackProgrammersRetrieval',
        'CQADupstackStatsRetrieval',
        # 'CQADupstackTexRetrieval',
        'CQADupstackUnixRetrieval',
        'CQADupstackWebmastersRetrieval',
        'CQADupstackWordpressRetrieval'
    ])

    model = RetrievalModel('PaDaS-Lab/arctic-m-bge-small')

    evaluation = mteb.MTEB(tasks=tasks)

    output_folder = os.path.join(RESULTS_FOLDER, 'mteb', 'arctic-m-bge-small')
    evaluation.run(model, output_folder=output_folder, overwrite_results=True)