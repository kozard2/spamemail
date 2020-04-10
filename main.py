import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;===========;
		;     S P A M  E M A I L    ;
		;---------------------------;
		; Author : Mr-Venom      ;
		; Callme : t.me/Kang-Venom ;
		;===========;

1. Spam BPJS
2. Spam OLX
3. Spam Surveyon
""")
		pilih=int(input('/Kang-Venom: '))
		if pilih == 1:
			import src.mail
		elif pilih == 2:
			import src.spamOLX
		elif pilih == 3:
			import src.spammail
else: print("[!] lihat menu bang(o)");self.menu()

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
