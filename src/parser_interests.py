import utils
from os import getcwd

def parse_interests(user_data: dict) -> dict:
    """ Goes through interests and parses number of interest per category """
    interests_path = getcwd() + "/temp/ads_and_businesses/ads_interests.json"
    interest_categories_path = getcwd() + "/src/interests.json"

    user_interests = utils.json_file_converter(interests_path)["topics"]
    interest_categories = utils.json_file_converter(interest_categories_path)

    interest_category_count = {}
    interest_category_total = {}

    category_list = list(interest_categories.keys())

    for category in category_list:
        interest_category_count[category] = 0
        interest_category_total[category] = 0
    
    for category in category_list:
        for interest in interest_categories[category]:
            interest_category_total[category] += 1
            if interest in user_interests:
                interest_category_count[category] += 1
    
    # standardise results by dividing by total number of interests per category
    for category in category_list:
        interest_category_count[category] = int((interest_category_count[category] / interest_category_total[category]) * 100)
        
    # transform to list
    interest_count_list = list(interest_category_count.values())

    print("interest_category_count: ", interest_category_count)

    # build a html interest string for the side list of interests
    html_interests = html_interest_list_builder(user_interests, interest_categories)

    user_data["interest_categories"] = category_list
    user_data["interest_count"] = interest_count_list
    user_data["html_interests"] = html_interests

    return user_data

