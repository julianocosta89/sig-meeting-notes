SIG: Kubernetes Operator SIG
Date: 2025-11-20
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/P90JzvX665yeglJVe_Uh_Td9CYJWd2fr5zI3oBbbxABxkYImXYOWwaNmUpOcqaDn.ldNU9ZLA_FLsiYvV
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 01:52 Hello.
**Joe Sirianni (Bindplane)** 01:55 Hey there.
**Mikołaj Świątek** 02:01 Okay, let's give it maybe 2 more minutes… Sounded like Antoine was going to join, at least.
And I just noticed nightly.
It's true.
**jea** 03:03 Blue.
We're here.
**Mikołaj Świątek** 03:06 Congratulations on the successful KubeCon talk.
**jea** 03:10 Thank you very much. It was great. We actually had a lot of questions, which was surprising.
**Mikołaj Świątek** 03:16 I haven't watched it yet. It's on my list. Were there pointed questions?
**jea** 03:22 Nothing pointed, more just, like, I think going to these things, it's always just surprising how… I kind of expect everybody already knows so much about stuff, but it turns out that that's just not true, and people still don't know a lot about the project and, like, offerings. Like, I was at a… I held a meetup Semi-recently in New York, and nobody knew what the target allocator was, and I was like, this solves many of your problems. And people were just like, huh?
It was, it was surprising.
**Mikołaj Świątek** 04:02 I see… I see David's here. Are we gonna talk about the… Stabilizing the configuration.
**David Ashpole (dashpole)** 04:11 I'll talk about whatever you want to talk about.
**Mikołaj Świątek** 04:15 Yeah, I see somebody opened an issue in conjube, actually, about Prometheus Receiv… for Prometheus Receiver, which was about stabilizing the configuration and asking the uncomfortable question.
You know, are we gonna… are we gonna, what are we gonna do about the fact that we use, like, Prometheus config constructs in our configuration? Like, how are we gonna declare this stable if they can just change it?
To which I think the… I haven't applied to it yet, but I think the answer is kind of… In that case, we can't declare it stable, because, like, by definition, the project that we have is kind of wrapping Prometheus, in a way, so… so we just have to do what they do.
Or, like, re-implement, like, some… Or re-implement everything, which we're not going to do, for obvious reasons, right?
**David Ashpole (dashpole)** 05:08 I think we just have to accept that we will have to do a V2 when Prometheus does… a, new major version, and that… Or maybe we won't, but probably we will.
**Mikołaj Świątek** 05:21 Oh.
On the other hand, like, the… the… the thing where you have to… set… collector ID is possibly not our… There was a complaint in that issue that I'm not sure if I understand correctly.
**David Ashpole (dashpole)** 05:46 I think it was inaccurate. I… I…
**Mikołaj Świątek** 05:49 I mean, it's… it's… it is true that you have to, like, in order to do the target allocation, your collectors have to have stable IDs of some sort. Otherwise, it just cannot happen, or you're gonna get, like, strange outcomes.
**David Ashpole (dashpole)** 06:06 If you try to do it with unstable IDs.
**Mikołaj Świątek** 06:10 But there is… there is, like, some things that are gonna get… become nicer in the… in the hopefully, hopefully near future.
Right now, we still do a little bit of hacky stuff to make the target allocation work, and it might become nicer now that Prometheus operator also did some things that make it easier for us.
to do it.
Anyway, we actually don't have topics on the list. Does anybody actually want to add a topic?
I'm gonna paste the document in the, in the chat.
Okay, is the managed… who added the managed CRD thing? Is Antoine here?
**Benedikt Bongartz** 07:34 assume that that's him. He's here.
**Mikołaj Świątek** 07:38 Is he in the call, or is he just in the document?
**Benedikt Bongartz** 07:42 And it was me the document. I think he's unfortunately not here.
**Mikołaj Świątek** 07:52 Alright.
This is a little bit… a little bit funny.
**Benedikt Bongartz** 07:59 Yeah, it seems that.
**Mikołaj Świątek** 08:04 Sorry, go ahead.
**Benedikt Bongartz** 08:18 I was hoping that we can make some progress on this, but yeah.
**Mikołaj Świątek** 08:27 So the… The issue I was talking to…
**David Ashpole (dashpole)** 08:33 I'm talking to David about, for the record, is…
**Mikołaj Świątek** 08:40 Here… Yep.
What's going on?
I don't actually need to discuss this, per se, but if I need this for reference for anyone interested.
There are… there are such questions coming up.
Which are a little bit, a little bit relevant to us.
**David Ashpole (dashpole)** 09:15 How close is the target allocator?
custom resource to… the Prometheus.
config. Those two are pretty orthogonal, right?
**Mikołaj Świątek** 09:25 Yes, there isn't anything in there. There are some… There… you can put raw scrape configs in there, but that is untyped in the CRD.
It's untyped in Prometheus itself. I mean, in Prometheus Operator, they don't even let you do that, I think, and they have, like, a… I think there's now a scrape config CRD, but I'm pretty sure that's also untyped.
And… There are some… some settings in there which are, in effect, just kind of proxied into the Prometheus operator CRD, but that's, like, not… that's not really a dependency on Prometheus. It's, like, a dependency on Prometheus… on Prometheus operator.
Oh my.
**David Ashpole (dashpole)** 10:23 Can I ask the general question of, like.
**Mikołaj Świątek** 10:26 Hmm?
**David Ashpole (dashpole)** 10:27 Are people happy with the target allocator?
Are… is it getting used?
**Mikołaj Świątek** 10:36 Whether they are happy, I don't… I don't know. They don't sound very angry in issues they open about this.
Okay, good.
And there are issues opened about it, so it is… it is, in fact, being used.
**PL Pavol Loffay** 10:52 I have a question for you, Nikolai, regarding the touch allocator. We have the TLS feature, like.
**Mikołaj Świątek** 10:59 Yes.
**PL Pavol Loffay** 11:00 enable a TLS.
Do you think we could make it to beta?
**Mikołaj Świątek** 11:06 No.
And the reason is that there's an open issue where people are complaining about their certificates renewing in the wrong order, and I don't understand what's going on.
And if you enable it by default, be aware, you enable it for everyone. Literally everyone who uses Target Allocator is now opted in to that.
Is it correctly?
**PL Pavol Loffay** 11:31 Could you please explain how it works at a higher level? My understanding is that this feature flags enables TLS in the service and port monitors.
And it requires a serv manager, which is confusing to me.
**Mikołaj Świątek** 11:46 No, no, no, no, no, no, no, no, it does not do that at all. It does not do that at all. What it does is it causes the target allocator and the collector to talk over a mutual TLS.
**PL Pavol Loffay** 12:00 So, if I want to use TLS in the series pod monitors, that's… Supported without that feature flag.
**Mikołaj Świątek** 12:08 Yes.
It is.
Wait, wait, is it, is it, or is it not? No, it's not, it's not, but that's like… It's not, because in order to do that with the setup, what you… so that flag allows you to do that, but what it actually does is it enables mutual TLS on the transport, and the reason for that is that we… the way… the only way for this… that we can make this work is by having the target allocator expose the secrets inside of its… In, in the, script config.
Script configs that it sends to the, to the collector.
And so… and if we do that, we can't just expose it on, like, a completely unauthenticated HTTP endpoint. So that's why we have mutual TLS in there.
To make that secure.
**PL Pavol Loffay** 13:02 Could you please rephrase what it actually does?
**Mikołaj Świątek** 13:06 So, starting from the top, okay? So, you want to use things like… It's not just TLS. Like, let's say you want to use some kind of secret to authenticate to a monitoring endpoint you have on your service, okay?
So normally, if you're using Prometheus operator, what you do is you just reference that secret inside of your service monitor.
And what Prometheus Operator is gonna do is it's gonna stick all of those into a secret, mount that secret into the right Prometheus instance, and then that Prometheus can just read those secrets from disk.
while scraping. Okay?
But we can't do that, because the target allocator doesn't scrape anything. The collector scrapes stuff.
And we would have to reload the whole thing inside of those, and just mount secrets, like, across namespace, potentially, and do all sorts of weird stuff.
So, instead, what we do is the target allocator loads it, it loads the secrets, and then it just exposes the secrets on the HTTP endpoint, or scrape configs, for which the collector hits to know which scrape configs it's using, okay?
So the secrets are in that endpoint, in the JSON output of it.
And this works fine.
If you have a question, please.
**PL Pavol Loffay** 14:38 So, essentially, secrets from the series and port monitors are mounted into the target allocator and are exposed as an endpoint.
**Mikołaj Świątek** 14:47 They're not even mounted, it just, like, gets them using the Kubernetes API. Right.
**PL Pavol Loffay** 14:52 But they are there and exposed as an endpoint, so the collector can query them, and this is available only when the feature flag is enabled?
**Mikołaj Świątek** 15:01 Yes. What the feature flag actually does, in terms of implementation.
is it causes the collector and the target allocator to talk over mutual TLS. So the, so the endpoint on which this is exposed is actually encrypted now. It is authenticated.
So, this is safe. So, not every single service on the cluster can just go in there and find out those secrets by just hitting that endpoint.
**PL Pavol Loffay** 15:30 But it essentially works without a feature flag. It's just not secure.
**Mikołaj Świątek** 15:34 Yes.
**PL Pavol Loffay** 15:34 Okay.
**Mikołaj Świątek** 15:35 Yes, you could, you could, in principle, do the same thing with network policies, maybe.
**PL Pavol Loffay** 15:39 Yeah.
**Mikołaj Świątek** 15:40 I think.
But… this is, like… a, more foolproof, I suppose. And the complexity of it is that it uses Cert Manager, and it provisions all sorts of certificates using Cert Manager, and there's, like, a lot of… a lot of additional stuff being done in there, and there's, like, there have been a couple of bugs in there, because there's a bunch of people who have enabled it, because they need it, and they reported a bunch of bugs in it, so I'm not yet, like, confident that it is ready for everyone to use it. Like, for example, I know there's a bug.
where… which I don't understand, I feel like this might even be a bug in Script Manager, or maybe I don't understand how SertManager works, but there's a bug where… We have the same renewal time set on all of our certificates.
And the result of that is that you might… Do something like you renew… like, you renew… because there's a CA certificate there, and you use that CA certificate to create your actual, two certificates from MutualTLS. And if you renew them in the wrong order, you might end up with… with, like, permanently invalid certificates. Like, you end up with certificates, which, for whom the CA certificate, the parent, is actually, Expired. But your two certificates are not expired.
So… so in theory, you're okay, but you're actually not.
**PL Pavol Loffay** 17:18 And that's the third estimation.
**Mikołaj Świątek** 17:22 That's the reason I don't want to enable it yet, by default. It is sup… we will enable it by default, eventually, I think, but… Right now, it's… it's too risky.
maybe it should… maybe it should be a setting, maybe it should be a… like, another feature flag, but rather it should be a setting, but I feel like it should be a feature flag just because… like… the… in Prometheus operator, the… The authentication secrets for service monitors and so on work just transparently, and they should work transparently with the target allocator as well.
Alright, so do we actually want to get… get… get on the lift, because it's… it looks like we have some… some… Do you have anything… by the way, can someone share your screen? Because I am… I am not… not confident enough.
Today.
to do that.
**PL Pavol Loffay** 18:30 What can we…
**Mikołaj Świątek** 18:39 I don't know if there's anything to talk about this CRD, because I've left a bunch of comments in this pull request, and none of them have gotten replies, so… I'm fine waiting until they happen.
Is there anything we, anyone here, would like to specifically discuss?
**Benedikt Bongartz** 18:59 And what's more the signal part on the CRD?
To get your opinions, but if Anthony isn't here, it's, I guess… You can skip it.
**Mikołaj Świątek** 19:12 You mean Antoine?
**Benedikt Bongartz** 19:17 Sorry, my pronunciation is… I just pinged all of you, also on the thread for the signals.
Pavel, your comment is included there, too, as a link. I just didn't want to split the conversation into two threads.
**PL Pavol Loffay** 19:37 Yeah, I think we should move it forward. I just want to make sure that… on the API level, it's done in a way that it will not block us extending it in the future and making it more fine-grained. I like the philosophy of making it, like, very simple from the beginning, but if you want to introduce more knobs to control it, we should be able to do it.
**Benedikt Bongartz** 20:03 Yeah, my point was with the sickness, so currently you can disable metrics or logs, which for me is a bit intransparent, but does it mean I disable logs? Okay, maybe it's lock ingestion, but also system blocks, or is it host? Or… what does it mean?
With metrics, I guess, it becomes even more clear.
can mean everything. Is the target allocator enabled? I don't know. So I need to look this up, and then I don't see really the value of enabling signals, because maybe I would like to enable lock ingestion, but disable host metrics.
And, since this might be… Yeah.
too much effort to discuss this now, I would simply advocate for just Removing it, and we can add something to enable or disable things afterwards.
That was my idea behind it, but I would like to discuss, but… Similar thing with your comments, like, this, exporter fields that are there.
So I would simply go there and remove them for now, and… We can add them afterwards.
**PL Pavol Loffay** 21:23 Okay, but I guess you want to wait for Antoine to have the conversation.
Okay, so let's move.
**Benedikt Bongartz** 21:29 So maybe next time.
**PL Pavol Loffay** 21:30 Second item, then.
**Mikołaj Świątek** 21:35 This is just… yeah, this is just… we already talked about this. This is just for… for your information.
that there is… the main takeaway from this is that there is some, like, conversation going on about trying to somehow stabilize the configuration that, like, Prometheus Receiver inherits from Prometheus.
And that also touches target allocator. We kind of have a similar problem, to an extent.
And I… if you have opinions on this, please, you know…
**David Ashpole (dashpole)** 22:12 So, specifically, this issue is just tracking that there is a target allocator section of the config.
Which is pretty basic. So I think this specific ask is, like.
If you work at all with a target allocator, review that, and make sure that we don't want to make any backwards incompatible changes to it. I think it's pretty simple.
But, it's worth double-checking, and… Like, then we can just close this issue.
**Mikołaj Świątek** 22:37 Okay, I'll have a look tomorrow.
I'm pretty sure the reason there's, like, an HTTP… config embedded in there is that… It's so we can have the ability to… All right, I'm not gonna finish that thought, I'm gonna check later. I remember we added it that way for a reason, but I don't remember offhand.
**PL Pavol Loffay** 23:13 Anything else Oh, the Prometheus conflict?
Okay, then we talked about the target allocator feature flag, and I wanted to briefly talk about the instrumentation V1, or V1, Beta 1.
I think recently we created this milestone to move the instrumentation to the new version. I will have cycles to work on it.
And I would like to think on the priorities, what is important for this project.
I think this… there are kind of two major items that I see right now. First one is that we want to probably change the CR to align more with the… Instrumentation config.
Or SDK config, instrumentation.
Which will, I think.
make it easier for users to use the CRD, because they are already familiar with the instrumentation.
configure.
That was one item, and second was the… you want to probably change the annotation.
To… to a label.
We got a couple of requests for it already.
And… And then what is not clear to me is there is this ongoing effort on the injector.
And I wonder how that could… Kind of change how we do injection with the operator, and whether we should wait for it.
**jea** 25:10 I think we should. I've been working with Antoine and the Dash Zero people on it. It should really, really simplify a lot of the code, and work.
That the operator needs to do around all of the, like, environment variable injection.
Which is really frustrating right now.
So, with the new injector, A lot of the code messiness that we have today just goes away.
And so I think in addition to all the stuff that you have here, we should include an issue for, reimplementing with the injector. I think we can do this all on a separate branch, in, like, a different package.
And I don't think we'll use the, migrating webhook this time. I think that that will be… that was really frustrating last time, and I think we should just avoid it. We also won't be able to use it because of the annotation to label change.
So… .
**Mikołaj Świątek** 26:07 Yeah, and for instrumentations.
**Benedikt Bongartz** 26:14 I was just asking for a reference, because you said the injector from Dash Zero, and… where you work with Antron.
**jea** 26:22 Yeah, I'll send you the link.
**PL Pavol Loffay** 26:29 Is there any known timeline when that… The kind of something we could consume in the operator will be ready.
**jea** 26:36 It… God.
I forget the date. But it shouldn't… it should be within, like, the next few months. Like, we're getting very close.
**PL Pavol Loffay** 26:50 Hmm.
**jea** 26:51 It's like Q1, Q2.
**PL Pavol Loffay** 26:53 26. Yes.
**jea** 26:54 Somewhere around that time, I believe.
**PL Pavol Loffay** 26:56 Here. I think… The question here is whether… We can introduce new… CR version… And it… we will be able to kind of swap the… Logic to the… injector.
Kind of transparently to the user.
So, like, do we need to surface it somewhere on the API that's gonna use the injector?
**jea** 27:32 I don't think so. I think it'll… it's just gonna be a different container, and we won't be the ones publishing that container, which is good. We'll just use the container that's published.
So we won't have to do anything there either.
**PL Pavol Loffay** 27:44 So, could be the plan that we start working on the new CRD version, we change the spec to align with the instrumentation config?
And then, once the injector is ready, we will just kind of change the implementation of how we inject the libraries.
**jea** 28:04 I think that should be fine. I think the only thing is I really… that code is real fraught right now, and doing, like, migration work is gonna be very frustrating.
So I think when we publish it.
We have to have some way to, like, not… tell users to move to it immediately, because I don't want to maintain, Both code paths, if that makes sense.
**PL Pavol Loffay** 28:35 Like, it's sort of, if you want to put it behind the features, like, initially, we would need to maintain both for some time.
Yeah, I guess what I want to avoid is it shouldn't be… if we can avoid it, if it's…
**jea** 28:46 if the CRD is not in the initial package, and someone has to, like, install the package, or install that CRD deliberately, that, I think, would be fine. I just don't want somebody to, like, be like, oh, V1 Beta 1, time to upgrade, and then they do, and then they're just, like, broken.
**PL Pavol Loffay** 29:06 Oh, so you don't want to maintain two instrumentation CR versions at the same time?
**jea** 29:10 But I don't want to maintain two… I don't want to maintain the new internal code path.
for V2, like, for V1 Beta 1, until we can do the injector stuff, basically. So it's okay if we begin on the actual config for what the CRD looks like, but I just don't think we should, like, implement The internal logic necessary for it yet.
**PL Pavol Loffay** 29:32 Yeah, I think my plan… Yeah, it was to work on the spec first, and then see if we could reuse what we have right now, with, like, maybe small shim.
Without the, mutating that… without the webhook, the conversion webhook.
**jea** 29:56 Yeah, we're definitely not gonna do the conversion webhook. I think that… Yeah, David, what's the standard for that? We tried to do a V1 Alpha 2 last time, and then I remember Kubernetes, like, yelled at us for that.
Do you remember that, Mikolai? Do you remember when that happened?
**Mikołaj Świątek** 30:12 No.
I mean, so I think it's fine if to have a conversion webhook, we just shouldn't assume that the… We shouldn't assume that everyone gets to have the conversion webcook enabled.
**David Ashpole (dashpole)** 30:30 Do you really?
Is that done in a webhook? I know for core types, it's all, like… Part of the… like, all the types files and stuff. Do we actually have to run a webhook for custom resources to do this properly?
To converge.
**Mikołaj Świątek** 30:48 To convert, yes.
**David Ashpole (dashpole)** 30:50 Oh man, that stinks.
**Mikołaj Świątek** 30:51 It has to be like this, because this conversion is really just code. It has to land into your operator in some way, right?
The pain of it is not even this, the pain of it is… writing it and actually using it is not really a big problem, it's deploying it. That's the big problem. It's shipping it to users.
via, like, Helm and so on, because that webhook is, like… it's something that your CRD, which is a global resource, has a reference to a service which is namespaced inside of it, and that causes all manner of annoying crap.
When you actually try to have people install it.
**PL Pavol Loffay** 31:40 The customizable namespace of the operator, that's the problem, right?
**Mikołaj Świątek** 31:46 And…
**PL Pavol Loffay** 31:47 presenting skills.
**Mikołaj Świątek** 31:48 there's some other problems in there. I don't recall off the top of my head, I'd have to find it, but we've had, like.
we've fiddled a lot with the help charts to try to make this work reasonably. And in the end, we had to basically tell users, depending on what you want, you have to pick one of these two options, and neither of them are, like, good options, really.
I can find the issue, if… Should give me a moment…
**PL Pavol Loffay** 32:55 Maybe it would be good if we could list these issues, and if they were… like, maybe part of the story is if we already have a solution for it in the Helm chart, it wouldn't be so… bad, maybe, this time, if we already have all the setup for us to handle it.
Well…
**Mikołaj Świątek** 33:26 There's also, for example.
There's also the issue that if you're installing a home chart, and at the same time you're installing… you're creating CRDs, you already have the problem where the operator has to be running, and if, in addition, you're applying something that's a resource that has to be converted in order to work, that also becomes a problem. So, in terms of, like, having a reasonable migration, it's much easier to have the reasonable migration by just supporting both versions and internally converting them into some representation that you then act on.
Let me… let me… I'll… I'll add some… I can… CRDs aren't guaranteed by Helm, or rather, there's also the problem that, you know, Helm doesn't actually update CRDs, depending on how you ship them, and you get into all sorts of… on the problems.
Because…
**PL Pavol Loffay** 34:31 That's a different issue, right? It's optical rule to be a conversion.look.
But okay, I think we are on sync, and we can start looking into the new version, and how the spec sheet looks like.
I think that's important now, and as we… As we go, we will then… Decide on the, on the, the book.
Yeah, shall we go to the next item?
Yeah, that's what we talked about. Okay.
So I can, I can remove it.
Sick.
**Mikołaj Świątek** 35:49 Well, I guess the question is, again, to what extent do we want to embed this?
Configuration format in the instrumentation resource.
Is this… is the… is the format actually stable, David? Do you know? Is it, like, properly… properly, you know…
**David Ashpole (dashpole)** 36:06 It's been released candidate for a few months now, and it's being driven by Jack, but… the… it's… to me, it's very unlikely to change. I think the more interesting question, maybe, is, like, how we deal with experimental fields.
So there are some things that are part of the… Declarative config that are marked experimental.
And they have, like, experimental in the name or something.
So… Yeah, con… it's unclear to me if, like, we should have a… eventually a V1 that has all the fields, and a V1 beta one, or sorry, a V1 that only has stable fields, and then a V1 beta one that has the rest.
And the other question is, how do we deal with Some of the extensibility points, like… Presumably, we can't list all of the exporters, so we'll have to make that be a little bit more opaque.
Whereas, like, we can definitely validate that the sampler you know… Whatever is all correct.
**Mikołaj Świątek** 37:10 We could do something where we only… where we don't use the, where we don't list the experimental fields at all, and just have, like, an additional field where you can… which is untyped, and where you can specify, like, an overlay.
Over your, over your configuration, where you can add whatever, whatever you want.
**David Ashpole (dashpole)** 37:31 Cut.
**Mikołaj Świątek** 37:32 Or, if you want to add… or if you want to add experimental fields, we can have two fields, one structured field, and one untyped field, and you can use one of those, but not both at once. And then you can do whatever you want. But you accept responsibility for using the experimental fields on your own, then.
**David Ashpole (dashpole)** 37:49 I actually… One other thought about this is I actually think us trying to use this spec in a Kubernetes resource would be excellent feedback.
For the declarative config group.
If I remember correctly, some of the, like, lists don't have named elements or things like that, which is gonna make our life a little bit harder.
So we might be able to make changes as well if there are things we find that, could make the Kubernetes experience better.
But it's in Release Canada, and I actually think that's a good thing, from our perspective.
**Mikołaj Świątek** 38:30 The other question is… If we're going to make this our primary method of configuring instrumentations.
Do all of them actually support it, even if under, like, some environment variable?
are optionally.
**David Ashpole (dashpole)** 38:49 No. I think the… the… But I think they will.
I think when I opened the issue, obviously declarative config was still quite a ways away.
And I had mostly looked at the existing instrumentation config and found that It had a lot of the same stuff in it.
as the declarative config does, like sampling rates and… but, like.
You know, a different structure, different keys and values.
**Mikołaj Świątek** 39:23 And so, my ask originally was more that…
**David Ashpole (dashpole)** 39:26 Like, we try and… Across hotel, try and use the same, like… like, we should hopefully only need one YAML structure for saying what an SDK can do. And my hope was that, like, it would also maybe make the… burden on… the operator maintainers slightly easier if you didn't… if you were just a pass-through mechanism for something that the SDKs already know how to support.
**Mikołaj Świątek** 39:57 Yes, it would, it would, but they also have to actually support it for us to be able to be a pass-through mechanism, and if they're like, some support it and others don't, or some support some bits and others support other bits, then our role as pass-through becomes more complex than it is right now.
Unfortunately.
**David Ashpole (dashpole)** 40:15 Right, so, like, the behavior I would expect right now is that you take the declarative config.
And for fields that have a good representation in environment variables, that you let That you basically use those for now.
You could even consider only implementing a subset of declarative config to begin with, with fields that map to environment variables if you wanted. I think those are all, like, viable.
Approaches, if you don't want to make your lives hard in the short term.
**Mikołaj Świątek** 40:48 Well, implementing as the subset that we can guarantee that all of our supported instrumentations actually support.
is… I think… the least user-confusing way. Like, the… I think that's, like, an optimal… optimal path between… not confusing to users, and also, like, reasonable for us to actually maintain.
Because, you know, we could add… and we could do something again, and the more I think about this, if we want this… if we want to make this, like, a condition of releasing the beta.
then this is, I think, something that we will have to do. We will have to have two configurate… methods of defining configurations. One is going to be the structured one, one's going to be the arbitrary one, where… if someone actually wants us to just… wants to just say, I want to pass this config into this instrumentation, and just use it as it is verbatim, you know, you don't have to do anything else, then… then I think we should support that use case. Like, then users are not going to be blocked by what we've put in there, or, like, what is common between all the instrumentations that we have, they're going to be able to just do whatever they want.
Maybe it's gonna be more work for them, but if they want to use experimental features, right, then… And they're probably okay with that.
I hope.
And other than that, yeah, like, just… it's starting to… even if it's just a subset of what… of the current config, just having, like, the fields being named consistently, and the structure being consistent, I think is already gonna be a win.
**David Ashpole (dashpole)** 42:34 Yep, I agree.
**Mikołaj Świątek** 42:39 Anyone else? Like, you… I keep talking, but I'm not actually the person who contributes most to instrumentation, so… Anyone else?
**jea** 42:49 I think tomorrow.
**Mikołaj Świątek** 42:50 opinions?
**jea** 42:50 I think as long as we can, do… well, yeah, David, what are the, like, stability guarantees for any braking changes? Like, will they… at this point, are they going to… Modify something that would, like.
break the structure of something, or, like, remove a field that we can't serialize into, or whatever. That's really the main concern, right?
**David Ashpole (dashpole)** 43:14 In the release candidate phase, like, yeah, if they decide, like.
If they decide, like, for example, they don't want to do integer… Milliseconds, or whatever they do, for export intervals, and instead want to do, like.
you know, more duration-y looking thing. Like, they could make changes that break the structure today. And in fact, like.
my hope is that this group even has some feedback for them to make it better, right? But, but that… assuming it goes stable as it is.
They won't break anything that doesn't have an explicit experimental tag on it.
I guess there's maybe an assumption that, like, this only applies to like, the current spec, and if OpenTelemetry were ever to do a V2, then… You know, that the declarative config would change as well.
**jea** 44:09 But so what would be our… the best way for us to consume it, then? Like, do we just take their ghost truck and go off of that? Like, that feels potentially fraught, right?
**David Ashpole (dashpole)** 44:18 They, it's a… JS, or no, OpenAPI V3 schema?
I think?
**jea** 44:28 So, we would just generate from that, then?
**David Ashpole (dashpole)** 44:32 That's a good question. I, I haven't… I haven't thought that far. Okay.
**jea** 44:37 Yeah, I guess I just want to know what the… what the integration path looks like, so that we can… like, the thing that we don't do right now, because of this type of issue, is, like, we can't embed the Prometheus configuration entirely because of the way that they do, like… deserial… custom deserialization, for example. I mean, you know that well, right?
And… I don't want to get into a scenario where they then need to do a bunch of, you know.
random… Tricks?
That we then need to, like, support, which would be very frustrating.
**David Ashpole (dashpole)** 45:14 I… I… I would very much like for the instrumentation resource to be, like, a first-class consumer of whatever artifacts the declarative config group publishes, so…
**jea** 45:26 Got it.
**David Ashpole (dashpole)** 45:28 I agree, but I don't know the answers to your questions.
**jea** 45:32 Okay, that's fine.
**Mikołaj Świątek** 45:34 Right, so… The… the way we define a CRD is via GoStocks.
Right? So, in principle.
If we just wanted to consume it, then, like, generating… generating something, a ghost truck out of a JSON schema, I think, is a pretty solved problem. Kubernetes does that.
Right?
Or maybe the other way, but it's definitely, it's definitely doable. The only question is, like.
If we want it to be a subset, is there, like, some reasonable way to control what we get?
out of it, because it would be nice to be able to say something like, okay, so from this, you know, from this schema, we would like to take the following keys and turn that into a ghost track for ourselves, but I don't know if that's not gonna turn into some kind of huge mess.
In practice.
**David Ashpole (dashpole)** 46:36 I don't know. Unfortunately, I have to drop as well, but it's been a really, I'm happy to see this getting some traction.
**jea** 46:45 Cool.
So yeah, it sounds like we have to wait a little bit on this… like, it sounds like there are a few things in the fire before we can maybe begin to do this, and it might be something that we should pick up in… like, we can start to do some of the work now, but I don't think we can, like, push a bunch of stuff today.
Is what it sounds like.
**Mikołaj Świątek** 47:07 Mmm… the label annotation thing might be backportable?
**jea** 47:12 That we can do… well, but that is a much, like… I guess if we're gonna ask a bunch of people to change a lot of different config things, We should have them do it all at once, is, like, my…
**Mikołaj Świątek** 47:26 No, no, I mean, like, in a… perhaps in a backwards compatible way, what I mean by that is, like, the reason we want to do the label is that primarily it's because it's more performant, right?
Right now, it's the annotation, we have to… our mutating podcock has to look at every single pod in the cluster and check if the annotation is there, and only then can we proceed. We can just start supporting the label and the annotation for V1 Alpha1, and just check for both.
And do nothing else.
And that's, like, gonna be behavior that's… that will just exist as is, for… for people to be able to use either one.
And then, when we move to V1 Beta 1, it's gonna be, like, a question of… Or maybe we should consider the, like, the migration path for this right now. Like, I feel like the annotation-to-label kind of migration I, I guess, I guess doing it in V1 Beta 1, it's gonna be, like… No, it's not gonna be.
So the plan is basically to not do a migration and just help people change what you're doing for ViewView and Beta 1, right?
**PL Pavol Loffay** 48:43 Yep.
**Mikołaj Świątek** 48:43 Verbatim.
We could try and migrate this.
**PL Pavol Loffay** 48:50 I think it depends, as I mentioned, with the webhook, with the conversion webhook. We should revisit the issues, and we… if we already solved them.
For the collector, then… then I think we should consider doing the conversion if it's gonna simplify users' migration.
**Mikołaj Świątek** 49:09 It's not gonna simplify it in this respect, because, like, the conversion webcook can convert the CRD for you, so what it does is it, like, covers for struct changes in the structure. Like, for… with Collector, the important part was that the configuration changed from, like, a blob into a structured field. That was the main thing.
But here, the migration is actually not in… not in the… it's not in the CRD, the migration is in the referenced resources. It's on the pods that you're tagging to be instrumented. So, it doesn't actually help you or anything. It might be… it might… it might help. The way it might help is that.
**PL Pavol Loffay** 49:54 It might help conversion. If we keep around the annotation, then the new… CRD will probably work seamlessly with the annotation as well.
**Mikołaj Świątek** 50:07 But we don't want to keep the annotation around, like, that's the thing. We don't want to keep it around for the new one.
**PL Pavol Loffay** 50:14 But we want to support both for some time.
Then, we would have to…
**Mikołaj Świątek** 50:21 Do we want to support both for some time? I thought the idea was, like, it was exactly to… to not do it.
I… I would like to support… I would even like to support both for V1 and Alpha 1.
Right now, if it's possible. And I think if you want to start working on this, I think that's, like, something to, like, think about. I don't know if, like, the code is gonna be really… it's gonna be a lot of code, but we have to kind of carefully think about what it means and how, because To give you a simple… simple proposal, right? We have a mutating webhook, right?
We can just add that label ourselves.
To any pod that we get, which has the annotation, we can just add the label.
If we want to.
**Benedikt Bongartz** 51:07 Such as…
**Mikołaj Świątek** 51:08 It was… yeah.
**Benedikt Bongartz** 51:09 We could technically then go and say we support this selected by labels, and if you set the annotation, we just set the label for you.
**Mikołaj Świątek** 51:19 Yes.
**Benedikt Bongartz** 51:19 strategic.
**Mikołaj Świątek** 51:20 That will actually not make us any more efficient right now, but it will… it will have the effect that, like, every pod is actually gonna have the label.
Which is gonna make it easier for people to migrate to, to view on Beta 1, but I don't know if this is actually a good idea, for the record. This is something that I just kind of… Came up with right now.
So, like, trying to figure out how to do this migration exactly is, I think, one of the most worthwhile things.
**PL Pavol Loffay** 51:56 Yeah, I think… I think we need to plan what… how it's gonna actually be executed, and how users will migrate, and have it in a bit more details.
**Mikołaj Świątek** 52:06 I think we should, as well…
**PL Pavol Loffay** 52:08 Look at this.
Struct and see how it could be… implemented in the CRD, if there are any issues.
And then give them feedback.
**Mikołaj Świątek** 52:28 Yeah, that sounds… sounds pretty good to me. We also have one thing that is… remains unsolved, which is the, the HTTP.
Semantic convention breaking changes?
It would be really nice to, to actually use the… It's just instrumentation by default.
Right.
**PL Pavol Loffay** 52:51 Maybe as well, like, think about… A way, how we want version.
instrumentations.
So do we want to… Do we want to introduce some concept into the CR, where people could kind of choose the semantic conversion version?
Or we want to… say that with this API version of Instrumentation CR, you get specific semantic conventions.
**Mikołaj Świątek** 53:28 I don't think that's, like, possible for us to do, because that will, like, bind us, our versioning, into whatever semantic conventions we're doing, and that will just be… even this… this one change is a huge problem for us. Imagine if you had that one for, like, every… every month, or every two months. It would be like a massacre.
So, to me, I am… I am fine making breaking changes, for the record. The main problem I have with the instrumentation is that it's a braking change that is not immediately visible, and it's difficult to back out of it. So what happens is that you have some instrumented applications, they send you a kind of data, you update the operator.
And then, sometime after, maybe, some of your pods are gonna get cycled, you're gonna get a new instrumentation version, and that will suddenly break. And that is, like, a very bad, bad experience.
Because you don't actually see the breakage immediately. And it's not clear what happened and how to revert out of it immediately.
So my thought… Which I should actually write down in that issue that I… and I keep putting it off.
My thought was basically this.
Set certain versions as non-upgradable.
Because we already upgrade instrumentation versions and collector versions and so on, right? So, certain versions are not upgradable from. If you're using that version, we're gonna keep you at that version, and if you… whenever you do any kind of change to that resource, we're gonna display a wording saying.
Hey, you're on a version that we won't upgrade because of X, look at this issue to understand more. But for newly created resources, we're gonna set the newest one.
Guys, the point is literally just so… so, like, we don't break the existing instrumentation.
**PL Pavol Loffay** 55:20 I see.
**Mikołaj Świątek** 55:21 A very nasty way.
**PL Pavol Loffay** 55:22 Would it make sense to expose this?
version in the CR.
So I can… Have it under control explicitly.
**Mikołaj Świątek** 55:35 I mean, it's already… it's already exposed, you can set whatever image you want, and misunderstand it.
**PL Pavol Loffay** 55:40 I want to… yeah, but I was thinking about…
**Mikołaj Świątek** 55:48 And… Am I the only person who can hear Paul anymore?
**Benedikt Bongartz** 55:51 No, the sound was gone. Maybe say something again?
**PL Pavol Loffay** 55:56 Can you hear me?
**Benedikt Bongartz** 55:57 Yes, another one.
**jea** 55:58 Yes.
**Mikołaj Świątek** 55:58 Now, but not the past few sentences.
**jea** 56:02 I do have to run, unfortunately, I gotta go.
Two other things, but… Sure.
**PL Pavol Loffay** 56:10 It's interesting. Let's book issue, Mikolai, for this, and… And continuing there.
**Mikołaj Świątek** 56:19 I was planning to post it on there, because… We have an issue for… specifically for the semantic convention, and I'm gonna post that there first, and then tag you, and then we can move it to a separate issue.
**PL Pavol Loffay** 56:31 you may be… Move it into the… milestone for DB1 Beta 1?
I think it's something we should kind of fundamentally solve, like, how we want to handle these changes in the new… Version…
**Mikołaj Świątek** 56:47 I mean, we… we can solve it right now. Like, this isn't… it doesn't have any… it doesn't have to require a new CRD.
Like, this is… we… we aren't really promising any… like, the way we upgrade stuff is not part of, like, our API. It's not a breaking change to change how upgrade works. Upgrades work.
So… we can change it right now. But I agree that we should, like, figure out what we want to do about this, because we're gonna keep having these kinds of problems, and… We are in the… again, we are in the unfortunate position that we have decided that we set default instrumentation versions, which is a good user experience, right?
Yeah, see us here, Jacob.
But also, instrumentations do braking changes, and we have no control over this, and we have, like, no way to indicate anything. Because, at least if you have, like, a collector.
usually, if there's a braking change, the collector won't start, or something obvious is gonna happen about this, but instrumentations are even worse because of what I described, so we have to be particularly careful about what we do.
And I think the best way to do it is to just, like, Hmm… Like, put it in users' faces, that they're on a version that we are not gonna upgrade manually, because that version contains some, like, major disruptive change that they have to actually deal with.
And I think that's, like, that's the best we can really do.
**PL Pavol Loffay** 58:29 Correct.
**Mikołaj Świątek** 58:30 I will open, I will open, yeah, I will open an issue and tag you, and we can try talking about this.
**PL Pavol Loffay** 58:38 Thank you, Kevin.
See you.
**Mikołaj Świątek** 58:41 do.
Let's see…
