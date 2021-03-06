from .models import *
from .data import *
from .ner.data import entities_from_gmb, entities_from_conll2003, entities_from_txt
from .ner.models import sequence_tagger, print_sequence_taggers
from .eda import get_topic_model
from .textutils import extract_filenames, load_text_files, filter_by_id

__all__ = [
           'text_classifier', 
           'print_text_classifiers'
           'texts_from_folder', 'texts_from_csv',
           'entities_from_gmb',
           'entities_from_conll2003',
           'entities_from_txt',
           'sequence_tagger',
           'print_sequence_taggers',
           'get_topic_model',
           'extract_filenames', 
           'load_text_files',
           ]


def load_topic_model(fname):
    """
    Load saved TopicModel object
    Args:
        fname(str): base filename for all saved files
    """
    with open(fname+'.tm_vect', 'rb') as f:
        vectorizer = pickle.load(f)
    with open(fname+'.tm_model', 'rb') as f:
        model = pickle.load(f)
    with open(fname+'.tm_params', 'rb') as f:
        params = pickle.load(f)
    tm = get_topic_model(n_topics=params['n_topics'],
                         n_features = params['n_features'],
                         verbose = params['verbose'])
    tm.model = model
    tm.vectorizer = vectorizer
    return tm



