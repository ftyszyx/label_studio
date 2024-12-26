# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class PromptsBatchPredictionsRequestResultsItem(pydantic_v1.BaseModel):
    task_id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Task ID to associate the prediction with
    """

    output: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Prediction output that contains keys from labeling config. Each key must be a valid control tag name from the labeling config. For example, given the output: `json {"sentiment": "positive"} ` it will be converted to the internal LS annotation format: `json { "value": { "choices": ["positive"] }, "from_name": "label", "to_name": "", ... } `
    """

    prompt_tokens: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Number of tokens in the prompt
    """

    completion_tokens: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Number of tokens in the completion
    """

    prompt_cost_usd: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Cost of the prompt (in USD)
    """

    completion_cost_usd: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Cost of the completion (in USD)
    """

    total_cost_usd: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Total cost of the inference (in USD)
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
