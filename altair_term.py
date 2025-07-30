from io import BytesIO

import altair as alt
import vl_convert as vlc
from PIL import Image
from term_image.image import BaseImage, KittyImage, Size

# I use Ghostty...not Kitty or Konsole
BaseImage.forced_support = True


# yanked from altair
# just gets the version like v15.2
def vl_version_for_vl_convert() -> str:
    from altair.vegalite import SCHEMA_VERSION
    return "_".join(SCHEMA_VERSION.split(".")[:2])


# also yanked from altair
# essentially is just their png renderer
# without their frontend
# accepts keywords: ppi, scale
def terminal_display(spec, **kwargs):
    scale = kwargs.get("scale_factor", 1)
    # The default ppi for a PNG file is 72
    default_ppi = 72
    ppi = kwargs.get("ppi", default_ppi)
    png = vlc.vegalite_to_png(
        spec,
        vl_version=vl_version_for_vl_convert(),
        scale=scale,
        ppi=ppi,
    )

    img = KittyImage(Image.open(BytesIO(png)),
                     width=Size.ORIGINAL, )
    img.set_render_method('WHOLE')
    print(img.height, img.width)
    img.draw(h_align='left', v_align='bottom', pad_height=0)
    return {}


# show() isn't useful if i have this
alt.Chart.show = alt.Chart._repr_mimebundle_
rend_name = 'terminal'
alt.renderers.register(rend_name, terminal_display)
alt.renderers.enable(rend_name)
