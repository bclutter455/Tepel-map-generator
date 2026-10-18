#import os
import pygame
import sys
import pytmx
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

#splita image into a tileset, saving for later seems like its not needed
tile_h = int(16)
tile_w = int(32)

#os.makedirs("tilesets/separated images", exist_ok=True)

#for i, y in enumerate(range(0, tileset1height, tile_h)):
 #       for j, x in enumerate(range(0, tileset1width, tile_w)):
 #           # Define box coordinates (left, upper, right, lower)
 #           box = (x, y, min(x + tile_w, tileset1width), min(y + tile_h, tileset1height))
  #          
  #          # Crop and save the tile
  #          tile = tileset1image.crop(box)
   #         tile.save(os.path.join("tilesets/separated images", f"tile_{i+j}.png"))
leveldata1 = [3] * (128 * 128)

def TMX_writer(map_name, tileset_name, map_height, map_width, level_data):

   #seting tileset
   tileset_image = Image.open(f"tilesets/{tileset_name}.png")
   tileset_width, tileset_height= tileset_image.size
   tileset_columns=int(tileset_width/32)
   tileset_rows=int(tileset_height/16)
   tile_count=tileset_columns*tileset_rows

   #make map for tmx format out of data 
   leveldata_csv = ',\n'.join(",".join(str(level_data[y * map_width + x]) for x in range(map_width)) for y in range(map_height))

   #writing xml file for tiled
   map1 = ET.Element("map", version="1.10",tiledversion="1.12.2", orientation="isometric", renderorder="right-down", width=str(map_width), height=str(map_height), tilewidth="32", tileheight="16", infinite="0", nextlayerid="2", nextobjectid="1" )
   tileset1 = ET.SubElement(map1, "tileset",firstgid="1", name="spritesheet", tilewidth=str(tile_w), tileheight=str(tile_h), tilecount=str(tile_count), columns=str(tileset_columns))
   layer1 = ET.SubElement(map1, "layer",id="1", name="Tile Layer 1", width=str(map_width), height=str(map_height))

   image1 = ET.SubElement(tileset1, "image", source=f"tilesets/{tileset_name}.png", width=str(tileset_width), height=str(tileset_height))
   data1 = ET.SubElement(layer1, "data", encoding="csv")
   data1.text = "\n" +leveldata_csv+ "\n"

   ET.indent(map1, space=" ")

   #making fnal file
   tree = ET.ElementTree(map1)
   tree.write(map_name, encoding='utf-8', xml_declaration=True)


TMX_writer("testmap1.tmx", "tiles", 128, 128, leveldata1)

pygame.init()

TILE_SIZE = 32          # Dimensions of your square tiles (e.g., 32x32 pixels)
MAP_ROWS = 10            # Number of rows in your game grid
MAP_COLS = 10          # Number of columns in your game grid

SCREEN_WIDTH = MAP_COLS * TILE_SIZE
SCREEN_HEIGHT = MAP_ROWS * TILE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PNG Tile Map Renderer")

print("welcome to map builder v1")
input("Press Enter to run")


pygame.quit()
sys.exit()