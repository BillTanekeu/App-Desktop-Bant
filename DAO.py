from abc import ABC
import mysql.connector as MC

class Lecture_BD(ABC):
   
    
    def get_filiere():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT nom_filiere FROM filiere'
            curseur.execute(req)
            filiere = []
            
            for item in curseur.fetchall():
                filiere.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("non")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return filiere

    def get_niveau():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT nom_niveau FROM niveau'
            curseur.execute(req)
            niveau = []

            for item in curseur.fetchall():
                niveau.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("non")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return niveau
    

    def get_matiereFN(filiere, niveau):  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = """SELECT DISTINCT
                        matiere.nom_matiere
                        FROM
                            groupe,
                            specialite,
                            niveau,
                            filiere,
                            matiere
                        WHERE
                        matiere.id_groupe= groupe.id_groupe AND
                        groupe.id_niveau = niveau.id_niveau AND groupe.id_specialite = specialite.id_specialite 
                        AND specialite.id_filiere = filiere.id_filiere 
                        AND niveau.nom_niveau = "{}"
                        AND filiere.nom_filiere = "{}" """.format(niveau, filiere)
            curseur.execute(req)
            matieres = []

            for item in curseur.fetchall():
                matieres.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return matieres
    

    def get_amphi(matiere):  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = """SELECT DISTINCT amphi.nom_amphi
                    FROM matiere , groupe , amphi  
                    WHERE matiere.id_groupe = groupe.id_groupe  
                    AND matiere.nom_matiere = '{}' AND amphi.capacite_amphi>= groupe.nb_etudiants
                    ORDER by amphi.capacite_amphi ASC""".format(matiere)
            curseur.execute(req)
            amphi = []

            for item in curseur.fetchall():
                amphi.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("non")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return amphi


    def get_enseignant(matiere):  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = """SELECT DISTINCT enseignant.nom_enseignant , departement.nom_departement
                    FROM matiere , groupe , enseignant, departement
                    WHERE matiere.id_groupe = groupe.id_groupe  
                    AND matiere.nom_matiere = '{}' 
                    AND matiere.id_departement=enseignant.id_departement 
                    AND departement.id_departement = matiere.id_departement """.format(matiere)
            curseur.execute(req)
            enseignant = []

            for item in curseur.fetchall():
                enseignant.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("non")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return enseignant
    
    def Dict_matiere( niveau, filiere):
        dict_matiere = {}
        for niv in niveau:
            for fil in filiere:
                dict_matiere[(niv,fil)] = Lecture_BD.get_matiereFN(fil,niv)
        return dict_matiere

    #print(Dict_matiere(n,f))
    def Dict_amphi(matiere):
        dict_amphi = {}
        for mat in matiere:
            dict_amphi[mat] = Lecture_BD.get_amphi(mat)
        return dict_amphi


    def Dict_enseignant(matiere):
        dict_enseignant = {}
        for mat in matiere:
            dict_enseignant[mat] = Lecture_BD.get_enseignant(mat)
        return dict_enseignant

    def get_departement():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT id_departement, nom_departement FROM departement'
            curseur.execute(req)
            departement = []

            for item in curseur.fetchall():
                departement.append({item[1]:item[0]})
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return departement

    def get_specialite():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT id_specialite, nom_specialite FROM specialite'
            curseur.execute(req)
            specialite = []

            for item in curseur.fetchall():
                specialite.append({item[1]:item[0]})
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return specialite
    
    def get_filiere2():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT id_filiere, nom_filiere FROM filiere'
            curseur.execute(req)
            filiere = []

            for item in curseur.fetchall():
                filiere.append({item[1]:item[0]})
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return filiere

    def get_niveau2():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT id_niveau, nom_niveau FROM niveau'
            curseur.execute(req)
            niveau = []

            for item in curseur.fetchall():
                niveau.append({item[1]:item[0]})
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return niveau

    def get_groupe():  
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = 'SELECT id_groupe, nom_groupe FROM groupe'
            curseur.execute(req)
            groupe = []

            for item in curseur.fetchall():
                groupe.append({item[1]:item[0]})
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return groupe
    
    def get_cellule(id_emploi):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = """SELECT emploi_temps.nom_filiere, 	emploi_temps.nom_niveau ,cellule.cle, cellule.nom_amphi, 							cellule.nom_matiere, cellule.nom_enseignant  FROM cellule, emploi_temps
				            WHERE emploi_temps.id_emploi = "{}" and emploi_temps.id_emploi = cellule.id_emploi""".format(id_emploi)
            curseur.execute(req)
            dico = {}
            data = ()
            for item in curseur.fetchall():
                dico[item[2]] = (item[3], item[4], item[5])
                f = item[0]
                n = item[1]
            data  = (f,n, dico)
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return data
    
    def get_emploi(id_projet):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = """SELECT emploi_temps.id_emploi FROM `emploi_temps` WHERE emploi_temps.id_projet = "{}" """.format(id_projet)
            curseur.execute(req)
            data = []
            for item in curseur.fetchall():
                data.append(item[0])
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return data
    

    def get_projet():
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "SELECT * FROM `projet` WHERE 1 ORDER by id_projet DESC"
            curseur.execute(req)
            data = {}

            for item in curseur.fetchall():
                data[item[1]] = item[0]
            
        except MC.Error as err:
            print(err)
            print("Echec BD ")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return data
    
    


    
"""
f = Lecture_BD.get_filiere()
n = Lecture_BD.get_niveau()
m = Lecture_BD.get_matiereFN("informatique", "LICENCE 2")
print(f)
"""
#print(Lecture_BD.get_projet())