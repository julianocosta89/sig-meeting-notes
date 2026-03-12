SIG: Java Declarative Configuration
Date: 2025-08-28
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 03:04 Hi!
**Jay DeLuca** 03:07 Oh, again?
**GZ Gregor Zeitlinger** 03:09 Let's hope we are as many as last week.
**Jay DeLuca** 03:15 I think, Trask is joining us, but he… he pinged in the… Channel that he's gonna be a few minutes late.
**GZ Gregor Zeitlinger** 03:21 Okay.
**Jay DeLuca** 03:23 Oh, there he is.
**Trask Stalnaker** 03:25 Hey, bud.
**GZ Gregor Zeitlinger** 03:26 Hello!
**Jay DeLuca** 03:28 Hey, Trask.
**Trask Stalnaker** 03:34 Hey, Antoine.
**GZ Gregor Zeitlinger** 03:36 Hello!
**Trask Stalnaker** 03:40 What is your time zone, Antoine?
**Antoine Toulme** 03:44 Same as yours, Pacific time.
**Trask Stalnaker** 03:46 Then good morning to you.
**Antoine Toulme** 03:49 Mind you.
Good day, everybody.
**Trask Stalnaker** 03:54 I actually have the same question for you, Jay.
**Jay DeLuca** 03:58 I'm on the East Coast.
It's 11 AM for me now.
You're in Seattle, Trask?
**Trask Stalnaker** 04:07 Portland.
**Jay DeLuca** 04:09 Portland, okay.
And then there's Gregor, across the sea.
**Trask Stalnaker** 04:16 Yes, yes.
Did we lose you, Gregor?
**GZ Gregor Zeitlinger** 04:21 No, no, I'm here.
**Trask Stalnaker** 04:22 Alright.
**GZ Gregor Zeitlinger** 04:30 Can you see?
The agenda now?
**Trask Stalnaker** 04:35 Yeah. Yes.
**GZ Gregor Zeitlinger** 04:38 Yeah, three topics for today. I kept the PR review as the first item, because that worked really well.
Then, Jay and I had a discussion about milestones, because, Some of the things, that I started, take a bit longer, including spec and semconf work, and that's why I wanted to discuss milestones, and then lastly, Testing, which we have started to discuss, but then we, … Or I at least forgot about it.
**Trask Stalnaker** 05:22 Cool, and, Lamila just joined, maybe, shall we start with… the topic that we wanted her input on, about the declarative config YAML modeling.
**GZ Gregor Zeitlinger** 05:39 Right, I forgot to put that on the agenda.
Did we have it?
Was it a spec?
**Trask Stalnaker** 05:52 So in FEMCOMF, the… basically how we could add into Weaver… well, Weaver slash some kind.
how to model… right now, your SEMCOM PR is just free-form text explaining in the notes the declarative config settings.
**GZ Gregor Zeitlinger** 06:16 Right.
**Trask Stalnaker** 06:16 And we would like to get that into some kind of structured YAML.
**Liudmila Molkova** 06:28 To be, precise, we don't… I don't actually think we have to do it for this pull request.
But we… it's something we need to start thinking about, and I would love to have some proposal in place that we can evolve.
For the real life.
**GZ Gregor Zeitlinger** 06:50 Yeah, I did not have, … Time to, … start a proposal yet, but we can, think about, What it would look like.
So either we start with, … The configuration as it looks like.
What is it? Implementation… Instrumentation.
**Liudmila Molkova** 07:18 So, if we actually… Oh, go ahead.
**Trask Stalnaker** 07:22 you're conflating two different things here, Gregor.
**GZ Gregor Zeitlinger** 07:26 Okay. ….
**Trask Stalnaker** 07:27 we're talking about not the YAML for the configuration YAML itself?
But for the SEMCOMs… YAML file.
**GZ Gregor Zeitlinger** 07:40 I get that.
**Trask Stalnaker** 07:41 Okay, got it.
**GZ Gregor Zeitlinger** 07:42 I'm… I'm just, trying to think if we can have a structure that mirrors the YAML, so, … We would say, … corresponds….
**Trask Stalnaker** 07:58 Sorry, Ludmila.
**Liudmila Molkova** 08:00 Oh, no worries.
I was saying the same thing, that we need two different… Representations of the same config option.
So… I think if we limit the scope, at least initially, to the HTTP headers, or things like that.
Like, the… DBQuery Parameters is a very similar example, and there are plenty of others.
**GZ Gregor Zeitlinger** 08:30 And I kinda see how it can be done easily.
**Liudmila Molkova** 08:35 We would… I can help you with the proposal, but essentially, under this attribute, we would have some extra thing that's called configuration, or… and there we would somehow express that you opt-in by providing the key for the header.
The part where it gets tricky in many, things is the peer configuration.
And maybe, we should spend a little bit of time Talking about whites in instrumentation at all? How would instrumentation use it?
Like, what would it do with this configuration? Why is it instrumentation, another processor?
**GZ Gregor Zeitlinger** 09:25 That's a good point, yeah.
… the… A peer service, … Mapping needs to have access to attributes that are… Not, propagated into… the metrics, exporter.
So, if the metrics exporter or processor or whatever just looks at the telemetry data, then it would not be able to come up with the peer service.
Let me, pull up the… open up the pull request for that. I think we discussed there.
… Wasn't cement a convention, I think.
**Liudmila Molkova** 10:18 Yeah.
**GZ Gregor Zeitlinger** 10:31 And the SDK does not have access to the URL. I think that was the problem, and the… And the matching can take into account the full URL.
So, not only the host and port, but also the path component.
That's how it works in Java, but I think that we need to have the same expressiveness in all the languages.
**Liudmila Molkova** 11:00 So the… the thing is, is when we… my understanding how it should work, there is a… at least what's written in the… in the spear configuration table is that it matches the IP address.
And if this… if I'm a client instrumentation, I talk to this IP address.
I would populate the peer service attribute.
There are, I don't know, 100 client instrumentations that populate … IP addresses.
HTTP, RPC database messaging, and so on.
not… even if it talk about HTTP, there are, I don't know.
20 in Java? Or how many do you have? And it… if we can avoid putting things like this in each instrumentation.
Oh, God. The life would be easier.
**GZ Gregor Zeitlinger** 11:56 It's also….
In Java, this is a single component that is reused in all the Instrumentation, so it's a common instrumentation logic, if you will.
**Liudmila Molkova** 12:09 It's the instrumentation API that does it.
**GZ Gregor Zeitlinger** 12:13 Not the API, but there are several common components, and one of them is doing it.
Maybe even the API, I'm… I'm not sure.
**Trask Stalnaker** 12:25 It is… so, it is… today, it's exposed, like, in library instrumentation, there is an API for when you create your OKHVP instrumentation, you can set Add your peer mappings that you want.
And… I do think that's a good question of… … Is that a, instrumentation? Like, do you care… would you care about doing that for instrumentation?
Not really sure you would.
If you did, somehow, that could potentially be modeled.
As the processor, based on instrumentation scope, anyways.
**GZ Gregor Zeitlinger** 13:12 I do not have all the information, so how would you do it as a processor, technically speaking?
**Liudmila Molkova** 13:20 Currently, Tomly uses IP to peer service, right? And IP is an attribute on the telemetry.
**GZ Gregor Zeitlinger** 13:29 No, no, it can also be example.com slash foo service, and that would be used to match.
Because that is how some, … HTTP clients address the surface, that the path is relevant.
**Liudmila Molkova** 13:46 So you can map based on the network… on the IP, you can map based on server address, you can map based on the URL, if there is a URL.
… So, if I would be writing this processor, I would write it in the way that, … The mapping is defined, like, if My car… my attribute… attributes match to something?
For example, network peer address equal to, or server address equal to, … Then something, and then something means eating this peer service.
… Does it make sense?
**GZ Gregor Zeitlinger** 14:34 No, sorry, I don't understand how you can access information that is not persisted in the metric, as metric attribute.
Let me… Try to, copy and….
**Trask Stalnaker** 14:48 Oh, you're thinking metrics, not spans?
**GZ Gregor Zeitlinger** 14:53 In spans, you usually have all the information, right? That's why it's easier for spans, but we also need to have it I see. Am I wrong about that?
….
**Liudmila Molkova** 15:06 So… If, some… if… Something instrumentation knows matches.
this, IP server address for URL, then you would like a metric to have an attribute.
of Visit PR service.
Right. Fun.
Well, measurement processor.
Huh.
Which is… I just stalled.
could do this.
And there is a… you have something like attribute processor in Java attached to views.
Has access to context, but obviously it's a hard one.
Okay, I see your point.
**GZ Gregor Zeitlinger** 16:01 I don't know how that would work with the attribute processor, I have to check that out.
**Liudmila Molkova** 16:06 You would need to put something in the context. Instrumentation would need to put everything it knows in the context, and then the processor would need to access it from the context. It's kind of wasteful.
**GZ Gregor Zeitlinger** 16:17 Oh, okay, this context object, okay, got it.
Okay, the metrics is a good point.
Maybe that's a good idea.
**Trask Stalnaker** 16:34 One other… One other thought there is, … Would you want to use it as a sampling attribute?
Gregor, today, do we calculate the peer service before starting the span?
Do you know?
I'm guessing probably we do, in which case it can be used as a span sampling attribute, which is nice.
Which is something you don't expect.
If you, … do it via span processor. We had, we have kind of a similar issue in Milo with, thread name.
Where we use a span processor to set thread name.
But we have had some requests to sample be able to use thread name in a sampler.
And so we've considered going in the other direction of taking that existing span processor and essentially embedding it into all the instrumentations, which is annoying, but… Currently, I think the only way to solve that.
**Liudmila Molkova** 17:55 I see.
So, essentially, we need a component in the instrumentation, all instrumentations, the common component, that would do some sort of Making an enrichment.
And….
**Trask Stalnaker** 18:14 Right.
**Liudmila Molkova** 18:15 It's not a processor, because… it happens before.
And because relying on the context, populating things in the context is expensive.
Performance Vice.
**Trask Stalnaker** 18:33 Yeah, you could almost do it in a sampler itself, to populate those attributes lazily, and then I think the sampler can return attributes that get stamped onto a span.
**Liudmila Molkova** 18:50 And then metrics are a problem.
Still.
**Trask Stalnaker** 18:57 Right, right.
**GZ Gregor Zeitlinger** 19:00 Ludmilla, I wanted to ask, … Are you saying that this is, an SDK concern, the peer service? Is that what you're… Driving at?
**Liudmila Molkova** 19:16 Yes and no. It's the locking component that we don't have the instrumentation … API, or the implementation behind it, right? We have it in Java, we don't have it in other languages.
If I say it's the SDK problem, you would hate me, and you would never come back and ask me anything again.
So… so I… I don't want to say it, we'll never fix it if it's the SDK problem.
**GZ Gregor Zeitlinger** 19:48 I don't think so, if we can agree that it should be specified on the SDK, people will implement it, it's just that, it has to be specified for SDKs to be implemented.
**Liudmila Molkova** 20:02 Exactly, yeah.
And the instrumentation API and all of the different scenarios we have in mind. Well… It will take years, my feeling, before we… figure it out, so I… I kind of want to find a solution that, that can work, It sounds like you found it in Java.
The question is how we can… what can we do to make it happen in other languages which don't have instrumentation API of some sort, or the common component for all instrumentations?
And maybe the answer is they don't support it, period, or they… Yeah.
**GZ Gregor Zeitlinger** 20:48 You mean, because it's too difficult in other languages to reuse a common component?
But I find it hard to believe.
**Liudmila Molkova** 20:59 I mean, if you look into Python, they don't have, much common across different instrumentations.
**GZ Gregor Zeitlinger** 21:09 I also noticed that, and I don't have a good answer.
If that has been a conscious decision, or if it just happened to be that way.
**Liudmila Molkova** 21:20 It's already this way, right? It doesn't matter if it's a conscious decision.
**GZ Gregor Zeitlinger** 21:25 Yeah, I'm trying to find a way how we can… … Have a good… Definition and declarative configuration without forcing too many decisions on language 6.
… Right now, there is a clear distinction. If it's instrumentation, then this… in the instrumentation part of the YAML, then this is ended in instrumentation.
But maybe, we can have a, … part in the YAML that is for common configuration, and it does not say where it has to be implemented. That would kind of, open it up for the language 6 to Decide where this is best implemented.
**Liudmila Molkova** 22:19 We can. The chances that, let's say.NET runtime implements it, is slim, then.
So they have their own enrichment thing, and it already works in some way, and there will be instrumentation component that can do it, or in Python, there may be one HTTP client that would make use of it, the others will not.
And we will end up in the… situation where….
**GZ Gregor Zeitlinger** 22:52 it's implemented on paper, it never works… well, it only works in Java in reality.
Hmm.
**Liudmila Molkova** 23:08 And, okay, so let's… let's maybe table this discussion. I don't know the answer. If it works in Java, awesome. Maybe the answer is that If you want to implement the configuration part.
this mapping part. It… there should be some common component that does it. Maybe all instrumentation should get on board and make use of it.
if we talk about the syntaxes, then, I still don't find the current syntaxes doing what you… What you were explaining.
It only maps the IP to the… Service name. Oh, sorry, peer, peer, peer service.
Right?
**GZ Gregor Zeitlinger** 23:51 Here in the example that I have in the document, it's the host and the path component and the port.
That, that maps to… Food service.
**Liudmila Molkova** 24:08 … Yeah, so… If, like, when… when you… Do… is there a description of… what… What… how to implement it?
I don't think it's obvious.
**GZ Gregor Zeitlinger** 24:27 Okay.
Yeah, that's a fair point, and I, … I will add an algorithm how this is implemented in the pull request.
Yeah, good point.
**Liudmila Molkova** 24:42 And… It's currently… I'm checking where it currently lives.
… It's under… Sorry, give me a sec.
It's under the pier.
So… One option to implement it would be that the, let's say, HTTP instrumentation would access it.
And… read it directly.
Or… The common component called peer mapping.
would… would do it.
Either way, right? It should work either way.
**GZ Gregor Zeitlinger** 25:42 That's right, yeah. So basically, when you start a span or emit a metric, you call the common component, and… … Give it all the attributes you have, and ask for the peer service.
**Liudmila Molkova** 25:58 Give it all attributes, you have for SPAN, the biggest set you have.
**GZ Gregor Zeitlinger** 26:07 If you… if you are creating spans and metrics in a way that you have the same pool of attributes, then yes, the span ones. But I think this is not the, … not the case in other languages. So in Java, this works, but I think in Python, they have a different set of attributes for metrics, and then you just … Provide the attributes that you have.
**Liudmila Molkova** 26:37 It can only work successfully if you… if you give it something … Some object that contains IP address, server address, and URL, the combination of these three, some, like, some could be missing, but this, these three are important. So there is some peer information, these three attributes.
… Arguably, you can put it on the context, all span attributes, and make it accessible for any process around there. Yeah. But anyway, you would give the… A set of attributes that contains All possible peer information, and it would give you the, yeah, the Duh.
So, it sounds like, … We are… we will describe the implementation of this thing.
But the implement… We better describe the interface.
as well.
Like, does it add things to the attributes? No, it probably just returns peer information.
The other thing about it is, okay.
It sounds like a generic problem. You give some component a set of attributes.
And it might give you something back.
To add, to enrich.
Is it the generic enrichment component, or is it a specific peer enrichment component? Why does it have to be peer-specific?
**GZ Gregor Zeitlinger** 28:34 Sure.
Because we are talking about a peer component.
Why would it talk about something else?
**Liudmila Molkova** 28:47 And you could… yeah.
**Trask Stalnaker** 28:50 Are we talking about, … How, like, how to make this gen… Like, adding a new spec component to… handled this. I'm not quite sure I, … I'm following… like….
**Liudmila Molkova** 29:11 So, oop.
**Trask Stalnaker** 29:12 No.
**Liudmila Molkova** 29:14 Yeah, let's assume we're just limited to the configuration.
Let's try.
… We have a… Let me just copy-paste it into the notes so we see it.
Alright.
Oops.
I'm sorry, no, it wouldn't work. ….
**GZ Gregor Zeitlinger** 29:49 You can paste it below the bullet points, then it doesn't… Add more bullet points.
**Liudmila Molkova** 30:01 And so….
**Jay DeLuca** 30:08 you know.
**Liudmila Molkova** 30:09 Oh, yeah.
Thank you. How did you do this?
**Jay DeLuca** 30:14 3 back ticks.
**Liudmila Molkova** 30:15 Oh, nice, thank you. Wonderful. Okay, so… … Let's remove comments for a sec so it's clear.
We have service mapping.
… If we limit it to the configuration, let's say tomorrow, we need to do something very similar.
for the… I don't know, 4… And there will be service mapping.
Bar.
Why would we do this?
to ourselves. Could it be… That there is a mapping section here.
And then there is a mature That says… That's work.
Pierre, … Press C++… 1, 2, 3, 4.
Hard to implement, I know.
And then the… action is… … And….
**GZ Gregor Zeitlinger** 31:41 This already exists in the collector.
Looks pretty much like you're writing it.
**Liudmila Molkova** 31:47 The OTTL, right. We… it would be hard to put OTTL here and implement OTTL In… inside Java, right? I would imagine it would not be straightforward.
**GZ Gregor Zeitlinger** 32:00 Yeah, that's….
**Liudmila Molkova** 32:03 … sorry, not service name up here.
Service.
Cool shirts.
And, well, we can technically come up with some simple YAML structures. We don't need to implement OTTL, we can say.
Equals… side… I don't know, side A, left and right.
**GZ Gregor Zeitlinger** 32:39 Sure, but it would still be, harder to implement and maintain … And I don't, have a use case for something similar.
So it would be, hypothetically.
if we would come up with something, but I would rather wait to see if we actually come up with this on a repeated basis.
**Liudmila Molkova** 33:08 That's a good point, yeah.
Okay.
I can get behind it.
**GZ Gregor Zeitlinger** 33:21 I would also like to discuss the other issues in the agenda.
**Liudmila Molkova** 33:26 Yeah, okay. Sorry for taking so much time.
**GZ Gregor Zeitlinger** 33:30 No, no, all good.
**Trask Stalnaker** 33:31 Oh, thanks for joining.
**GZ Gregor Zeitlinger** 33:38 … Alright, … Peer review is, basically just, the pull request about the bridge, that is… unlocking other PRs, so I can… Just look at that.
**Trask Stalnaker** 34:01 Yeah, can I share?
**GZ Gregor Zeitlinger** 34:03 Yeah, sure.
**Trask Stalnaker** 34:37 Yeah, this is going to be an interesting part of the rollout.
is… But… Making it super clear to people that it doesn't interrupt with the existing parameters.
**GZ Gregor Zeitlinger** 34:57 Right, yeah, there's going to be… A couple of PRs for documentation.
**Trask Stalnaker** 35:07 So, this is, this is moving… … Right. We're moving it from the… tooling… Okay.
Got it. So this is just a straight move, okay? Great.
And… … Thank you.
**GZ Gregor Zeitlinger** 35:32 You can see what is added, because that is what the real changes are, like, this new method is actually edit.
**Trask Stalnaker** 35:41 Okay, and it's not internal because you actually want to use it.
**GZ Gregor Zeitlinger** 35:52 In the Contra repository, right.
**Trask Stalnaker** 35:56 Oh, you want to use it in Contrib.
Right, I remember this.
So that this is what's going to allow… The contribib components to only implement the logic once, the declarative config logic once.
**GZ Gregor Zeitlinger** 36:15 The business logic ones, so… Getting, the… I don't know, region for GCP only once, instead of from two different places.
**Trask Stalnaker** 36:27 Right, right, okay, nice.
And it creates… Remind me which, … This is going to map This is bridging… will the GCP resources then use the config, the older config properties API, or will they use the declarative config properties?
**GZ Gregor Zeitlinger** 36:53 Sorry, say that again, I… I didn't get that.
**Trask Stalnaker** 36:57 … So… okay, this is bridging from declarative… To… the holder.
**GZ Gregor Zeitlinger** 37:07 You can also look at one of the PRs in contract where this is actually used. It's based on a copy of the bridge, but that copy will Obviously, be removed.
the spend stack trace is a… That's a simple one.
Inferred span, sorry.
**Trask Stalnaker** 37:37 Gotcha, okay, yeah, this helps, thanks.
So… Okay, so we've got the infer… the component provider for… this is for declarative config.
And….
**GZ Gregor Zeitlinger** 38:02 Yeah, the ad mapping is exactly the part where the bridge is utilized, and then it, … passes an object to the create method, and the create method Works for both old and new configuration.
So in the config method class below.
You see that it's config properties, and this can be the bridge.
**Trask Stalnaker** 38:31 I see, okay. And what if this wants to use… … The structured, the declarative config.
Like, I'm almost… I was….
**GZ Gregor Zeitlinger** 38:47 then, you, would not be able to treat it in a uniform way. So you would then have two different Configuration methods, and we already have, a con… In instrumentation in the agent, the methods instrumentation, that is first checking, am I using declarative configuration, then use method A, otherwise use method B.
**Trask Stalnaker** 39:16 I see, okay.
I was trying to think if it could even work doing the bridge the other direction.
Where you bridge the properties into declarative config.
So that you could then have one thing that has both the old and also could have New structured config in it.
**GZ Gregor Zeitlinger** 39:44 But, … That would only work for primitive types, like, if you are getting, a complex attribute using declarative configuration, but it's actually backed by system properties, then this would throw an exception or something, so at least it would be surprising.
**Trask Stalnaker** 40:07 I… But it wouldn't have… in that case, it wouldn't have, … Okay.
I guess that makes… that does keep it simpler to, like, if you want to… If you want, because we do want to encourage people to start using… more… more richer config options. But once you do that, say for, … The rule-based config… Is probably a good example.
Rule-based sampler, sorry.
**GZ Gregor Zeitlinger** 40:56 Yeah, exactly, that's a good example.
**Trask Stalnaker** 41:04 This one's only gonna support declarative config anyways, so….
**GZ Gregor Zeitlinger** 41:10 Right, and this is fine.
**Trask Stalnaker** 41:11 bridge.
Okay… Okay, and this is how we're doing it in the agent anyway, so… … … Is… so in the agent, We are… we basically… Split, and either… Now, what are we doing in the agent?
How does this work?
**GZ Gregor Zeitlinger** 42:10 We are using the bridge, … In the, startup phase, when we create the SDK.
And we also have this, ad mapping section.
There, I think.
Right.
**Trask Stalnaker** 42:40 If config provider is not null .
**GZ Gregor Zeitlinger** 42:44 This means….
**Trask Stalnaker** 42:47 They're not using declarative config?
**GZ Gregor Zeitlinger** 42:49 Well, we are using declarative config. Config Provider is a new… concept.
**Trask Stalnaker** 43:01 are using declarative config.
Otherwise, we just returned… SDK auto-create… what is this? Sorry, this is creating a wrap.
OpenTelemetry SDK….
**GZ Gregor Zeitlinger** 43:39 Exactly.
And, when you… Take the config properties out of it, then you get the bridge.
**Trask Stalnaker** 43:51 The config properties, and it can be used from the… Configuration file.
new… Okay, and the SDK, I was… I thought the SDK, if we're using declarative config, that it wouldn't use config.
Properties….
**GZ Gregor Zeitlinger** 44:21 That is right, so, … in the, getter from AutoConfig SDK, the properties return null .
And, … We're patching that to return something that is not Nile, but the bridge instead.
**Trask Stalnaker** 44:42 Oh… Okay, and that allows… The… because all of our components are still expecting To get passed in a config properties.
**GZ Gregor Zeitlinger** 45:00 Right.
**Trask Stalnaker** 45:14 Okay.
Yeah.
That is really… All very confusing.
**GZ Gregor Zeitlinger** 45:22 It's true. Great.
**Trask Stalnaker** 45:23 Thank you, Jay, for reviewing.
Let's get this merged….
**Jay DeLuca** 45:30 Yeah, I would say the one thing that I was just a little unsure about was just the changes to the… that build.gradle, but they seem okay to me, but, just around the exclusion of certain classes, I think because they were moved from the… the tooling.
**GZ Gregor Zeitlinger** 45:52 Yeah, we are, … Putting classes into the instrumentation incubator.
That belonged to a different, class loader. So previously.
all the classes, had to go to the bootstrap class loader, but, the bridging part belongs to the agent class loader.
That's why I had to add a couple of rules.
So, Incubator SDK is, the new part, and, yeah, the other five… packages, … go to the bootstrap class loader and, … Therefore, they are excluded from the agent class order.
**Trask Stalnaker** 46:45 Okay, and where are they included in the bootstrap?
Let's see….
**GZ Gregor Zeitlinger** 46:53 Well, it's a bit hard to see if you only look at the diff, you have to look at the full file to see that.
**Trask Stalnaker** 46:59 Okay.
**GZ Gregor Zeitlinger** 47:07 It took me quite a while to figure this out, honestly.
**Trask Stalnaker** 47:12 squared….
**GZ Gregor Zeitlinger** 47:13 So this is a method, exclude bootstrap classes, and where this is called, I think you can also see what is actually added.
**Trask Stalnaker** 47:28 Yeah, I'm just trying to remember how this worked with… Exclude the bootstrap part of this.
Did the bootstrap exclude non-bootstrap?
Bishop from the Java Agent Libs… Okay, right… Don't want those in the class data.
**GZ Gregor Zeitlinger** 48:07 Are you wondering how it actually looks in the layout of the jar file?
**Trask Stalnaker** 48:14 I was trying to see where… so, we're… Normally, we… Pick and choose an artifact, either lives in the bootstrap or lives in the… Agent Class Loader.
**GZ Gregor Zeitlinger** 48:32 Yeah, that is easier to handle.
**Trask Stalnaker** 48:35 Yeah.
Except we have this one exception here.
And… … So, okay, so then you needed these… You needed the bridge in the….
**GZ Gregor Zeitlinger** 48:54 Agent part, not on the bootstrap.
**Trask Stalnaker** 49:03 Oh, I see, that's why you have all the other packages besides the bridge here.
**GZ Gregor Zeitlinger** 49:09 Right. Gotcha.
**Trask Stalnaker** 49:12 And so the bridge you need in the bootstrap.
because it's accessed In the bootstrap at startup?
Why?
**GZ Gregor Zeitlinger** 49:30 You mean why those packages are in Bootstrap?
**Trask Stalnaker** 49:33 No, why did… why did you need the, … bridge in the bootstrap?
**GZ Gregor Zeitlinger** 49:39 No, it is the other way around. Bridge is not in the bootstrap, it must not be in bootstrap.
**Trask Stalnaker** 49:45 Oh, it can't be in the booth. I see. Oh, so they… these… Okay, why are these in the bootstrap?
**GZ Gregor Zeitlinger** 49:54 I did not, think about that part, but I wanted to change as little as possible.
**Trask Stalnaker** 50:02 Yeah, yeah.
**GZ Gregor Zeitlinger** 50:03 My… my understanding is, that, they… are not part of instrumentation, and therefore they can be in Bootstrap, but I might be wrong.
**Trask Stalnaker** 50:17 Generally, we default… we put as little as possible in the bootstrap.
It's just probably for bridging the incubator.
Because we bridge… … So… we bridge the instrumentation API So that when people use that in their… … In their apps directly.
We bridge that into the… Java agent, so that it interrupts.
**GZ Gregor Zeitlinger** 51:03 But isn't that for the OTEL API, not the instrumentation API?
**Trask Stalnaker** 51:09 I think it's both.
**GZ Gregor Zeitlinger** 51:11 Okay.
**Trask Stalnaker** 51:12 Let's… Let's see, instrumentation… So… You're definitely right, the main one is… OpenTelemetry API, this is the bridge there, but I think we also bridge….
**GZ Gregor Zeitlinger** 51:38 Yeah, right, I didn't know about that one.
**Trask Stalnaker** 51:40 certain… things. So yeah, we only bridge… A few specific things. So that's probably why… and it's probably shaded.
….
**GZ Gregor Zeitlinger** 51:55 Right.
Yep, makes sense.
**Trask Stalnaker** 52:05 Okay.
on… Yeah, I think it's… I'm, probably worth… we could ask Lori… … I, in general.
If he's got thoughts on that, he would be the… the one to have a better idea.
If there is one.
**GZ Gregor Zeitlinger** 52:31 Should I put it on the agenda there?
**Trask Stalnaker** 52:33 Yeah, yeah, let's just… May as well.
Cool, … I've got a couple more minutes if there was something short-ish that… Still wanted to look at.
But yeah, go ahead, you can start building. I think it generally looked good and, allow… allows us to move forward.
incrementing.
**GZ Gregor Zeitlinger** 53:10 No, actually, I don't have a short one.
But we can discuss where to discuss this,
**Trask Stalnaker** 53:17 Oh, the milestone thing?
**GZ Gregor Zeitlinger** 53:19 Exactly. Jane, I have talked about milestones. Is it something for the general meeting?
Or should we discuss it next week?
**Trask Stalnaker** 53:28 Throw it on there. We may have time.
I don't know if we have much… yeah, it looks like we don't really have much.
agenda yet.
**GZ Gregor Zeitlinger** 53:40 Yeah. Maybe people have something to put on, then I don't want to take the whole time, but if we don't, then yeah, let's do it there. And let's just stop here, then we have a couple of minutes.
Till the next meeting. See you there!
**Trask Stalnaker** 53:53 Bye.
