# Mesh-Wifi

Ce projet visait à évaluer les performances réseau d'un réseau mesh wifi.  
Il s'agissait d'établir des protocoles de test et définir des architectures afin de réaliser des mesures de débit grâce à Iperf3.  
  
  3 Protocoles de test ont été effectués:  
  - Arrangement linéaire des noeuds, avec mesures de débit en position fixe à chaque noeud du réseau maillé
  - Arrangement en L des noeuds, avec mesures de débit en position fixe à chaque noeud du réseau maillé
  - Stream vidéo en arrangement linéaire des noeuds: déplacement le long du réseau afin d'observer d'éventuels latences lors de saut d'un noeud à l'autre  

Une Raspberry PI a été utilisée avec un OS installé et Iperf. La Raspberry était utilisée en tant que serveur, elle était connectée au point d'entrée.  
  
Afin d'automatiser les tests et d'avoir un rendu graphique des variations de la bande passante, un script python a été réalisé <client.py>.  
Ce script utilise un module iperf3 pour lancer en tant que client la machine et se connecter au serveur dont l'adresse IP est spécifiée dans le script.  
Ainsi un test d'une durée de 30 secondes est lancé et les résultats sont stockés dans un fichier JSON généré par le script.  
Pour l'affichage et la visualisation des résultats, la librairie matplotlib a été d'abord utilisée. Le script possède encore le code qui générait à la suite du test un graphe de la variation du débit en Mbit/s en fonction du temps en secondes.  
Puis par soucis d'esthétique, Grafana, un logiciel de monitoring et d'affichage de metrics/données temporelles, a été utilisé. Cet outil permettait ainsi de créer un dashboard pour chaque noeud du réseau et rassembler les différents graphiques des tests.  
  
Lien vers le dashboard Grafana pour l'arrangement linéaire, Noeud Couloir:  
https://snapshots.raintank.io/dashboard/snapshot/Z50UxOExFlOHDVUhNqnTbTFWyPaX6RN1  
  
Lien vers le dashboard Grafana pour l'arrangement linéaire, Noeud Techlab 2:  
https://snapshots.raintank.io/dashboard/snapshot/VrbxYR7pQfK2axtd4FQJBSloBkXgGot7  
  
Lien vers le dashboard Grafana pour l'arrangement en L, Noeud Techlab2:  
https://snapshots.raintank.io/dashboard/snapshot/KnX4RQye9PcB9DcVr0Asfll4OiZG0Ok3  
  
Concernant le stream vidéo en déplacement le long des noeuds du réseau, aucune latence n'a été observée. Le test a été réalisé lors de la visualisation d'une vidéo internet. Peut-être aurait-il fallut tester avec un stream live vidéo du type Teams, Google Meet, FaceTime ...  
