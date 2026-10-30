SIG: System Sem Conv Stability SIG
Date: 2026-10-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens (Datadog)** 00:39 Hello?
Thought you were on vacation, Braydon.
Was it just… yesterday?
Can…
**Alex Boten** 01:54 He might not be hearing you.
**Pablo Baeyens (Datadog)** 01:56 Yeah.
**Alex Boten** 01:58 I think he just realized he's not hearing us.
**Braydon Kains (Google LLC)** 02:00 Sorry, I forgot that when my headphones were unplugged, it's a different audio setting on this laptop.
So I was muted, sorry. What was that?
**Pablo Baeyens (Datadog)** 02:10 No, I said I thought you were on vacation, was it just, like, yesterday or something?
**Braydon Kains (Google LLC)** 02:15 It was just yesterday, yeah, yesterday was my wife's birthday, so I took the day off.
**Pablo Baeyens (Datadog)** 02:19 Oh, thank you.
Nice.
**Braydon Kains (Google LLC)** 02:34 I know Christos is missing today, I don't know if that also means, donald will be missing today.
**Alex Boten** 02:57 Guess we have one item.
The agenda, we can… Start with it.
**Igor Peschinskii** 03:04 Yes, I wanted to discuss my issue in the collector country.
We have the definition of the hostage, the definition, and Recently, we discussed with Pablo that we have, like, two ways to implement it in the search detector processing.
We basically have all the building blocks, like, all the detectors.
And I recently updated the Kubernetes API detector to detect host ID of the node.
So… The… There is an ability for users to configure resource detection processors that way for the text host ID.
Conformed to semantic conventions definition.
But… And we probably need to document it in the README.
And because… It requires some, like, conditional… Settings for the detectors, and… The second thing is weep.
Probably need to change the default detection behavior.
So, it detects the host.id attribute when no other detectors are specified. But… There… there are probably, like.
problems we need to solve before we can do it. I described it in, indonesia.
So I just wanted to… like, hear your thoughts, maybe, I think, maybe now.
**Alex Boten** 04:48 Do you have any more details on the problems to solve? Like, number one, the one about the default behavior of some detectors not conforming to it?
**Igor Peschinskii** 04:57 Some detectors, by default, are not… Detecting the host.id attribute.
So, some detectors need some configuration.
like, it… it can be used out of the box. So… We either need to reconsider the defaults of the detectors, Or… Find another way, maybe, like, pre-configure it somehow in the default detector.
**Alex Boten** 05:37 Yeah, I mean, I… Seems to make sense to me that they would all have the same default.
And I guess default on probably makes more sense from an end-user perspective.
At least, that's my thoughts on it.
**Braydon Kains (Google LLC)** 05:54 The only thing I would be… wary of… I mean, I don't know if this actually applies to many backends, but, like, technically under the OTLP spec, adding a new resource attribute, I think, identifies a new resource?
But I don't know if any… Backends actually care that deeply.
About that particular… behavior.
**Pablo Baeyens (Datadog)** 06:22 Is there a particular environment where you wouldn't want to have the host detected as a resource?
**Braydon Kains (Google LLC)** 06:31 Maybe not that we don't want it detected as a resource, but just that, like, people who have Existing long-running telemetry jobs with certain resources known would then, like, the shape of it would change, because there's a new attribute?
This might not actually be a… a real… a real big deal. That might actually be fine.
I know for Google, we wouldn't care. If there was a new attribute suddenly produced by resource detectors, and people started sending us with that attribute, it wouldn't matter, because we don't actually do any mapping to our, like, proprietary schematized thing with host.id right now, so it would just kind of get tossed away. So, doesn't matter for us.
I don't know about other backends.
I feel like it's probably okay, though, like, the… if… if all of these resource detectors detected host.id.
And we'd still need to tell them to configure it in the right order, right? Like, we'd still need to tell them to configure it in the same order as the semantic conventions say, where it's like, if you're a… If you're on a service, then you want the services, host ID, Or down to Kate's API, or down to… Etsy machine ID if you can't find anything else. I think that we had a priority order, and we still need to tell people to put the detectors in the right order, right? I don't see.
**Pablo Baeyens (Datadog)** 07:55 We…
**Braydon Kains (Google LLC)** 07:56 Issue.
**Pablo Baeyens (Datadog)** 07:57 We talk about that, Igor and I, and… I mean, my preference would be that we change the… Sort of default list of detectors, so that they… Are listed in the order that appears on the spec.
And that way, like, the… if you don't set anything, then you get what the spec says. If you want to customize it, you get, something different.
**Braydon Kains (Google LLC)** 08:28 So we would… we would still… even the EKS, EC2, Azure, GCP, like, we would set all of those?
**Pablo Baeyens (Datadog)** 08:38 Yeah, there's some… Work to be done there, probably, to avoid, like.
Things taking a long time, because you have to wait to… timeout on a request to an IP that doesn't exist on the cloud provider that you're on.
Yeah. But, if that's a solver problem, yeah, I don't… B, why not?
You can always disable it.
And most existing users would have set up explicit lists of detectors, like… I think most people are not… Using the default settings there.
**Dmitrii Anoshin (Splunk Inc.)** 09:20 Yeah, and I remember some of the detectors not, don't have consistent behavior. Some of them fail fast, others would… would be stuck.
That's just what I'm… what I recall.
We need to make them.
consistently, need to make the consistent behavior for all of them. And I, in general, like the idea, just… I'm gonna say that. I think that's the right way to go.
**Braydon Kains (Google LLC)** 10:01 I guess I can get behind it, because… Ideally, if people were building their own distributions, too, they could, like, disable the resource detectors they don't want entirely, also.
So… I guess I'm… and if… and we can also tell people… to… Configure a specific list.
So, yeah, I guess I'm okay with it.
With option 2.
**Igor Peschinskii** 10:32 Okay, cool.
**Braydon Kains (Google LLC)** 10:35 I'll comment the same.
The issue, so that it's… there's a record of it.
**Igor Peschinskii** 10:41 Thanks.
I will probably start with option A, option 1, because it's, like… I used to doing that.
**Braydon Kains (Google LLC)** 10:49 Yeah, just because it won't require any changes, like, at least we can start that way, and then move towards… Making the defaults easier.
**Pablo Baeyens (Datadog)** 11:02 Yeah, I guess ultimately we need David and Pablo to… Agree as well, go ahead.
I think our opinion, as I say, carries some weight.
**Dmitrii Anoshin (Splunk Inc.)** 11:35 Let's also capture everything we discussed as follow-ups, I guess.
Like, default order, and ensuring the consistent behavior of detectors.
Sounds good.
**Braydon Kains (Google LLC)** 12:07 The current way the resource detection processor works… It… it… actually does run the detectors linearly, right? Like.
Runs the first one, and then the first one finishes, and then it runs the second one?
**Dmitrii Anoshin (Splunk Inc.)** 12:22 Yeah, that's what I remember, yes.
**Braydon Kains (Google LLC)** 12:25 Okay.
**Dmitrii Anoshin (Splunk Inc.)** 12:28 But it's only at the start, so… There is no detection on the hot path, yeah.
**Pablo Baeyens (Datadog)** 12:36 Yeah, like, the… the only issue there… so on the data exporter, we have some logic to detect host names, and… The issue that we've seen sometimes is that it… If your environment is weird enough, it takes too long for the component to initialize, and… dot… Trips the, like, startup probe.
I think that's soluble, but yeah, it's something to be… A roof.
**Braydon Kains (Google LLC)** 13:09 Well, I was wondering if we were going to introduce something like this, where, like, we're gonna… we would start to introduce a list of default detectors where we know for a fact that at least 3 of them will fail, like, because you can't run on Azure, AWS, and GCP at the same time.
if we… Actually, like, ran all the detectors as a weight group, and then actually selected the.
**Pablo Baeyens (Datadog)** 13:31 Yo.
**Braydon Kains (Google LLC)** 13:32 I was, like, priority order out of them after they were done, but at least… Like, they would all run their initialization at the same time?
**Pablo Baeyens (Datadog)** 13:40 Yeah, yeah, that's what we do on… on the data exporter, and it works well for us, so I think we could do it here.
Basically, we… I think that it depends a bit on what… how you run things, but for something like our case, where you just have the host name, you can run them in parallel, and whenever The first one in order… does an error out, you use that value. I think here is going to be a bit more… involved on that, but… something like that.
**Braydon Kains (Google LLC)** 14:16 The way I was thinking of it was, you run… you run all of them, and wait… I mean, either success or failure, you wait for them all to resolve all… like, all of their resource attributes, and then you select… Like, the first one that gives you host ID, that's your canonical value.
Even though the rest of them did successfully resolve a host ID, you'd only take the first one you see.
**Pablo Baeyens (Datadog)** 14:39 Right, yep.
**Braydon Kains (Google LLC)** 14:40 Yep.
I think if there's nothing else on this one, then we can… Well, there's no other agenda items, I guess.
I'll comment on the issue.
I'm… And… I guess the only other thing is that… Lyudmila reached out to us in our SIG channel, on Slack, and… Asked if we were okay to… merge the… the system attributes… PR to RC to make it into the next SemCom release?
And… I think… we are pretty much okay with that. The only relevant, like, change happening right now is we are… Making some fixes to our memory usage metric.
Based on discussions that Roger and I had, and that's going to involve the removal of Some attributes from memory.usage.
In favor of just two, that will always sum to a proper Value, like, a reasonable value.
And then introducing new metrics for all the attributes we're removing.
But I think we can merge this going… This… our CEPR without impacting that other work. So that's my understanding. So I think we're okay to merge this and get it into the… KubeCon Sem Conv release.
**Pablo Baeyens (Datadog)** 17:24 Cool, I guess we just have to wait for… Let me know.
**Braydon Kains (Google LLC)** 17:31 I think we responded to her in Slack, right? Saying it was okay. Oh yeah. Yeah, Donald did that this morning.
**Pablo Baeyens (Datadog)** 17:37 Yep.
Yeah, and Alex, yes, pink her as well.
**Braydon Kains (Google LLC)** 17:45 Okay, cool.
Well, that'll be a nice little thing to mention at KubeCon, then.
Maybe.
for KubeCon itself, I think not… many of us from the system say are gonna be there. I think me and… me and Roger are doing a talk, obviously, so we're gonna be there.
And I think Christos is gonna be there.
**Dmitrii Anoshin (Splunk Inc.)** 18:14 I'll be there as well.
**Braydon Kains (Google LLC)** 18:15 That's it.
Oh, oh, Dmitrii's there, okay, okay. So, we could potentially meet up, but I just saw that the SIG Meeting calendar opened up a couple days ago.
Last couple times we did… we did a meeting… We didn't have any, like.
people outside the group join us, so I don't know if it's… necessarily worth booking something on the SIG calendar, because the last few times, we didn't get, like, public interest.
We still could.
**Dmitrii Anoshin (Splunk Inc.)** 18:50 There is an official way to… book it, I guess, why not? Maybe some of us.
**Braydon Kains (Google LLC)** 18:55 Yeah, there is one.
It's… it's no observatory again, it's… but it… but we actually have a booth at the Project Pavilion all three days this time.
**Dmitrii Anoshin (Splunk Inc.)** 19:05 Hmm.
**Braydon Kains (Google LLC)** 19:06 And we're doing SIG Meetings in, like, the tables near the project pavilion again, I think, like, like in EU.
**Dmitrii Anoshin (Splunk Inc.)** 19:13 Nice.
**Pablo Baeyens (Datadog)** 19:14 Yeah, we talked with, Lindsay from the CNCF to see if we could get something a bit more… I don't know.
comfortable to have SIG Meetings, but that seems tough. She did say that, There's the maintainer's meeting room, I tried to go there on that last Kipkoni U, and it was locked, the door, but she said, like, we can ping her on Slack if we run into trouble with that, or we want to book it for a particular time. So, yeah, I can send you her name.
**Braydon Kains (Google LLC)** 19:52 Sure, yeah, that'd be good, because I also need to book one for the network group.
**Dmitrii Anoshin (Splunk Inc.)** 20:02 Network got its own SIG.
**Braydon Kains (Google LLC)** 20:04 Yep.
**Dmitrii Anoshin (Splunk Inc.)** 20:06 Nice.
**Braydon Kains (Google LLC)** 20:11 They're doing, they're doing some Semcom stuff and some collector stuff there. They're taking over the SNMP receiver… And I think they're doing some OB stuff, too.
**Dmitrii Anoshin (Splunk Inc.)** 20:22 Nice.
We have a GitHub repo called OpenTelemetry Network.
**Braydon Kains (Google LLC)** 20:29 Yeah, we talked about that, and that we want, we want to get rid of it, because it's super old and has been supplanted by new EBPF…
**Alex Boten** 20:40 I got… I got archived.
**Dmitrii Anoshin (Splunk Inc.)** 20:42 Oh, okay. Okay, cool.
**Alex Boten** 20:44 Yep.
**Braydon Kains (Google LLC)** 20:47 That was probably because, I think there was some confusion, there was some… there was some, like, security vulnerns that needed to be merged, and so we pinged the hotel network group, but none of us knew what that repo was, because… We kind of just, like, took over the same name, but we're a different set of people.
Is there anything else to discuss today?
Alright, we can call it early.
Thanks, everyone.
**Pablo Baeyens (Datadog)** 21:29 To you.
