import os

ENCODING = "utf8"
DEL = "\",\""
MAIN = "cdiscount"
EXT = ".csv"

def delete_file(csv_file_name):
    if os.path.isfile(csv_file_name):
        os.remove(csv_file_name)

def divide_csv(csv_file_name,dest_csv_file_name,n_col):
    f = open(csv_file_name,encoding=ENCODING)
    f_dest = open(dest_csv_file_name,encoding=ENCODING,mode="a+")
    for line in f:
        content = line.split("\",\"")[n_col] + "\n"
        if content != "":
            if ";" in content:
                contents = content.split(";")
                for el in contents:
                    f_dest.write(el.replace("\n","").replace("\"","") +"\n")
            else:
                f_dest.write(content.replace("\n","").replace("\"","") +"\n")
    f.close()
    f_dest.close()

def show_cols(csv_file_name):
    f = open(csv_file_name, encoding=ENCODING)
    for i,line in enumerate(f):
        if i == 0:
            for el in line.split(DEL):
                print(el.replace("\"",""))
    f.close()

map = [
    MAIN + "_horo", # Horodateur
    MAIN + "_utilisation_cdiscount", # Avez-vous déjà utilisé le site Cdiscount
    MAIN + "_pb_rencontre_cdiscount", # Avez-vous déjà rencontré un ou plusieurs problème(s) avec Cdiscount ?
    MAIN + "_hors_cdiscount_site_used", # Hormis Cdiscount, quel(s) site(s) ou application(s) e-commerce utilisez-vous ?
    MAIN + "_nb_achats_mois_cdiscount", # Combien de fois par mois achetez-vous des articles chez Cdiscount ?
    MAIN + "_nb_achats_mois_autre_ecom", # Combien de fois par mois achetez-vous des articles sur d'autres sites ou applications e-commerce?
    MAIN + "_categorie_fav_cdiscount", # Quelle catégorie d'article consultez-vous le plus régulièrement chez Cdiscount ?
    MAIN + "_categorie_fav_autre_ecom", # Quelle catégorie d'article consultez-vous le plus régulièrement sur d'autres sites ou applications e-commerce ?
    MAIN + "_service_client_cdiscount", # Comment trouvez-vous le service client Cdiscount ?
    MAIN + "_ergonomie_cdiscount", # Comment trouvez-vous l'ergonomie du site cdiscount.com ?
    MAIN + "_ameliorer_cdiscount", # Si vous aviez quelque chose à améliorer sur Cdiscount, que choisiriez-vous ?
    MAIN + "_utilisation_autre_ecom", # Utilisez-vous d'autre(s) site(s) ou application(s) e-commerce ?
    MAIN + "_quel_autre_ecom", # Quel(s) site(s) ou application(s) e-commerce utilisez-vous ?
    MAIN + "_freq_achat_autre_ecom", # À quelle fréquence achetez-vous des articles sur des sites ou applications e-commerce ?
    MAIN + "_fav_cat_autre_ecom", # Quelle(s) catégorie(s) d'article consultez-vous le plus régulièrement sur des sites ou applications e-commerce ?
    MAIN + "_reco_achat_ligne", # De manière générale, quel site ou application e-commerce recommanderiez-vous dans le cadre d'un achat en ligne ?
    MAIN + "_fav_carac_ecom", # Quelle caractéristique est la plus importante pour un site ou une application e-commerce ?
    MAIN + "_genre", # Vous êtes
    MAIN + "_age" # Quel âge avez-vous ?
]

for i,el in enumerate(map):
    delete_file(el+EXT)
    divide_csv(MAIN+EXT,el+EXT,i)