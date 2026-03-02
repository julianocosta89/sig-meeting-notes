SIG: Prometheus WG
Date: 2025-07-16
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/dZLl8V4kA7_T5dDk6MlmPn07UMFtHAyPEXnts1LJjXdRq30Lv0hBcKiujZR0QrEP.HOJrO3ABOUOdFHjS
============================================================

## Zoom Recording Transcript

**Jonathan (jojo)** 00:52 Hey? Hello! Karju.
**krajo Krajcsovits** 03:32 Are you waiting for people that might be on holiday or.
**Arthur Silva Sens** 03:38 I don't know.
I I probably I'll probably need to drop meet mid-meeting.
But I I guess you yeah. Once I leave, you can take it away. No problems, right?
**krajo Krajcsovits** 04:00 Yeah, there's there aren't many topics so they can probably got through them.
**Jonathan (jojo)** 04:10 So I think that I can talk about my my topic
some ice. Send some message on the public channel asking for mentorship.
and I participate off the 1st term, and I would like to be a mentor in this 3rd term.
and probably I need some help.
I don't know art, or someone else would like to be.
Contribute with me.
**Arthur Silva Sens** 04:43 I would love to. But I also need to be careful because I'm doing another ux research mentorship, and that takes time.
So if I do a second mentorship, I need to acknowledge that it will also take
some of my time.
We also need to think of a project idea. And I know you, you suggested making the remote right receiver
beta or graduated. I think this is too big for a 3 months project.
I'm not. But but I'm open to to discussions I like.
Do you think you could like? Do you know what would?
What do we need to make it, Beta, for example.
**Jonathan (jojo)** 05:32 No to promote to better. I I'm not sure about what we need to to do, but I thought that 3 months would be enough, but I'm not sure.
**Arthur Silva Sens** 05:44 I I would expect that the requirements go up right, and only to make it making it. Alpha, you
you took like 4 or 5 months.
I we finished the mentorship, and we continued for another one a month or 2, and we are still not. We're still not Alpha.
So I expect the Beta will take even longer.
But now like to be honest, I I didn't see the requirements yet.
**Jonathan (jojo)** 06:13 Okay, I will take a look into the requirements, and we have, like 10 days to submit the the mentorship. But I can send a message to you
after.
**Arthur Silva Sens** 06:27 Yeah, no problems.
I would if others in this group would like to be mentors, like, I'm also happy
to give this opportunity to other people, and I'm doing mentorships every quarter now, for, like almost 2 years.
**krajo Krajcsovits** 06:44 How much of your time is it because I've never done it? I will probably not have timeline to prom con.
and
and I probably suck at it, because I'm not really good at mentoring, but like, how much time is it.
**Arthur Silva Sens** 06:58 So we ha! Usually we have a 1 h meeting every week.
But then the time that I need to spend with the mentee changes diamonty like.
If I do a very good job in selection phase.
I, if I choose a very independent mentee, I my my life is too easy, like the person. Just do everything, but if it, the person needs a lot of hand holding, then I then
then my life is I wouldn't say miserable, but, like I, I have a hard time balancing grafana work and mentorship.
So it depends on the selection phase
like Jonathan, for example, was pretty easy, like he just weekly meetings and reviewing Prs, and that that was it.
I. If you're up for it, cryo I. It could be a a 3 mentor, 3 mentors. So it's not too hard on the 3.
**krajo Krajcsovits** 08:10 Like, I said I. My priority is to get native program stable by prom con
in primitives, so I I very much doubt I will have time, but after that I think
we should come back to this.
**Arthur Silva Sens** 08:27 Okay, then then it's it's gonna be next next year. Cause this is the last turn of 2025.
**krajo Krajcsovits** 08:33 Oh, okay.
**Arthur Silva Sens** 08:47 Jonathan, do you wanna try reaching out to others as well? That might not be here like David Ashball. But maybe Bartek sometimes also wants to to mentor.
**Jonathan (jojo)** 08:57 Yeah. Are you trying to send a message on the public channel asking for help and tagging them?
We try to do that on this week.
**Arthur Silva Sens** 09:09 Cool. Thank you.
**Jonathan (jojo)** 09:18 I think that you or the next one, Carl.
**krajo Krajcsovits** 09:28 Oh, yeah, I just need to find the unmute button. So yeah, there's an issue
regarding somebody complaining that the service name that they get from
from aus receiver, especially when they use Kubernetes service discovery. It's kind of useless and not what they expect.
And I'm not sure how to
like some of this. I know that in like in Grafana labs, the Do relabell rules
to set the job based on the namespace, and the
maybe the pod name or container name or something.
So there are. There are workarounds
but I'm not sure what to tell them in in open telemetry. Should we just tell them to
use the relaber rules? But then, like what to suggest to put in there? Because the other side is that
the service name should have some kind of meaning for for open damage as well.
just throwing it out there.
**Arthur Silva Sens** 10:54 0.
**Cyrille Le Clerc, PM @ Grafana Labs** 10:56 Yes. So at Grafana labs, we we are at the moment doing user research to to get back on how users use the resource attribute promotion
on the 1st usage that we see is people move away from using job on instance, labels
in favor of using service name service namespace. Rve was with me on some user interviews.
What it tells me is that really people want to adopt this semantic meanings that they have put in a service name, service, namespace.
And so I think it's what they want on. There is this hotel specification that is mentioned in the ticket.
With this rule it should be the Kubernetes annotation called Resource dot hotel dot I/O slash.name, or it should be apparentities. I/O slash name, or it should be deployment name, or it should be so on. So on.
I think people really want to adopt
hotel practitioners. They expect to to use more and more these semantic names over what has been in practice since the in the
primitive ecosystem of Job, with naming conventions on the on the job.
That's my 2 cents.
So I would be in favor of yeah honoring what they of having
the scraping logic adopting the hotel semantic conventions on service name.
**krajo Krajcsovits** 12:32 But is there something that we could like easily adopt as default? Because
you mentioned a couple of things that could be done
and could be put into the service name so like we could add some kind of feature into the promise receiver to automatically do this. So people are not surprised, and are like comfortable in open, but, like what would it can? Can we even choose one thing that would be good.
**Cyrille Le Clerc, PM @ Grafana Labs** 12:59 It's specified by the in the Kubernetes attributes processor by this hotel underscore notation, Colon true, is what activates it
on just before the contributor mentioned it. Sorry I have to find it again.
There is a doc in in the hotel specs on its reference in the ticket as well.
Okay.
so there is one spec. I have to find it.
**krajo Krajcsovits** 13:49 Could you put it into the doc? Not not the chat, or yeah, thank you.
I mean, if there's something like, you know, very deterministic and like exact.
Then we could do it, I think. But then someone has to open up your to actually
try to add it. Maybe behind the feature flag. I don't know if that makes sense.
**Cyrille Le Clerc, PM @ Grafana Labs** 14:17 It's in the Kubernetes resource attribute processor. Yeah, I just dropped the link.
**krajo Krajcsovits** 14:39 Okay?
Well, I guess.
Yeah. Like.
for the Kubernetes discovery that should be doable automatically. Question is, if we want to make it
the default, or or just as an option or something.
**Arthur Silva Sens** 15:00 I I would expect for me to use my dinners to be a little bit skeptic about this
or or not.
**krajo Krajcsovits** 15:15 Why?
**Arthur Silva Sens** 15:18 Prometheus has this own thing it shouldn't adopt. Sorry Prometheus has its own thing. It shouldn't adopt open telemetry stuff. Blah blah blah!
I if I'm the only one thingy like this side, then
that's and we can just ignore.
**krajo Krajcsovits** 15:41 I mean. My impression was that
everybody's kind of doing this to set the job on discovery, because otherwise the job is just the name of the discovery job, which is.
**Arthur Silva Sens** 15:52 Yeah, yeah, exactly.
**krajo Krajcsovits** 15:53 So. But I I mean I'm not the expert, so I can ask.
Oh.
**Arthur Silva Sens** 16:00 I hope what I meant is peop. People. The premises maintainers would be skeptical about. Instead of adding job. Add something.
There was hotel convention.
**krajo Krajcsovits** 16:14 I'm not talking about that. I mean, I'm just talking about what to put into job
because the job gets turned into service name. So that's fine, I think.
**Arthur Silva Sens** 16:23 Okay. Amazing. The project.
**krajo Krajcsovits** 16:25 Oh, sorry. Yeah, I wasn't. Wasn't exact sorry, Cijo. You keep your hand up.
**Cyrille Le Clerc, PM @ Grafana Labs** 16:30 Yeah, I think it's very important to embrace this hotel conventions, because what we see is people they produce some metrics, maybe with promisive style, scraping some traces, maybe with Hotel SDK, and then they will also collect the board logs, and then they will say, I want all these to be correlated together
on the only way we found so far is to say, let's align everybody on Kubernetes metadata
like Kubernetes, annotations, labels.
or metadata themselves, so that whatever you are in process, you are in a monitoring library in process of the code that executes or outside, like kubernetes daemon set so on. You can introspect. This metadata onto the job.
**David Ashpole** 17:18 Welcome!
There we go!
**Cyrille Le Clerc, PM @ Grafana Labs** 17:21 When I say when you are in process, it's because when you use something like the opentem 3 operator, it's capable of injecting through environment, variables.
or the config. You should be aware.
**krajo Krajcsovits** 17:35 I think that makes sense but sorry.
**Arthur Silva Sens** 17:38 No go ahead!
**krajo Krajcsovits** 17:40 No, I I think that makes a lot of sense, and that list seems to be quite
exact and like
deterministic. So my only question would be if I were to open a Pr. Would it be about making this the default and.
**David Ashpole** 17:55 Maybe giving an option to revert to the.
**krajo Krajcsovits** 17:58 Old way of working, or make this optional.
and by this I mean, you know, overwriting the job in the Primitives.
**David Ashpole** 18:10 Remote, receiver.
**Cyrille Le Clerc, PM @ Grafana Labs** 18:18 I think you will have Kubernetes. Permission issues because it
vanity's attributes. Processor, to be able to discover this metadata needs to be granted some permissions.
**krajo Krajcsovits** 18:30 So you think the formative service discovery will not have all this data is what you're saying.
**David Ashpole** 18:37 Prometheus service discovery does have a lot of that. Actually.
So because today, we already, for example, put like the pod name, yeah.
**Cyrille Le Clerc, PM @ Grafana Labs** 18:49 I, yeah, I have a ticket on this. There are some. It's missing, some stuff.
**David Ashpole** 18:54 Yes, I did like a initial implementation a few years ago, and then
I didn't really get any feedback.
I guess I expected people to think it was the coolest thing ever, and
nobody said anything. So I was like, clearly, nobody cares about these labels.
Yeah, there's a few of them there we can expand that especially to match the spec, I think, would make sense.
**Cyrille Le Clerc, PM @ Grafana Labs** 19:17 Let me copy the ticket I created recently
on the Sd. Con Kubernetes, Sd. Config is what you are thinking of. Correct.
**David Ashpole** 19:29 Who do we need? I don't know if we need the deployment or Cron chop name.
**Cyrille Le Clerc, PM @ Grafana Labs** 19:35 If you want to be aligned. Otherwise it's a nightmare. When you assist people.
I can tell you dozens of stories where we had
customers will be to understand on the.
**David Ashpole** 19:49 I mean, do you think?
Do you think this is something that Prometheus users want as well?
It seems like being able to relabel my deployment name
would be helpful. I think it's mostly a question of like.
how would somebody turn turn that on or off like we don't want to spam people's logs with, like.
you know, don't have permission for people who are just using Kubernetes. Sd.
**Arthur Silva Sens** 20:16 Thank you.
It could be. It could be a Boolean in the St. Config struct.
**David Ashpole** 20:27 Yeah.
**Arthur Silva Sens** 20:35 This Boolean would add new labels, or or it would rename the old labels to the hotel, waste.
**David Ashpole** 20:46 For Prometheus, it would make new underscore underscore Meta label labels available for relabeling.
So that's the it would just it would have the metadata available.
But users wouldn't get any changes unless they actually do the relabeling.
and since it would be off by default like
nothing would like it wouldn't really matter.
or it wouldn't change anything. It's just like some more complexity in the Service discovery implementation. And then for hotel, we can sneakily grab all of the underscore underscore Meta labels that we care about
as assuming they're provided by Prometheus and convert those into the appropriate service. Discovery, art resource labels.
**Cyrille Le Clerc, PM @ Grafana Labs** 21:36 And we have identified. There is a benefit is that today you can collect the pod name with service discovery
on. Many people shoot themselves in the food because it's higher dimensionality that higher canality than what they would like. And then they say, Yeah, yeah, you have a cost explosion, and so on
on here, if they can collect deployment name, which is a very good semantic meaning.
maybe it will make the life of a from each users easier.
**krajo Krajcsovits** 22:07 Okay. So basically.
the the scope blew up a little bit. I was thinking that this was easy. But nothing is easy. So
basically, service discovery needs to provide these.
And then we have to make sure that we actually put it into the job.
whether it's by default or an option. That's something to figure out later.
And then I don't know what the target all locator is using is that relevant, even.
**David Ashpole** 22:36 Not gonna work at all. It's using Http.
Sd. Configs, I think, or is it using static targets?
**krajo Krajcsovits** 22:46 Of the season.
**David Ashpole** 22:47 Sd. Configs, which was served by, because that lets you like curl an endpoint to get your targets.
And so it's using that and the target allocators, which is like a
deployment running in the cluster is serving the targets
based on it having done service discovery.
and those are just like IP addresses and stuff.
**krajo Krajcsovits** 23:15 Right.
**David Ashpole** 23:16 And then each one figures out what its targets are. But you won't get any metadata then, so it completely breaks. If you're using the target allocator.
**krajo Krajcsovits** 23:28 Okay. Hmm.
**David Ashpole** 23:32 I don't.
I don't know if Http. Sd. Config is allowed to provide meta labels.
But like, but yeah, now we're just talking about more features.
**krajo Krajcsovits** 23:51 Yeah.
**David Ashpole** 23:53 My, my feeling is that maybe the right 1st step is to simply implement the fallback specification
as it's described in the hotel document, using whatever resource attributes we have on hand.
and then we can talk about adding additional ones
as we're able to get them so like we wouldn't have deployment name.
But we may have access to annotations, for example, on pods or any of the other things that it specifies.
So maybe we can get 80% of the way there
and then solve these harder problems later.
Yep.
**krajo Krajcsovits** 24:36 Yeah. But then I definitely wouldn't make it this default. Maybe either config it or put it behind feature flag until it's like.
**David Ashpole** 24:43 According to, spec.
**krajo Krajcsovits** 24:45 Okay, that's clear.
Okay, let me write it down.
**David Ashpole** 24:55 Yeah, it'll be a big change.
Okay, let's move on to the next topic, then or no, you're still writing.
**Arthur Silva Sens** 27:01 But is there anything else to discuss.
**krajo Krajcsovits** 27:09 I got the answer.
**Arthur Silva Sens** 27:12 Hey mine is just a fy I
We reverted a feature that we introduced to Prometheus, because there was some weird discussions that we might or might not need to
to use a different prefix for the telescope attributes.
But at the end we we noticed that we don't need to change anything. So I'm just
reintroducing the same feature.
I know. I saw I saw a review from David. If others that were involved could review as well. And then we get it merged. This is kind of blocking other work, because we are doing a lot of merge conflicts
by like removing and re-adding the same feature over and over.
But yeah, we can go to the next.
**David Ashpole** 28:20 Surreal.
**Cyrille Le Clerc, PM @ Grafana Labs** 28:21 He's the next time
it. It's related to what Arthur said. Do we have docs documenting how the scope infometric on all these things work, because
it seems that we prefix stuff. Now.
when in the past for resource attributes, at least we did not prefix.
We didn't prefix. Target is target info, not audel target info. When we do a resource, attribute promotion, we don't prefix
the resource attributes names that are promoted as hotel metrics, and we have very good feedback from users.
Emojis.
**David Ashpole** 28:59 For.
**Cyrille Le Clerc, PM @ Grafana Labs** 29:00 On the fact that we don't prefix.
**Arthur Silva Sens** 29:03 So in the past we had a metric called hotelscope info, that would hold the attribute. The scope attributes
the hoteloscope. Infometric is is now removed by the spec.
Instead of adding the labels only to that scope.
scope info, we add the scope.
**David Ashpole** 29:26 We had.
**Arthur Silva Sens** 29:27 The scope attributes to all metrics that are originated from that that scope.
You might, you might see some
different stuff, because not all Sdks
are up to date with this spec.
**Cyrille Le Clerc, PM @ Grafana Labs** 29:48 Scope, underscore, star, attribute, label names.
**David Ashpole** 29:56 I want to also, like the the change that happened that caused us to remove hotelscope info
in favor of having prefixed labels on the metric itself is that scope attributes became identifying
because of that like we can no longer like with resource
on a Prometheus endpoint in particular, like job and instance are identifying right? Because your resource.
because, like for Prometheus, when it scrapes something, Java and Instance are always identifying.
It's a little bit confusing with the Otlp endpoint. Now, because in theory all the resource attributes are identifying or like some subset is.
but for Prometheus exporters, job and instance are identifying, and you can always use that as a join key
between your resource attributes and any metric right?
See, Arthur,
But because scope attributes are identifying.
We have to put them on every metric.
And so we.
I think the hotel scope, name, and version labels make sense. I think the main question here is whether
we should prefix scope attributes on metrics with hotel underscore scope, underscore.
or whether we should put them as is right. That's your question.
**Cyrille Le Clerc, PM @ Grafana Labs** 31:26 Right?
Yes, I think so. Yeah.
**David Ashpole** 31:33 And I think there's.
**Cyrille Le Clerc, PM @ Grafana Labs** 31:34 We've prefixed it just by scope, underscore or hotel underscore scope, underscore.
**Arve Knudsen** 31:41 It's a hotel underscore scope underscore. That's that's what the spec says. Right?
**David Ashpole** 31:48 Yeah, it's everything in hotel ends up namespaced so
like things that opentelemetry defines are usually in the hotel namespace.
as in like things related to opentelemetry sdks
are usually in the hotel namespace.
Is there an ask or like something you don't like about the current behavior, or do you just
one. Did you just want to know?
**Cyrille Le Clerc, PM @ Grafana Labs** 32:35 I'm brainstorming on the impact. I yeah, I'm thinking, across metrics on logs of the usage of a scoop.
I don't know but I would be very interested in seeing some
popular examples of hotel metrics, of
of hotel metrics that are scoped.
that you leverage the scope attributes
and see what it would look like in in primitives.
**David Ashpole** 33:02 Yeah. Almost nobody uses scope attributes today.
**Cyrille Le Clerc, PM @ Grafana Labs** 33:06 It seems like.
Is this.
**David Ashpole** 33:09 What's that?
**Cyrille Le Clerc, PM @ Grafana Labs** 33:10 Hotel collector is doing this.
**David Ashpole** 33:12 Yes.
**Cyrille Le Clerc, PM @ Grafana Labs** 33:14 It's the only use case I am aware of.
**David Ashpole** 33:17 But if you get feedback from users or anything like that like, now is definitely the time for the
make adjustments to this cryo.
**krajo Krajcsovits** 33:28 Yeah, so I'm I'm done so. So more concrete example. So if I use the promise.
remote right exporter, for example, or the Prometus exporter.
This means that the scope attributes will be added as regular labels on the matrix and not not put into target info, but just put on the to the metric.
**David Ashpole** 33:53 Yes, that's.
**krajo Krajcsovits** 33:54 As long as they are, as long as they are actually set. So you don't set like empty ones, like
whatever.
**David Ashpole** 34:01 Yeah, I think that's just a Prometheus convention that empty labels are equivalent to unset ones.
**krajo Krajcsovits** 34:10 Okay.
**David Ashpole** 34:13 But we we have to do that because scope attributes are identifying.
**krajo Krajcsovits** 34:17 Yeah. And I have to like, read up on all the scope, attributes, resource, entities and everything. Because
I it's a lot, and I'm
I'm never sure that I understand things correctly. So is there like a good intro course, or or like, I don't know slide where on on this.
on the topic of attributes and entities, and everything like, Are you good nurse?
**David Ashpole** 34:42 Scope. Attributes are a distinct topic from entities.
Entities to me is the one that's very confusing and hard to understand and unclear what
we, as the Prometheus Compatibility Work group should do about them. I think so that that to me is a big can of worms. I think scope attributes are actually quite simple, which is
the attributes on a scope they're identifying for all of the metrics within the scope.
The only option for us is to add them to each metric.
**Juraj Michalek** 35:14 I mean.
**David Ashpole** 35:15 The only question is.
should they be prefixed or not? And if they should be prefixed, what should the prefix be today? The prefix is hotel
underscore, scope, underscore, attribute key right? But we could. We could not prefix them
which would prevent us from round tripping them, but maybe it would be more usable for users.
or we could choose a different prefix.
**Cyrille Le Clerc, PM @ Grafana Labs** 35:46 Have a question, please.
All right, go for it. Yeah. I found it.
I copy pasted the specification I found
in the instrumentation scope. You have a name.
a version, a schema URL, on attributes.
If we talk about scope attributes, we only talk about them later on. Then it means that we don't map
name version on schema. URL.
Am I right, or are we talking about
scope attributes, or the scope double.
**David Ashpole** 36:23 This.
**Cyrille Le Clerc, PM @ Grafana Labs** 36:26 Think it's a scoop.
**David Ashpole** 36:26 So we've always handled, I think part of it is like a little bit of history. We've always handled scope, name, scope, version, and Schema URL,
by adding them as labels to all your metrics by default.
The new thing that was introduced
8 months ago, or something, is that scope has attributes.
So
We've always handled scope, or in most in like the Prometheus receiver and Prometheus Exporter, Prometheus. Remote right, I think, might have come later, but we've always handled scope, name, scope, version.
and Schema URL. As labels.
Only recently have we added scope attributes, and
even more recently, scope attributes were
marked by the specification as being identifying. So they used to be descriptive.
And so we could put them in a separate info metric. But now that they're identifying, they've moved back into being present on every metric.
**Arve Knudsen** 37:27 Think the Prometheus or Tlp endpoints never produce scope info, I mean the metric.
which is, I think, so. I think it. It's the utility endpoint never, never touched the scope, attributes.
**David Ashpole** 37:41 Yep.
**Arve Knudsen** 37:42 Scope, name, and so on.
**David Ashpole** 37:44 Yep.
**Juraj Michalek** 37:48 I remember the fiat to introduce it to remote exporter, but I don't know if it was ever merged. By the way.
**Cyrille Le Clerc, PM @ Grafana Labs** 38:01 On. When we
the attributes it's hotels, the prefix is hotel scope, or is hotel scope attributes.
**David Ashpole** 38:14 It's currently hotel scope. So if you defined a scope, attribute with the name version, get a collision. We had a discussion on a Pr
this week and last week, where we decided that that was okay, because
open telemetry requires namespacing on labels. I think there is a risk there.
But
yeah, the trade-off is having an even longer prefix for for these labels. So
it seems it seems acceptable of a risk, and
it just means we'll drop if you have a
scope attribute named name will just always drop that which hopefully doesn't cause problems.
**Juraj Michalek** 39:09 Do you wanna maybe provide context on what it's used in all the auto collector.
one might be helpful potentially.
**Cyrille Le Clerc, PM @ Grafana Labs** 39:24 Got an explanation. But I forgot, it's about differentiating. I think. Hotel collector components. Each hotel collector components provide
an identifier.
**Juraj Michalek** 39:34 Yeah, I think that caused some conflicting metrics sometime ago.
**Cyrille Le Clerc, PM @ Grafana Labs** 39:47 But in traditional instrumentation I don't see much use of Odell scope attributes.
**Juraj Michalek** 39:52 I think
I can imagine a use case and draw in the auto instrumentation right where it it tells you sort of, because you'll have metrics that you don't necessarily know where they came from. So it might be useful to to tell you. Okay, this came from auto instrumentation of this library.
**Cyrille Le Clerc, PM @ Grafana Labs** 40:08 I think it's the scope name that will do it, at least on traces. The scope name.
**Juraj Michalek** 40:12 That's true. That's already there.
**Cyrille Le Clerc, PM @ Grafana Labs** 40:15 Cat, 0 7, 0, 18.
**Juraj Michalek** 40:18 If.
**Cyrille Le Clerc, PM @ Grafana Labs** 40:18 And I will love to have it.
The scope name is will be helpful to troubleshoot as a vendor attributes. I'm not sure.
Yes, it's not a big issue we have a risk of.
Will it be activated by default because
some promise implementation have a maximum number of labels at rest
on here. We are going to add 3 labels at least.
**Juraj Michalek** 41:14 Very devil mentioned that it's not gonna be enabled by default, and that's what it says in the Pr. 2, because
so big like it is a breaking change in fear, I guess.
**David Ashpole** 42:45 Any more thoughts.
If there's a specific bug that you're finding with this, then it would definitely be helpful to to know about it.
Or if you get any feedback
cool, otherwise, let's move on to the next topic.
All right, which is mine.
I just wanted to sync on the efforts we have ongoing to
either migrate to the Otlp endpoint, writing directly to the storage appender or migrate to 2.0,
or decide to stay on changing
Otlp to remote right? 1.0 1.st
So I've I've at this point written
or written. Migration Prs for both Prometheus 2.0. And for one that writes directly to the appender.
the appender one actually saw significant performance improvements. I think it was like
close to 40% reduction, which was pretty good. So I'm definitely
leaning in favor of that, assuming we can make it work. But I wanted to get broader feedback from the group on.
Yeah, whether whether we think that'll work for other projects. And yeah, crow.
**krajo Krajcsovits** 44:24 Yeah, I I'm I'm so far I'm definitely in favor of the upender approach.
I I commented on your Pr. And with that
change on. You know where we do the dependence injection.
I could move all our mimere specific code back into Mimir and out of mimere primitives which would make it so that we don't have to like run into conflicts all the time.
which is super annoying when we update permitives from from upstream.
So I'm very much favor of that. But like
I need to test it, basically. And my 1st attempt at at
taking your patches failed because there were too many conflicts. So now I basically reset
media promoters to upstream and apply your patches. And I'm trying to
kind of make it work. So I think I think we are on the right track in the
up under especially since it wouldn't stop us from, you know.
if ever needed in primitives have a different path for the Otip data, because you would just use a different appender.
So I think it. It gives you more opportunities.
But the big question that
Brian is bugging me with is is the performance. And whether those labels are okay, I'm not.
Yeah. I don't know. I I need to basically measure it. So.
**David Ashpole** 46:02 The performance for Mimir, that is.
**krajo Krajcsovits** 46:08 Yes, because I wouldn't be.
I would be doing the same thing as before, just behind the interface. But there is a change that the labels are used differently.
So in in the previous code we went from the we copied the labels from
**David Ashpole** 46:30 You know the.
**krajo Krajcsovits** 46:31 Hotel payload into Prom label slice.
And now we are using the labels, labels.
**David Ashpole** 46:39 Type, which is.
**krajo Krajcsovits** 46:42 Some encoded stuff, so I don't know.
We see. I don't know the performance. I might have to do some tricks to get that to perform.
**David Ashpole** 46:57 I would hope that using like scratch, builder and labels, builder and stuff is actually more performant than the maps and stuff that we were using before. So maybe there's some performance win there. But yeah, we'll have to.
**krajo Krajcsovits** 47:09 Yeah, I, yeah, I have to test. I mean, there, there's options. Obviously. I mean, if you go
remote, right? 2 in promitives upstream, then we could stay on our code in mimere promiss, and just deviate even further until we have remote right to properly supported.
Right now we we support it, but like it's converting back into our own format, so it would be a double double conversion.
Or
**David Ashpole** 47:42 Yeah, that that's no work.
**krajo Krajcsovits** 47:44 Either we deviate or or we use this kind of open door approach.
So I
I basically, I'm asking for time to to get it. Get my poc up and running. I have a branch.
but like it's it's not finished, and if you could change
your Pr to to move the injection point up.
According to my my comment, that would be great, because then that makes it easier.
**David Ashpole** 48:16 To New Api, or to new, remote right handler.
**krajo Krajcsovits** 48:20 New Api, because that's what we are calling. Give me a oh, because then
it would be like extremely nice, because then I could just do the
Mimere specific code in Mimere and not in Mimi promitives and not mix primitives code with Mimere cooled.
**David Ashpole** 48:39 Okay, I am probably going to avoid rebasing
until the revert is merged. So if people could definitely take a look at Arthur's Pr. That would help all this.
**Arve Knudsen** 48:53 So can I. If I understand you correctly, you you are trying to. You are trying to integrate David's appender pr into Vimere.
So you're kind of like you're you're you're doing the job of figuring out if it's maybe you're compatible.
**krajo Krajcsovits** 49:11 Yeah, I think it's definitely going to be very compatible. I'm less sure about the the performance right? Especially since Brian is bugging me about the labels, even though he wrote those label structures. So I'm not sure.
**Arve Knudsen** 49:27 Hmm.
**krajo Krajcsovits** 49:28 But yeah.
**Arve Knudsen** 49:30 Yeah, okay, but that's great that you are on this, because then because then I I won't have to do it.
And.
**krajo Krajcsovits** 49:40 Yeah.
So my project wasn't this at all? My project was to do open time at 3 start time into
created time.
So so basically convert the open time to start time into yeah creative time.
And the conflicts come from the fact that we have an implementation right now using
remote right one plus some special non values like silent 0, we call them
so I want to replace that with created time in in remote right protocol whatever version?
But then they are really come. Yep.
**David Ashpole** 50:25 Another question for the group. Actually.
my pr, that migrates to appender actually adds
a couple features right, it adds the created timestamp, appending and metadata appending as well, which
may throw off benchmarks if people are actually
like trying to treat them as equal, I could rip that stuff out so that it's a pure
A to B.
But it was almost easier just to write everything.
Oh, but you won't even be using
the that appended piece so it, doesn't, it? Shouldn't matter. Okay, never mind. I'll leave all the features in.
and we can go from there. Okay, sorry.
**krajo Krajcsovits** 51:09 Yeah, I mean, my plan is to also throw away our this weird
way of handling the start time with the silent Nons.
and but yeah, you're right. For my comparison, it's fine. I'm going to write the code that I'm pairing to. And I'm not adding metadata feature and stuff like that. So yeah.
I make it fair. I mean, I do want this to succeed, because again, this is like 2 birds with one stone kind of thing, because if I can move the whole thing into Mimere.
then we can
simplify the the code and and upstream updates from upstream, and and a whole bunch of things. So it sounds like a good idea.
**David Ashpole** 51:53 And I also was originally just supposed to pick up Arthur's type in unit feature Pr
and ended up doing this.
Oh, yeah, cool any other comments or questions
awesome, great to see so many faces here.
I think that was the last item on the agenda.
So I'll see everyone. Actually, this will be the last meeting that I'm able to attend for a month. So
I will see everyone in 8 weeks.
But hopefully we can get my stuff merged before I go on leave again.
Cool.
Thank you.
**krajo Krajcsovits** 52:43 Bye-bye.
