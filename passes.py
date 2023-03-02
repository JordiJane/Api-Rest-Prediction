class Passes:
    startAz: float
    startAzCompass: float
    startEl: float
    startUTC: int
    maxAz: float
    maxAzCompass: str
    maxEl: float
    maxUTC: int
    endAz: float
    endAzCompass: str
    endEl: int
    endUTC: int
    mag: float
    duration: int
    startVisibility: int

    def __init__(
        self,
        startAz,
        startAzCompass,
        startEl,
        startUTC,
        maxAz,
        maxAzCompass,
        maxEl,
        maxUTC,
        endAz,
        endAzCompass,
        endEl,
        endUTC,
        mag,
        duration,
        startVisibility,
    ) -> None:
        self.startAz = startAz
        self.startAzCompass = startAzCompass
        self.startEl = startEl
        self.startUTC = startUTC
        self.maxAz = maxAz
        self.maxAzCompass = maxAzCompass
        self.maxEl = maxEl
        self.maxUTC = maxUTC
        self.endAz = endAz
        self.endAzCompass = endAzCompass
        self.endEl = endEl
        self.endUTC = endUTC
        self.mag = mag
        self.duration = duration
        self.startVisibility = startVisibility
