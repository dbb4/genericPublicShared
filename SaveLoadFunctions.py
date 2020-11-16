import pickle
from pathlib import Path
import os.path

class SaveLoadFunctions():
	@staticmethod
	def SaveObject(objectToSave, filename):
		filepath = SaveLoadFunctions.GetFileInPyFileDirectory(filename)

		if filepath.parent.exists()==False:
			os.makedirs(filepath.parent)

		with open(filepath.absolute(), 'wb') as output:  # Overwrites any existing file.
			pickle.dump(objectToSave, output, pickle.HIGHEST_PROTOCOL)

	@staticmethod
	def LoadObject(filename):
		filepath = SaveLoadFunctions.GetFileInPyFileDirectory(filename)

		with open(filepath.absolute(), 'rb') as input:
			objectLoaded = pickle.load(input)

		return objectLoaded

	@staticmethod
	def GetFileInPyFileDirectory(filename,fileMustExist=False):
		basePath = Path(os.path.dirname(os.path.abspath(__file__)))

		fileToReturn = basePath / filename

		if fileMustExist and fileToReturn.exists()==False:
			raise IOError("{0} does not exist in {1}".format(fileToReturn.name,fileToReturn.parent.resolve()))

		return fileToReturn

