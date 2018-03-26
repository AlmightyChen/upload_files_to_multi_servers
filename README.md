# Upload the files to servers
 Chen Guowei

## 使用方法

#### 環境：
 	MACや 「 Python２ 」 をインストールした端末に

#### 実装する前
 	Psftpをインストール
 		pip を インストールしてるかとうか確認する pip --version
 		pip インストールしたら、psftp を インストール方法 sudo pip install psftp
 		pip インストールしてない方は、自分でインストール方法を探してください。

#### 設定
###### ユーザー名
 		username = "chenguowei"

 		keyのPATH
 		private_key = "/the/path/to/the/key"

###### IP :
 		stage用のIPセットと本番用のIPセットを定義して、hostというパラメターよりstageと本番を引き換えできます。
 		stage_api_IPs = [stage用のIPセットを定義する]
 		prod_api_IPs = [本番用のIPセットを定義する]

 		IPセットの選択
 		例 ： hosts = stage_api_IPs

###### Folder：
 		サーバの目標フォーダーセットとLocalのフォーダーセットを下記のパラメターに設定する
 		サーバのフォーダーセット
 		target_folder = ['/home/chenguowei/AAA','/home/chenguowei/BBB']
 		Localのフォーダーセット
 		local_folder = ['/Users/chenguowei/Documents/CCC','/Users/chenguowei/Documents/EEE']
		
 		目標は順番でMatchする
 		例 ： '/Users/chenguowei/Documents/CCC'' の中身は '/home/chenguowei/AAA' にアップロードする

#### 実装
 	python auto_deploy.py