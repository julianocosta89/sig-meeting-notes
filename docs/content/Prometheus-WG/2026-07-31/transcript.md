SIG: Prometheus WG
Date: 2026-07-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**David Ashpole (Google LLC)** 00:16 Alrighty.
Yeah, yeah, I found the new link.
**krajo Krajcsovits** 00:23 Okay, okay, I… yeah, I called into the, entity SIG on Monday, and with two other people, and we were like, where is Josh? And we were in the wrong meeting, obviously.
Oh, we can continue discussion, actually, because… What is it?
I mean, if nobody has choice, we can continue working on the… Job and instance stuff.
**David Ashpole (Google LLC)** 00:57 I can't hear you.
Wait. Oh, there you are.
**krajo Krajcsovits** 01:01 Can you hear me?
**David Ashpole (Google LLC)** 01:02 Yeah, I can hear you.
**krajo Krajcsovits** 01:03 Okay, okay.
And I was just saying that, If nobody joins, we can just continue discussing the Joban instance. I mean, it's on topic.
**David Ashpole (Google LLC)** 01:15 Yep.
**krajo Krajcsovits** 01:16 Although…
**David Ashpole (Google LLC)** 01:17 Accordingly, of course.
**krajo Krajcsovits** 01:18 Yeah, yeah, yeah, I will not say anything bad about stuff.
Like I did in the previous meeting. I'm just joking.
Yeah, wherever we… Okay, I wanted to… Yeah, maybe comment… what I said in… in… with what I just said about the… New labels showing up.
So, this might… Brick… Compare, and also… Or… they're both?
Limit… Let me get ejected.
Yeah, I just wanted to note what I said.
Anywho…
**David Ashpole (Google LLC)** 02:39 Actually, here's a question. So, already, we already have, This… this would presumably be gated by the… Keep additional, or keep identifying resource attributes.
Or no?
**krajo Krajcsovits** 03:00 I'm thinking… So…
**David Ashpole (Google LLC)** 03:16 Actually, there is one more thing I'd like to write out.
If it sounds okay with you.
I'd like to write… I think the things that are missing are… If there's an… older collector with a newer Prometheus server.
And a newer collector with an older Prometheus server.
So if we made the change everywhere.
But people had mismatched things. I think that's… that's the other, like…
**krajo Krajcsovits** 03:55 Yeah, that's probably worth writing down.
Okay, so in the meantime, I'm trying to think… So, if I turn on… So, before the… Before that, there's nothing… After that, we're good.
Let me put in… Whoa.
I'll just put an example.
Let me ask.
Same question, but… Keep it empty.
Oh, good.
Choose is Anna Blood.
I think we… Yeah, I don't think it's solved.
We have the example at the bottom, and I'm going to add A new case where this config is enabled.
And also, I'm running Cloud to verify it.
So, if it's true, I think my guess… Is that you get a second so, serv… service.
Name… my service… It literally just means what we're keeping targeting for. Survive? What am I writing?
Repositz… So, service… Stillside D equals… Oh, it's actually, underscores.
**David Ashpole (Google LLC)** 07:25 Were you close?
**krajo Krajcsovits** 07:27 I mean, I was close, I wrote with dots, but I don't have UTA faith.
Turned on, so it turned down… turned service.name into service underscore name.
**David Ashpole (Google LLC)** 07:37 Oh, I see, I see.
**krajo Krajcsovits** 07:41 But it's… it's not keeping the job and instance. That… that setting is literally just about service name and service instance. It doesn't change how the… job and instance are created.
So it's not… it's not doing what… Not doing the new, spec.
I… I feel… hmm… Shoot… like, I want to be able to migrate in Prometus, so… We need to add some config to enable this new way of working.
How does it interact with this key identifying stuff?
Yeah, by the way, when I did that naming for that configuration, I had no idea about anything, so… again, sorry about the name. But,
**David Ashpole (Google LLC)** 08:48 That's fine. Yeah.
We can figure it out together.
**krajo Krajcsovits** 08:52 Yeah.
I think what needs to happen is probably for that to be deprecated.
To be removed in 4.0, to keep identifying attributes, and have some new name.
Or is it… no, that's stupid, no.
**David Ashpole (Google LLC)** 09:07 I mean.
**krajo Krajcsovits** 09:07 I don't know.
**David Ashpole (Google LLC)** 09:08 I think the… we could even consider just removing it if… like, it exists to solve the problem that we're trying to solve here. So if we solve it here, then we don't need it anymore.
**krajo Krajcsovits** 09:19 Yeah, but you need to deprecate it before you remove it in 4.0. That's what I'm kind of.
**David Ashpole (Google LLC)** 09:23 Yeah, yeah, that's…
**krajo Krajcsovits** 09:24 So, but let… okay, but this is something to write down, so… So this is… by Spatz.
**David Ashpole (Google LLC)** 09:37 You're escaping.
**krajo Krajcsovits** 09:40 So… And the today version, that's also bi-spec and also implanted by Prometus.
So, bias… Back… Bye, prom.
And this is… And the key identify attributes is not by spec, because the spec says to convert, right? Right now.
**David Ashpole (Google LLC)** 10:12 Sorry, I'll look at what you're doing.
True, implemented by Prom.
**krajo Krajcsovits** 10:19 Because the spec today says… Oh, no, the… yeah, the current spec is… is undefined on this, that's what I wrote, I think.
**David Ashpole (Google LLC)** 10:33 I think it… It's not opinionated.
**krajo Krajcsovits** 10:37 Yeah, yeah, not explicit.
Yeah, the spec isn't really… So… Nice perk.
But for sure, I think this one is against the spec, actually, a little bit, the skip I don't fair, but… And then, what do we want? So… becomes… Future Prometheus.
So… Yeah, we want to follow the spec.
That you write.
but also… I have to… What, what, what would be the config name here? Oh.
Hmm… What would… what would be a good name? It's not… is it… I mean, is this where you suggested owner labels, or was that on the Promptuy side?
**David Ashpole (Google LLC)** 12:17 Honor Labels is on OTLP to Prom. Okay.
**krajo Krajcsovits** 12:20 here.
**David Ashpole (Google LLC)** 12:21 Controls whether to… Respect incoming job or instance labels.
When they exist.
**krajo Krajcsovits** 12:30 2…
**David Ashpole (Google LLC)** 12:32 In future Prometheus.
**krajo Krajcsovits** 12:34 Yes, sir.
**David Ashpole (Google LLC)** 12:34 honor labels equals true to be the default.
For this.
Which is one potential reason not to name it on our labels.
Because everywhere else…
**krajo Krajcsovits** 12:45 Oh, right. Okay, so… Okay, then how… but naming is hard, like, what the heck do you name it, Dan?
**David Ashpole (Google LLC)** 12:56 I mean, in the future version of Prometheus, I might just delete the… I'm fake.
Future Prometheus, I would expect.
simply does not have this config, and when job and instance come in, are treated as job and instance, if they already exist.
**krajo Krajcsovits** 13:18 I don't know if that's reasonable with knowing what I know about customers.
Okay. Wanting to keep stuff forever.
I mean, that… I mean, you could say that that's my problem and the Mimir problem, but, like.
**David Ashpole (Google LLC)** 13:30 I don't know, I… I… I'm a Prometheus team member, hey, that's my problem, too.
**krajo Krajcsovits** 13:36 Sorry, I forget sometimes.
I mean, the obstacles…
**David Ashpole (Google LLC)** 13:45 Can I… can I show you… can I interrupt and show you what I had written down?
**krajo Krajcsovits** 13:49 Yeah, yeah, yeah.
**David Ashpole (Google LLC)** 13:50 So, if you jump up to… After PR, old collector, new Prometheus server behavior. So this is if someone has enabled In my proposal, honor labels true and keep identifying resource attributes true.
**krajo Krajcsovits** 14:06 Wait, which one, which one, again?
**David Ashpole (Google LLC)** 14:08 Do you see the one I'm highlighting here?
**krajo Krajcsovits** 14:09 Yes.
**David Ashpole (Google LLC)** 14:10 Okay, great. So, this is if you have an old collector, but a new Prometheus server. So, it is now respecting incoming job and instance labels, and it is leaving service attributes as they are when they come in.
So this is all the original stuff.
Right?
**krajo Krajcsovits** 14:29 Yes, you just copy-pasted it, I guess.
**David Ashpole (Google LLC)** 14:31 Right? So, right, copy-pasted this, it's still… Drops data here and is kind of ugly for here, right?
**krajo Krajcsovits** 14:39 Dude.
**David Ashpole (Google LLC)** 14:39 But the good news is, if we start respecting incoming job and instance labels, even with a new collector.
It just has the same behavior.
Neither of these cases are actually impacted.
If we have a new… if we have the new server behavior, but the current collector behavior. Because the funny thing is.
That nobody today is actually ever going to be sending raw job or instance resource attributes.
Unless they have them from some other source.
**krajo Krajcsovits** 15:11 Yep.
**David Ashpole (Google LLC)** 15:12 So, the new behavior in this case doesn't actually change anything if you still have the old collector behavior.
And this is, I think… This is, I think, the more worrying one. So if you have a new OpenTelemetry collector, but the current Prometheus server behavior, right? So if all we did was, quote-unquote, fix the Prometheus receiver and do nothing else.
we get the… Much nicer looking…
**krajo Krajcsovits** 15:47 Yep.
**David Ashpole (Google LLC)** 15:47 TLP representation in the collector, but here's where we run into some problems, right? Because now… Job has actually switched to… my service. Yes. An instance has switched to my instance ID, whereas the original one in the before PR, all the way up here.
is actually, I think, more reasonable, where job was the original scrape job, and instance was the original scrape instance.
And then the underscore escaping, I think, is potentially the worst case, because it'll actually get rejected today.
We have… because we have no service.name or service.instance.id.
Yeah, sorry.
**krajo Krajcsovits** 16:33 Yeah, it doesn't matter. I think we can just let Gemini fix the typos afterward.
**David Ashpole (Google LLC)** 16:40 I should do that.
**krajo Krajcsovits** 16:41 That's what…
**David Ashpole (Google LLC)** 16:41 But…
**krajo Krajcsovits** 16:42 Okay. Yep.
**David Ashpole (Google LLC)** 16:44 But, I think this case… maybe it's not the worst case, because then people will just tell people to enable honor labels, but…
**krajo Krajcsovits** 16:52 Yeah, I think, what… actually, the one step that I missed, which is on all… all feature develop… this is kind of feature development, so on all feature developments, you have to specify the migration path. So, how do you migrate to the new behavior without… lost… losing data, I guess.
Oh, God.
**David Ashpole (Google LLC)** 17:19 Based on this, you want to upgrade your Prometheus server first, and then upgrade your collector.
But I suspect that's not ac… By upgrade, the issue is we actually mean change behavior. Like, it's upgrade… it's enabling some new feature flags, essentially, right? Like the honor labels, or, keep identifying resource attributes.
**krajo Krajcsovits** 17:44 Yeah.
**David Ashpole (Google LLC)** 17:45 So… Yeah, I think… I think that's gonna be the hard part, is, like, the Prometheus server wants to remain backwards compatible.
So, we don't want to change it.
But users are actually going to have a worse time if we change the Prometheus components in the collector without Updating their Prometheus server first.
**krajo Krajcsovits** 18:32 This is… this is becoming… I thought I had a grasp on this.
And then the migration case and then upgrade is really… Messing with my mind.
**David Ashpole (Google LLC)** 18:46 In terms of figuring out why this…
**krajo Krajcsovits** 18:51 In terms of, like, what is reasonable to… to tell people how to migrate. Like, if we don't enable the new behavior by default, then they can upgrade their software And that's fine, nothing will change, right? If it's not… Because, yeah.
**David Ashpole (Google LLC)** 19:08 If we don't touch anything anywhere, yeah.
**krajo Krajcsovits** 19:10 Yeah, then… then nothing bad… well, then probably nothing bad happens. Okay, but then… So, I tell them to… Update the server, enable… on our labels.
Or, or whatever we're going to call it.
And… and that's the… that's the first… First one that you said…
**David Ashpole (Google LLC)** 19:33 Right. So then they get this… then that's a no-op.
**krajo Krajcsovits** 19:37 That's nope, so that's… Okay, that's good, because… In general, there's more senders than receivers.
So, if we can update the receiver first… That's awesome.
Because if you have to… Selectively enable this feature per receiver in the server, then we are screwed.
Although… We did have to add… I mean, ARV added a feature recently for a customer where they can send us an HTTP header that tells the server what translation mode to use.
And… like… Yeah, I don't love it, because I think it should be some processor on the OTRP side, so that you can do it per sender.
And I don't… like, because I don't… I don't want to maintain that code 10 years from now, but whatever, now it's done.
But yeah, that's…
**David Ashpole (Google LLC)** 20:39 I'll still maintain it 10 years from now.
**krajo Krajcsovits** 20:42 Oh, yeah, yeah, I hope so, yeah, that's true. Claude2000 or something.
But that, yeah, that's… that's… okay, that's actually… I think that's actually workable, but we need to obviously You have to basically document it, and just have a migration guide, like, how do you change to this?
Yo.
But, I mean, what you're highlighting shows that You cannot enable this new thing by default.
The default… the default setting must be off.
**David Ashpole (Google LLC)** 21:26 Well…
**krajo Krajcsovits** 21:27 Yeah, right?
**David Ashpole (Google LLC)** 21:28 No, actually…
**krajo Krajcsovits** 21:32 On the sender side, on the OTLP.
**David Ashpole (Google LLC)** 21:36 Well… I, I think… I think there's a few… there's a few things. One is… if this is the use… if this is, like, the stack that we care about, right, which seems reasonable.
Because it's the whole thing that we're trying to serve.
then we can't safely update the Prometheus receiver's behavior by default, until after the Prometheus server has gone 4.0.
Which seems… not doable.
like, I think we want to stabilize our specs before 4.0, unless 4.0 is coming soon, but…
**krajo Krajcsovits** 22:26 We haven't talked about it.
**David Ashpole (Google LLC)** 22:28 It's like.
**krajo Krajcsovits** 22:28 We just started marking issues and boot requests for the tool.
Project.
**David Ashpole (Google LLC)** 22:36 Let me… I'll finish typing my comment then.
So I think it either makes a case.
for not updating the Prometheus receiver for a long time.
to… Avoid breaking… Prometheus server users.
Or it makes the case for… Being more aggressive about how we enable this on the server side.
Right, so… if… If we buy that… this… is correct, that basically nobody is sending raw job and instances today?
So there's no behavior change?
Ben… It's actually safe.
for Prometheus to start respecting incoming job and instance.
But… And that would… that would mean that fewer people are actually broken, but it would be a, like… it would certainly be a breaking change from the Prometheus server perspective. So, Yeah, I think it's a bit of a pickle. Like, originally I had wanted… Originally, I was like, oh, it would be nice if we turned it on by default in the server, because nobody should be sending it.
But…
**krajo Krajcsovits** 24:07 Yeah.
**David Ashpole (Google LLC)** 24:08 If somebody is sending it, then they're just broken without… Like… Without really anything they can do about it.
Other than… I guess, like… They can filter out… like, the… If we enabled it server-side, then the answer is, like, well, it's really easy to filter out job and instance client-side, but that seems like a bad… I don't know, that seems like… We broke you, and here's a… like, I guess the mitigation.
**krajo Krajcsovits** 24:37 Here's what you need to do.
**David Ashpole (Google LLC)** 24:39 Here's what you need to do.
**krajo Krajcsovits** 24:41 Yeah, that's not… that's not fun.
**David Ashpole (Google LLC)** 24:42 And, like, for a stable project, it's not that cool, so…
**krajo Krajcsovits** 24:50 Yeah, we GA'd the OTIP receiver, like, I think last year in Graflo Cloud.
So we cannot break it. And again, thousands of users, I can I mean, to be… Where I can do maybe something where we measure if anybody is sending JoeBend instance.
To give us an idea how… But the problem is… And, you know, go by that, but… The other thing is that Another way to migrate… from… from, like, our… from Grafna perspective, is that… For new signups, we enable it.
And then for the old ones, we check if they are using Joben Instance, if not, enable it. Otherwise, send them an email. Like, we've done stuff like this before.
But…
**David Ashpole (Google LLC)** 25:57 That's a lot of work for you, I'm assuming, though.
**krajo Krajcsovits** 25:58 That's what I was going to say, that it's a lot of work, so I would need to convince A bunch of people.
That it's worth doing, starting with the people that work on You know, the dashboards, knowledge graph, blah blah blah, that work with the data itself.
Because they have spent… I think probably a considerable number of hours working on the current state.
So, yeah.
**David Ashpole (Google LLC)** 26:28 I'm just… actually, I guess this is a public call, so I won't ask.
Do you work with Cyril, or whoever?
Sorry? Is that… there's the other… I thought he was Grafana, but maybe he's not. I don't remember his name. Cyril, the other person who's been… He's the one who originally advocated for something like this.
**krajo Krajcsovits** 26:53 I, let me check the name, because I was in a meeting with a serial this morning, but for a very different… Toveno. Serial Tovanna, you mean?
Do you mean Syria Tovanna?
**David Ashpole (Google LLC)** 27:12 I don't think… let me just…
**krajo Krajcsovits** 27:14 So…
**David Ashpole (Google LLC)** 27:14 it up so I know.
Serve job and instance.
It's, I completely make up.
**krajo Krajcsovits** 27:41 Or do you mean Syria LeClarque?
**David Ashpole (Google LLC)** 27:44 Yeah, he's not Grafana, is he?
**krajo Krajcsovits** 27:47 Who… not anymore.
**David Ashpole (Google LLC)** 27:49 Okay, that's where that came from.
Nevermind that.
That makes some sense.
Okay.
You know, if you're able to get any numbers on people using it easily, that would be helpful.
If you think there's a chance that this can just be turned on.
**krajo Krajcsovits** 28:16 Let me write it down somewhere for my action point.
Well, I'll, maybe not here, maybe I'll just put it into the… Meeting notes of the verdub.
**David Ashpole (Google LLC)** 28:31 It's… I should also mention that the… the Google OTLP endpoint already accepts job and instance, has for… A year or two now.
So, I could get data from ours as well.
**krajo Krajcsovits** 28:49 But… Oop.
**David Ashpole (Google LLC)** 28:50 It would likely be tainted by the fact that it's an advertised API to customers.
But maybe it would be helpful.
**krajo Krajcsovits** 28:59 I mean, we also take it… Sometimes we overwrite it, but we… you can send it to us, we're not going to reject it.
Okay,
**David Ashpole (Google LLC)** 29:08 the orig… like, the original job in it. Like, if you send the… A resource attribute.
J-O-B to the… Google OTLP endpoint, we'll just stick it in there, and assume that you know what you're doing.
**krajo Krajcsovits** 29:21 Right, right.
Okay, okay.
I'm just writing into the… Minutes of meeting for the working group.
**David Ashpole (Google LLC)** 29:42 Would you like me to try taking a stab at updating the design document, or do you want to talk with our first?
**krajo Krajcsovits** 29:52 I can… yeah, let's… let me talk to Arv first.
Next week, he's coming back from vacation.
**David Ashpole (Google LLC)** 30:02 Okay.
And then maybe, maybe if we want, we can toss out this… this doc and… Kind of… co-write one.
That makes more sense to all of us.
I don't feel like the current state of the doc is very helpful for anyone.
**krajo Krajcsovits** 30:26 Yeah, it's a bit of it… yeah, it's a bit of a mess, but I think we can start, like.
Push the current content down, and then… kind of start fresh with the use cases, because I think we did good today.
Okay. At least I think so, but then, you know, your mileage may vary, and Arvind might not like it, but… we'll see next week, so… I wrote an action item into the WorkGroup doc. Do you agree? This is what we want, right?
**David Ashpole (Google LLC)** 31:26 With Doc.
Oh, that dog.
Sorry, I don't have it… I don't even have it open.
**krajo Krajcsovits** 31:35 Yeah, yeah, I just opened myself, yeah.
**David Ashpole (Google LLC)** 31:42 Yes, that would be helpful. I… even if you came back and said, we have no one at Grafana sending it.
or we have, like, you know, a handful of people sending it, I would still be a little bit nervous about the change upstream.
Just because people do whatever they want with Prometheus, so… it would be useful, but I feel like I need to think a little bit about what we should do, because if… I don't know.
I also don't want to just make the update everywhere. Like, if we make all the updates the way it's proposed.
and keep everything off by default in the Prometheus server, then… A lot of people will just get weird stuff.
When they upgrade their collector. Anyways, they'll have to go… I guess they'll just go flip on these options.
Hopefully, but…
**krajo Krajcsovits** 32:38 In Grafunnel Cloud, you cannot just slip on the option, you have to.
**David Ashpole (Google LLC)** 32:42 Oh.
**krajo Krajcsovits** 32:43 Send a support ticket.
**David Ashpole (Google LLC)** 32:45 Exciting.
**krajo Krajcsovits** 32:47 Yeah, we are actually adding more and more self-service that I've been advocating for a long time, like, I don't see why a lot of this stuff needs to… to Portugit, it's kind of dumb, but whatever.
That's why I said that maybe You know, if this is the direction.
We're going, it might make sense to enable it by default for new users.
**David Ashpole (Google LLC)** 33:11 Hmm, and then…
**krajo Krajcsovits** 33:12 4D.
Existing users, keep it off, and then, you know.
I don't know what to do with them.
But, I… yeah, I tried to get this number, and also need to… To some people that work with the actual data, like the folks that that Syria used to, manage.
**David Ashpole (Google LLC)** 33:39 Cool, cool, cool. I think that's good. And then I'll… we can talk with Arv when he gets back.
**krajo Krajcsovits** 33:45 Yep.
**David Ashpole (Google LLC)** 33:47 Alright.
**krajo Krajcsovits** 33:48 All right. Yeah.
**David Ashpole (Google LLC)** 33:50 Meeting early.
**krajo Krajcsovits** 33:51 Yeah, yeah, I'm exhausted, so I… it's also Friday night, and…
**David Ashpole (Google LLC)** 33:56 Yeah, yeah, true, it's nighttime for you. I'll let you go.
**krajo Krajcsovits** 33:58 Yeah, yeah, alright. Thank you so much. Cheers. Bye. Bye.
Turn this off.
I believe it is.
