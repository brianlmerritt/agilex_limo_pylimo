"""
This file registers the model with the Python SDK.
"""

from viam.components.base import Base
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .limo import limo

Registry.register_resource_creator(Base.SUBTYPE, limo.MODEL, ResourceCreatorRegistration(limo.new, limo.validate))
