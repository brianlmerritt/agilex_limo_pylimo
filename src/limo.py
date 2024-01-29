from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from dataclasses import dataclass
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.base import Base
from viam.logging import getLogger

import time
import asyncio

LOGGER = getLogger(__name__)

class limo(Base, Reconfigurable):
    
    """
    Base represents a physical base of a robot.
    """
    @dataclass
    class Properties:
        width_meters: float
        turning_radius_meters: float
        wheel_circumference_meters: float
    

    MODEL: ClassVar[Model] = Model(ModelFamily("brianlmerritt", "base"), "limo")
    
    # create any class parameters here, 'some_pin' is used as an example (change/add as needed)
    some_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        # here we validate config, the following is just an example and should be updated as needed
        some_pin = config.attributes.fields["some_pin"].number_value
        if some_pin == "":
            raise Exception("A some_pin must be defined")
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # here we initialize the resource instance, the following is just an example and should be updated as needed
        self.some_pin = int(config.attributes.fields["some_pin"].number_value)
        return

    """ Implement the methods the Viam RDK defines for the Base API (rdk:component:base) """

    
    async def move_straight(
        self,
        distance: int,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the base in a straight line the given ``distance``, expressed in millimeters,
        at the given ``velocity``, expressed in millimeters per second.
        When ``distance`` or ``velocity`` is 0, the base will stop.
        This method blocks until completed or cancelled.

        Args:
            distance (int): The distance (in millimeters) to move.
                Negative implies backwards.
            velocity (float): The velocity (in millimeters per second) to move.
                Negative implies backwards.
        """
        ...

    
    async def spin(
        self,
        angle: float,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the base in place ``angle`` degrees, at the given angular ``velocity``,
        expressed in degrees per second.
        When ``velocity`` is 0, the base will stop.
        This method blocks until completed or cancelled.

        Args:
            angle (float): The angle (in degrees) to spin.
            velocity (float): The angular velocity (in degrees per second)
                to spin.
                Given a positive angle and a positive velocity, the base will turn to the left.
        """
        ...

    
    async def set_power(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """Set the linear and angular velocity of the Base
        When ``linear`` is 0, the the base will spin.
        When ``angular`` is 0, the the base will move in a straight line.
        When both ``linear`` and ``angular`` are 0, the base will stop.
        When ``linear`` and ``angular`` are both nonzero, the base will move in an arc,
        with a tighter radius if angular power is greater than linear power.

        Args:
            linear (Vector3): The linear component. Only the Y component is used
                for wheeled base. Positive implies forwards.
            angular (Vector3): The angular component. Only the Z component is used
                for wheeled base. Positive turns left; negative turns right.
        """
        ...

    
    async def set_velocity(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Set the linear and angular velocities of the base.


        Args:
            linear (Vector3): Velocity in mm/sec
            angular (Vector3): Velocity in deg/sec
        """

    
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the base.
        """
        ...

    
    async def is_moving(self) -> bool:
        """
        Get if the base is currently moving.

        Returns:
            bool: Whether the base is moving.
        """
        ...

    
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the base width and turning radius

        Returns:
            Properties: The properties of the base
        """
        ...

