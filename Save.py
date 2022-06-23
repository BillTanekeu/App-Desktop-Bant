from abc import ABC
import mysql.connector as MC

class EcritureBD(ABC):
    
    def save_project(nameP):  
        
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            project = (curseur.lastrowid, nameP)
            req = "INSERT INTO `projet` (`id_projet`, `nom_projet`) VALUES (%s, %s)"
            project = (curseur.lastrowid, nameP)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    

    def save_Amphi(amphi, capacite):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `amphi` (`id_amphi`, `nom_amphi`, capacite_amphi) VALUES (%s, %s, %s)"
            project = (curseur.lastrowid, amphi, capacite)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    
    def save_departement(nom_dep):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `departement` (`id_departement`, `nom_departement`)  VALUES (%s, %s)"
            project = (curseur.lastrowid, nom_dep)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id

    def save_filiere(nom_filiere, dep):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `filiere` (`id_filiere`, `nom_filiere`, `id_departement`) VALUES (%s, %s, %s)"
            project = (curseur.lastrowid, nom_filiere,dep)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    
    def save_niveau(nom_niveau):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `niveau` (`id_niveau`, `nom_niveau`) VALUES (%s, %s)"
            project = (curseur.lastrowid, nom_niveau)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id

    def save_specialite(filiere, nom_specialite):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `specialite` (`id_specialite`, `id_filiere`, `nom_specialite`) VALUES (%s, %s, %s)"
            project = (curseur.lastrowid,filiere, nom_specialite)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    
    def save_enseignant(nom_enseignant, dep):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `enseignant` (`id_enseignant`, `id_departement`, `nom_enseignant`) VALUES (%s, %s, %s)"
            project = (curseur.lastrowid,dep, nom_enseignant)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    

    def save_groupe(id_specialite, niveau, groupe, nb):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `groupe` (`id_groupe`, `id_specialite`, `id_niveau`, `nom_groupe`, `nb_etudiants`) VALUES (%s, %s, %s, %s, %s)"
            project = (curseur.lastrowid, id_specialite, niveau,groupe,nb)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    

    def save_matiere(groupe, dep, nom_matiere):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `matiere` (`id_matiere`, `id_groupe`, `id_departement`, `nom_matiere`) VALUES (%s, %s, %s, %s)"
            project = (curseur.lastrowid,groupe, dep, nom_matiere)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    

    def save_emploi(projet, filiere, niveau):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `emploi_temps` (`id_emploi`, `id_projet`, `nom_filiere`, `nom_niveau`) VALUES (%s, %s, %s, %s)"
            project = (curseur.lastrowid,projet, filiere, niveau)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    
    def save_cellule(emploi, matiere,amphi,enseignant, horaire, jour, cle):
        try:
            conn = MC.connect(host = 'localhost', database = "Bant", user = "root", password = "") 
            curseur  = conn.cursor()
            req = "INSERT INTO `cellule` (`id_cellule`, `id_emploi`, `nom_matiere`, `nom_amphi`, `nom_enseignant`, `horaire`, `jour`, `cle`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            project = (curseur.lastrowid,emploi, matiere, amphi, enseignant, horaire, jour, cle)

            curseur.execute(req, project)
            conn.commit()
            id = curseur.lastrowid
            
        except MC.Error as err:
            print(err)
            print("Pas de connection avec la BD")
        finally:
            if(conn.is_connected()):
                conn.close()
        
        return id
    



#print(EcritureBD.save_cellule(1,"inf",'ef','g','v','f',11))
