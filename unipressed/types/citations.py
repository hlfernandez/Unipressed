from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class CitationsQueryDict(TypedDict):
    and_: NotRequired[Iterable["CitationsQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["CitationsQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["CitationsQuery"]]
    "Negate a filter"
    title: NotRequired[str]
    "Title\ne.g. sample title"
    author: NotRequired[str]
    "Author\ne.g. sample author name"
    journal: NotRequired[str]
    "Journal\ne.g. sample journal"
    published: NotRequired[str]
    "Year published\ne.g. sample"
    id: NotRequired[str]
    "Citation Id\ne.g. 15772651"
    doi: NotRequired[str]
    "DOI\ne.g. 10.1007/s11882-009-0055-9"


CitationsQuery: TypeAlias = Union[CitationsQueryDict, str]
CitationsLiterature: TypeAlias = Literal[
    "id",
    "doi",
    "title",
    "authors",
    "authoring_group",
    "journal",
    "publication_date",
    "first_page",
    "last_page",
    "volume",
    "reference",
    "lit_abstract",
    "statistics",
]
CitationsFields: TypeAlias = Literal[
    CitationsLiterature,
]


@dataclass
class CitationsSearch(unipressed.base.Search):
    """Client for querying the [citations Uniprot dataset](https://www.uniprot.org/help/citations)"""

    dataset: Literal["citations"] = field(default="citations", init=False)
    query: CitationsQuery
    "A query that filters the returned proteins"
    fields: Iterable[CitationsFields]
    "Fields to return in the result object"
