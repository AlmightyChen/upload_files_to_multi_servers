# Upload the files to servers
# Chen Guowei

# 使用方法

# 環境：
# 	MACや 「 Python２ 」 をインストールした端末に

# 実装する前
# 	Psftpをインストール
# 		pip を インストールしてるかとうか確認する pip --version
# 		pip インストールしたら、psftp を インストール方法 sudo pip install psftp
# 		pip インストールしてない方は、自分でインストール方法を探してください。

# 設定
# 	SFTP:
# 		ユーザー名
# 		username = "chenguowei"

# 		keyのPATH
# 		private_key = "/the/path/to/the/key"

# 	IP :
# 		stage用のIPセットと本番用のIPセットを定義して、hostというパラメターよりstageと本番を引き換えできます。
# 		stage_api_IPs = [stage用のIPセットを定義する]
# 		prod_api_IPs = [本番用のIPセットを定義する]

# 		IPセットの選択
# 		例 ： hosts = stage_api_IPs

# 	Folder：
# 		サーバの目標フォーダーセットとLocalのフォーダーセットを下記のパラメターに設定する
# 		サーバのフォーダーセット
# 		target_folder = ['/home/chenguowei/AAA','/home/chenguowei/BBB']
# 		Localのフォーダーセット
# 		local_folder = ['/Users/chenguowei/Documents/CCC','/Users/chenguowei/Documents/EEE']
		
# 		目標は順番でMatchする
# 		例 ： '/Users/chenguowei/Documents/CCC'' の中身は '/home/chenguowei/AAA' にアップロードする

# 実装
# 	python auto_deploy.py


import pysftp
from itertools import izip

# the IPs
stage_api_IPs = ['12.12.12.12']
prod_api_IPs = ['8.8.8.8','0.0.0.0']

# which IP sets are going to be used
hosts = stage_api_IPs

# sftp username 
username = "chenguowei"
# sftp key files
private_key = "/the/path/to/the/key"

# the target folder *** DON'T FORGET THE '/' 
target_folder = ['/home/chenguowei/AAA','/home/chenguowei/BBB']

# the local folder 
local_folder = ['/Users/chenguowei/Documents/CCC','/Users/chenguowei/Documents/EEE']

# get all of the hosts
for host in hosts:

	# acclaim a global variable to save the connection
	srv = None
	try:
		# get the connection 
		srv = pysftp.Connection(host=host, username=username ,private_key=private_key)
		print "connect to %s" %host

		# get all of the folders and fetch each other
		for target,local in izip(target_folder,local_folder):
			print "Upload ",local," to ",target

			# if the folder is not exist, then make it 
			if srv.isdir(target) is not True:
				print "create folder : ",target
				srv.mkdir(target,mode=777)

			# upload the files
			print "start uploading %s" %target			
			# why put_r -> because it can upload the folders in the folder
			srv.put_r(local,target,preserve_mtime=False)
			print "File Transfer: SUCCESS"

			# to list the files in the folder, if you wanna show it 
			#print srv.listdir()

		print "close to connect to %s" %host

	except StandardError as reason:
		# Error control
		print "Got some errors to upload the files to %s" %host
		print "File Transfer: FALSE"







