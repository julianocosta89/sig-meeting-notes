SIG: Prometheus WG
Date: 2026-09-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

krajo (Grafana Labs) 00:00:22 Hey, dude.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:00:24 Hello, krajo.
krajo (Grafana Labs) 00:00:26 Hey, Dad.
Oh, where are you?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:00:29 Yes, I'm, I'm sitting in Berlin until tomorrow.
krajo (Grafana Labs) 00:00:35 Oh, yeah, yeah, I saw that, actually.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:00:36 I… I'm in, the… in a co-working… co-working space?
So we, we had, like, a Grafanaista lunch today, which was very nice.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:01:20 It's a Grafana fest.
Hey!
Kyle Eckhart (Raintank, Inc. – Grafana Labs) 00:01:28 Glad to be here.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:01:31 Same.
Arthur Sens 00:01:36 Yeah, Prometheus Sig is usually David Ashpole and Grafana.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:01:44 Bless David Ashpole.
Arthur Sens 00:01:52 I mean, we're waiting on him.
To… So, oh, there we go. Hello.
Sorry, I'm repeating.
David Ashpole (Google LLC) 00:02:18 I just saw Jack's comment.
Arthur Sens 00:02:23 Which comment? I think I missed.
David Ashpole (Google LLC) 00:02:30 Just, just on my… Current stance.
Okay, cool.
Alright, how do we want to run this?
Arthur Sens 00:03:15 Hmm… Somebody… With the dock open, maybe we can, very quickly review the options, and then we talk about the… the small conversation we had last week, Jack?
And others.
David Ashpole (Google LLC) 00:03:34 Yeah, I'd be happy to… To hear what… I'm very interested in what was discussed in the conversation, because obviously I wasn't there.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:03:45 Yeah, so we had a… we had a Grafana offsite.
Last week, and you know, a bunch of us were there in person, and we just took the opportunity to get together and try to, like, hash out this conversation, and try to at least maybe reach a consensus amongst us, or at least further our own understanding.
And, I'm sort of like the odd man out in the group, because I don't understand Prometheus, Nearly as much as the rest of the folks on this call, but I do have an interest in Prometheus stabilizing. It's been a thorn in the side of SDKs, it's been a thorn in the side of declarative config, and it's getting in the way of the collector, the collector's adoption of declarative config, and, you know, in some ways, the collector's stabilization, because those things are all sort of, like, intertwined in some ways, so… That's… that's sort of my business here. And… I don't know what to add besides what I sort of wrote down in the consensus section. You know, after talking with, you know, Arve and Cryo and Arthur a lot, you know.
I came to the conclusion that the most important thing to protect is that there is There is a join, there's a job and instance that can be reliably joined on to access all of the resource information and all of the, you know, the Prometheus job, Prometheus instance information that you might want to access in queries. And, I tried to sort of boil down the difference between option B and C, there's… there's a ton of text in the comparison document. I think it's… I think it's overwhelming.
And, and, you know, so, like, for me, what I was trying to do is, like, can we boil this down to some, like, more simple trade-offs that are easier to, like, wrap, you know, your head around? And I know that the detail matters, but, like, also, the big picture matters, because we're gonna have to communicate this to end users.
And end users aren't gonna, like, read 10,000 words on the subject.
Right? So, you know, whatever we agree on, even if it's from, like, top down, like, you know, from simple principles going down to details, or the other way around, starting with the details and getting back to, like, simple principles, like, the thing we have to communicate outwardly is the simple principles behind the thing.
And I sort of, in my head, the difference between B and C, was… And, like, I think, like, the place I landed on was a modification of C, but, like, it was a difference between, like, better compatibility, better backwards compatibility for OTLP Push and Prometheus. That's what… that's what C offers.
And…
David Ashpole (Google LLC) 00:06:45 identical, actually.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:06:46 Yeah, identical.
David Ashpole (Google LLC) 00:06:48 Well, nobody is pushing… Prometheus.job from their application today. Like, so that's… I don't think that's a real scenario. They're identical from a… OTLP instrumented thing pushes to Prometheus perspective. There's only… there's this very complicated set of hoops you have to go through before B and C actually have any meaningful difference.
More or less, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:16 I guess, I guess the behavior that I'm talking about compatibility on is, like, if we go with option C, then if you're, you know, pushing OTLP to a Prometheus server, that your queries, in terms of what values are in job and instance, are as close as possible as they are today. So it's sort of like protecting that use case in the option C path.
David Ashpole (Google LLC) 00:07:44 What would be… it would be… Sorry, hold on, actually, I'll let you finish. I won't keep interrupting.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:49 And then on the option B path, it's, it's protecting the backwards compatibility of Of, like, you know, the… Prometheus collector scraper to an OTLP internal representation to Prometheus, you know, either remote right or Prometheus scrape again on the other side. So, like, you know, the… you know, it's protecting the backwards compatibility of the job and instance that you would see in your queries if you're using that path.
So, like, that's sort of the trade-off. Are you directly pushing via OTLP to Prometheus? And if so, do you want to protect, you know, the job and instance that you see in your queries today? Or, you know, are you using the collector to scrape?
And then, you know, the OTLP internal representation, and then, you know, Prometheus remote right on the other side, and do you protect that Prometheus job and instance?
I, I don't feel strongly about B versus C. I, I, like, I would like… I, like, lean towards C, but it's, like, not, like, a strong lean.
And, you know, I think both do a good job at this one invariant that I was proposing before, which is, like, there is a job and instance ID that you can join against. I think that's the most important thing for me, and, you know, the other things don't really matter as much.
David Ashpole (Google LLC) 00:09:06 Yep, and I agree. And I think all the options on the table, even option D, which is do nothing.
give you a reasonable join key. I don't think there's any… like, difference between them. There are cases today, obviously, where you don't have job and instance or service name, service instance ID.
And that's the case that, like, maybe the hash-based approach could improve on. But I think for things that are coming from, like, standard OpenTelemetry instrumented apps or Prometheus scraped endpoints, like, that doesn't… But those all already have good join keys today.
I wanna… I wanna correct one thing, which is… the idea that if something is pushed via OTLP to the Prometheus server, that option C maintains backwards compatibility. Because I think that… if you think about it from the perspective where you start with the OTLP, And then what does it turn into? You're right, that in that, like, more narrow view, it preserves backwards compatibility.
But option C makes a breaking switch in the Prometheus receiver that means that anyone who's coming through the Prometheus receiver is going to get different stuff at the end of the day, right? So.
If you look at half the story, it's not breaking, but because we're breaking on the other side, actually the overall behavior is breaking, right? And it would break a lot of users, which is why I oppose it, right?
Option B, actually, Doesn't break anyone end-to-end.
But in a very extremely technical sense, because we're adding support for Prometheus.job, which doesn't exist today, right, could be considered breaking, but only in, like, this very theoretical way. Otherwise, it more or less preserves exactly the behavior we have today.
Arthur Sens 00:11:01 Could you elaborate a little bit on how this breaks on the Prometheus receiver? Because I think we didn't look at that standpoint when we talked last week.
David Ashpole (Google LLC) 00:11:11 Yeah, so you're no longer… Setting service.name based on job, right?
And because you're not doing that, then you no longer get your job back.
when it goes to Prometheus.
Right? So, if we stop doing it on one half.
And don't change the other, then we get a big change in behavior for the vast majority of users.
But if… so, in my mind, we either have to decide… so, if we're just concerned about backwards compatibility, and we're not… I understand that there's a separate discussion about, like.
Maybe more philosophically, like, Do we care about scrape identity?
Or do we care about service identity? And, like.
which of those is more important? And, like.
That's maybe interesting, but if we're just talking about Existing behavior.
preserving overall existing behavior. Then our choices are either we make a change to both The Prometheus receiver.
and to the point where… and to the OTLP receiver in Prometheus, and preserve the overall experience, which is what option B is. Or… we make no changes to either, and we preserve the existing experience. Option C is actually a very large change in how we've been operating.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:12:33 I guess, help me understand, so, I understand… I understand what you're saying about, you know, how… which backwards compatibility story option B protects.
And, you know, basically, if you're using the Prometheus receiver today and the collector, like, we're protecting that route. But… In my head, option C is protecting any path that doesn't include the Prometheus receiver. So either if you're an SDK pushing directly OTLP to Prometheus, or if you're an SDK pushing OTLP to the collector.
and then ultimately using RemoteWrite, or, or, you know, having Prometheus scrape the collector directly. Those two… no, no, no, no.
Sorry, if you're an SDK pushing OTLP directly to Prometheus, or you're an SDK pushing OTLP to the collector, and the collector pushing, like, OTLP to Prometheus. Like, in those two routes.
The… the Prometheus OTLP endpoint.
is doing a particular thing with service name. It's setting, you know, the service attributes as job and instance, and option C protects that.
And doesn't need a change to that. And so, like, for those users, which surely there are users that are doing those paths, option B, I think, degrades that from a compatibility standpoint.
David Ashpole (Google LLC) 00:14:03 So the key thing I would say is the only way you get a Prometheus.job and Prometheus.instance resource attribute.
By and large, like, we can assume, like, there might be some weirdo out there who's, like, actually setting those.
But by and large, the only way you get those is if there's a Prometheus scraper somewhere in your pipeline.
And so everybody who doesn't have the Prometheus scraper in their pipeline doesn't see a change in behavior.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:30 I'm not talking about the change in behavior for Prometheus.job, Prometheus.instance. I'm talking about a change in behavior for job and instance on, like, the metrics themselves.
David Ashpole (Google LLC) 00:14:39 Oh, sure, sure. So, that was option… so just to be clear.
I think there's two flavors of this. One is where it's job and instance, which was option A, and I think everyone has said that they don't like that.
Because someone may actually be legitimately using the key job in their hotel resource today.
Right.
For whatever reason.
But if we went with option B, which is to define a new semantic invention called Prometheus.job and Prometheus.instance.
then… And we set those in the Prometheus receiver, or, right, in the Prometheus and Prometheus remote write receivers.
Then the only way you get those, and thereby could change the behavior of the other side of it is if you're actually using those components. So for everybody else out there who's just pushing OTLP, who's doing other things, who isn't scraping Prometheus.
These attributes never appear. They never… matter for the purposes of backwards compatibility there. So it's identical unless it's somewhere in your pipeline.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:15:49 But, like, rule that out. Just think about the OTLP push situation directly. It's just an SDK pushing directly to Prometheus' OTLP endpoint. Is it not true that today, the Prometheus OTLP endpoint is assigning service name and service instance ID to job and instance? Not Prometheus job, Prometheus.
David Ashpole (Google LLC) 00:16:08 will continue.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:09 Phenomenal.
David Ashpole (Google LLC) 00:16:10 That's maintained in option B, right? Because option B says, If there's Prometheus.job and Prometheus.instance.
Those become job and instance. Otherwise, use service name and service instance ID.
as a fallback. So that's… and you'll never hit the first case.
from… or not ever, but you won't hit the first case if you're just pushing OTLP, and you'll always hit the second case, and get identical behavior to what you have today.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:16:40 So, I want to say that I… I think the problem The adoption B is that it, kind of proposes to introduce a logical inconsistency in the OTLP receiver.
Which is that if… the resource attributes Prometheus.job and Prometheus.instance are encountered, which represent the scrape target identity.
They… they become, essentially, The, the resource identity?
I think that's… I think that's just, like, There's just an inconsistency. There's an inconsistency.
Even, like, even if you disregard backwards compatibility there, it's, like, Like, because… because target info is essentially, when you convert from OTLP to to Prometheus is… represents the resource. So… So you join on Job and Instance, because those are supposed to… represent the resource in Prometheus? So then you have this weird situation that you are referring to the resource, but actually via the scrape target identity. And that's just, like, to me, it's just weird, or inconsistent.
And the other problem, which I've discussed at length with krajo.
Is when the scraper, scrapes several, several resources.
And can you explain to me that, Actually, in that case, you, you have… In that case, you have to… you have to make the exception that you cannot use the scrape target identity. You have to use the individual resource identities. You have to make an exception. So in that case, it doesn't work in any case, so that's another, like, weird inconsistency, if I haven't misunderstood completely.
Where you… you have to make the exception that if a scraper scrapes several resources, then you can no longer apply this scheme. Then you have to send… you have to respect the individual, resource identities instead.
David Ashpole (Google LLC) 00:19:04 So, I think the second is, like, a very… like, already well-solved problem in Prometheus, right? If you scrape a federated endpoint and it has lots of like, target info metrics from a variety of previously scraped things, then yeah, you have to use honor labels, and that resolution is, like, already very much a solved problem. I don't know if, like.
like, we need to encode that behavior in the spec or not, but as a general rule, I think the idea that there's these aggregated endpoints that already have job and instance information on them that you scrape, and you need to respect the Java instance that are already on there, as Prometheus typically does. I, like, I don't see that as, like, a huge… Issue that needs to be solved.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:19:50 Can I… can I, if I understood you correctly, to solve that case, would you have to send the resource… the resource, identifying attributes as… Prometheus.shop and Prometheus.instance, or… can you, can you… no, can you remind me how that had to be solved?
krajo (Grafana Labs) 00:20:07 I can… sorry.
David Ashpole (Google LLC) 00:20:09 I'm sorry, go ahead.
krajo (Grafana Labs) 00:20:11 Yeah, so I, in the testbed that I did, I just took David's PR and what is actually written in the PR for this case, which is under the aggregate exporters.
section, which says that you should generate a job and instance, index position, and just… essentially put service name and service instance ID in them.
Because… Or something that identifies the resource, and for practical purposes, that's kind of your… Current best choice.
Which makes it… you know.
Which tells me that it's very practical to put the resource identifier in those… in the Jovan instance.
To join on, which is… What I wrote in, my opinion. Like, yeah, overall.
I am also, like, very much hesitating between option B and C, but for practical reasons, especially for… because of this aggregated exporter's case, and for backward compatibility, I thought eventually that option C RC1 is the better choice, because that job and instance, as Arva says, becomes an identifier of the resource, because that's what you put in your time series and join on target info. And then, why invent a new identity when you already have an identity, basically? That's the reasoning.
David Ashpole (Google LLC) 00:21:42 And… I'll just respond quickly to Arve's first point, which was… It seems weird to have… the Prometheus job.
become… Or, sorry, it seems… I forget what the first point was. It was something like, there's an inconsistency where the scrape identity can become your service identity, right? And I just… I just want to clarify that that is… that is today the existing behavior in the Prometheus receiver. So, we're not talking about, like.
you know, From my point of view.
We're proposing a big change, and that's fine, like, we can talk about big changes, but, like.
it's an inconsistency that we've lived with for 4 years now, right? So it's not like… this new weird thing that comes along with option B. Like, that's already a thing that we… That we do today, because of how… Job and service name interact.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:22:45 Yes, I think the difference is that we, we, with option B, the Prometheus OTLP receiver becomes, It gets sort of hoarse to adopt this, design quirk.
Which has now been living… until now been living in the hotel collector, receiver, right?
So, so yeah, so… So that's kind of, like, the problem that I'm seeing, that there's this, like, weird quirk, and then you kind of, like, sort of institutionalize it in Prometheus… Prometheus itself.
Mmm… And only in one case. It's only in… because it's conditional on the case that that, that the scraper represents only one hotel resource, identity, and not several, because as krajo had figured out and explained before.
If the scraper represents multiple hotel resource identities, then you can no longer apply that scheme. So it's like.
So it's like, not only is it kind of weird in the first place, in my opinion, it's also dependent on the case. So it's… So yeah, so for one case, you apply the scheme, and for other cases, for another case, which is just that you have multiple resources for the script target, the scheme no longer applies, and… To me, this is just, like, it's just… Too… it's kind of too… too inconsistent of a… of a design.
So, so that's kind of, like, my opinion. That's why I think, I do think, like, C's… is, you know, it's more consistent, it's, and it's more, like, it's better to oper… it's going to be better to operate, in my opinion, like… I fear that, you know, we're going to get some, like, really weird, like, support, cases, in the future, if option B, gets implemented.
David Ashpole (Google LLC) 00:24:55 Are you getting those weird cases today? Like, option B is what we have today with a change that gives you some additional stuff, right?
Like, that's… that's what I can't figure out, is… we're talking about all these problems, but they all exist today. Yes, it's implemented in the Prometheus receiver instead of in the OTLP endpoint, but it's, like.
Option C is extremely scary to me, because it flips… What we've been doing for the past 4 years on its head.
And, like, you know, I don't see how we could… But… To me, that's, like, a huge change, and, you know.
like, I obviously also have stuff for support customers, and they're doing things like this, and it's like, yeah, that change seems really scary to me.
Maybe it's… like, we can make the case that it's worth making, but… I feel like… yeah. Anyways, I've said my bit.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:25:50 Krajo, you tested how it would work with scraping multiple Also resources, right?
krajo (Grafana Labs) 00:25:59 Yes.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:26:00 And so… So… So, like, so how… so that's kind of difficult to implement correctly, right? In the… on the client side?
krajo (Grafana Labs) 00:26:11 I mean, right now, there is no direct support in the SDK. I could make it work, you can take a look in the testbed code.
Again, I feel like… the… the weirdness of option B, if you can score it that, comes from the fact that VR… We have to, you know, figure out a way to assign a good identity to… to targets.
Or… or services that we… script.
Without using the… We are choosing their existing identity already, and I guess… I understand what David is saying, that we have already been doing it, so it kind of works.
I guess the question is, is that something we want to enshrine for the future?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:27:11 M… But it has to be… it has to be implemented differently on the client side, with the new Auction B scheme.
than what's done today, krajo, like, to… Mmm… I mean, so the option B scheme changes things, because the client will have to send Prometheus.job and Prometheus.instance, research attributes.
David Ashpole (Google LLC) 00:27:38 So… Just to be clear. Like, so… having a Prometheus endpoint.
which exposes multiple OpenTelemetry resources, is already implemented today in the collector's Prometheus exporter.
It behaves identically.
to a Prometheus, or not identically, but it mimics, as closely as it can, a Prometheus federated endpoint, which means it doesn't set Prometheus.job and Prometheus.instance, because that wouldn't make sense where were in Prometheus format on this endpoint. It sets job and instance, and then scrapers, whether they are the Prometheus receiver or a regular Prometheus server, use the standard honor labels config.
to choose to accept the identity provided by the endpoint. So, like.
If we introduce this in client libraries, they would have to behave the same way, where they would have to say.
Yes, I… you know, I am actually a federated endpoint.
I have job and instance already present, and they would have to do that, because that's how, in Prometheus.
you represent… An endpoint that is an aggregation of multiple identities, right?
like, Prometheus could invent a new way to represent that, and then we could adopt it here. But this is, like… from my perspective, very much like OpenTelemetry using the tools that Prometheus has to support multiple targets, right?
We could also come up with a new info metric. If we didn't want target info.
Then we could have a different infometric that is… like, a resource info, or something like that. We've adopted, like… Anyway, I think this is slightly orthogonal, but, like, these concepts exist in Prometheus, and we've adopted them, and we could choose to change that.
But I feel like that's slightly different from… The problem we've been talking about.
krajo (Grafana Labs) 00:29:46 I just wanted to… sorry, I raised my head.
I just wanted to ask.
As it is implanted now, what is it?
what does the exporter, I guess, then… put in the JobN instance that it generates.
David Ashpole (Google LLC) 00:30:02 It follows the specification, which says the service name… it follows the exact same logic that the Prometheus Remote Ride Exporter or the Prometheus server do today, which is to use service name and service instance ID as job and instance.
krajo (Grafana Labs) 00:30:16 Right, I guess you… but you see the weirdness that we're talking about here, like, but then… When we scrape something, we don't do that. We don't… Replace your brand instance.
David Ashpole (Google LLC) 00:30:28 We scrape… Say that again?
krajo (Grafana Labs) 00:30:31 Well, if we were…
David Ashpole (Google LLC) 00:30:32 to scrape it with the Prometheus receiver.
krajo (Grafana Labs) 00:30:35 No, no, I'm…
David Ashpole (Google LLC) 00:30:35 Then it would go back to service name, right? That's how it's all done today.
krajo (Grafana Labs) 00:30:41 Yeah, but my point is that… If the exposition… if the exporter is just a single application, so not federated.
then we don't do this. We don't put service name, service instance ID in the JobN instance. We generate one, and hope that whoever did the Prometus configuration made sure that that actually works.
David Ashpole (Google LLC) 00:31:02 Yep. Yeah, yeah.
krajo (Grafana Labs) 00:31:03 That, that, I mean, that's the…
David Ashpole (Google LLC) 00:31:04 I completely agree.
krajo (Grafana Labs) 00:31:05 Yeah, yeah, yeah, yeah.
Yeah. Anyway, so, yeah, that's, like, interestingly, I think… Overall, in the future, you know, in the far future, when we can associate time series with metadata, without having to do this weird join.
You know, you still need to put some label on your time series that make them Identifiable for that service.
So that when you have two time series.
You need some extra label.
That says, okay, this belongs to this service, this belongs to other service.
Right?
David Ashpole (Google LLC) 00:31:46 Right, so if… In the case where there's a Prometheus scrape endpoint.
That has multiple resources on it.
You need to have a join key.
that associates… the resource.
with… the metric. And this is actually the same problem we have when we're querying, right? So it's not… it's not like that… The exposition is maybe the interesting part, like, you could represent them as multiple scrape targets.
which is… even though they may have come from multiple OpenTelemetry SDKs, or from, like, multiple meter providers within an OpenTelemetry SDK, I think is maybe the weirder case.
Because we're… we're mapping hotel resource to scrape Target, and that's what the spec… has been doing for, you know, the last 5 years, right? So, like, I agree that there's some weirdness there, and, like.
we could decide not to do that. I think there's… We did that, obviously, for, I think, good reason back in the day.
Debatably, right? And so… Yeah, like… it's a big thing to revisit, and I think it might be worth revisiting If and when we decide to… in SDKs support multiple Resources on a single endpoint.
But at least today, that's not, like, a… like, that's something we need to design for in the future, not, like…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:14 Not do that.
David Ashpole (Google LLC) 00:33:17 Yeah, but…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:25 I left a comment in the notes doc, because I just wanted to be clear about this, so, I made some statements about option C, and I want folks to, you know, help me understand if these are true.
So, is it true that with option C, the job and instance of series will change for anyone using the collector Prometheus receiver?
You're muted, dear.
Arthur Sens 00:33:55 distributed,
David Ashpole (Google LLC) 00:33:58 So… There's a little bit of nuance here.
Because… According to the spec, Everyone should change.
But there's currently a bug in the Prometheus receiver.
Where, if you have UTF-8 enabled.
You actually won't see a change.
for… those cases. But everyone who's using the default settings will see a change.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:26 But that's most people.
David Ashpole (Google LLC) 00:34:29 That's… like, I don't have a.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:30 We obviously don't have data, but, like, I think it… we can intuit that it's most people.
And then, as a result of that, anyone using Java and Instance directly in queries without a join, will have their queries break.
David Ashpole (Google LLC) 00:34:45 That's… that's my primary concern.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:34:50 I can relate to that concern.
Arthur Sens 00:35:00 Hey, this honor label thing, I assume you get this experience from maintaining KSM for a very long time. Like, KSM also behaves like a federated endpoint. It collects metrics from several sources.
And, yeah, looking at how KSM is used in the industry.
I think it's, like, the default. I'll just always have our owner labels set to true.
I think we haven't discussed this when we were together. It sounds reasonable.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:35:51 We think that OTEL Prometheus community users can, you know, tolerate a breaking change of this magnitude.
For option C?
Like, where the queries of anybody, depending on job and instance, directly?
venue users using the Prometheus receiver are going to break.
Arthur Sens 00:36:19 I think Java Instance is a very, very common filter.
I… most of Mix, Prometheus Mix Sens have those filters. I think most of, Grafana products… I don't know, Google, but we all have those filters.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:48 Because what I'm getting at is, like, if we don't have the appetite, if we don't think we can, you know, have the sort of social capital to make a breaking change of that magnitude at this stage, then we can treat that as a design constraint.
And design around not breaking that. And that simplifies the solution space.
So if we say, like, what the non-starters are, what's left?
And I guess, like, to make it, you know, explicit here, is it a non-starter?
to break… any queries using Java and Instance of any users using the Prometheus receiver with default settings.
David Ashpole (Google LLC) 00:37:49 That's what I wrote in my opinion section.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:37:54 Yeah, I mean, that sounds like it's best avoided. I mean, I kind of want to go through, I want to kind of collect all relevant use cases, and that's… that's what you're trying to do in your table, right, Kyle?
I want to kind of… it's so difficult, I mean, I kind of keep all the use cases and, like, scenarios in my head, like, I really need to… I think we need to have, like, a written definition of relevant use cases, and the scenarios, and go through them and see what actually breaks in practice.
How complete is your table now, Gail? Maybe that's something I should help you with.
krajo (Grafana Labs) 00:38:34 I have a… The scenario of… Having a simple application export with default settings.
And then… Remote flight exporter.
So, simple application with default settings, scraped by the OTLB collector, and sending it.
We are a remote ride exporter.
both default settings and UTF-8.
And also, I implemented the aggregate exporter that generates its own Joban instance.
Which… I don't know if David looked at this, but which case would this be, that we are talking about?
David Ashpole (Google LLC) 00:39:14 This is the… is this the default case, or does that not actually change?
krajo (Grafana Labs) 00:39:21 Yes. Let me see…
David Ashpole (Google LLC) 00:39:24 I think the default.
krajo (Grafana Labs) 00:39:31 Yeah, the default case… in the default case, the job… both my job, and night becomes my service. So, yep.
That… that would… I mean, it… It's kind of… It's weird.
Right? Because… You don't… have a different label, you have the same job instance, it's the content of it.
Changes, so you would still be able to join on it, but it means something different.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:40:03 Yeah, and so if you had any queries that hard-coded against those values that said, like, you know, essentially if or where the job and instance are these explicit values.
krajo (Grafana Labs) 00:40:16 Yeah, I mean, to be… to be fair, I don't… like… This is, again, the weirdness to me. Like, why would you name something the job of the script, why not the service name? Like.
In my head, maybe people just name the job the same as the service, and that's why this works, and none of this matters.
Right. I don't know.
David Ashpole (Google LLC) 00:40:42 I think that… so, I would say, historically, that's been the assumption, that, like, oh, they're roughly the same, so… We'll just use them interchangeably.
I think the… the impetus for this… Whole effort was… A small subset of users who do differentiate between them.
For whatever reason.
And asked for… There's… yeah.
more or less, like, the… I think, actually, Keeping the current behavior.
and making it consistent isn't the end of the world. I think there's some, like.
There is the case where, like, we have to drop one or the other, and people find it confusing to drop one or the other.
But yeah, like… I think for the vast majority of users, this has been okay.
Arthur Sens 00:41:39 I just wanted to clarify one thing, like… Historically, it is roughly the same, because OpenTelemetry started mostly as a tracing.
Oh, with tracing being mature, and everything that emits a trace is kind of a service?
But as we start… like, as OpenTelemetry starts to… Get momentum in infrastructure.
Like… It's not services anymore. A host is not a service, a database is not a service.
And that's where it gets complicated, where we're not getting the service resource attributes.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:42:25 I mean, what I would like to see, personally, are which scenarios, options C against C.1, a break with regards to backwards compatibility.
Because that's not clear to me at the moment, like, I'd like to kind of understand what that actually means.
What that means in practice.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:42:47 Maybe we should boil down each of these.
each of these solution options into, like, some sort of, like, small list of the salient points about it. Like, like, what are the… what are the key use cases that are enabled or broken by this? And, you know, keep it short, because this is a priority list, and… you know, what we're trying to do is gauge the impact. I think both of these options, B and C, are impactful to some slice of users. It's just like a… I think what we're kind of… Arguing here is about, like, you know, how big the respective slices are, and…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:43:26 I think that would be, like, an actual fit for pros and cons, like, if pros and cons… if the con sections of the respective options could list the scenarios breaking, I would love that.
This is the sort of thing, right, you know, where I'd really like, you know, like, a written, definition of which, scenarios break with the individual, options, because I cannot, kind of, deduce that, mentally. It's just too complex.
Okay, So, krajo says that… It should be possible to see from… From his table, which cases break.
So, I guess that's a bit of a homework for myself, at least.
To kind of enumerate which cases break and why.
krajo (Grafana Labs) 00:44:33 Yeah, I'm on the same page as Arve on this, that this is super complicated, and it's hard to… See all the cases in your head.
So that's why I started these tables, that's why… I think what Jack started in his opinion would be super useful for all the options to have some pseudocode.
Because I would read that probably easier than English, actually, at this point, because that's more precise.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:45:02 I'm reading your table, krajo, like, I see it now for the first time.
Is it right that C.1 doesn't break in the scenarios?
It's like… it's either identical to current, or byte identical to option B.
krajo (Grafana Labs) 00:45:19 I mean this is the code that… created this was done by Claude, and then.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:45:27 No?
krajo (Grafana Labs) 00:45:28 I went through and tried to fix, and also David fixed some bugs.
But I would need… Like, U to verify option C and C1.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:45:38 Yeah, but I mean, if this table is correct, does it actually say right now that C.1 doesn't break any scenarios?
Or break backwards compatibility, I mean?
krajo (Grafana Labs) 00:46:00 Not in the default case. There's, another table for the UTFA translation, and there it, it does break, because it does take the declared identity.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:13 Like, there's a C option that doesn't break the queries that I was just talking about in the default case.
See, that one doesn't change the value of job and instance?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:46:24 That's quite possible, because it's… I think that's the tweak in C.1, that it, retains back… it kind of retains the current behavior.
like, it… option C performs a certain translation, which C.1 does not.
So I'm, like, I'm also curious whether the cases that, David has identified, where C breaks backwards compatibility, if that's the… If those cases are also broken by C.1.
David Ashpole (Google LLC) 00:46:58 And just, just to be clear, like.
the Prometheus receiver right now is not spec compliant, right? So… It depends on whether we're talking about like, in the UTF-8 case, it depends on whether we're talking about What the spec says?
Or what's implemented today.
Thanks, Mike.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:16 Gotta be what's implemented, because that's what we're trying to evaluate breaking for, is users in the real world, and the spec is not the real world.
David Ashpole (Google LLC) 00:47:22 Okay, then that's fine.
then, in that case, I think C1 isn't breaking.
And B is a change… is the same change that would bring the Prometheus receiver into compliance with the specification.
Right, so B does change the UTF-8.
Case, but in a way… it… basically in the way that it was originally designed to work.
I don't know if that makes it better or worse, but… Yeah, there's other… Sorry, go ahead.
Arthur Sens 00:48:01 I think it is for the better, because all the mixed Sens that exist today, and that's where most of the Prometheus users get their dashboards, they assume translation. They don't do no translation. They all use underscores.
But we wouldn't break any mix-ins, because they don't have dots in them.
David Ashpole (Google LLC) 00:48:21 Yep.
So that, that should work, because… We don't… we don't have any special treatment for service underscore name, for example.
Despite that being the original service name today.
I think… Yeah.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:48:42 But… The, okay, so, so, so… My, my plan now is basically to… to enumerate the scenarios, with the help of krajo's table, probably, that… that option C and C.1 break, Respectively, because then… then that concretizes, like, the whole discussion.
So… so then… I've made, like, you know, a reminder for myself to try to do this next week, and then… then I will want to… Stick… stick those into the respective columns sections of those options.
So that's kind of, what, I think, what I want to do, because I want to concretize, in a way I cannot just do, like, mentally.
So, what do the rest of you think? Like, Ikaya, first of all, does that sound right to you? I mean, you're the most familiar with your tabular approach.
krajo (Grafana Labs) 00:49:44 Yeah, I mean, I always try to urge everybody to review this testbed and the tables, because I also cannot keep everything in my head, and when I'm going by First principles for B and C have its pros and cons, basically.
with the weirdness of B, and the… You know, consistency of… Oh, see, but breaking stuff, so… Yeah, I would love if… You guys would, you know, sign off on those columns, and if you have, like, a new idea, the code is there. Like, it's, you can… Everything is linked from this AutoJube testbed, and you can just implement and run it.
And… and, you know, see what… what it does.
I'll be… On vacation for the next 2 weeks.
So far.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:50:39 I think this sounds great, Kyle. Like, I really think this is the way forward. Like, I can't see why option C would break certain things, but that's actually why there's C.1. It's there to retain a certain… it's there to… to retain a certain aspect of current behavior, so I'm, like, wondering… whether those scenarios also break backwards compatibility with, with 0.1, so that's kind of what I want to see in practice.
David Ashpole (Google LLC) 00:51:07 I'll just say I don't think it does. I still think both C and C.1 are unacceptable from my point of view. But, you know, like, if people want to work on this, that's fine.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:22 So is there then a disagreement about… is there a disagreement, then? Because I'm hearing, sort of, like, CDAT1 doesn't have the breaking changes that we said that C does, and that the concern about C was, but, like, it seems like it either does or doesn't, and that's sort of what the conversation hinges around.
David Ashpole (Google LLC) 00:51:40 Braking… it would be a braking change to the specification.
Right? For either one.
But if we're going based off of what the Prometheus receiver specifically implements, then it wouldn't break any users. It would still have the issue of being Your job and instance.
the job instance you get depends on whether you use UTF-8 translation or not.
Right, so that's, like… Just, yeah, kind of a bizarre outcome of it, where… Just because of how things end up interacting.
And for me, I still hold the requirement that Java and Instance properly round trip between the two.
And… I think it would be worth it to fix the Prometheus receiver to bring it into compliance with the current specification.
So that…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:52:28 I mean…
David Ashpole (Google LLC) 00:52:28 And…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:52:29 I would… Yeah. Yeah, I would like to see… I mean, I feel like this is all very abstract. I would like to see concretely, you know, what breaks with options… option C.1.
I mean.
David Ashpole (Google LLC) 00:52:40 does not… does not break. I can tell you that already.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:52:44 Yes, but then… but then I would like to see concretely what is the problem, if there's any old one.
David Ashpole (Google LLC) 00:52:48 what… where… Job and instance.
flip-flop, depending on whether you use UTF-8 or not.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:52:55 But, okay.
David Ashpole (Google LLC) 00:52:55 You can see that in this table, yeah.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:52:57 But that's the current behavior, right? So at least we maintain the current behavior, and…
David Ashpole (Google LLC) 00:53:04 And we should fix it.
fix it, because that's within the… what's in the spec.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:53:08 But I think that should be, you know, that should be discussed, like, concretely, whether Whether that's something, we want to tackle, and whether on how we deal with the fallout of, you know, during pregnancy.
David Ashpole (Google LLC) 00:53:23 worth it. We've been on this for months and months now, so… We've been through iterations of building, we've brought other people in, It's like… we can go through another iteration of that, that's fine. It'll just be another month, and…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:53:39 There's, there's.
David Ashpole (Google LLC) 00:53:40 Same thing from the beginning.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:53:42 There's one more thing, like, that I want to discuss, which is whether option B actually takes in… does it actually define how to deal with entities when entities start carrying a resource identity?
This option be actually, tucked up.
David Ashpole (Google LLC) 00:54:02 Source identity already.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:54:03 cycle that I mentioned.
David Ashpole (Google LLC) 00:54:05 resource identity already exists, right? Today, all resource attributes are identifying. The fact that entities allow you to mark some as descriptive is… It's like… Doesn't seem to me to make a huge difference.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:54:19 So, concretely, when, when Prometheus sees, sees, like, an entity, and it, it picks Then it should pick the resource identity from that, but how do you combine that with the rule that Prometheus.job and Prometheus.instance should, define the identity. I think that is not defined in… Prometheus.
David Ashpole (Google LLC) 00:54:42 Prometheus.job and Prometheus.instance don't define identity. They just define the job and instance.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:54:48 But I mean, that's the point with option B, which differs… which, which I don't agree with, that… It basically… it basically states… it basically states that, the converter should… should treat Prometheus… should treat Prometheus top job and Prometheus don't… instance, as the identity.
From a… from which to generate the job and instance labels for target info.
David Ashpole (Google LLC) 00:55:14 Job and instance are not generated in… Option B. They're simply, like.
sorry, we've had this discussion many times. I don't know if this is particularly interesting to others. They can let us know, but, Like, we're trying to find… the Java instance.
It… I think… there's maybe a world in which we choose other joint keys, right? But… Job and instance.
like, I think it's extremely confusing for users when we put random things in Java instance.
That are…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:48 I'm truly sorry, but I have to drop now, because I'm in a space where I have to go immediately.
David Ashpole (Google LLC) 00:55:55 Okay.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:55 Yeah, thanks for the discussion, so, see you all Bye-bye.
David Ashpole (Google LLC) 00:56:03 Oh, Arthur?
For some reason.
Arthur Sens 00:56:05 I… Yeah, I wanted to change topics, but I don't want to do this while we don't agree on how to proceed.
asynchronously.
Oh, Are we going to the dock? What are we doing?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:26 So I think Arve is interested in making some of these conversations that we've been having about breaking changes concrete. Like, you know, and I don't think there's any problem with that.
And I also think we don't necessarily have We don't have great options, because, this is a conversation about Prometheus and OTEL compatibility, which means that, like, we can't do, like, an escalation process within the OTEL governance model, and just say, like, hey, escalate to the TC or something like that, and then, you know, somebody makes a call, and then we disagree and commit, because we need cooperation between two different organizations that have separate governance.
And so, like, we have to reach a consensus one way or the other.
Or else we're gonna have inconsistent implementations and inconsistent messaging.
And everybody will suffer, and we'll all look bad.
So, like, you know, what does that mean? I think that means we have to, sort of, like, Go forward with this and do our best to maybe simplify the discussions around the different options and their respective pros and cons.
And, and hope that, like, after everything is made plain and clear for everybody, and everybody agrees with the methodology, and everybody agrees with the, you know.
Like, the premise is that, you know, everybody reaches the same conclusion about, you know.
What… what matters, and like, you know, what types of braking chains are allowed or not acceptable.
I think we're, like, despite having, like, talked about this for seemingly forever, for a long time, there is still disagreement about, like, the premise. Like, there's disagreement about, like, what the actual implications are about these different options and the repercussions, so…
David Ashpole (Google LLC) 00:58:27 I don't know if there's actually any disagreement about the implications. Well, maybe, maybe, maybe not disagreements.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:33 Yeah, everybody hasn't… everybody hasn't fully digested the outcomes and, you know, the implications of… of… Thanks.
Arthur Sens 00:58:45 That's how you can go,
David Ashpole (Google LLC) 00:58:47 Incredible, yeah.
Arthur Sens 00:58:49 No, Cry, you can go, because I'm gonna switch topics.
krajo (Grafana Labs) 00:58:51 Okay, yeah, yeah, yeah. So, yeah, I arrived, like, a couple of weeks back, I arrived at this position that I don't… Really care from, like, from a… from a big picture, like.
point of view, whether it's B or C, or C1, or whatever.
Because in my head, all these Joe Band instances is just a join key in the end, and we shouldn't actually treat them as containing some service name or whatever, that in the perfect word, you would have an API and PromQL that would Could get you the… Your service name, or whatever identity that you want to use.
And you wouldn't be stuck with it. So I don't care.
and… And I can live with either. I think… To, kind of, make everybody… happy and have something to talk about. The word salad that we have in the… in the dogma is a bit hard.
So that's why I'm pushing for, you know, Making these labels.
And possibly the observer code. So that's all I wanted to say.
Arthur Sens 01:00:09 Okay, what I want to say, we are already out of time, so I'll be very brief.
Been working with the collector maintainers to release a new… New distribution of the collector?
I have a PR up already, this PR… includes, a few Prometus exporters, but, like, the goal is that we keep including new exporters to this… this… to this distribution.
to the group, the Prometheus SIG is becoming a maintainer for this distribution?
So we have a saying on which components get included, which components should not get included.
And for now, the SIG is just me and David, but I would love to grow the group as people understand all the responsibilities.
That's it. If we don't have any questions, happy to end the meeting.
David Ashpole (Google LLC) 01:01:15 Cool. Let's… let's end it then. Thanks, everyone, for joining.
Arthur Sens 01:01:20 electric.
David Ashpole (Google LLC) 01:01:20 Excuse me.
