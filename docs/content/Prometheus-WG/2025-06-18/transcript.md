SIG: Prometheus WG
Date: 2025-06-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo Krajcsovits** 00:22 Hey! Hey!
**Arve Knudsen** 00:23 Hello, hey? Kyle.
**krajo Krajcsovits** 00:28 Okay.
**Arve Knudsen** 00:30 How, how are things going in the upstream lands?
**krajo Krajcsovits** 00:35 It's fine.
**Arve Knudsen** 00:36 Yeah. Can't complain.
**krajo Krajcsovits** 00:37 Fine! Can't complain. Yes.
**Arve Knudsen** 00:42 That's something at least.
**krajo Krajcsovits** 00:45 Yeah. Well, I've got plenty to do, so that's good.
**Arve Knudsen** 00:48 Yes, that's like that's always the the case for myself, at least.
Hello, Owen.
**Owen Williams (he/she)** 00:56 Hello!
Zoom is gray now.
**Arve Knudsen** 01:01 It's gray. Oh, okay, like the the theme change, do you mean?
I don't think I ever noticed.
Did you hear that slack is shutting down Cncf slack and community slack.
I just heard it like 5 min ago.
so I think the they might be moving over to discord instead.
**krajo Krajcsovits** 01:32 You mean, Cncf decided, or Kubernetes, or somebody decided to move. It's not like Slack is shutting us down right.
**Arve Knudsen** 01:41 Slash the shut them down, or gave them a week, I think, to migrate.
**krajo Krajcsovits** 01:48 Okay. I heard.
**Arve Knudsen** 01:49 But I just heard. I just heard this from Ted. Young.
**krajo Krajcsovits** 01:52 Okay.
**Arve Knudsen** 01:52 In the Hotel Guild call.
**krajo Krajcsovits** 01:56 I thought it was voluntary, but fair enough. Okay.
**Arve Knudsen** 02:00 And I just know what I heard.
**Owen Williams (he/she)** 02:02 A link to that.
**Arve Knudsen** 02:04 I think I saw. I think I'm just trying to find it back.
Is it possible? I forgot to click it. Oops?
There was like a culminate. This announcements.
**jurajmichalek** 02:30 Hey?
Oh, yeah. The slack thing.
Hello! Hello! Hello!
**Jonathan (jojo)** 02:49 Hey! Hello!
**jurajmichalek** 02:52 So I guess we're migrating to this course.
**Jonathan (jojo)** 03:02 We? We have topics, because I drop one on the on the document.
**jurajmichalek** 03:09 I dropped 1, 2, mine should be particularly still.
Where's the single? Go ahead.
**krajo Krajcsovits** 03:39 Okay, Google no longer. Lets me edit the file for some so, for example, get David, I think he's 1 of the people who can give you permissions to edit it?
No, I had the permission. It just says, can't sync changes. Blah blah. I'm like, Okay.
**jurajmichalek** 03:56 Oh, that's cheers!
**krajo Krajcsovits** 03:58 Yeah, I I gave up.
Everybody can add themselves.
**jurajmichalek** 04:12 Opping David. See if he's joining.
**David Ashpole** 04:20 Hey!
**jurajmichalek** 04:22 Hey!
**David Ashpole** 04:40 All right. Looks like we've got quite a few people on the call. Awesome.
And we have some agenda items. Jonathan, do you want to kick us off.
**Jonathan (jojo)** 04:51 Yeah, I dropped this question here, Ellie, suburb comment on an issue saying that we are not accepting a specific prototype.
But I'm not sure if we should accept this type of prototype, maybe you or Kraju could help me do? Do you have the the link?
This one.
**krajo Krajcsovits** 05:26 Or can you share and point at? What?
What, exactly, is he asking? Because I'm a bit lost.
**Jonathan (jojo)** 05:35 Is the 1st bullet point on the this one. Thanks.
**krajo Krajcsovits** 05:55 Oh, so this is about the version of Protobuff itself.
What?
I would have to read this through, because it's a veered.
I guess I guess he's meaning remote right? Version 2, because that line in the code.
It's remote flight protocol message, too, so that has nothing to do with Protobuff versioning. I don't even know if Protobuff has different versions honestly.
What the heck is this.
**jurajmichalek** 07:22 Yeah. The remote right receiver only supports remote right fee, too, I guess.
**krajo Krajcsovits** 07:30 Is it.
**jurajmichalek** 07:31 Well, that's why the yeah, I think. That was the because there was concern right with with v 1 you get histograms. You don't get histogram right? The individual buckets can come in multiple, remote, right requests.
So there was concern right? Like, how can we interest this when we don't know if we're gonna get the you like in the single message when you're doing the translation of the one message, you don't have a guarantee. You get the full, actual full histogram, with all its packets.
**krajo Krajcsovits** 08:04 But I think that's true for both remote right one and 2 works.
So estrograms.
**jurajmichalek** 08:10 In yeah, with classic, right? Yeah.
**krajo Krajcsovits** 08:16 Okay and and remote. Right? b, 1 works perfectly with native programs. We use it all the time.
So yeah, I truly don't know what? What's the problem here, but like I can.
how parse it, and then read it through. And well, you know, understand it.
**David Ashpole** 08:38 Is, but there's no different version of Protobuff required by v. 2 compared to v. 1.
**jurajmichalek** 08:45 Brought up messages different.
**David Ashpole** 08:48 Like, the the actual.
**jurajmichalek** 08:53 The actual protograph content changed heavily. Right. The the format of the message right.
**krajo Krajcsovits** 09:04 Yeah, but I haven't heard of, you know, remote right to requiring different protobuf implementation or or or you know, something like that like that someone would have called attention to it. I think if that was the case.
**David Ashpole** 09:31 Using proto, 3.
**jurajmichalek** 09:37 I think.
**David Ashpole** 09:40 Versus.
**krajo Krajcsovits** 09:43 The weird thing is, by the way, that enabling native programs in promitives doesn't automatically change remote right? That's a different setting.
So right there. That's kind of weird. The 1st thing they say.
**jurajmichalek** 09:59 I think what like what she's talking about. The prototype? 2 is the remove red proto message? V. 2.
Because that's what the link in the issue leads to.
**krajo Krajcsovits** 10:11 Yeah.
**jurajmichalek** 10:12 So she's basically saying, it looks like this, we only supports prototype 2, meaning like, remove right, 2
**krajo Krajcsovits** 10:20 Yeah, and the day.
**jurajmichalek** 10:22 And one of the question is, if there's gonna be planned support for, I guess remote right? One.
**David Ashpole** 10:29 Cool.
**jurajmichalek** 10:29 Like 0 something or whatever it's, it's the name of it.
And then the the second issue is the second part is higher memory consumption under 2.0 and some caches with the 2.0.
**David Ashpole** 10:47 I don't know what she could be comparing it to.
**jurajmichalek** 10:49 Yeah, that's not clear to me, either. Right? Because, like.
like, is she comparing it to running collector without the receiver? Then like, Yeah, that's gonna use less memory if you're.
But I think that definitely. The 3rd point is something we need to fix, which is, I guess, under memory pressure the collector can crash because of our implementation.
**krajo Krajcsovits** 11:30 I mean, you know, remote right to the 0 has some extra processing both on the sender and receiver side. So if that's not optimal or something. Then you could see some increased.
**jurajmichalek** 11:42 Sure we just don't know what she's comparing it to.
Yeah, yeah, that's true. Yep, like, if you run it with other like.
maybe interesting. Otlp directly is less intensive. I don't know.
**krajo Krajcsovits** 12:08 Also, I think it's a bit strong to say we cannot support remote right? One. I mean, we could, but doesn't make much sense, because that that doesn't have.
The nativestogram custom buckets.
So you would be throwing away a lot of histograms so remote, right is is better for sure to get support. Yeah.
**David Ashpole** 12:58 Okay.
Sent awesome anything else on that topic. Jonathan.
**Jonathan (jojo)** 13:11 Nope, thanks.
**David Ashpole** 13:13 Great.
**jurajmichalek** 13:16 And I guess mine is the next one. So in the pull request that I linked in the translation package, I'm implementing a translation of if you open it for like adding support for histograms in the remote right. V 2. Exporter. And in the initial implementation, I'm basically just redoing the same thing that v 1 did, which is, by the way, what basically Prometheus does also, as far as I can do like, it's actually not using for, for, like old style histograms, it's still using the like, it's still generating histograms in the same in remote right. And David asked like, because, as he pointed out right. We have right v. 2, histogram.
and I guess the question is, and there there was even now merge pr into Prometheus, which adds, and I link it.
Yeah, that adds a config option which allows optionally to translate auto histogram to native histogram with custom buckets.
So, and this is not enabled by default.
So I guess my question is.
1st question is, do we want to do we want to block the pull request on having this implemented?
Or are we okay with like implementing that in a follow up, pull, request. And then the second question is.
do we want to add a config option for it, and if so, do we want to enable it or disable it by default? Basically like, do we want to couple you? Having done the migration from remote right to remote be 2 to also. Now, suddenly, you have to update your dashboards and queries, I guess, to work with the native histograms right? Or do we want to give you like an option to like? Okay? First, st you do the switch, and then we can enable it by default right? Like by default. You're gonna get already the native histograms and you can disable it if that's a problem for you. But at least like people who are newly adopting it already will be coming with with native histograms.
Or do we want to and disable it by default? And people have to enable it.
**krajo Krajcsovits** 15:40 I guess the question is, if you already have I I guess you already have users of the Prometheus remote right exporter. Right.
**jurajmichalek** 15:49 Yes, but with the v 1, nobody's using the V 2. We made it very clear in all the like. Read me and all the release notes for all the pull requests I'm doing. It's not ready for use, because, among other things, we don't have all the metric types implemented. The the translation, logic for them.
**David Ashpole** 16:06 Even if they were using v. 2, they can't be using histograms yet, because.
**jurajmichalek** 16:10 They're literally not there. Yeah, we disturb them. For now.
like, for example, I added, we got support for sell summaries merged like yesterday.
**krajo Krajcsovits** 16:23 Yeah. But don't you have people using remote right exporter and having histograms.
**jurajmichalek** 16:33 With this one.
**krajo Krajcsovits** 16:34 Everyone's split into separate series, right?
**jurajmichalek** 16:38 Yes.
**krajo Krajcsovits** 16:39 Okay. But so that if if you.
if if somebody tries, this turns on V 2 remote right and they get an Hcb, so the custom buckets.
As you said, there are dashboards, and everything will will fail, and they will be very confused. I I feel like.
**jurajmichalek** 16:58 He?
Yeah, yeah, it's a question of like, yeah, do we want to couple 2 migrations together because one is migrating from remote right? v, 1 to remote v, 2, and the other one is updating all your dashboards and alerts to work with native histograms.
And then, yeah, so I guess that's the question. The 1st question. Do we want to couple this? Maybe to like, gain her well, at least inferior to like sort of force. The adaptation of the native histograms.
**krajo Krajcsovits** 17:28 Hmm.
**jurajmichalek** 17:32 Yeah.
**krajo Krajcsovits** 17:35 It wouldn't be much of a migration path, though.
**jurajmichalek** 17:39 Well.
**krajo Krajcsovits** 17:41 Because you you'd suddenly get the Nhcv. And you broke everything. So maybe we actually need to improve this information as well.
**jurajmichalek** 17:51 In parameters. It's disabled by default, right.
**krajo Krajcsovits** 17:54 But enabling it, enabling it is pretty good for like a new user.
But for migration scenario, maybe it's not actually the right thing. Maybe we should have a a, an intermediate step where you still keep the classic histograms and the Nhcb. At the same time. So you can migrate over.
**jurajmichalek** 18:18 That's 1 approach to the migration. It's just sort of almost like in, well, not like it's gonna just say more resources, right? Because, like, you're interesting the same data twice, once as native Instagram. And one says.
**krajo Krajcsovits** 18:35 I mean, as long as you don't use this stuff for alerting and like critical stuff, then, you know, you can switch over.
But actually, for, like the the native program, migration from like classic histograms to native program, migration is is usually like 2 steps. One. Is you you doing just stuff twice for a while until you have your alerts working, and then you turn off the classic ones.
Hmm!
**David Ashpole** 19:20 I would prefer, if the default.
if the default started out as still doing the structured histogram rather than the individual series.
But if we want to offer an option to undo that. Then that seems like, maybe okay, to help people migrate. It's just for new users. I would hate for them to start with the old series, you know.
**jurajmichalek** 19:47 Down. Yeah, I mean, that makes sense. That's that's my like, at least having the escape hatch for the people who need it. And like, hey? If you don't need it cool like eventually, we can deprecate it right.
But if you, if you do need it.
**David Ashpole** 19:59 It would. It would also be really funny in a sad way, if our receiver and exporter didn't work together.
By default, the remote right to.
because the receiver is only going to support the structured ones.
**jurajmichalek** 20:14 That's a very good point. Yeah, yeah, let's unless I guess, unless anybody is against it. Let's let's default to, I guess, sending the V 2, we'll do the native histogram and add an escape hatch to yeah, right? We do histogram.
Okay? And then question is, do we want to include that in this pr, or is it okay to like, implement it for like support for rewrite. V. 2. Histogram in a follow up here, it will definitely like, slow this one down because, I saw the code base and it it's daunting my could potentially use a help with with implementing this, the the support for this.
**David Ashpole** 21:24 It's still. Pre alpha! Right? So.
**jurajmichalek** 21:27 I'd like, I'm pretty sure. Literally nobody is using this. Yeah, well, it's not right, like, I don't know. I think that's the character I'd like the state of the actual component. Technically, says Beta Beta.
**David Ashpole** 21:39 Or sorry, but it's behind the Alpha feature gate, right? Or is.
**jurajmichalek** 21:42 This is, yeah, this is behind the feature gate, and I'm as far as I, and I'm not aware of anybody enabling it yet anywhere.
**David Ashpole** 21:50 Okay.
that's fine. Then as long as we make sure that we get to the the right place, where people don't adopt this without just as a default.
**jurajmichalek** 22:04 Yeah.
**krajo Krajcsovits** 22:06 Do you think there will be people using, you know, the remote right exporter with vivon in production and relying on alerts.
**jurajmichalek** 22:18 Yeah, I mean, I can tell you. That's what in their company.
**krajo Krajcsovits** 22:22 So I guess that escape hatch needs to be like kind of an enum or or 2 things, you know. Again, you need a kind of a transition period where you.
in just both.
**jurajmichalek** 22:39 So now there's another way. You can save the auto collector. You can use the pipelines to send the data twice through one instance of the remote right exporter that sends it with well, I guess what you would then would have to like in the right, like a logic in the pipeline that you you sent twice only the.
**David Ashpole** 22:59 Histogram.
There was an interesting thing, I think you mentioned earlier, which is.
is there any chance that this splitting into like basically writing duplicates should be done somehow in a compatibility layer layer in Prometheus.
like all the data, seems best represented by the structured, remote right histogram rather than like the individual samples. I don't know. If, like.
you know, there's some compatibility thing you could enable in Prom Ql. To.
you know, fake the suffixes, or, if we want to enable that for remote right ingestion to double right server side, but.
**krajo Krajcsovits** 23:48 I mean, we talked about the an emulation layer for the queries, and we quickly decided that just not worth it, because that's we don't even know how to do it. And also we would maintain it for hopefully a short time. So that's out of the question, basically to make it, so that on the Prometus remote right receiver.
I mean in promitives on the.
you know, when we receive remote right to. So the handler and also Otip, I guess.
Could add something to to enable duplicating the Nhcb. Into classic as well, and provide migration that way.
**jurajmichalek** 24:32 An approach we have used to handle migrations like this. When metric names, changes, and things like that we have done is like in Grafana. You can just have a query, A and query B query a can be like the old histogram and query, B can be the new histogram. That's how we get dashboards working.
and then you just need to duplicate the alerts for a bit also, and then you can just flip the switch on the on the like config, right? And you don't have to interest the data twice like it deserves alerting for a bit. If you have a query that looks at like last 6 h.
But that's like bit more, less resource, intensive way to to do it, though.
**David Ashpole** 25:13 Isn't there already a config option for custom bucket, histogram, or something like that?
**jurajmichalek** 25:22 In permetues.
**David Ashpole** 25:24 I like. I thought it was, for even just scraping.
**krajo Krajcsovits** 25:28 Yeah, that was for scraping only.
**David Ashpole** 25:30 Okay, right? I don't know if it makes sense to like, have a similar behavior right?
**krajo Krajcsovits** 25:39 Yeah, I think that's that's something we should consider for sure, because that would be kind of like, not like that would put this whole thing in in promitives. In one place.
**jurajmichalek** 25:53 Can. Can you open the the Pr link from Prometheus? One more time, please.
In the in the comment David.
**David Ashpole** 26:04 Oh, yeah, sorry. I forgot which tab I was.
**jurajmichalek** 26:06 Oh!
**David Ashpole** 26:07 There we go!
**jurajmichalek** 26:09 But in Prometheus this is only This is only a bull right now, so do we want to make it a pool in like it's just one or the other right like this doesn't support.
**krajo Krajcsovits** 26:24 Yeah, in in script. We did it with 2 options.
One is to convert and the other is always script classic. So we could do the same thing, add one more option to also keep doing.
**jurajmichalek** 26:36 This is the Tlp receiver, right? So I guess.
like in the Otlp receiver, informative right now. And this is merged like I don't know a couple of days ago.
Right now, you you have to choose, basically which how it's gonna get interested.
**krajo Krajcsovits** 26:51 Yes.
**jurajmichalek** 26:53 So.
**krajo Krajcsovits** 26:54 It was just yeah.
I was just saying that we could do it.
We could do it similarly to script where we have 2 options.
I didn't say it was that way.
**jurajmichalek** 27:05 Okay, yeah, yeah.
**krajo Krajcsovits** 27:06 We could do it.
**jurajmichalek** 27:10 Any preference with the rest of the group.
And I guess, okay, good. Yeah.
**David Ashpole** 27:39 I like the idea of always sending the best representation of the data we have. Like. It's very.
It should be easy to go from the structured histogram back to a set of samples. But it's a lot of work to go the other way to like. Accumulate those and group them properly.
**jurajmichalek** 28:00 No, no. I was just wondering, like, yeah, definitely, we can do the config option. I think we agreed, sort of agreed on that. And and having it enabled by default. I guess the the next question is, do we want it just to be pool, or do we want it potentially be, for example, in them, so it can be like, send one the other, or both.
**David Ashpole** 28:18 Or both.
and and enum is fine. If you want to implement that like, it's not gonna hurt anything.
**jurajmichalek** 28:31 Okay, I can. I can do this.
**David Ashpole** 28:34 More work for you. So.
**jurajmichalek** 28:35 I mean. That's why I would prefer it to be a bull to be to be honest.
**David Ashpole** 28:40 Is it?
It's not more work for.
**jurajmichalek** 28:43 No, it's like most of the point testing right? Because, like.
**David Ashpole** 28:46 If a, or if not a versus, if.
**jurajmichalek** 28:51 All of these.
**David Ashpole** 28:52 And then one of those 2.
**jurajmichalek** 28:54 I just wonder if anything would break if you send it in those same request.
But I guess no right like it should just read an interest. It's just a bit more testing, right? To make sure. Like, if you just dump it into a single request that it doesn't break anything.
**David Ashpole** 29:09 We definitely shouldn't do. Duplicated by default.
Oh.
**jurajmichalek** 29:12 No.
**David Ashpole** 29:13 Something. People are intentionally doing.
**krajo Krajcsovits** 29:17 Yeah, that's a specific migration case where you have alerts, and especially if you use range queries and alerts.
It's ex- explained in the talk that I linked. Why, you need this kind of overlap.
Yeah, I'm still thinking of of.
Is it worth doing on our end? On Prometu's end?
**jurajmichalek** 29:51 Yeah. I mean, then it's not just permitive. Right? Then it has to be implemented in Mimir in cortex, in tunnel.
Yeah, exactly.
So. It's a question of like, okay, which which side is the? It's the resources. Right? Is it that the side that like sends? Or is it the same side that receives.
**krajo Krajcsovits** 30:08 Yeah.
Hmm.
**jurajmichalek** 30:12 Okay, we can. Let's do this right for now, I'm just gonna let's let's get this merged. It's working when it's approved. And then when I open the actual, follow up Pr to like.
add the logic to do the translation into native packet histogram. We can make a decision then.
**krajo Krajcsovits** 30:29 Yup!
**David Ashpole** 30:35 Sounds good.
**jurajmichalek** 30:37 And and I don't know. We can then resolve it as a poll in auto primitives, and everybody can can go.
**David Ashpole** 30:43 Yes.
**jurajmichalek** 30:43 Yeah, I don't know just to get more input.
**krajo Krajcsovits** 30:49 Yeah, these migrations are always like pain in the ass anytime. You do this, it's so soon.
**David Ashpole** 30:57 Yep.
**jurajmichalek** 30:59 That's it for my side.
**David Ashpole** 31:02 All right. Any other topics.
Is there any stuff that Arthur was working on that needs to be picked up? I think there was a sorry go ahead.
**jurajmichalek** 31:14 I think I went, picked up the the Otlp translator Pr.
**Owen Williams (he/she)** 31:19 Yeah.
**jurajmichalek** 31:20 Country.
**Owen Williams (he/she)** 31:21 Been spending most of my time figuring out what's easiest to pick up.
And yeah, started with, yeah, a few things and then doing reviews for Draj. And then, like the Constance Pr that we were talking about today.
So yeah, I don't think I'm not going to be moving as long as fast as he was going. But like, yeah, we're making sure things are still going along.
**David Ashpole** 31:49 I think I saw there was a Pr for type in unit in the Otlp endpoint. I was maybe going to pick that up unless someone else wants to do it.
That these are the type in unit has labels, thing.
**Arve Knudsen** 32:06 In the Prometheus. Ethiopian points.
**David Ashpole** 32:09 Yes.
**Arve Knudsen** 32:10 But didn't you just review that Pr.
**David Ashpole** 32:15 Did I
**Arve Knudsen** 32:21 Let me see if I'm no type in units.
Oh, yeah, sorry.
I was confusing with the scope method.
But type in unit is. Now let me see.
**David Ashpole** 32:38 It was. I'll link it in the meeting notes.
**Arve Knudsen** 32:40 Oh, yeah, sorry. I was confusing the 2. Hey, yeah.
Is that Arthur's? Pr.
**David Ashpole** 32:48 Yes, I was. I was considering picking it up, but.
**Arve Knudsen** 32:51 Then I know what you're talking about.
**Owen Williams (he/she)** 32:54 Carrie, how does that relate to your work, if at all?
**CE Carrie Edwards** 33:00 And it's 1 of the tasks that needs to be done for type and unit and Arthur started it, I believe.
But yeah, I've been working on other tasks.
**jurajmichalek** 33:17 When I do quick question off topic if I can. When I do write the I saw that you were the author of the pull request to Prometheus for the for the translation to native histogram with custom buckets. When I do end up implementing the same in auto collector, could I ping you for a review to make sure I don't do. Okay, okay, that would be great. Thank you.
also, we're going with the like, exposing the type as a label approach.
**David Ashpole** 34:08 Yes, it's behind a feature gate. It's kind of orthogonal to some of the other things we're working on, but I think it'll be helpful for ensuring that if and when you have even hotel applications that have like where one has one unit and one has the other unit which has happened in the past that Prometheus can still distinguish those, and in theory properly handle them and query over them, and stuff.
**jurajmichalek** 34:38 Guess it may help in when you write like. Also.
**David Ashpole** 34:40 Alerts in the Vmwa file.
Yep.
**krajo Krajcsovits** 34:46 Yeah, we'll on a related note. I started a Pr in open metrics, 2.0 on relaxing the suffix rules and the.
for, you know, total and unit.
But I realized that it has many dependencies like, if if I want to make it nice and not very complicated, I need to also introduce a single line version of the classic histograms and summaries.
so that I can say like generic things about metric names.
So yeah, I don't know how long that will take, or open metrics to in general, how long that will take, because it's a it's a lot.
**David Ashpole** 35:24 What? Why do you think that's a requirement for not having type suffixes?
Oh, you, you mean not having type suffixes for summaries and histograms as well.
**krajo Krajcsovits** 35:33 It's not a requirement, but like I wanted to say regarding suffixes that the name of the metric in the metadata, you know the hash type hash something, and the and the and the lines of samples is the same. And you cannot say that generic rule, which would been very nice to say.
without getting rid of the you know the the representation with the unders underscore sum underscore count and blah blah for for histograms and and summaries.
So I'm trying. I'm giving it a shot.
I I do need I? I have a lot more to do on the natives program side of open metrics, anyway. So it's not like It's it's super urgent. At the moment.
**jurajmichalek** 36:28 Some of the things, maybe also easier to update once we migrate to the Otlp translator package. So you don't have to like duplicate a lot of work across parameters and collector.
**David Ashpole** 36:54 See everything else. Looks like it's okay. I think I linked the few Prs that he was that he had in flight.
Cool?
All right. Anyone else have any topics.
Otherwise I'll see everyone in 2 weeks.
Good work.
**krajo Krajcsovits** 37:37 Over, and can you stay a bit.
**Owen Williams (he/she)** 37:40 Yeah.
**krajo Krajcsovits** 37:41 Like I saw you go.
**Owen Williams (he/she)** 37:43 Yeah. But I was going to ask if you wanted to talk about that. Yeah, everybody else, unless you want to talk about defaults in escaping schemes.
**krajo Krajcsovits** 37:50 Yeah.
**jurajmichalek** 37:51 If you have a by the way, if you have an approved Pr and want somebody to merge it, you can think the auto collector, auto, dash, collector, dash left channel, and the maintainers usually read it well. The people with merge permissions.
**krajo Krajcsovits** 38:06 As long as we have that channel right?
Anyway. I see when you said that maybe the default should be different. But I'm I'm shooting for something that's not the default.
I'm shooting for something sane or open thermity corrector, which would be the backward compatible with what we had before.
**Owen Williams (he/she)** 38:32 Okay, I still think the slightly more complicated thing is correct, though, because it's it switches, depending because it's not necessarily true that if escaping scheme is not set. That validation scheme is also not set, so you don't want to end up in a situation where the metric, the validation scheme was set to Utf. 8. And then suddenly the escaping scheme defaults to underscores. So it's just it's it's not too complicated. It's just if the validation scheme is blank, set it to Utf. 8, and then, if the escape escaping scheme is blank.
if the validation scheme was Utf-eight set it to utf-eight, and if the validation scheme was set to legacy, set it to underscores. So there's only 2 possibilities.
**krajo Krajcsovits** 39:22 Wait. Yeah, but be. But wasn't. Isn't the backward compatible?
Think to say that the validation is legacy.
**Owen Williams (he/she)** 39:34 Currently, that is not what Prometheus does.
Well, sorry. Okay.
The current default when you create a configuration in Prometheus is, if you don't set the validation scheme. It defaults to Utf-eight.
**krajo Krajcsovits** 39:59 Yeah, I don't care about that. Yeah, that's let's establish that. I don't care about that. I care about.
**Owen Williams (he/she)** 40:04 Okay.
**krajo Krajcsovits** 40:05 We or somebody. I think Arthur, or or maybe you or I updated primitives in the opentime as recollector underneath the the permit receiver. And suddenly things broke and I want to unbreak them.
Okay, what happened?
And before the upgrade.
**Owen Williams (he/she)** 40:23 What would help me to know is, what is this target? Allocator? What is a target allocator?
What is? What is this code doing.
**krajo Krajcsovits** 40:34 You're muted.
**Owen Williams (he/she)** 40:36 Am, I.
**David Ashpole** 40:37 No sorry the target allocator. All it does is it fetches its targets from an Http endpoint like raw static targets, and then monitors, those using Prometheus until it gets new targets. So it's a way of like replacing Prometheus service discovery and delegating it to some remote endpoint to say, just let me know what the static endpoints are that I should take a look at right and the target allocator can like watch kubernetes, objects, and stuff, and give Ips that it should monitor. And so basically, you can think of it like, here's a bunch of static endpoints, and they get refreshed often.
**Owen Williams (he/she)** 41:24 Okay. And they're just when. And these are just slash metrics, endpoints.
**David Ashpole** 41:28 Yep, just regular Prometheus endpoints. All that's happening is like the config is being refreshed. Often.
**krajo Krajcsovits** 41:37 Yeah. So before we upgraded to.
I think, 3 dot 2. I think that was the upgrade that brought this.
You know, the allocator would give you an IP address, and you would scrape it. And I wonder what validation was used then in in 3 dot. 2, I guess, because that's what the default should be. Then.
**Owen Williams (he/she)** 41:58 Prometheus, 3.2.
**krajo Krajcsovits** 42:00 Yeah.
**Owen Williams (he/she)** 42:01 Prometheus now defaults to Utf. 8.
The the error is not that the metric names are invalid. It's just.
**krajo Krajcsovits** 42:15 Yeah, yeah, I know. I know.
**Owen Williams (he/she)** 42:16 Okay. Okay.
**krajo Krajcsovits** 42:17 I understand.
**Owen Williams (he/she)** 42:20 It. I so.
And these targets are they hotel targets? Or they're just they're just Prometheus targets.
**krajo Krajcsovits** 42:35 Targets. This is the promitous receiver, so.
**Owen Williams (he/she)** 42:37 Yeah. So I think we should just be consistent with the rest of Prometheus, which is to default to Utf-eight unless it's set in the config.
**krajo Krajcsovits** 42:46 Okay.
**Owen Williams (he/she)** 42:47 I guess the question. So the question is, okay. So the question is, in regular Prometheus, you've got a global config and then scrape configs and that and the scrape configs inherit from the global config. These target allocator configurations do they? Should? Can they inherit from the global config.
**krajo Krajcsovits** 43:14 Not that I know of. I think they are directly supplied, and like we said them. If you see the Pr. I I made a.
**Owen Williams (he/she)** 43:23 Yeah.
It's like.
**krajo Krajcsovits** 43:25 I mean.
**Owen Williams (he/she)** 43:27 There's an initial config.
Where's that coming from?
My question is, why are we inventing a config from 1st principles and not loading it from a from a why is this not set in the Prometheus configuration in general?
**krajo Krajcsovits** 43:46 I mean, it could be.
I mean, if somebody like okay.
we could say that we, you know, drop this Pr and tell everybody to set the default.
But like, that's the problem. Is that I think we can do some good saying defaults and not break stuff.
**Owen Williams (he/she)** 44:11 Yeah. But my point is, we already have a bunch. Oh, oh, right? Right? Because because the Prometheus code has all this global config stuff, not the open telemetry collector. Yeah, so there's a prom config that it's getting passed in from New man. So basically, it's incorrect that.
So so it's it's getting an initial config, and then it's iterating over them.
It is incorrect that the hotel collector is providing a Prometheus config where the validation and escaping scheme are not set.
So then we have to back up the tree and say, Okay, where are those configs coming from?
**krajo Krajcsovits** 44:59 I mean the.
**Owen Williams (he/she)** 44:59 Because that's.
**krajo Krajcsovits** 45:01 Yeah.
**Owen Williams (he/she)** 45:02 Yeah, that's that's supposed to be where this all comes from. So in Prometheus it defaults to Utf. 8. And if somebody is like, no, I want legacy. They can set that in their global config, and then it propagates all the way down, and I feel it should work the same for open telemetry.
**krajo Krajcsovits** 45:19 Yeah, I mean in the, if you look at the test.
the the target allocator is kind of 2 step.
First, st it gives you targets that are actually service discoveries.
And then the second step is that it gives you actual targets like actual hosts.
and in the tests I set up the service discovery in inside the script config. Which is that initial thing, basically. And I can say, there.
maybe I maybe I can share. Let me share my screen. That's probably simpler to show oh, shit! What is this? The
**Owen Williams (he/she)** 46:04 Add this.
**krajo Krajcsovits** 46:08 Do you see my screen.
**Owen Williams (he/she)** 46:09 Yeah.
**krajo Krajcsovits** 46:10 Okay.
**Owen Williams (he/she)** 46:11 Okay, so, okay.
**krajo Krajcsovits** 46:12 I can. I can make the problem go away by having the target allocator say, you know, set the this validation scheme and and the and they are skipping here.
but that's outside the promitive receiver. So I have nothing. I have nowhere to actually put that this is just test.
Got it. I don't. Yeah.
**Owen Williams (he/she)** 46:40 What? Yeah, what I'm saying is, I think the problem is higher up. I think it's so. This create default config calls prom config default, global config. And the default, global config is vendored or no. It's yeah is from Prometheus, and that should be setting.
Yeah, let me let me.
**David Ashpole** 47:12 Is the problem that the default global config is invalid.
**Owen Williams (he/she)** 47:15 Correct. Yeah, the default global config is not. Or at least I'm getting confused because my Vs code is linking to my package installed Prometheus, which I think is old, so I'm not sure I'm looking at the right code.
but that's where these that's where these defaults should be set is much higher up, and if they're not getting set higher up, then that's the real bug and fixing it in fixing it. Yeah, okay, here it is.
**krajo Krajcsovits** 47:52 I'll stop sharing.
**Owen Williams (he/she)** 47:53 This is actually Prometheus Bug, where it's not setting.
Yeah, it needs to be. Yeah. It should be setting validation and escaping scheme.
That's where those defaults should be set.
and in Prometheus those should be Utf. 8, and allow Utf 8.
**krajo Krajcsovits** 48:19 But how how does that get to to me like.
**Owen Williams (he/she)** 48:25 Yep, so then.
**krajo Krajcsovits** 48:26 Problem yeah.
**Owen Williams (he/she)** 48:27 If you follow the let me share my screen.
Let's see if let's see if we can do this.
It's this alright. Is that readable? I mean, I can make it smaller.
That's not smaller.
So target allocator.
It's Manager has a has a new manager, and that takes a config and a prom and a prom config and.
**krajo Krajcsovits** 49:14 Wait, wait, where? Where? Sorry, where?
**Owen Williams (he/she)** 49:17 So we're in Manager dot go.
**krajo Krajcsovits** 49:18 Yep.
**Owen Williams (he/she)** 49:19 And this is here we take a prom config passed into the constructor for the.
**krajo Krajcsovits** 49:26 Yep.
**Owen Williams (he/she)** 49:27 Yep. So then, going to that that is called from New Prometheus receiver.
**krajo Krajcsovits** 49:33 And there's the call to New Manager.
**Owen Williams (he/she)** 49:36 And it passes in a base config, which is this.
and if we just keep going back up the chain.
we end up with a call to create default config.
and that calls Prometheus default global config.
So when we fix it in Prometheus, the default, global config will have the correct defaults for those values, and those will sprinkle all the way down to you. And my guess is that this is a problem elsewhere as well.
**krajo Krajcsovits** 50:11 Okay.
**Owen Williams (he/she)** 50:12 So I can. I can. Yeah, I can fix that
**krajo Krajcsovits** 50:21 Okay. In the meantime, should we just tell people to not upgrade to 128 collector, because.
**David Ashpole** 50:31 Is this, for in the target allocator portion.
**krajo Krajcsovits** 50:37 Yeah, this is target allocator only, and I think I guess you could probably configure the whole thing differently. So you don't run into this.
**Owen Williams (he/she)** 50:50 Yeah, it does seem that configs get sort of merged in down the line. But I think I think it's also okay to patch this just to unbreak things and just put a comment saying, and then, like, I'll file an issue and say, Oops, we're not setting it in the default config, and you could just file, and then you could just link to that issue and say, Oh, hey! Prometheus is broken when Prometheus fixes this well, 1st of all that code will just never get called.
but it can be removed.
**krajo Krajcsovits** 51:21 Okay. That means also that my test is kind of too simple, because it's making up the the base config for the target allocator.
**Owen Williams (he/she)** 51:35 Right. And the whole problem is, this is the construction of the yeah.
So the the face config should be valid by the time it gets passed in, and it's not.
**krajo Krajcsovits** 51:43 Right? Okay, no, I'm just, I spent some time on this.
**Owen Williams (he/she)** 51:53 Yeah, that was completely listed.
**krajo Krajcsovits** 51:56 No, I am sorry.
no, it's it's all right. It's all right. I thought I had something crap. Okay.
**Owen Williams (he/she)** 52:05 Alright
**David Ashpole** 52:10 This also fix that issue someone was having with secret, unmarshalling.
**krajo Krajcsovits** 52:18 No, that's different. That turned out to be that basically.
The way we load the prometers config is to marshal it into Yaml and then load it with a single function which does all the magic to it that needs to be done.
But the marshalling replaces the strings with secret because it's sensitive.
But you can set a global variable to not do that. And and suddenly you get the correct thing. So if.
**David Ashpole** 52:51 I just do that, or is it.
**krajo Krajcsovits** 52:55 I mean.
Well.
I don't know. Like if we, if we ever expose the marshalled data, because if we expose it in a log or or in a file somewhere. And this is a global variable.
**David Ashpole** 53:12 Isn't there like an Api endpoint that you can hit to get your config?
No, okay.
**krajo Krajcsovits** 53:20 Maybe
**David Ashpole** 53:21 Media's Http.
**krajo Krajcsovits** 53:23 Yeah, yeah.
So my, my 1st reaction was, you know, let's set that global variable through to keep the secrets and then differ and set it. But then concurrency.
like, okay. But what happens if.
We are doing something concurrently, so I don't know but there's no like the good solution would be if if you could.
I don't know. I don't know what the good solution would be.
**David Ashpole** 54:04 Is there a way for us to like, marshal it, and then insert the correct secret afterwards.
like just work around the fact that it's not.
Anyways, I'll let you, or whoever is going to own the issue, own it.
Or, if you need help, I can also take a look.
Do we know why it broke? Is this like hiding of stuff new or.
**krajo Krajcsovits** 54:40 It's yeah, it's new. It's in 3 dot, 2 for me to change the Api.
**David Ashpole** 54:45 So if it's new and we've been using the.
I'll say, unsafe one before then we would just be preserving our existing behavior right.
**krajo Krajcsovits** 54:58 We didn't use the unsafe one because we didn't need this trick of marshalling and non-marshalling.
**David Ashpole** 55:06 So that's.
**krajo Krajcsovits** 55:08 So there was a Pr. To upgrade Prometheus version in the collector, and that needed to add, well.
a new code path where this marshalling happens.
So yeah, it's complicated. Because there was.
If you take the collector config and take the primitives config out of that, that's a different type, and you can marshal that to to text, and that that that kind of works.
But if you take the Primitives type and marshal that, then that will hide the secrets.
So maybe the solution is is to is to type convert before the the marshalling. Maybe that's another solution that we could try.
I'm I'm just worried that the Prometus marshalling I. I looked into it a little bit and it said that, okay, we need to do this thing like extra bits to do inline things in the config, and I didn't even understand what it was, so I'm afraid of like hacking around it.
anyhow. I think, David, you should just revoke the proof on my Pr. Or I can dismiss it because I think I need to update the test to not use the handmade configuration, but actually use the default config from parameters, so that the the problem is more obvious, because I think I'm as as always explained, I'm hiding hiding the problem right now.
**David Ashpole** 57:06 Oh, good!
**krajo Krajcsovits** 57:08 So I guess I'll be working on this tomorrow as well.
Yeah, okay, anyway, thanks for indulging me and see you next time.
**Owen Williams (he/she)** 57:30 Try to get this fixed quick. Bye-bye.
**krajo Krajcsovits** 57:32 Okay. Thank you. Bye.
