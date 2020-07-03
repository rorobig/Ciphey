from abc import abstractmethod
from typing import Set, Any, Union, List, Optional, Dict, Tuple

from loguru import logger

from .ausearch import Node, AuSearch
from ciphey.iface import SearchLevel, Config, registry, CrackResult, Searcher, ParamSpec, Decoder, DecoderComparer

import bisect


class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: Set[Node]) -> Node: return next(iter(nodes))

    def handleDecodings(self, target: Any) -> (bool, Union[Tuple[SearchLevel, str], List[SearchLevel]])

    def __init__(self, config: Config):
        super().__init__(config)
        self._checker = self._config().objs["checker"]
        self._final_type = config.objs["format"]["out"]


registry.register(Perfection, Searcher)
