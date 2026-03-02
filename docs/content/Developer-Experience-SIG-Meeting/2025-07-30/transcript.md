SIG: Developer Experience SIG Meeting
Date: 2025-07-30
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/LzTjDOziqnuZZq3Vw7mfD--AsjQJ4VItCV9XcqtFb0yTGNyqsMRfFi0HM-ZyeNFX.t-TXfWiINDrnIqJw
============================================================

## Zoom Recording Transcript

**patrickpok** 09:29 Le loup. Antoine Hohio Canumi.
**Antoine Toulme** 09:35 De la
de
Il y a.
**patrickpok** 09:42 Juste pour savoir parce que j'aimerais donc je suis nouveau là et j'aimerais donc contribuer pour le côté Java. Donc En fait, il y a un projet Java qui s'appelle Apache Spark, et je voudrais savoir comment comment on fait.
**Antoine Toulme** 09:59 Comment on fait
tout d'abord, nous sommes ici dans un meeting qui supposé être à propos de l'expérience des développeurs qui développent avec Open diameterie, qui est donc
une
une attitude différente. On est pas là pour parler d'un framework en particulier, mais supposément, je crois, et c'est la première fois que je viens à ce meeting, il y a des notes pour le meeting.
est-ce que c'est-à-t-il.
**patrickpok** 10:33 Voilà, merci!
**Antoine Toulme** 10:36 Donc nous sommes le 30 lundi.
**patrickpok** 10:40 Là, je suis moi, je suis en Chine, là actuellement, et donc il fait les deux heures du matin, je suis en pyjama, etc. Donc j'ai pas tourné ma caméra, je n'ai pas envie de tourner.
**Antoine Toulme** 10:51 Pas de problème.
donc si tu veux, tu peux mettre ton nom euh
dans le document.
donc ta question est plus par rapport à Patty's Park Quelle est ta relation avec Appathis Park Est-ce? que tu es un utilisateur ou est-ce que tu es un développeur de Spark ou.
**patrickpok** 11:08 Utilisateurs dans le monde Java Tu connais un tout petit peu Java.
**Antoine Toulme** 11:15 Il y a.
**patrickpok** 11:16 Il y a une grande entreprise derrière qui s'appelle Databric. J'ai aucun rapport avec Data Bricks Il y a une communauté open source qui le maintient en fait
et nous en fait, on développe ce parc rapide, qui est donc Spark sur le Gpiu
et donc nous, on comprend ce qu'on appelle.
**Antoine Toulme** 11:41 Par contre.
**patrickpok** 11:41 Pour le côté Jpe, mais on est très faible pour le côté. Observabilité de la Pachis Pack et.
**Antoine Toulme** 11:50 Comme tu as bien dit. C'est un orchestrateur pour jobs qui permet d'utiliser une flotte de
machines pour utiliser des jobs en Parallèle C'est parfait pour les gros jobs de batchu et donc ça fait sens.
nous moi. Je travaille pour une compagnie qui s'appelle Sprinter.
**patrickpok** 12:14 On est utilisateur de très très gros utilisateurs de Smunk. J'étais chez Apple avant où on a un des plus gros contrats du monde peut-être.
au de
connaître le.
**Antoine Toulme** 12:24 Merci pour particulièrement pour ce Plank Observability, qui est une solution qui est basée sur Opentametery qui permet de faire tout ce qui est métrique et trace. Les logs continuent de venir de ce plan plateforme.
Donc, de cette Il y a des composants qui sont utilisés aujourd'hui par Spank, qui font partie d'open diamétrie que tu peux utiliser tout de suite qui te permettraient de voir un petit peu Ce qui se passe et aussi le fait que ce parc elle-même, c'est une comment dire n'a pas une bonne.
une bonne histoire au niveau faisabilité surtout parce que Data bricks est en fait un fork
de leur produit qui est pour azur, donc on a le problème. On a des clients qui sont sur Azur qui ont donc leur version et leur of laver de ce parc, donc on a dû créer pour eux une solution. Je vais te donner
juste pendant que.
**patrickpok** 13:26 Cherche donc deuxième link qui est
parce que nous, moi, d'après ce que j'ai compris, je pense que nous on veut travailler sur le Java Agent.
Toi, tu nous as donné un lien pour le.
**Antoine Toulme** 13:39 Parce qu'il y a plusieurs façons d'avoir de l'instrumentation que tu vas vouloir faire sur ton job.
**patrickpok** 13:43 Mm.
**Antoine Toulme** 13:44 Est-ce que tu vas l'écrire en Java et tu vas vouloir avoir une vue de ce qui se passe dans ton job. Par exemple, si tu attends pour le Jp, la Latten Sea, cette flotte d'agents Java va vouloir envoyer cette information à peutêtre des collecteurs et éventuellement un back end, c'est déclenchement.
**patrickpok** 14:01 Le jazza et je peux l'envoyer directement dans le back-end sans passer par le collecteur non.
**Antoine Toulme** 14:06 Oui, tu peux
d'accord.
Cela dit, une bonne raison pour laquelle on fait, c'est que si tu le fais par le collecteur, Tu as un peu plus de backpresser ton agent, par exemple, vu que c'est des jobs qui sont éphémères
possible qu'il collectionne pas l'information à temps ou que l'information soit envoyée avant que le truc soit tué. Il y a aussi le collecteur peut faire des gens à utiliser sa mémoire et il peut utiliser pas mal de mémoire juste parce qu'il a un back up, une queue de l'information.
**patrickpok** 14:37 Compris le.
Et puis bon, il y a des gens qui font ça par sécurité, puisqu'ils aiment bien aussi pouvoir avoir un point d'entrée, donc ça, tu peux juste filtrer par Ipp, etc.
D'accord.
**Antoine Toulme** 14:48 Mais ce que je t'ai envoyé là c'est un truc qui s'appelle Apache Park Receiver, qui est en fait quelque chose qui se connecte à ce park et qui va pouvoir aussi avoir des métriques qui sont données par l'orchestrateur, qui sont aussi intéressantes, par exemple, combien de jobs qui sont en train de tourner.
est-ce qu'il y a des jobs qui sont pending Est-ce? que tout va, bien est-ce, qu'il y a les échecs de certains jobs? Même si tous tes agents Java qui donnent cette information, il va falloir que tu puisses aussi avoir une vue de l'orchestration en elle-même n'est-ce, pas?
Le problème de cette orchestration, c'est qu'elle n'est pas disponible directement, donc Il va falloir que tu utilises un truc qui s'appelle un initcript qui va pouvoir se déployer sur la
puisque ça s'est un petit peu laissé aux gens, Tata Brix va avoir plus de guidelines que nous, mais par exemple, pour injure, il y a juste une taxbox où tu peux faire un drop script et tu dis exact: si tu veux dans ici tout.
**patrickpok** 15:58 D'accord.
**Antoine Toulme** 16:00 Ok, donc voilà voilà les instructions, le peu d'informations.
toujours un bon en savoir et ça, c'est une recherche qui a été faite par un de mes développeurs à l'époque et tu peux voir aussi le petit bashcript qui l'a mis. Tu peux t'inspirer de ça, tu es pas obligé d'utiliser ça Verbatine.
tu sais, Open Source tu peux faire ce que tu veux, avec pourtant, c'est que quelqu'un l'utilise, qu'on ait un peu plus d'usage de ce genre de solutions parce que, en général, je voudrais parler avec un Pm de Data Brix. Et je lui dis: C'est pas possible, comme on fait votre orchestre m'a dit:
on n'avait pas vraiment bien pensé
pour Azur y'a un truc qui s'appelle Agios Moniteur, donc ce qu'on envoie en fait, c'est qu'on envoie des logs depuis notre orchestrateur et tu peux utilisant un jeu, transformer ce log en métrique et avoir des informations. C'est dégueulasse, parce que maintenant tu utilises deux services d'azur et tu vas te payer pour avoir cette information et cette information
Question: Pour lui, c'était est-ce: qu'elle est vraiment à jour ou estce que c'est toutes les cinq secondes 10 s 30 s, Tu as un update, pas vraiment, c'est vraiment à toi de juste faire confiance au système. Quoi donc trop de Moven Pace? Au lieu de ça, tu vas direct, tu dis: Toi, ton truc, t'as un collecteur qui tourne directement sur la Noad et tu peux avoir toutes les informations qui sont envoyées exprimées directement au back.
Pour ce qui est javaage bon alors engerbage. C'est mignon, c'est
s'est fait plusieurs choses: D'abord, il y a Openty Java, qui est donc un Sd qui dit: Voilà comment Est-ce qu'on va discuter avec un back end? Et voilà à quoi ressemble un sdoké? En général, donc ça, c'est le truc de base. Le top, le Java.
un truc qui vient avec des opinions c'est-à-dire, qu'il dit: si jamais je vois dans la base dans le code, Vous pouvez utiliser cette librairie pour aller instrumenter cette fonction de cette librairie. Par exemple, je suis en train de regarder quartz juste avant qu'on démarre ce coall.
Je sais pas s'ils ont le truc pour Spark, mais s'ils ont
voilà un truc pour ce parc, j'ai jamais regardé, je ne sais pas exactement ce qu'ils font, mais ce que je peux imaginer.
**patrickpok** 18:14 Ça, c'est Spark le Web service, donc c'est pas Apachey's Park, ça, le sport qui est ici, c'est le.
C'est vrai, c'est vrai.
parce que nous, c'est une direction, moi, je suis tout à fait d'accord avec ce que tu viens de dire, et c'est une direction à laquelle nous on veut essayer, et donc moi je suis là pour essayer ça ou de faire un appâtis. Park.
**Antoine Toulme** 18:37 D'accord, donc est-ce qu'il déjà quelque chose, une issue open pour ça.
je ne vois pas d'open issue dans jamais présentation pour ça.
donc le truc aussi, c'est que
il faudrait comprendre exactement qui est-ce que tu veux instrumenter? Il y a des choses que tu peux faire toi-même c'est-à-dire, que tu peux prendre ton Job et ton Job, tu l'écris en Java toi-même, tu sais ce que tu veux tracer, tu sais ce que tu veux émettre en termes de métrique, etc.
Donc tu peux directement là-dedans dire. Ouvre un spa. Capture cette durée d'exécution. Pas besoin d'avoir quelque chose qui soit commun, tu peux ensuite dire, c'est tellement commun et ça m'arrive toujours tout le temps, J'aimerais que ce soit quelque chose que je n'ai pas besoin de dire à tous mes développeurs à chaque fois qu'ils écrivent un job, donc on va créer une librairie, on va peutêtre même la pousser dans Open diamétrie comme ça, ils peuvent juste
utilisez ça.
**patrickpok** 19:35 Ce deuxième cas, le deuxième cas. Donc déjà maintenant le premier, ça veut dire dans notre job, on écrit nos traces, par exemple, pour qu'on met quelque chose dans une Db ou qu'on envoie quelque chose dans Kafka et tout, ça, on le fait on doit écrire le code nous même, mais c'est possible et c'est faisable.
Par contre, là, c'est dire, on est en train de refaire ça sur tous nos jobs, et demain on a des centaines, voire même milliers, de jobs, et au lieu de copiés ou d'écrire des librairies. On s'est dit pourquoi c'est ce que moi, j'essaie de faire, mais je comprends pas comment ce repos. Il fonctionne, pas trop. Le code Pour le moment. J'arrive sur ce repos, je sais lire jamais, mais c'est
c'est compliqué, c'est pour ça que je voulais demander.
**Antoine Toulme** 20:23 Ouais donc l'instrumentation fonctionne avec du métata c'est-à-dire, qu'elle manipule bitcode des trucs existants, n'est ce pas.
**patrickpok** 20:31 Hmm.
**Antoine Toulme** 20:32 Donc si tu prends, puisque j'étais dans quartz juste maintenant, Quartz t'as trois. C'est un truc qui est capable de faire de la réflexion
pour lire n'importe quelle référence d'utilisation de quartz dans un code pour ensuite aller faire l'instrumentation.
**patrickpok** 20:53 Donc Uh.
**Antoine Toulme** 20:55 Donc le quartz Instantan module, par exemple, capable d'injecter de lire, donc je pense que c'est le
C'est le boulot qui est difficile ensuite dans
si tu reviens au Top Label, donc Quartz Library, c'est le truc qui en fait l'instrumentation elle-même. En ayant accès au code de manière libre
et donc qui fait la création du spam, mais aussi qui comprend comment mettre les informations sur le spam c'est-à-dire, quel est le nom du span qu'on va prendre. Quels sont les attributs qu'on va aller chercher, et ils peuvent les extraire des objets modèles de type quartz Job, par exemple, ça serait pareil pour vous parce qu'en fait un job, que ce soit Quartz ou Spark C'est un peu la même idée exécution, donc ça va être quelque chose qui va être similaire à ça.
L'idée pour t'aider le mieux, c'est que tu ouvres tout de suite une issue dans option en me disant: Hey, c'est ce problème, j'ai maintenant le besoin de créer ça, et il faut que ça soit nickel et bien fait, donc s'il vous plaît est-ce, que vous pouvez m'aider à même juste avoir.
Est-ce que c'est important dans ce genre de projets? Vu la taille d'open diamétriques?
Bonne soirée
et même des gens qui disent: Je suis intéressé aussi parce que ça va être intéressant de voir qui d'autre aussi vient t'aider si tu veux parce que tu ne vas pas vouloir être la seule maintenance de ce truc, la vie est courte, ça veut être aussi un recordman pour ajouter ça dans le Pository parce que, sinon on a beaucoup de codes qui commencent à mourir sur son pied.
donc et ouais donc ça, c'est un truc à faire. Je ne sais pas si tu étais au courant. Il y a un truc qui s'appelle auto-instrumentation Est-ce. que tu es au courant de ça?
**patrickpok** 22:45 Nous on.
**Antoine Toulme** 22:47 Bon, c'est bien d'avoir une instrumentation, mais après il faut la délivrer, et ça ça fait mal, parce que c'est difficile de C'est difficile de rendre ça facile pour les gens, tu ne vas pas leur demander d'ajouter la librairie chaque fois. Enfin, des problèmes d'instrumentation. Là dessus, en plus, tu vas voir manager la version de ton instrumentation et tu vas vouloir faire ça à l'extérieur du Job n'est-ce, pas.
**patrickpok** 23:11 Ok.
**Antoine Toulme** 23:11 Donc ils ont créé un truc. Mon collègue qui s'appelle Jason Brown, qui en parle très bien, il explique ce qui se passe.
Youtube.
**patrickpok** 23:26 Mm.
**Antoine Toulme** 23:27 Ah! Voilà
comme
donc
mon collègue en parle bien en gros, ce qui se passe, c'est que tu peux en Java créer ce qu'on appelle des Java Agians, Java Egun. Ce sont des trucs qui tournent avant que la démarre.
c'est très utilisé par tout ce qui est Memory Ofiler Truc comme ça. Open Symétrie Osso utilise ça également
ce que tu
Java Autuntation.
**patrickpok** 24:01 D'accord.
**Antoine Toulme** 24:01 Donc maintenant ce genre va pouvoir faire une introspection du code avant que le Job démarre.
**patrickpok** 24:07 Ok.
**Antoine Toulme** 24:08 Quand tu fais cette introspection, il lit le Bycode et il s'arrête à chacune des endroits ou qui ferait sens d'avoir une instrumentation, c'est à dire, ça ressemble à un collège Http, ça vautrait le coup d'aller mettre un span autour pareil pour tout ce qui est Spark spécifique. Tu pourrais faire en sorte que il fasse ok, donc je vois bien que cette fonction du Code, on a normalement une instrumentation qui est là pour ça. Par défaut, on va instrumenter ce code sans que le développeur n'ait rien à faire.
**patrickpok** 24:35 D'accord.
**Antoine Toulme** 24:36 Cela.
donc tu pourrais même faire un bandeau de ça, parce que toi tu as complètement contrôle de comment le skadulaire dans ce parc va skaduler les jobs.
**patrickpok** 24:46 Et du.
**Antoine Toulme** 24:46 Pour tous les jobs en Djava De ce type, Tu vas me mettre cette variable qui va dire injecte le toling de Java Pour faire tout ce qui est expression détresse, tu peux utiliser la même technique avec des variables d'environnement pour dire où est ce que le code doit aller le niveau de logging, tu peux avoir plus d'informations assez facilement.
Et justement, c'est ce qu'on recommande à nos consommateurs. La plupart du temps, c'est avant d'aller faire un tas de boulot vous même estce que vous pouvez essayer d'utiliser cette fonction pour voir ce que vous avez qui arrive gratuitement.
Si tu veux. Parce que la plupart de nos clients sont leurs applications sont du web Teare. Toutes ces instrumentations sont déjà là, donc tu as déjà tout ça qui arrive, donc je sais pas pour toi si ça donnerait quelque chose, mais ça pourrait avoir des surprises en tout cas.
et voilà.
**patrickpok** 25:46 D'accord, je vais essayer ça juste pour les petites questions, plutôt paperasse et et
paperasse. Demain je pense, j'ai vu il y a une Java Sig, c'est là où on parle de l'instrumentation, parce que c'est au musée de la nuit, mais je vais essayer de penser ça.
plus de questions, j'ai, c'est très clair, je vais commencer juste, j'ai fini toutes mes questions. Open télémétrie, je ne savais pas qu'il y avait quelqu'un de ce plan qui va venir Est-ce. que je peux te poser des questions? Plus Sprinter.
**Antoine Toulme** 26:21 Ce meeting est enregistré et.
**patrickpok** 26:25 Ah, d'accord.
**Antoine Toulme** 26:25 Tous les gens de Sncf. Si tu veux avoir une discussion avec nous.
bon pas de problème, on peut être du faire ça à un autre moment. Puis il est deux heures du matin. Pour toi, on peut parler plus tard, moi je suis basé en Californie. Donc je peux parler avec la Chine après dans l'après-midi. Si tu veux mon e-mail, je peux te le donner ici parce que c'est pas du tout privé,
tu peux prendre contact avec moi, et puis on peut avoir une discussion plus longue avec toi et ton équipe. Je peux inviter aussi des gens de Splank qui travaillent sur ce genre de technologie qui peuvent vraiment parler en détail et qui peuvent t'aider pour aller plus vite. On A également d'ailleurs des discussions à avoir avec invida parce que nous on a on a également un intérêt
pour faire un meilleur travail pour avoir, par exemple les Metrix qui viennent de Carttenvida avec le Dc, exporter des trucs comme ça, donc
ça peut être une discussion.
**patrickpok** 27:22 J'ai aussi c'est enregistré, j'ai juste t'envoyer un e-mail après parce que j'ai moi personnellement de mon utilisation de ce plan. J'ai beaucoup de pas de questions, mais justement, des choses à discuter, et puis je sais que ma boîte a des directions côté Esplan que j'aimerais juste en parler, voilà en tout cas. Merci beaucoup pour
pour toutes les deux mois pour cette journée là, j'ai des choses à faire pour que tu es Open télémétrie et puis je vais essayer de préparer mes questions pour commencer à la même heure
dans 24 h. Je vais
s'il va y avoir des gens qui vont arriver au moins.
**Antoine Toulme** 28:09 Oui.
**patrickpok** 28:10 Que j'essaie de faire
d'accord très bien.
**Antoine Toulme** 28:12 Beaucoup de.
**patrickpok** 28:12 Bonjour Antoine, je te souhaite une très très bonne journée, Je ne savais pas du tout à quoi m'attendre. C'est un de mes premiers meetings où il y a quelqu'un, généralement je vais dans les autres meetings où il n'y a personne, et donc Je suis super content, donc merci beaucoup à toi.
**Antoine Toulme** 28:25 Pauvre. Ok, ben oui, non, mais maintenant il y a plus de gens que ça, c'est étrange.
ne pas
d'ici.
**patrickpok** 28:31 D'accord. Merci beaucoup, salut.
**Antoine Toulme** 28:33 Ouais.
