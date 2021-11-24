# Constants
indexes = {
    'TRUE': 'TCI',
    'NIR': 'B01',
    'BLUE': 'B02',
    'GREEN': 'B03',
    'RED': 'B04',
    'RED_EDGE': 'B05',
    'NIR': 'B08',
}

# Vegetation Index Functions
def calculate_ndvi():
    return (NIR - RED) / (NIR + RED)


def calculate_gndvi():
    return (NIR - GREEN) / (NIR + GREEN)


def calculate_endvi():
    return ((NIR + GREEN) - (2 * BLUE)) / ((NIR + GREEN) + (2 * BLUE)) 


def calculate_ndre():
    return (NIR - RED_EDGE) / (NIR + RED_EDGE)

if __name__ == '__main__':
    print("This shouldn't run")