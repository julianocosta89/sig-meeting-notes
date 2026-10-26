SIG: Prometheus WG
Date: 2026-10-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo (Grafana Labs)** 00:17 Hey, hoo.
**David Ashpole (Google LLC)** 00:22 Hey, Crow.
**krajo (Grafana Labs)** 00:29 I haven't checked on my PRs today, because it's a holiday here, so I'm just only calling into this meeting.
**David Ashpole (Google LLC)** 00:36 Do you think anyone else is gonna join?
**krajo (Grafana Labs)** 00:39 I have an absolute no idea.
**David Ashpole (Google LLC)** 00:41 Okay.
**krajo (Grafana Labs)** 00:43 I want to see… Did anyone comment on my… spec, clarification, PR, I think… Hard to recommend, you know?
some things…
**David Ashpole (Google LLC)** 00:55 I think he just said he found bugs in the collector.
**Arthur Sens** 00:59 Yep.
**krajo (Grafana Labs)** 01:00 Oh, okay, you have to.
**Arthur Sens** 01:02 Hello.
And… and both… both PRs fixing the bugs were already approved by David and Shuttimersh very soon.
**krajo (Grafana Labs)** 01:17 Oh, okay, then I have to… C and… Update.
Do I have to update this pack, do you think?
**David Ashpole (Google LLC)** 01:26 I think this is bringing it into compliance with your new spec, right?
**krajo (Grafana Labs)** 01:30 Oh, Jesus, it wasn't even accepted, what happened? That's…
**David Ashpole (Google LLC)** 01:36 I think the behavior is just strictly buggy today, right? Oh, okay. Which is that it gets set to zero if it's on set.
Is that right, Arthur?
**Arthur Sens** 01:46 Yeah, so if an OTLP message does not have a sum in the histogram, today we expose it as a zero, which is incorrect.
**krajo (Grafana Labs)** 01:56 Oh, oh, that one! Yeah, okay.
Oh, perfect. Yeah, I was talking about the job instance, so basically the, you know, clarifying… current… OTRP to Prometus, Prometus to OTRP… Conversion related to resource attributes?
So this whole job instance… Inc.
**Arthur Sens** 02:20 Okay…
**krajo (Grafana Labs)** 02:22 Maybe I should… boot my… We are in the meeting notes, because I was asking, and… I'm sure I posted it in the… Auto Prometus channel.
**Arthur Sens** 02:47 Hi, Kemal.
**Kemal Akkoyun** 02:50 Hello?
I was meaning to join these meetings for ages now, finally.
**Arthur Sens** 02:59 Nice.
Better late than ever.
**Kemal Akkoyun** 03:03 Yes.
But I will be a fly on the wall, like, for a couple of meetings to understand what you are discussing, so…
**David Ashpole (Google LLC)** 03:14 Do we have something to discuss?
I don't… I don't know, krao, if there's… If we should bring up… Or, I guess I'll look at the agenda, I haven't looked at it yet.
At baseline.
It looks like I started a review on this, but never finished it.
**krajo (Grafana Labs)** 03:59 Yeah, it's not easy, because I spent, like, a day writing it, and I purposefully didn't use Oh, Arve is asking for the link to the, Zoom meeting.
Just a sec.
**Arthur Sens** 04:16 It's… it's a blender.
**krajo (Grafana Labs)** 04:47 Hope he can join now.
Oh, yeah, there it is. There, there it is.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 04:55 Hello! I still have the… had the old link, so… Can I hold the melts.
**Arthur Sens** 05:03 I see, I see.
Krao, looking at this, this PR, I'm trying… I'm having a hard time understanding how this connects to the… the old one that we've been discussing for months now. This is… This is… this is somehow… somehow related, right? But I don't… I don't understand the connection.
**David Ashpole (Google LLC)** 05:34 The idea was that we would clean up the current language.
before we… Tried to make changes.
But I still don't think we have… Any agreement on, like, what changes we want to make after we clean up?
I think that's the current state. Okay.
**krajo (Grafana Labs)** 05:55 Yeah, so my idea is that, I tried to implement, or basically write down an option with normative language.
And then I ran it by Arve, and we looked at it, and he was like, yeah, this is… This doesn't make much sense, and the reason why it didn't make sense, really, it wasn't working, because the baseline was really not good enough.
It wasn't well defined enough.
And, I basically started by adding option… I think it was maybe option C or B, I don't remember. I tried to add one of them.
And I ended up rewriting the whole thing, just to make it clearer.
And then… that doesn't make sense. I mean, Arve pointed out that it would mean that I'm rewriting the thing 3 times, so it's duplicated effort, so I should just clean up the current.
you know, text.
And then we can have… B, C, whatever, and my idea as well, with normative language defined, because I feel like the design dog got a little bit away from us.
**Arthur Sens** 07:17 Got it.
So, do we… do we want to go through your PRs?
or this first PR, at least, and revealed together, what are we doing today?
**krajo (Grafana Labs)** 07:33 Yeah, we could do that.
I have to remind myself, because it's been a week, and, like, I've been dealing with other things.
But, yeah, we can do that.
I know there were already some comments, but, like, I was waiting for more, so I'm not sure if I fixed all the comments yet.
I… Yeah, most of them I fixed for… from what Arthur commented, so yeah, we can take a look. Want me to share it? Share the screen, or something?
**David Ashpole (Google LLC)** 08:19 Yeah, yeah. Go for it.
**krajo (Grafana Labs)** 08:20 Okay, let's see… I never do this with Zoom.
So, I'm sharing my… Firefox, that has it. Do you see it?
**Arthur Sens** 08:42 Yes.
**krajo (Grafana Labs)** 08:43 Is it readable? Do I make it bigger?
**Arthur Sens** 08:47 I can read it, at least.
**krajo (Grafana Labs)** 08:52 Okay, so, yeah, the first thing I did was adding a metric attributes section.
Because… There wasn't anything actually explicitly saying what to do with the labels, I mean, the data point attributes.
And what came out of this is this section, this metric attributes section, saying.
Levels of metrics possibly copied to data point attributes.
Except for the full liberals.
Which must not be copied. And that's name, because we handled that special.
We… Juben instance, the LD label of classic histogram buckets, quantile label from Promethe summaries, And, otoscope.
Prefixed stuff, which is handled according to the instrumentation scope rules.
And then… With a note saying that the target info metric is implicitly excluded, as we did, like.
the process that… Complicitly, separately.
I've… I would hope that this is not very controversial, so I would not linger on this right now, you can… You know… Yep.
**Arthur Sens** 10:09 This is Prometheus to Hotel.
**krajo (Grafana Labs)** 10:11 Oh, yes, sorry, yes, we are starting from Prometus Dota. Yeah, yeah, that's the order in the spec as well, yes, sorry.
**Arthur Sens** 10:16 So, I would call, instead of metric attributes, I would call labels.
**krajo (Grafana Labs)** 10:21 Oh, very well.
**Arthur Sens** 10:22 Yeah, nitpicking.
**krajo (Grafana Labs)** 10:28 yeah, okay.
Sure. Anyway, you can take a look at the list later, like, this is not the meat of it, I guess. It's just something that, like, was kind of weird.
That wasn't defined.
So… Yeah, then we got into… The next thing is resource attributes, so it's not talking about the source, Prometheus, but it's talking about where we put it, but Whatever.
I don't want to change the existing… Whoa.
title here Our section name?
And it's specifically calling out then scraping Prometus endpoint, which is kind of weird, in the sense that actually the collector is implementing the same kind of thing, but not exactly the same thing for the remote right receiver.
So I put a to-do to somehow handle the remote ride receiver. I don't know how we should do that, but it feels like a separate, like, discussion.
And then I removed the… this section.
in particular, service name, service and side, I need to ensure Prometus receivers can disambigate the metrics. So, this section that I removed is talking about the other direction, basically.
it's… it's writing down some motivation for the Joban instance.
Like, why do we even bother with Joben Instance?
But… It felt a little bit.
Oh, the only reason why it's… yes, Arve, sorry. So, the only reason why it's in draft mode, because nobody said that this is a good idea yet, like, I… posted it, and Arto commented, but, like, there was no… Kind of agreement that we actually want to do this.
But I guess nobody's…
**David Ashpole (Google LLC)** 12:32 I think it's a good idea.
**krajo (Grafana Labs)** 12:34 Okay, then I'll set it to ready to review.
So anyway, I removed this part, which is kind of only motivation, it's not normative, we can bring it back if you want it, obviously.
And then I reward the… Basically, the rest of it.
Because it was kind of, very underdefined, in my opinion.
So… instead of this motivational stuff, I actually just start with Prometus metrics.
Wow, this is kind of… in Prometus metrics, the Joban installs are considered identifying.
And therefore, a new resource must be created for each Jobel instance pair and carton in metrics labels, except for the target info metric.
And… I verified this with LMs as much as you can, you know, trust them, that both the Prometus receiver and the remote right receiver works this way. So basically.
this… they consider Java instance de-identifying labels, and… and that's how they build their internal model, basically.
That's what they start their maps on.
**Arthur Sens** 13:46 Yeah, I… Like, there's something there, like… Strikes me in the wrong way.
Like, Java instance… I… I think, from Prometheus metrics, the whole label set is… identifies, a series, right? But we are… here we are talking… oh, here we are talking… resource to identify… identifies the resource. Okay, yeah, yeah, sorry, that makes sense.
**krajo (Grafana Labs)** 14:15 I can clarify, but that's a good point.
**David Ashpole (Google LLC)** 14:19 I think it identifies a target, so if you want to join with target info, then… That's how…
**Arthur Sens** 14:26 Yeah.
**krajo (Grafana Labs)** 14:28 Or a target, maybe?
I can… yeah, I'll just comment this, and then I can make it nicer.
To not, mix up with… Goodbye.
Terrifying nature.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:51 I mean, it is also the working definition in Prometheus that… drop an instance, identify a resource, as resources are encoded in Target Info. I mean.
That's… that's… that's how it works, even at the moment, at least, even… Even if that, would not be… An ideal definition?
**krajo (Grafana Labs)** 15:18 Wait, are you saying in Prometheus that's how it's defined?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:23 Yes.
**krajo (Grafana Labs)** 15:24 Find or implemented, sorry.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:27 It's also defined in documentation that job and instance are how you… How you, join with target info to get, to get resource attributes?
So it's, like, essentially, it's, It is Prometheus' definition of resource identity.
**krajo (Grafana Labs)** 15:51 Oh, I see.
I mean… Hmm.
I feel like saying that could be… Cyclical dependency?
like, isn't that definition based on this OTRP compatibility thing? I'm not sure I want to say that here. Like, I like the idea of constantly identifying for target, although… You can have multiple resources inside the target, so that's not… Perfect.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:27 Yeah, I'm not sure exactly in this context, if it's correct… I don't know exactly what's correct to say in this particular context.
I just know that, like, within Prometheus, job and instances are considered, identifying of the resource, and we also document, that, kind of to get resource attributes, you use job and instance labels to join the target info.
So it's like… it's like a working definition that Prometheus has, and it advertises, although… maybe, maybe it turns out it's not, it's not a great, definition, if you see what I mean.
**krajo (Grafana Labs)** 17:09 No, sir.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 17:09 As I said, I'm also not sure, I'm not 100% sure if… if that is… You know, correct for the context you are describing right now.
**krajo (Grafana Labs)** 17:21 No.
I… Anyone wants to respond before I respond?
So, yeah, I think… I think in the past, definitely Job and Instance.
was identifying targets in the Prometheus.
word, in the Prometus sense, already, before OTRP, I think.
Bought… Considering aggregate exporters, or, you know, federated things. It's not actually… target, it's… it's a… it's a resource, so I think it might be fair to say a resource here. What do you think, David?
Oh, we lost it.
**David Ashpole (Google LLC)** 18:11 No, no, I'm here, I'm thinking. It's… It's really interesting, I guess, because we… we sort of stuff We stuff a resource inside of a target.
**krajo (Grafana Labs)** 18:30 Yeah.
**David Ashpole (Google LLC)** 18:31 And so… And Prometheus metrics, the job and instance.
**krajo (Grafana Labs)** 18:46 I don't know if we have a word for it in Prometus and might as well just use resource, but Arva has his hands up.
**David Ashpole (Google LLC)** 18:53 Yeah, I would rather… I don't know if Prometheus has a notion of resource. I could be okay with simply saying that they're considered identifying.
Yeah, it would feel a little bit weird, especially given that this is just the hotel spec, and that would be, like.
Considered. Maybe, maybe treated would be a better word if we wanted to use resource.
I don't know if it matters too much.
But it… it's like… They're not… It's like they're not defined that way.
But it… in practice, it is… Like, what we use to join between metrics and their resource, right?
**krajo (Grafana Labs)** 19:40 Yep.
Arve?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:45 Yeah, so kind of to get the definitions straight, target is a scrape target, right?
**krajo (Grafana Labs)** 19:51 Yes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:52 So, then… then Prometheus receives remote writes, like, it receives OTLP, and there's no scrape in the pipeline.
**krajo (Grafana Labs)** 20:02 Yeah.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:02 It will still… generate target info, and, and, use job and instance as the join, as the join labels.
So, I think, you know, in that context, there's no scrape target to speak of, and job and instances are purely used as identity of the resource, of the auto resource.
I just wanted to point that out, that, that this connotation or this association, it exists outside of the scrape domain, outside of scrape targets. Does that make sense?
So, so, yes, I mean.
Prometheus doesn't have a concept of resource per se, but it… after it gained the OTLP endpoint, it has a concept of open telemetry resource.
So, whether this is a good definition or not, Prometheus does have, like, a documented definition of… German instance being, being, the, being identifying of OTL resources as, as, ingested via OTLP.
So, I know that much.
So, like, that's kind of, like, the, the sort of, like, context I can provide.
**krajo (Grafana Labs)** 21:31 Okay, somebody else had their hands up.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 21:34 I put it down. I kind of said a bit of what I was saying. And, like, even as you were typing it out, it's like, dude, I don't know that it's useful to be.
Like, pedantic about, like, resource versus target.
**krajo (Grafana Labs)** 21:47 Yeah, I feel like we all know what we mean here, and it's… still better than saying just identifying, as Arthur pointed out, that can be misunderstood as identifying for time series in general, so… I've… yeah, I'm happy to save for a resource if everybody's happy.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:06 I'm just one… I'm just… I don't know if this is useful, I'm just, like, wondering whether we should be specific and say, optometry resource.
Because, maybe resource is more general, and maybe open the limited resource is a subset of resource in general, I don't know.
**krajo (Grafana Labs)** 22:24 I definitely think that when you use the… collector as a drop-in replacement for Prometus, in that sense, job and installs.
our script target.
It can be easily a script target.
So it would… it would be… I think this is more generic.
than, than OTLP resource.
So that's why I was thinking that maybe I need to do, like, a list here of things that can be a resource.
For a…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 23:06 Do you think it would be helpful to maybe include examples? Like, if you don't think that resource should be only open telemetry resource?
Maybe you could say that, for example, it could be OpenTelemetry resource?
Does that work?
**krajo (Grafana Labs)** 23:26 I think…
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 23:30 I think the examples are good, because, like, to some extent, Target… a target is a resource.
Right? Unless I'm mistaken, right? Like, you could call a target a resource.
**David Ashpole (Google LLC)** 23:40 I would generally say that Prometheus models open telemetry resources.
as scrape targets today, right? Prometheus doesn't have A native notion of resource, but it models resources as scrape targets.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 23:58 I think maybe this is a bit ambiguous, to be honest. Like, I mean, I mean, OpenTele… sorry, Prometheus does document that it, it, encodes OpenTelemetry resources as target info, but it's… I think… I think it is ambiguous as to whether, resources are modeled, explicit, explicitly as, scrape targets, if you see what I mean.
I mean, there may be… there may sort of be that connection, but I… I think… I don't… I think that is ambiguous, within Prometheus.
**krajo (Grafana Labs)** 24:42 I mean… I feel like it's hard to refute these two examples here.
So… I would suggest to… to… Keep this formulation, and maybe we can… Think about better.
For variation offline.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 25:00 It's probably the best we can come up with right now, right?
**krajo (Grafana Labs)** 25:03 That's kind of what I'm saying.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 25:05 No, I, I, I, like, I personally think this is probably good enough, so, let's hear, let's hear from others, if anyone else.
has opinions.
**David Ashpole (Google LLC)** 25:17 I mean… I still take issue with… Resource being something that's… in the Prometheus side of the spec. Like, that's not something we've typically done before.
**krajo (Grafana Labs)** 25:29 Hmm.
**David Ashpole (Google LLC)** 25:30 Like, generally, we should map Prometheus concepts to open telemetry concepts, and vice versa.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 25:41 But… are we not speak… are we not, kind of, speaking in terms of OpenTelemetry concepts here? Like, what, What exactly are you, kind of, taking issue with?
**David Ashpole (Google LLC)** 25:59 I mean, I think the correct The correct thing to say here would be.
The job and instance are considered identifying.
for a scrape target, right? Like, that would be the correct… Like, way to phrase this.
And we…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 26:13 We could do…
**David Ashpole (Google LLC)** 26:14 Additionally, like, the spec is obviously clear that we model resources as scrape targets in Prometheus.
Prometheus doesn't have A notion of resource.
That I'm aware of.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 26:24 But I… that is kind of what I pointed out, that Prometheus does have, like, a documented notion of OpenTelemetry resource.
Since, since it gained, ever since it gained the, all TLP endpoints.
**Arthur Sens** 26:40 Yeah, but the… that endpoint… what krajo said before, that endpoint was… Created based on this document, and if this document is created it is documented on top of Prometheus, we have, like, a kind of cycle dependency between the two.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 27:00 I don't know if I would say that. I mean, I think, you know, Prometheus… because I, you know, I've written this documentation myself, and I've read it again recently. I mean, Prometheus does have, like, a documentation about OpenTelemetry resources, and I think… as model Prometheus, and I think this documentation stands on its own. That's my opinion, at least. I mean, I welcome others to read it, and… If you think, if you think differently, I mean, please say so.
I mean, if you… if you think ahead, you know, in time, I mean, right now it's all a bit ambiguous, because resources are encoded as target info. But if you think ahead, when we have, presumptively, the native metadata model, I mean, there will be an explicit… Prometheus will have an explicit model of OpenTelemetry resources.
**Arthur Sens** 28:04 Yeah, like, for the future, I agree. I think right now we are trying to just clarify the current behavior, so we can do the changes for the future.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 28:15 Yeah, but I still have the argument that Prometheus does… does have, like, a documented, explicit notion of OpenTelemetry resources being modeled.
**David Ashpole (Google LLC)** 28:32 but that they're modeled as Prometheus concepts, right? Like.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 28:39 That's the part, that's the dimension I think is admittedly ambiguous in Prometheus.
**krajo (Grafana Labs)** 28:52 Hmm…
**Arthur Sens** 28:54 Would you be very much against, if we just keep it simple, identifying for a resource, and later we We work towards where we want to be.
**David Ashpole (Google LLC)** 29:05 I think that's more ambiguous?
well, I guess lowercase resource… I think everyone will read it as OpenTelemetry resource. I don't know if there's, like, a specified notion of resource.
Otherwise, that we would be pointing to.
**krajo (Grafana Labs)** 29:22 Yeah, I'm also thinking that if you write resource, people will think open time to resource, and… And again, thinking of the drop-in replacement use case, it clearly will be a script target, so it's not just open territory resource.
Oops, sorry, just…
**David Ashpole (Google LLC)** 29:42 Just to that, like, the… Like, it will be a resource.
when it's converted to OpenTelemetry.
**krajo (Grafana Labs)** 29:51 Right, yeah.
**David Ashpole (Google LLC)** 29:52 Like, so it's… A scrape target, in a sense, becomes an open telemetry resource today.
When it's in… OpenTelemetry's form, right? And then when it goes back to Prometheus today, we model it as a scrape target again.
So that's how I would describe it, is, like, each… we each have… today, we each have non-overlapping like, you know, OpenTelemetry hasn't added an explicit notion of scrape target.
And I know Prometheus is obviously working on A native representation of resource.
But today, we mapped the two concepts back and forth.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 30:34 Yeah.
But I mean, that's what kind of what… maybe I misunderstood, but this is kind of what I talked about before that.
every resource model in Prometheus doesn't necessarily represent the scrape target, because it's… Because it's possible there's no scraping in the pipeline. Like, there may be, like, an OTL client just sending OTLP.
**David Ashpole (Google LLC)** 30:59 I completely agree. It's still…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 31:01 to the committees.
**David Ashpole (Google LLC)** 31:02 it's still represented as a scrape target, is what I would say.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 31:07 Yes, yeah, that's what I… that's what… I think, is actually explicitly modeled as an auto resource in Prometheus, but it's ambiguous.
So that's, that's kind of, like, my, my view, or my take on this.
**krajo (Grafana Labs)** 31:33 Oh.
I feel like… You're going… They're going a little bit in circles here.
Can we say some… like… Can we use a different wording than resource, you know, for, God, that's… ugh.
That sounds stupid.
**David Ashpole (Google LLC)** 32:05 I'm not wholly against… The bottom statement. Or, even without for a scrape target.
I would say that generally today in Prometheus, job and instance are considered identifying.
I don't know if that's helpful.
identifying for what is a good question. I would say that, like.
you know, 5 years ago, the answer would have been, well, identifying, obviously, for a Prometheus scrape target, but now there's other things in the mix.
And so it's… maybe less.
Yeah.
**krajo (Grafana Labs)** 32:45 Or… how… how could we… like, what… what are we saying about the… the target info and how we model OpenTe? Could we say… Inc.
Prometus terms, what that means. It means that LFX website, or, Like, a group of… metrics joined… having the same job analysis, I don't know, that's… Beautiful.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 33:20 I mean, is it so bad? I mean, is the original formulation on the first line so bad? Like, I think it reflects reality.
**David Ashpole (Google LLC)** 33:29 I… I don't… I would, I have a different suggestion, which is, what if we said in Prometheus metrics, the job and instance.
Labels are used as join keys between metrics and target info.
I think that… Would be technically correct.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 33:47 Yes, I think so, too. It's like, that works on the, like… Concretely technical, though.
**krajo (Grafana Labs)** 33:59 as…
**David Ashpole (Google LLC)** 34:12 I kinda like it with the H.
**krajo (Grafana Labs)** 34:15 What age? With what? Sorry.
**David Ashpole (Google LLC)** 34:17 I'm sorry, jokes.
**krajo (Grafana Labs)** 34:19 Yeah, I didn't catch it. I mean, yeah.
This is cert… Did I do this right? Yeah, so… yeah, I was thinking about something… well, not exactly this, but something that describes it holding in Prometus data model, and the Prometus data model in the docs certainly doesn't have open territory, it has metrics, metric names, labels, names and values, and etc. So the… and I'm talking about the data model specifically, Arve, not the… not the hotel endpoint. So I feel like this could be a good compromise here.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:04 Yeah, I mean, it looks… it is correct in a narrow technical sense, at least, so I think… I guess this works.
**krajo (Grafana Labs)** 35:11 Okay.
So, yeah, once again.
So, in Prometus metrics, the ZoomMate instance are used as joint keys between metrics and the target info metric.
Therefore a new resource must be created for each job and instance pair, and contained in the metrics labels, except for target info metric. Well, yeah.
And, yeah, this is how it works, and… This means that Basically, whatever you put into an instance.
will eventually… Identify your resource as well, but… That's not where it comes from.
Alright, so, if there is no job label on the metric, and the metrics are being scribed.
Then the job label must be considered to be equal to the job label of the scrape target.
During script, the job label of the target may be equal to the script job name or customized by variable rules. Again, I'm… I have to do this… If they are being scraped thing, because… remote. Like, I tried to do this… Do it with the… remote right receiver.
together, but it just got so complicated, I couldn't, basically.
**David Ashpole (Google LLC)** 36:42 I have… I have one suggestion, maybe, which is… Yep.
Is there anywhere in the Prometheus documentation or specs?
That describes how… job and instance are selected. Because, like.
This doesn't even get into, like, honor labels and… You know, it's… I think it's easier for us to write this document if we just say, like, oh, there's a job label that comes from Prometheus, and it decides how to set it.
And all we're doing is taking that and applying a transformation to it, instead of, like.
trying to re-specify… sorry, I'm really cold. Everything that the Prometheus server does for us, if that makes sense.
**krajo (Grafana Labs)** 37:24 So, to add that, I would say that this part that I highlighted.
It's wholly done by the collector.
So it actually… if it doesn't receive a job label, there's code in the collector that will look at the script target.
So it's… it's not… Prometus doing.
**David Ashpole (Google LLC)** 37:46 Interesting.
There's no doubt.
**krajo (Grafana Labs)** 37:48 This part is done by Prometus, so… I mean, this is explanation, I can take this out.
**David Ashpole (Google LLC)** 38:01 Well, I think we would have to figure out what to link to. I'm not sure if… it depends. If there is no good, like, docs page that describes it, then we should keep it in here.
**krajo (Grafana Labs)** 38:11 Okay,
**David Ashpole (Google LLC)** 38:13 Otherwise, maybe just add honor labels as part of the… Decision.
**Arthur Sens** 38:18 Kyle shared, A link to the page in the docs that talks about jobs and businesses.
**krajo (Grafana Labs)** 38:28 Can you comment on the PR, maybe, Kyle?
I'll send you the… Okay.
**Arthur Sens** 38:34 Kyle left already.
But, I'm… but I'm adding… In the comment. If you refresh… if you refresh the page, you'll see the… the link there.
**krajo (Grafana Labs)** 38:47 Awesome, thank you.
Yeah, I didn't tell… clue to not just verify me, but also give me references. That was a mistake.
But, yeah.
So, yeah, there's… there's more… talk about… The job label here.
Like, if we cannot figure out… figure it out, basically… Script must feel.
And actually, that's again different from what Prometheus does, because Prometheus will happily scrape if there's no job or set to empty value.
But the collector will actually fill the script.
Which is not that great, because it should be a dopamine replacement, but whatever. Usually people have a job.
And then… Lots of it is, Kind of repeated for the instance level.
So, the instance level is coming from… From the… from the skip.
And note… so, yeah, this part is the collector.
The node part is, again, Prometheus.
how it calculates it, I guess I can replace it here as well, like the instance calculation with the link. I'll take a look.
I guess the interesting part comes here.
So, we get… Zoom an instance, and we create a resource.
Based on these keyed by a triple instance, and then for each resource.
The service.name attribute must be set to the service.name label in the target info metric.
If that label exists in the target info metric, with the same job and stones key as the resource.
Otherwise, search.name must be set to the value of the job label. So… Yeah.
This is the current behavior.
And, Right, I have the note here that this is by… In the default translation mode.
You get the service underscore name, and the job is… is not… the service name, it's the actual job from Prometus.
So this is described in the current situation.
Okay.
And then for the… For each resource, the service instance ID attributes must be set to service instance ID label and target infometric.
If it exists, if it's not… if it doesn't exist, then it's going to be set to the instance label.
And again, this is why the default translation does what it does.
And, yeah.
And then there was a… Yeah, I updated the table to be a bit more precise, based on what Alan was telling me, on what Attributes to put into the… Resource attributes on top of the… service.name and service instance ID.
So server address… It's a bit more well-defined. So, report.
URL scheme, but… They are almost the same, but just a bit more… Precise in what they actually are.
**Arthur Sens** 42:37 For these resource attributes, I think it's very, very common to not have Like, something that looks like an address and park.
Because of relabeling rules.
So, yeah, yeah, I… I don't know, I… Wait, I'm sorry, I need to read this again.
I think it's not just empty for server port.
Because… If the instance doesn't look like a hostname at all, should it be… should it become a host?
**David Ashpole (Google LLC)** 43:20 I… the other question I have is… Even if someone relabels instance.
would it be helpful for us to still set this properly? Like, I don't know if we can… If it's possible for us to access the original original instance.
That it was scraped from, like, pre-relabeling. But that might be something worth investigating, because… It would honestly be kind of nice if we always set this correctly.
Like, it would make these values more reliable, maybe.
But yeah, address can definitely not be a hostname.
Or not be, okay.
**Arthur Sens** 44:03 server hosted server.
**David Ashpole (Google LLC)** 44:13 It would be before metric relabel rules.
I assume that you can… I assume that if you relabel it to point at something else, we should still… Yeah.
**krajo (Grafana Labs)** 44:25 Yeah, I never can keep it in my head what the heck is the difference between metric labels and reliable rules.
Oh, yeah.
Alright, so… Then there was a… I'm wondering where the… I'm trying to find… Whatever. So there was a section about Kate's… service discernment levels.
Further attributes, such as from CAD service discovery metadata labels, may be added to the recent set rules.
labels from the target infometric take precedence over all derived resource attributes. This is copy-pasted from somewhere else where It was moved, so this is not new, actually.
**David Ashpole (Google LLC)** 45:16 Yep.
**krajo (Grafana Labs)** 45:16 And then… Like, the rest of the… the doc was… The fluffy part, so… like I said, I rewrote it to be more precise above, and then I… instead of having normative language in the fluffy part, I rewrote it to be kind of a summary.
So, to summarize, service name and service instance are needed to ensure… Prometheus Export Task and descend… oh, this is where I moved it, where I… what I removed from the start, yeah.
So, service names are needed to ensure Prometus exporters can disaggregate metrics using JobN instance labels.
As described below, in the… in the OTRP to Prometheus section.
Therefore, this specification ensures that serves.name and serves.instance ID are always defined.
**David Ashpole (Google LLC)** 46:09 Do… do we reject?
this is a question for the remote right receiver. Do we reject points that have no Job, instance, service name, or service instance ID.
**Arthur Sens** 46:22 I don't remember.
**David Ashpole (Google LLC)** 46:24 It's like this… because this is a guarantee for the scrapers, right? Because you always get a job in instance.
**Arthur Sens** 46:29 I…
**David Ashpole (Google LLC)** 46:30 I do wonder if we should soften this language somewhat.
**Arthur Sens** 46:33 I think we don't reject… But… but we have a cache of target infos.
**David Ashpole (Google LLC)** 46:40 As a mesh, yeah.
**Arthur Sens** 46:41 We mesh the cache with these keys, so you get the metric, but you don't get the resource attributes.
But this, yeah, I think it needs to be verified, because it's been a long time since I've touched this code.
**krajo (Grafana Labs)** 47:06 David, did you say all of them are missing, or just some of them, or what do you mean?
**David Ashpole (Google LLC)** 47:11 Also… So the mapping to service name is, do you have a service.name, or do you have a job? For service.name to be unset, you would have to be missing both of them.
Right.
Or, right, so service name plus job. Like, basically, do we actually guarantee that these are always set, or is that just a property of the Prometheus receiver?
**krajo (Grafana Labs)** 47:39 Oh, I see what you meant.
**David Ashpole (Google LLC)** 47:40 obviously a good… I think ensuring that they're set is a good thing.
We have to balance that with whether to reject metrics in the remote right receiver, but… I don't think this is a big… since this is just copied, I'm also maybe okay to just leave it as is.
I also think it's… yeah, it's not normative, so it doesn't… It doesn't matter. It just may mislead people.
**krajo (Grafana Labs)** 48:08 Okay, I, I, we can definitely check that.
And then, in addition to the attributes above, the target infometric is used to supply additional resource attributes.
If… Present, the target info metric must be… What? Oh, yeah, I'm… Agreed.
**David Ashpole (Google LLC)** 48:33 I thought we needed to get rid of additional.
Because that's part of what makes it ambiguous today.
**krajo (Grafana Labs)** 48:40 Yeah, that's a different PR.
**David Ashpole (Google LLC)** 48:42 Okay, that's fine.
**krajo (Grafana Labs)** 48:43 So, this has to be… if we… if that PR is merged about all attributes, this needs to be rebased.
**David Ashpole (Google LLC)** 48:51 Okay.
**krajo (Grafana Labs)** 48:52 So… Yeah, so yeah, if present, the target info metric must be dropped from the batch of metrics, and all labels except job instance, underscore underscore name from the target info metric must be converted to resource attributes attached to all other metrics.
Which are part of the same resource identified by Job and Inissance.
So… Still, as we started out, we identified resources by job instance.
So when we put the… labels from Target Info, basically the rest of the labels from Target Info.
into the resource, it needs to go into the right resource. This is what it says. It's a… maybe it's a bit convoluted way of saying it, so I can probably work on… Making this just simpler language.
Because it is a fairly simple idea that You define resources, you put the targeting full stuff into the right one. That's it.
And, yeah, this is copy-paste from existing.
By default, hierarchies and values target information must not be altered, such as replacing other scores.
With dot. So this is cop- copied.
I think…
**David Ashpole (Google LLC)** 50:20 for this.
**krajo (Grafana Labs)** 50:22 Yeah, sure, no problem. I think this will probably need more review, like, I feel like I… Knew everything, and was… sure about everything when I did it, when I was also using LLM to verify myself at every step.
But, I think I need to do it once more, especially if I make the updates.
What's interesting to me, by the way, is that like, I didn't actually know what the receiver were… receivers were… Keying the resources on.
And, Where, where's it? It's, yeah, and so this is the interesting part to me, that in… they… they use the Joban instance to do the keying.
**Arthur Sens** 51:25 Yeah.
We… we… I did not implement the initial, Prometheus receiver, but I was there for the remote ride receiver, and we just followed the SPAC set job and instance, so we did that.
**krajo (Grafana Labs)** 51:45 So… like, in a… in an… In a sense, it means that If you don't intend the JobN instance to be identifying… The same resource as the service attributes?
basically… You cannot do that, because… the script identity, so basically the Jobel instance.
We'll key your resources, and There isn't really a way around it, at the moment. Arve?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:21 Yeah, I just wanted to say, I think this reflects kind of what I'm saying, that… like, even if this is not ideal, this is kind of the working definition within Prometheus, that, So, like, one, Prometheus needs a way to identify open telemetry resources.
**krajo (Grafana Labs)** 52:41 Yep.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:41 And two, that way, that way is currently via the job and instance labels.
And three, you know, I've come to the conclusion that this is not… this is, unfortunate, because it means that Jobin Instance is overloaded as a concept. It's both kind of, like, scrape target identifying, and also resource identifying, not, you know, because it's, like, it makes sense, but because it's how it is, and you need something.
So this is why I think, like, long-term, we should have, like, another label for identifying open telemetry resources, because we need it, really.
**David Ashpole (Google LLC)** 53:21 So, I mean… The key invariant here that the spec follows is that When you have a Prometheus metric, And a target info series.
And you want to join the two.
you join on Job and Instance.
So it's not that we're joining OTEL Resources on Job and Instance or anything like that, it's that… when we… when we, like, when we take an OTEL resource and want to pass it through target info. We make sure that… it can be rejoined on Java instance, right? So that's what we're trying to do, is we're trying to take the existing join keys for targets.
And make sure that it allows us to round trip.
the resource, right? So… The reason why we key in the receiver on job and instance is because that's how target info it is joined, right? So it's… this is just the inverse of the earlier statement we set.
It's nothing about hotel resources, here.
Like, it could apply to generic open metrics, target info usage.
**krajo (Grafana Labs)** 54:32 You mean generic Prometus targeting for usage, but I think I know what you mean.
**David Ashpole (Google LLC)** 54:36 Well, target info comes from the original open metrics project, right?
**krajo (Grafana Labs)** 54:39 Oh, OPAM metrics, oh, I, yeah, then, right, right, right, right.
Arthur?
**Arthur Sens** 54:46 I was gonna say that we have only 5 minutes left.
**krajo (Grafana Labs)** 54:51 Oh, yeah.
**Arthur Sens** 54:51 And I think… I think we did, like, a lot of progress today.
And wondering if we… If it makes sense to people to start meeting weekly, I feel like, bi-weekly.
it's taking too long for us to make progress, and, like, we forget what we discussed. Yeah, I just want to, like, keep in touch more frequently.
If that works, david, do you have the power to switch your meetings to weekly?
You're muted.
**David Ashpole (Google LLC)** 55:32 Oops, I think we file a PR with OpenTelemetry Community.
Is that how we change our meeting schedule? I don't think we just edit the calendar directly.
**Arthur Sens** 55:42 Yeah, I honestly… I have no idea.
**Kemal Akkoyun** 55:45 I think there's a Google Group that you need to be added to that, and then if you are in that Google Group Calendar admin thingy, then you can change those things.
I remember doing this, but I… Totally forget how I did that.
**David Ashpole (Google LLC)** 56:06 Either way, I can take the action item to figure that out.
**Arthur Sens** 56:09 Thank you. Yeah. Once we get… we solve this Java and instance spaying, we can go back to bi-weekly.
**krajo (Grafana Labs)** 56:20 Yeah, I agree. I'm like a small elephant, you know, learn hard and forget easy.
So, yeah.
**Arthur Sens** 56:30 Okay, I didn't mean to… okay, but we still have 4 minutes left. I… that was quick.
**David Ashpole (Google LLC)** 56:36 I think we got through your PR, right, kryo? Is there anything else? I don't know if we're gonna open any new conversations in 3 minutes, so… Yup.
**krajo (Grafana Labs)** 56:44 We got through. I would suggest you also take a look at the OTRP2 Prometus.
side, I thought that it was more precise, and I felt I didn't need to make changes, but, you know, take a look at it. If you disagree, we can… Like, this PI is about, you know, clarifying things, so if you need something clarified there, then let me know.
**David Ashpole (Google LLC)** 57:10 Yep.
Cool. Thank you, everyone.
**Arthur Sens** 57:15 Thank you. Bye-bye.
**krajo (Grafana Labs)** 57:17 Bye-bye.
