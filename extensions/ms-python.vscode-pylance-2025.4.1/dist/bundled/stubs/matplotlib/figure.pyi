from io import BufferedWriter, BytesIO
from typing import Callable, Literal, overload

import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from ._typing import *
from .artist import Artist, _finalize_rasterization, allow_rasterization
from .axes import Axes
from .backend_bases import FigureCanvasBase, MouseButton, MouseEvent, RendererBase
from .colorbar import Colorbar
from .colors import Colormap, Normalize
from .gridspec import GridSpec, SubplotSpec
from .image import FigureImage
from .layout_engine import LayoutEngine
from .legend import Legend
from .projections.geo import AitoffAxes, HammerAxes, LambertAxes, MollweideAxes
from .projections.polar import PolarAxes
from .text import Text
from .transforms import BboxBase

class _AxesStack:
    def __init__(self) -> None: ...
    def as_list(self) -> list[Axes]: ...
    def remove(self, a: Axes) -> None: ...
    def bubble(self, a: Axes) -> None: ...
    def add(self, a: Axes) -> None: ...
    def current(self) -> None: ...

class SubplotParams:
    def __init__(
        self,
        left: float = ...,
        bottom: float = ...,
        right: float = ...,
        top: float = ...,
        wspace: float = ...,
        hspace: float = ...,
    ) -> None: ...
    validate = ...
    def update(
        self,
        left: float | None = ...,
        bottom: float | None = ...,
        right: float | None = ...,
        top: float | None = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
    ) -> None: ...

class FigureBase(Artist):
    def __init__(self, **kwargs) -> None: ...
    def autofmt_xdate(
        self,
        bottom: float = 0.2,
        rotation: int = 30,
        ha: Literal["left", "center", "right"] = "right",
        which: Literal["major", "minor", "both"] = "major",
    ) -> None: ...
    def get_children(self) -> list[Artist]: ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def get_window_extent(self, renderer: RendererBase = ..., *args, **kwargs): ...
    def suptitle(self, t: str, **kwargs) -> Text: ...
    def supxlabel(self, t: str, **kwargs) -> Text: ...
    def supylabel(self, t: str, **kwargs) -> Text: ...
    def get_edgecolor(self): ...
    def get_facecolor(self): ...
    def get_frameon(self) -> bool: ...
    def set_linewidth(self, linewidth: float) -> None: ...
    def get_linewidth(self) -> float: ...
    def set_edgecolor(self, color: Color): ...
    def set_facecolor(self, color: str) -> None: ...
    def set_frameon(self, b: bool): ...
    frameon = ...
    def add_artist(self, artist: Artist, clip: bool = False) -> Artist: ...
    def add_axes(self, *args, **kwargs) -> Axes: ...
    @overload
    # Decorators make this look like a callable. This is an upstream issue
    def add_subplot(self, *args, projection: Literal["3d"], **kwargs) -> Axes3D: ...  # pyright: ignore[reportGeneralTypeIssues]
    @overload
    def add_subplot(self, *args, projection: Literal["aitoff"], **kwargs) -> AitoffAxes: ...
    @overload
    def add_subplot(self, *args, projection: Literal["hammer"], **kwargs) -> HammerAxes: ...
    @overload
    def add_subplot(self, *args, projection: Literal["lambert"], **kwargs) -> LambertAxes: ...
    @overload
    def add_subplot(self, *args, projection: Literal["mollweide"], **kwargs) -> MollweideAxes: ...
    @overload
    def add_subplot(self, *args, projection: Literal["polar"], **kwargs) -> PolarAxes: ...
    @overload
    def add_subplot(self, *args, **kwargs) -> Axes: ...
    @overload
    def subplots(
        self,
        nrows: Literal[1] = ...,
        ncols: Literal[1] = ...,
        *,
        squeeze: Literal[False],
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        subplot_kw: dict = ...,
        gridspec_kw: dict = ...,
    ) -> list[Axes]: ...
    @overload
    def subplots(
        self,
        nrows: int = ...,
        ncols: int = ...,
        *,
        squeeze: Literal[False],
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        subplot_kw: dict = ...,
        gridspec_kw: dict = ...,
    ) -> list[list[Axes]]: ...
    @overload
    def subplots(
        self,
        nrows: Literal[1] = ...,
        ncols: Literal[1] = ...,
        *,
        squeeze: Literal[True] = ...,
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        subplot_kw: dict = ...,
        gridspec_kw: dict = ...,
    ) -> Axes: ...
    @overload
    def subplots(
        self,
        nrows: int,
        ncols: int,
        *,
        squeeze: bool = ...,
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        subplot_kw: dict = ...,
        gridspec_kw: dict = ...,
    ) -> list[Axes]: ...
    def delaxes(self, ax: Axes) -> None: ...
    def clear(self, keep_observers: bool = False) -> None: ...
    def clf(self, keep_observers: bool = False) -> None: ...
    def legend(self, *args, **kwargs) -> Legend: ...
    def text(self, x: float, y: float, s: str, fontdict: dict = ..., **kwargs) -> Text: ...
    def colorbar(self, mappable, cax: Axes = ..., ax=..., use_gridspec: bool = ..., **kwargs) -> Colorbar: ...
    def subplots_adjust(
        self,
        left: float = ...,
        bottom: float = ...,
        right: float = ...,
        top: float = ...,
        wspace: float = ...,
        hspace: float = ...,
    ) -> None: ...
    def align_xlabels(self, axs: list[Axes] = ...) -> None: ...
    def align_ylabels(self, axs: list[Axes] = ...) -> None: ...
    def align_labels(self, axs: list[Axes] = ...) -> None: ...
    def add_gridspec(self, nrows: int = 1, ncols: int = 1, **kwargs) -> GridSpec: ...
    def subfigures(
        self,
        nrows: int = 1,
        ncols: int = 1,
        squeeze: bool = True,
        wspace: float | None = None,
        hspace: float | None = None,
        width_ratios: ArrayLike = ...,
        height_ratios: ArrayLike = ...,
        **kwargs,
    ): ...
    def add_subfigure(self, subplotspec: SubplotSpec, **kwargs) -> SubFigure: ...
    def sca(self, a: Axes) -> Axes: ...
    def gca(self) -> Axes: ...
    def get_default_bbox_extra_artists(self): ...
    def get_tightbbox(
        self,
        renderer: RendererBase = ...,
        bbox_extra_artists: list[Artist] | None = ...,
    ) -> BboxBase: ...
    def subplot_mosaic(
        self,
        mosaic: list | str,
        *,
        sharex: bool = ...,
        sharey: bool = ...,
        subplot_kw: dict = ...,
        gridspec_kw: dict = ...,
        empty_sentinel: object = ...,
    ) -> dict[Text, Axes]: ...

