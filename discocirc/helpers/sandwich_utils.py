from discopy.cat import Ob as ObCat
from discopy.monoidal import Diagram, Ob, Id, Box, Swap, Ty
from discopy import hypergraph
from discocirc.helpers.closed_nbc import Ty as TyClosed, Func as FuncClosed
from discocirc.pipeline.text_to_circuit_nbc import noun_normal_form
from discocirc.helpers.discocirc_utils import get_last_initial_noun
import re

#Use these imports on this branch to call the sandwich functor without using the BobCat parser
