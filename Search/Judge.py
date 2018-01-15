import numpy
import math
import copy
from Search.Piece import *
from Search.Frame import *

class Judge:
	def new():
		return Judge()

	def isOverlapped(self,frame,piece):
		frame_vertexes = frame.getVertexes()
		piece_vertexes = piece.getVertexes()
		#piece_check_vertex2_list = numpy.concatenate((piece_vertexes[1:],piece_vertexes[0:1]))
		frame_check_vertex2_list = numpy.concatenate((frame_vertexes[1:],frame_vertexes[0:1]))
		for i,frame_check_vertex1 in enumerate(frame_vertexes):
			for h,piece_check_vertex2 in enumerate(piece_vertexes):
				frame_check_vertex2 = frame_check_vertex2_list[i]
				#piece_check_vertex2 = piece_check_vertex2_list[h]
				if numpy.any(numpy.cross(frame_check_vertex2 - frame_check_vertex1,piece_check_vertex2 - frame_check_vertex1) < 0):
					return True		
			
		return False
