from enum import Enum

from pydantic import BaseModel


class Actions(int, Enum):
    nothing = 0
    left = 1
    main = 2
    right = 3


class ObservationModel(BaseModel):
    horizontalPadCoordinate: float
    verticalPadCoordinate: float
    horizontalSpeed: float
    verticalSpeed: float
    angle: float
    angularSpeed: float
    leftLegContact: int
    rightLegContact: int

    def to_numpy(self):
        return [
            self.horizontalPadCoordinate,
            self.verticalPadCoordinate,
            self.horizontalSpeed,
            self.verticalSpeed,
            self.angle,
            self.angularSpeed,
            self.leftLegContact,
            self.rightLegContact,
        ]


class ActionResponse(BaseModel):
    action: Actions
