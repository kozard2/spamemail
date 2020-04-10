import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;     S P A M - E M A I L    ;
		;---------------------------;
		; Author : Mastah - Venom     ;
		; Callme : t.me/kang_Venom ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam BPJS
2. Spam OLX
3. Spam Surveryon
""")
		pilih=int(input('/Kang-venom: '))
		if pilih == 1:
			import src.mail
		elif pilih == 2:
			import src.olx
		elif pilih == 3:
			import src.spamemail
		elif pilih == 4:
			import src.price
		elif pilih == 5:
			import src.mediatek
		else: print("[!] lihat menu boss(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
