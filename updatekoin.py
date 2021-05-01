@@ -23,6 +23,7 @@ def main():
          "User-Agent": "okhttp/3.12.12"
     }
     print(ttp+"["+g+"%"+ttp+"] Inject Data ...")
     requests.get("http://www.litatom.com/api/sns/v1/lit/follow/6007e9665a80e9116050cdd9?sid="+ses+"&loc=ID&uuid="+uuid+"&version=3.8.2.1&lang=in&platform=android", headers=headers).text
     time.sleep(3)
     for i in range(jml):
          print()
