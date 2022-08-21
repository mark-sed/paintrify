
import cairo
import numpy
import PIL

class Config:
    """
    Configuration values
    """

    def __init__(self, argopts):
        """
        Constructor that sets default value
        """
        self.debug = argopts.debug
        self.width = 1024
        self.height = 600

def pilImageFromCairoSurface( surface ):
   cairoFormat = surface.get_format()
   if cairoFormat == cairo.FORMAT_ARGB32:
      pilMode = 'RGBA'
      # Cairo has ARGB. Convert this to RGB for PIL which supports only RGB or
      # RGBA.
      argbArray = numpy.fromstring( bytes(surface.get_data()), 'c' ).reshape( -1, 4 )
      order = [2,1,0,3]
      rgbArray = argbArray[:, order]
      pilData = rgbArray.reshape( -1 ).tostring()
   else:
      raise ValueError( 'Unsupported cairo format: %d' % cairoFormat )
   pilImage = PIL.Image.frombuffer( pilMode,
         ( surface.get_width(), surface.get_height() ), pilData, "raw",
         pilMode, 0, 1 )
   pilImage = pilImage.convert('RGBA')
   return pilImage

class Generator:
    """
    Main image generator class
    """

    def __init__(self, config, info_method):
        """
        Constructor
        """
        self.config = config
        self.info = info_method

    def generate(self):
        """
        Does initial image generation based on configuration
        :return 
        """
        self.info("Started generating")
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.config.width, self.config.height)
        
        cr = cairo.Context(surface)

        cr.translate(self.config.width/2, self.config.height/2)
        cr.arc(0, 0, 50, 0, 2*3.14159265)
        cr.stroke_preserve()
        
        cr.set_source_rgb(0.3, 0.4, 0.6)
        cr.fill()

        pil_image = pilImageFromCairoSurface(surface)

        self.info("Done generating")
        return numpy.array(pil_image)




