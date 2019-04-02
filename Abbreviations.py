from nltk.stem import WordNetLemmatizer


def afkortingen(x):
    abbrevs={' d.a.v. ': ' daaraanvolgend ', ' d.m.v. ': ' door middel van ', ' d.t.v. ': ' door tussenkomst van ', ' d.w.z. ': ' dat wil zeggen ',
         ' d.z.z. ': ' dezerzijds ', ' depri ': ' depressief ',' desp. ': ' despotaat ', ' drs. ': ' drams ',
         ' dwz. ': ' dat wil zeggen ', ' dyn. ': ' dynastie ',' a\'dam ': ' Amsterdam ',  ' a.h.w. ': ' als het ware ',
         ' a.j.b ': ' alsjeblieft ', ' a.m. ': ' ante meridiem ',' a.s. ': ' aanstaande ', ' a.u.b. ': ' alstublieft ',
         ' aanw.vnw. ': ' aanwijzend voornaamwoord ',' abd. ': ' abdij ', ' abm. ': ' aartsbisdom ',
         ' abs. ': ' aartsbisschop ', ' achterv. ': ' achtervolging ',' afl. ': ' aflevering ', ' asa ': ' als en slechts als ',
         ' b. v. ': ' bijvoorbeeld ', ' b.v. ': ' bijvoorbeeld ',' bab. ': ' Babylonisch ', ' bet. ': ' betekenis ',
         ' betr. ': ' betreffende ', ' bib ': ' bibliotheek ',' bijv. ': ' bijvoorbeeld ', ' bijw. ': ' bijwoord ',
         ' bm. ': ' bisdom ', ' bn. ': ' bijvoeglijk naamwoord ',' bs. ': ' bullshit ', ' bv. ': ' bijvoorbeeld ',
         ' bw. ': ' bijwoord ', ' byz. ': ' byzantijns ',' c.q. ': ' in dat geval ', ' c.s. ': ' cum suis ',
         ' ca. ': ' circa ', ' cgn ': ' gorpus gesproken nederlands ',' e.d. ': ' en dergelijke ', ' e.e.a. ': ' een en ander ',
         ' eil. ': ' eiland ', ' enz. ': ' enzovoorts ',' es. ': ' echtscheiding ', ' evt. ': ' eventueel ',
         ' fed ': ' federatie ', ' ff. ': ' even ',' form. ': ' formeel ', ' fr. ': ' frans ',
         ' fra. ': ' frans ', ' ft. ': ' fort ',' g ': ' gram ', ' ghert. ': ' groothertogdom ',
         ' gr. ': 'grieks ', ' grs. ': ' graafschap ',' grvm. ': ' grootvorstendom ', ' g.v.d. ': ' godverdomme ',
         ' h.m. ': ' hare majesteit ', ' ha ': ' hectare ', ' hert. ': ' hertogdom ', ' hr. ': ' harer ',
         ' hr.ms. ': ' harer majesteits ', ' i.p.v. ': ' in plaats van ',' i.t.t. ': ' in tegenstelling tot ', ' i.v.m. ': ' in verband met ',
         ' idd ': ' inderdaad ', ' iem. ': ' iemand ',' inf. ': ' informeel ', ' ing. ': ' ingenieur ',
         ' inz. ': ' inzonderheid ', ' ir. ': ' ingenieur ',' jwt ': ' je weet toch ', ' jwz ': ' je weet zelf ',
         ' kg. ': ' koning ', ' ki ': ' kunstmatige intelligentie ',' kilo ': ' kilogram ', ' kk ': ' kanker ',
         ' kkr. ': ' koninkrijk ', ' km/u ': ' kilometer per uur ', ' kvdm. ': ' keurvorstendom ', ' kymr. ': ' kymrisch ',
         ' lat. ': ' latijn ', ' lgrs. ': ' landgraafschap ',' lidw. ': ' lidwoord ', ' lvdh ': ' lees verdomme de handleiding ',
         ' m. ': ' mark ', ' m.a.w. ': ' met andere woorden ',' m.b.t. ': ' met betrekking tot ', ' m.i. ': ' mijns inziens ',
         ' m.i.v. ': ' met ingang van ', ' m.n. ': ' met name ',' m.u.v. ': ' met uitzondering van ', ' m/s' : ' meter per seconde ',
         ' maced. ': ' macedonisch ', ' me. ': ' middelengels ',' mgr. ': ' markgraaf ', ' mgrs. ': ' markgraafschap ',
         ' mhd. ': ' middelhoogduits ', ' mnd. ': ' middelnederduits ',' mr. ': ' meester ', ' ms. ': ' majesteits ',
         ' muz. ': ' muziek ', ' mv. ': ' meervoud ',' n ': ' noord ', ' n. chr. ': ' na Christus ', ' n.chr. ': ' na Christus ',
         ' n.n.b. ': ' nog niet bekend ', ' ngt ': ' nederlandse gebarentaal ',' nhd. ': ' nieuwhoogduits ', ' nieuw arch. wisk. ': ' nieuw archief voor wiskunde ',
         ' nl. ': ' namelijk ', ' nnd. ': ' nieuwnederduits ',' nr. ': ' nummer ', ' ns ': ' nederlandse spoorwegen ',
         ' o ': ' oost ', ' o.a. ': ' onder andere ',' o.c. ': ' opere citato ', ' o.i.d. ': ' of iets dergelijks ',
         ' o.m.' : ' onder meer ', ' o.t.t. ': ' onvoltooid tegenwoordige tijd ',' o.t.t.t. ': ' onvoltooid tegenwoordige toekomende tijd ', ' o.tk.t. ': ' onvoltooid toekomende tijd ',
         ' o.v.t. ': ' onvoltooid verleden tijd ', ' o.v.t.t. ': ' onvoltooid verleden toekomende tijd ',' o.v.tk.t. ': ' onvoltooid verleden toekomende tijd ', ' oe. ': ' oudengels ',
         ' ohd. ': ' oudhoogduits ', ' on.ww. ': ' onovergankelijk werkwoord ',' onfrank. ': ' oudnederfrankisch ', ' onz. ': ' onzijdig ',
         ' orth. ': ' orthodox ', ' os. ': ' oudsaksisch ',' osm. ': ' ottomaans ', ' ov.ww. ': ' overgankelijk werkwoord ',
         ' p.l.o.r.k. ': ' prettig lichaam ontzettende rotkop ', ' prof. ': ' professor ',' prot. ': ' protestants ', ' prov. ': ' provincie. ',
         ' pun. ': ' punisch ', ' r\'dam ': ' rotterdam ',' r.k. ': ' rooms-katholiek ', ' rep. ': ' republiek ',
         ' resp. ': ' respectievelijk ', ' rom. ': ' romeins ',' st. ': ' sint ', ' stu.fi. ': ' studiefinanciering ',
         ' t.g.v. ': ' ten gevolge van ', ' t.w. ': ' te weten ',' t/m ': ' tot en met ', ' taalk. ': ' taalkunde ',
         ' toep. ': ' toepassing ', ' tv ': ' televisie ',' tw. ': ' tussenwerpsel ', ' uitdr. ': ' uitdrukking ', ' v. ': ' van ', ' t.o.v. ': ' ten opzichte van '
         }

    abbrevs2={}
    for w in abbrevs:
        # print(w)
        # print(abbrevs[w])
        abbrevs2[w.replace(".","")]=abbrevs[w]

    # Dictionary with most used abbreviations in the Dutch language
    abbrevs3={**abbrevs,**abbrevs2}

    # Replace all abbreviations with the full-written equivalent
    for w in abbrevs3:
        x = x.replace(w,abbrevs3[w])

    return x

vbzin = 'Wat een zeer merkwaardige plek t.o.v. is langs deze route is Bruly, nabij Couvin.Datryrtyrar had Hitler voor een paar weken zijn hoofdkwartier. De kerk werd omgevomrd tot filmzaal voor Hitler. In de nabijgelegen bossen zijn de barakken omgevormd tot museum.'
vbzin=vbzin.lower()
print(afkortingen(vbzin))