def html_interest_list_builder(user_interests: list, interest_categories: dict) -> str:
    """ Takes a list of user interests and the interest categories dict, and produces a string in HTML format of user interests """
    start_html = """<li class="list-group-item"><div class="widget-content p-0"><div class="widget-content-wrapper"><div class="widget-content-left"><div class="widget-heading">"""
    mid_html = """</div><div class="widget-subheading">"""
    end_html = """</div></div></div></div></li>"""

    politicians = ['Adrien Quatennens', 'Adrien Taquet', 'Agnès Buzyn', 'Agnès Evren', 'Agnès Marion', 'Agnès Thill', 'Alain Carignon', 'Alain Juppé', 'Alexandra Siarri', 'Alexandre Jardin', 'Alexis Bachelay', 'Alexis Corbière', 'Ali Soumaré', 'André Chapaveire', 'André Chassaigne', 'André Gattolin', 'André Santini', 'Anne Hidalgo', 'Anne-Sophie Frigout', 'Anne-Sophie Pelletier', 'Arash Derambarsh', 'Arnaud Danjean', 'Arnaud Montebourg', 'Arnaud Robinet', 'Arnaud Viala', 'Audrey Azoulay', 'Aurélia Beigneux', 'Aurélien Taché', 'Aurore Bergé', 'Axelle Lemaire', 'Aymeric Chauprade', 'Barbara Pompili', 'Barbara Romagnan', 'Béatrice Descamps', 'Benjamin Cauchy', 'Benjamin Griveaux', 'Benjamin Lucas', 'Benoist Apparu', 'Benoît Hamon', 'Bernard Accoyer', 'Bernard Cazeneuve', 'Bernard Monot', 'Bernard Perrut', 'Blanche Chaussat', 'Brice Hortefeux', 'Brigitte Barèges', 'Brigitte Fouré', 'Brune Poirson', 'Bruno Beschizza', 'Bruno Bilde', 'Bruno Bonnell', 'Bruno Gilles', 'Bruno Gollnisch', 'Bruno Le Maire', 'Bruno Questel', 'Carine Petit', 'Caroline Cayeux', 'Catherine Griset', 'Cécile Duflot', 'Cédric O', 'Cédric Villani', 'Chantal Jouanno', 'Charles-Henri Gallois', 'Christian Eckert', 'Christian Estrosi', 'Christian Jacob', 'Christian Kert', 'Christian Lechevalier', 'Christiane Taubira', 'Christine Lagarde', 'Christophe Boudot', 'Christophe Castaner', 'Christophe Clergeau', 'Christophe Najdovski', 'Claire Monod', 'Claude Bartolone', 'Claude Raynal', 'Claudine Schmid', 'Clémentine Autain', 'Corinne Lepage', 'Corinne Morel Darleux', 'Corinne Vignon', 'Damien Lempereur', 'Daniel Cohn-Bendit', 'Danièle Obono', 'Danielle Simonnet', 'David Cabas', 'David Douillet', 'David Rachline', 'Delphine O', 'Denis Baupin', 'Denis Broliquier', 'Didier Guillaume', 'Didier REAULT', 'Didier Tauzin', 'Djordje Kuzmanovic', 'Dominique Bertinotti', 'Dominique Bilde', 'Dominique de Villepin', 'Dominique Estrosi Sassone', 'Dominique Martin', 'Dominique Tian', 'Edouard Martin', 'Édouard Philippe', 'Edwige Diaz', 'Eléonore Bez', 'Elisabeth Borne', 'Elisabeth Pouchelon', 'Elsa Faucillon', 'Emmanuel Macron', 'Emmanuel Maurel', 'Emmanuelle Cosse', 'Emmanuelle Ménard', 'Emmanuelle Wargon', 'Eric Ciotti', 'Eric Coquerel', 'Éric Dupond-Moretti', 'Eric Woerth', 'Esther Benbassa', 'Eva Joly', 'Fabien Gay', 'Fabien Roussel', 'Fabienne Keller', 'Fiona Lazaar', 'Fleur Pellerin', 'Florence Parly', 'Florence Portelli', 'Florian Bachelier', 'Florian Philippot', 'Florie Marie', 'France Jamet', 'Franck Allisio', 'Franck de Lapersonne', 'Franck Louvrier', 'François Asselineau', 'François Baroin', 'François Bayrou', 'François Cuillandre', 'François de Rugy', 'François Fillon', 'François Hollande', 'François Kalfon', 'François Lamy', 'François Loos', 'François Rebsamen', 'François Ruffin', 'François Sauvadet', 'François-Xavier Bellamy', 'François-Xavier Pénicaud', 'Frédéric Cuvillier', 'Frédéric Lefebvre', 'Gabriel Amard', 'Gaëlle Lenfant', 'Gaëtan Dussausaye', 'Gaspard Gantzer', 'Gauthier Bouchet', 'Geoffroy Didier', 'George Pau-Langevin', 'Georges Fenech', 'Georges Mothron', 'Gérald Dahan', 'Gérald Darmanin', 'Gérard Collomb', 'Gérard Filoche', 'Gérard Larcher', 'Gérard Trémège', 'Gilbert Collard', 'Gilles Deterville', 'Gilles Le Gendre', 'Gilles Pennelle', 'Grégory Besson-Moreau', 'Guillaume Balas', 'Guillaume De Longeville', 'Guillaume Gontard', 'Guillaume Guérin', 'Guillaume Lacroix', 'Guillaume Peltier', 'Hélène Laporte', 'Henri Guaino', 'Hervé Gaymard', 'Hervé Juvin', 'Hervé Mariton', 'Hervé Morin', 'Hubert Falco', 'Ian Brossat', 'Isabelle Attard', 'Isabelle Balkany', 'Isabelle Surply', 'Isabelle Thomas', 'Jack Lang', 'Jacques Bompard', 'Jacques Borie', 'Jacques Boutault', 'Jacques Cheminade', 'Jacques Colombier', 'Jacques Domergue', 'Jacques Mézard', 'Jacques Myard', 'Jean Castex', 'Jean Hugues Ratenon', 'Jean Lassalle', 'Jean Messiha', 'Jean-Baptiste Djebbari', 'Jean-Christophe Fromantin', 'Jean-Christophe Lagarde', 'Jean-Claude Gaudin', 'Jean-François Copé', 'Jean-Frédéric Poisson', 'Jean-Jacques Bridey', 'Jean-Jacques Urvoas', 'Jean-Lin Lacapelle', 'Jean-Louis Borloo', 'Jean-Louis Fousseret', 'Jean-Luc Bleunven', 'Jean-Luc Mélenchon', 'Jean-Luc Moudenc', 'Jean-Marc Ayrault', 'Jean-Marie Le Pen', 'Jean-Marie Tetart', 'Jean-Marie Verani', 'Jean-Michel Blanquer', 'Jean-Paul Delevoye', 'Jean-Paul Garraud', 'Jean-Paul Huchon', 'Jean-Philippe Tanguy', 'Jean-Pierre Chevènement', 'Jean-Pierre Decool', 'Jean-Pierre Sueur', 'Jean-Vincent Placé', 'Jean-Yves Le Drian', 'Jérôme Rivière', 'Joachim Son-Forget', 'Joël Labbé', 'Joëlle Mélin', 'Johanna Rolland', 'Jordan Bardella', 'José Bové', 'Julie Lechanteux', 'Julien Dray', 'Julien Leonardelli', 'Julien Odoul', 'Julien Sanchez', 'Karim Ouchikh', 'Karima Delli', 'Karl Olive', 'Laetitia Avia', 'Laura Slimani', 'Laurent Fabius', 'Laurent Nunez', 'Laurent Wauquiez', 'Lionel Tardy', 'Lionel Tivoli', 'Loïc Hervé', "Loïc Prud'homme", 'Louis Aliot', 'Luc Chatel', 'Ludovic Pajot', 'Manon Aubry', 'Manuel Bompard', 'Manuel Valls', 'Marc Fesneau', 'Marie Duret-Pujol', 'Marie-Christine Arnautu', 'Marie-Christine Blandin', 'Marie-Christine Parolin', 'Marielle de Sarnez', 'Marie-Noëlle Lienemann', 'Marine Le Pen', 'Marion Maréchal', 'Marlène Schiappa', 'Martin Malvy', 'Martine Aubry', 'Martine Vassal', 'Marylise Lebranchu', 'Mathieu Klein', 'Mathilde Androuët', 'Mathilde Panot', 'Matthieu Chamussy', 'Maurice Leroy', 'Meyer Habib', 'Michel Barnier', 'Michel Pouzol', 'Michèle Alliot-Marie', 'Mounir Mahjoubi', 'Muriel Pénicaud', 'Myriam El Khomri', 'Nadine Morano', 'Naïma CharaÏ', 'Najat Vallaud-Belkacem', 'Natacha Bouchart', 'Nathalie Germain', 'Nathalie Griesbeck', 'Nathalie Kosciusko Morizet', 'Nathalie Loiseau', 'Nicolas Bay', 'Nicolas Doucerain', 'Nicolas Dupont-Aignan', 'Nicolas Florian', 'Nicolas Hulot', 'Nicolas Perruchot', 'Nicolas Sarkozy', 'Nicole Belloubet', 'Noël Faucher', 'Nora Berra', 'Nora Preziosi', 'Olivier Besancenot', 'Olivier Bettati', 'Olivier Dussopt', 'Olivier Faure', 'Olivier Véran', 'Pascal Canfin', 'Pascal Cherki', 'Pascal Durand', 'Pascal Savoldelli', 'Pascal Terrasse', 'Patrick Le Hyaric', 'Patrick Mennucci', 'Patrick Thevenin', 'Philippe Berta', 'Philippe de Beauregard', 'Philippe de Villiers', 'Philippe Doucet', 'Philippe Gosselin', 'Philippe Martin', 'Philippe Noguès', 'Philippe Olivier', 'Philippe Poutou', 'Philippe Pradal', 'Philippe Richert', 'Philippe Saurel', 'Philippe Sueur', 'Philippe Vardon', 'Philippe Vigier', 'Pierre Cohen', 'Pierre Jouvet', 'Pierre Larrouturou', 'Pierre Laurent', 'Pierre Moscovici', 'Pierre Serne', 'Pierre-Yves Bournazel', 'Rachida Dati', 'Rafik Smati', 'Raphaël Glucksmann', 'Raquel Garrido', 'Régis Juanico', 'Richard Ferrand', 'Robert Baud', 'Robert Hue', 'Robert Ménard', 'Roger Karoutchi', 'Ronan Loas', 'Roselyne Bachelot', 'Salah Amokrane', 'Sally Chadjaa', 'Samia Ghali', 'Sandrine Bélier', 'Sebastien Jumel', 'Sébastien Lecornu', 'Ségolène Royal', 'Sergio Coronado', 'Sibeth Ndiaye', 'Sophie Dion', 'Sophie Taillé-Polian', 'Stanislas Guerini', 'Steeve Briois', 'Stéphan Rossignol', 'Stephane Durbec', 'Stéphane Le Foll', 'Stéphane Peu', 'Stéphane Ravier', 'Stéphane Vidal', 'Sylvain Maillard', 'Sylvie Goulard', 'Thierry Mariani', 'Thierry Robert', 'Thierry Solère', 'Thierry Tsagalos', 'Thomas Gassilloud', 'Ugo Bernalicis', 'Valérie Boyer', 'Valérie Létard', 'Valérie Pécresse', 'Victorin LUREL', 'Vincent Chauvet', 'Vincent Peillon', 'Virginie Joron', 'Wallerand de Saint Just', 'Xavier Bertrand', 'Younous Omarjee', 'Yves Contassot', "Yves d'Amécourt", 'Yves Jégo', 'Yves Yves Pozzo di Borgo']
    html_interests = ""

    for interest in user_interests:
        corresponding_category = "Other"
        for category in interest_categories:
            if interest in interest_categories[category]:
                corresponding_category = category
            elif interest in politicians:
                corresponding_category = "Political Orientation"
        html_interests += start_html + interest + mid_html + corresponding_category + end_html

    return html_interests