class Figure(FigureBase):
    callbacks = ...
    def __repr__(self): ...
    def __init__(
        self,
        figsize: tuple[float, float] = ...,
        dpi: float = ...,
        facecolor: Color = ...,
        edgecolor: Color = ...,
        linewidth: float = ...,
        frameon: bool = ...,
        subplotpars: SubplotParams = ...,
        tight_layout: bool | dict = ...,
        constrained_layout: bool = ...,
        *,
        layout: LayoutEngine | Literal["constrained", "compressed", "tight"] | None = ...,
        **kwargs,
    ) -> None: ...
    def set_layout_engine(
        self, layout: LayoutEngine | Literal["constrained", "compressed", "tight"] = ..., **kwargs: dict
    ) -> None: ...
    def get_layout_engine(self) -> None: ...
    def show(self, warn: bool = True) -> None: ...
    @property
    def axes(self) -> list[Axes]: ...
    get_axes = ...
    dpi = ...
    def get_tight_layout(self) -> bool: ...
    def set_tight_layout(self, tight: bool | Literal["w_pad", "h_pad", "rect"] | None): ...
    def get_constrained_layout(self) -> bool: ...
    def set_constrained_layout(self, constrained: bool | dict | None): ...
    def set_constrained_layout_pads(self, **kwargs) -> None: ...
    def get_constrained_layout_pads(self, relative: bool = ...): ...
    def set_canvas(self, canvas: FigureCanvasBase) -> None: ...
    canvas: FigureCanvasBase

    def figimage(
        self,
        X: ArrayLike,
        xo: int = ...,
        yo: int = ...,
        alpha: None | float = ...,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float = ...,
        vmax: float = ...,
        origin: Literal["upper", "lower"] = ...,
        resize: bool = ...,
        **kwargs,
    ) -> FigureImage: ...
    def set_size_inches(self, w: float, h: float = ..., forward: bool = True) -> None: ...
    def get_size_inches(self) -> np.ndarray: ...
    def get_figwidth(self): ...
    def get_figheight(self): ...
    def get_dpi(self) -> float: ...
    def set_dpi(self, val: float) -> None: ...
    def set_figwidth(self, val: float, forward: bool = ...) -> None: ...
    def set_figheight(self, val: float, forward: bool = ...) -> None: ...
    def clear(self, keep_observers: bool = ...) -> None: ...
    @allow_rasterization
    def draw(self, renderer) -> None: ...
    def draw_without_rendering(self) -> None: ...
    def draw_artist(self, a: Artist) -> None: ...
    def __getstate__(self): ...
    def __setstate__(self, state) -> None: ...
    def add_axobserver(self, func: Callable) -> None: ...
    def savefig(
        self, fname: str | PathLike | FileLike | BytesIO | BufferedWriter, *, transparent: bool = ..., **kwargs
    ) -> None: ...
    def ginput(
        self,
        n: int = ...,
        timeout: float = ...,
        show_clicks: bool = ...,
        mouse_add: MouseButton | None = ...,
        mouse_pop: MouseButton | None = ...,
        mouse_stop: MouseButton | None = ...,
    ) -> list[tuple[float, float]]: ...
    def waitforbuttonpress(self, timeout=...) -> None: ...
    def execute_constrained_layout(self, renderer=...) -> None: ...
    def tight_layout(
        self, *, pad: float = 1.08, h_pad: float = ..., w_pad: float = ..., rect: tuple[float, float, float, float] = ...
    ) -> None: ...

def figaspect(arg: float): ...

class SubFigure(FigureBase):
    callbacks = ...
    def __init__(
        self,
        parent: FigureBase,
        subplotspec: SubplotSpec,
        *,
        facecolor: Color = ...,
        edgecolor: Color = ...,
        linewidth: float = ...,
        frameon: bool = ...,
        **kwargs,
    ) -> None: ...
    @property
    def dpi(self) -> float: ...
    @dpi.setter
    def dpi(self, value: float): ...
    def get_dpi(self) -> float: ...
    def set_dpi(self, val: float) -> None: ...
    def get_constrained_layout(self) -> bool: ...
    def get_constrained_layout_pads(self, relative: bool = ...): ...
    def get_layout_engine(self) -> LayoutEngine: ...
    @property
    def axes(self) -> list[Axes]: ...
    get_axes = ...
    def draw(self, renderer: RendererBase) -> None: ...
