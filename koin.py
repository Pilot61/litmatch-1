@@ -5,6 +5,7 @@
b = ("\33[0;36m")#Blue")
red = ("\33[31;1m")#Red")
ttp = ("\033[0m")#LightGrey")
underline = ('\033[4;37;48m')

def main():
     os.system("clear")
@@ -29,8 +30,8 @@ def main():
          r = requests.post("http://www.litatom.com/api/sns/v1/lit/account/deposit_by_activity?sid="+ses+"&loc=ID&uuid="+uuid+"&version=3.8.1&lang=in&platform=android", headers=headers, data=json.dumps(data)).text
          cek = json.loads(r)
          if cek['success'] ==True:
               print(ttp+"["+g+str(len(i))+ttp+"] Berhasil")
               print(ttp+"["+g+str(i)+ttp+"] Berhasil")
          else:
               print(ttp+"["+red+str(len(i))+ttp+"] Coba Lagi Besok")
               print(ttp+"["+red+str(i)+ttp+"] Coba Lagi Besok")

main()
