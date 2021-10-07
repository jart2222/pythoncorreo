class correos():
	def __init__(self):
		self.a=input("Introduce tu correo por favor: ")

	def inicio(self):
		micorreo.limpiezaydescomposicion()
		micorreo.ciclo()
		print("correo valido. muchas gracias")

	def limpiezaydescomposicion(self):
		self.a=self.a.lstrip()
		self.a=self.a.rstrip()
		self.c=int(self.a.count("@"))
		self.b=self.a.split('.')
		self.chequeoultimafila()
	def chequeoultimafila(self):
		if self.b[-1].startswith("com")==True:
			self.d=True
		elif (self.b[-1].startswith("mx")==True):
			self.d=True
		else: 
			self.d=False

	def ciclo(self):
		while (self.c>1 or self.c==0 or self.a.isascii()==False  or self.d==False):
			print("correo invalido ")
			self.a=input("Introduce tu correo por favor: ")
			self.limpiezaydescomposicion()
			self.chequeoultimafila()

micorreo=correos()
micorreo.inicio()
