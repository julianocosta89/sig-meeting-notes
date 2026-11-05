SIG: Community Demo App SIG
Date: 2026-11-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tobias Oka** 00:22 Juliano.
**Juliano Costa (Dash0)** 00:23 I know, hello!
This one's gonna be… it's gonna be big.
**Tobias Oka** 00:30 What a discussion. I mean, I was almost getting the popcorn out, because… yeah.
**Juliano Costa (Dash0)** 00:39 I went and to reactivated the Michael popcorn, you know, like, the…
**Tobias Oka** 00:47 Yeah.
**Juliano Costa (Dash0)** 00:50 But I… I think we… we're gonna get, just Martin here. I don't… I don't know if Michele will be able to… to join.
**Tobias Oka** 00:57 Yeah.
Hi Martin, nice to see you in person.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:01 It's been a while.
**Juliano Costa (Dash0)** 01:04 Hello, hello!
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:05 So, Brussels was the last time, I think.
**Tobias Oka** 01:11 I'm not entirely sure when… if we met before, I mean, maybe you met Juliano in Brussels.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:18 Yeah.
**Tobias Oka** 01:19 I don't know.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:22 I mean… When do you mean… when did I see you, Juliano, last,
**Juliano Costa (Dash0)** 01:27 Last time it was QCon.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:29 CubeCon, yeah.
**Juliano Costa (Dash0)** 01:31 Yeah. You called me da-da-da guy.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:38 Yeah, but now I can use worse insults.
**Tobias Oka** 01:42 That's Josh Dashin', huh?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 01:47 Yeah, we can stick a big dash through the Datadog jokes.
**Tobias Oka** 01:55 Oh, man.
**Juliano Costa (Dash0)** 01:57 Cool, will you be at, Southlake next week, Marty?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 02:04 Oh, I will be in Berlin for lead dev.
**Juliano Costa (Dash0)** 02:08 Not cool.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 02:11 I will be at reInvent, though.
You going to… are you going to reinvent?
**Juliano Costa (Dash0)** 02:15 No.
I'd never be to reinvent. I don't know if AWS is my type of, folks, like, if the AWS crowd is,
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 02:27 Yeah, you know what my, my affiliation is, don't you?
I am a Microsoft MVP, and I.
**Juliano Costa (Dash0)** 02:35 Yeah, true. Yeah, yeah, yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 02:37 premier AWS conference. They are definitely not my people.
But they all like observability, so, you know.
**Juliano Costa (Dash0)** 02:47 I'm gonna open the… MIDI notes here.
And… They… I'll just copy… From last week.
Cool.
So, I think we have a hot topic to discuss, and Let's jump into it. Let me find the issue that I created.
to see… Yup, okay.
I'll share on the Meeting Notes doc.
But also here on the chat, so everyone can… and see.
So basically, we had a couple of, back and forth here, discussing… the work that Tobias was… was doing on replacing the SDKs in code with the SDKs.
coming in… coming in on the Docker file.
So the idea here is to companies like Datadog and Elastic that have their own distro for the SDKs, they can override the SDK and then use their own hotel SDK distro.
Instead of the… like, the idea is to… instead of the hotel, the idea is to make vendors' life easier when showcasing the demo and using the demo with their own SDKs.
The problem is that, in order to do that, the initial PR that, got merged from Tobias, was one that, it's fetching the… the SDK from the…
**Tobias Oka** 05:28 operator image.
**Juliano Costa (Dash0)** 05:30 From the operator, yeah. That's great, because Dependabot can bump those dependencies, but the problem is that this is not… a good practice. I know that in the demo we have a couple of stuff that is not recommended in production, but this is a… total new approach, and not recommended at all. So, like, if folks are using auto-instrumentation, they would do it in a different way, and not on the Dockerfile.
So, the point… the thing that I want to discuss is, like, what we do here. There are two threads going on. I linked on the… on the issue. One is on the demo, and another one is on the hotel packaging.
The, the packaging one today was, fun. I… I grabbed, popcorn and, just… I spent some time seeing Marty and… and Michael talking, so… Yeah, so the thing is… do we have a way to do that? Is that something that we should do?
And, yeah, next steps.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 06:42 So… So the essence of where that thread came to was… The demo should match the docs.
We shouldn't be doing something in the demo that, is a jump from people who, build using the docs.
So the… when we were updating all of the docs, so me, Philip, and Severin going through, updating all the Getting Started docs, changing all of the, Changing all of the, the getting started.
**Juliano Costa (Dash0)** 07:17 I deserve it.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 07:18 to ride the day.
**Juliano Costa (Dash0)** 07:19 Guys, yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 07:19 working on all of the, zero-code versus auto-instrumentation versus, custom instrumentation language. So originally it was auto-instrumentation was a word that people were using for zero code.
But also auto-instrumentation was being used for libraries that auto-instruments common functions in your code. So, an auto-instrumentation would potentially be instrumenting HTTP client in, Go or .NET, But also meant side-loading an SDK, and we went through and we normalized all of the docs. So we had 3 different ways of talking about this, which is zero code, which is the idea of sideloading the SDKs and the instrumentation libraries.
To do auto-instrumentation, and all of that is done from the outside. You don't change any of the code.
And then the, the auto-instrumentation, is using libraries. Both zero code and custom instrumentation, where you do coded, sorry, zero code and coded instrumentation.
can both use auto-instrumentation libraries. That's the distinction that we came up with in the docs, and the getting started for each of the languages starts with coded instrumentation.
That's when… when we did that, we also updated all the demos to use the same syntax. So, when we did the .NET one to update the cart service, it was to follow the same syntax as the Getting Started Guide uses when it's doing the roll the dice, so the two matched up.
So, that was when we did the whole, like… there was a whole thing around how the .NET team wanted to host the… all of the demo code inside of their repo, rather than in the demo repo, and there was a whole debate around how all of that should… no, it should match the docs. We shouldn't be matching what the OTel SIG want.
we should be matching it in the docs. The docs are the first place that we go to, and then everything else should come off the back of those docs.
what we've started doing in the demo with that PR and then the subsequent four PRs around, moving that around, is different to that.
That isn't an approach that's in the docs at all.
There's no guidance in the docs that says, sideload the SDK and then use the API in your code, there's no examples of that.
So, if we do want that to be an approach for the demo, that should be tackled from the docs, it should be tackled from the TC and the GC, as this is the narrative that we're pushing on how people will do that. We need to be talking to the end user SIG to work out whether this is going to change people's ideas around OTEL. We can't just come at this from the demo and say, we're just going to change the demo because the packaging SIG have built some Linux packages.
it needs to be tackled from the demo, and that's where I was coming from, is I don't really care which one it has.
I care that it is deviating from what we've done.
by side-channeling it through the packaging SIG.
**Juliano Costa (Dash0)** 10:17 -
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 10:18 That's… you know, if that is the desired approach, it comes through GCTC, it comes through End User SIG, it comes through, on the docs, as this is how we recommend that you get started with OTEL, then, yeah, that's what we should be doing. But we shouldn't side-channel it through the packaging SIG and change the demo to do it.
But, and then there's the debate around, do we do both?
Which is absolutely fine, we should… we should perhaps do both.
But if we're doing both, even if we are doing both, that second approach of using the sideload the SDK, and then do your custom instrumentation on top.
That should be in the docs. There should be something in the docs that we can, revert back to and say, this is the approach that this replicates.
Doesn't really matter which one, but unless it is debated in the docs, the TC and the GC, and user SIG, We shouldn't be bringing it into the demo yet.
**Juliano Costa (Dash0)** 11:19 Yeah, and I think that that goes also together with the review that we got from Pyotr on the…
**Tobias Oka** 11:30 botnet.
**Juliano Costa (Dash0)** 11:31 on the .NET. So, in the .NET, Tobias also opened the same… following the same approach, and he pushed back a bit, saying, hey, yeah, this is cool, but that's not the way that we recommend doing, so… Yeah. And people use the demo to learn.
And if they… and also, the LLMs use the demo to learn.
**Tobias Oka** 11:54 Yeah. Oh my god, oh my god.
Yeah, people.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 11:57 pinging me on this. But, so, this wasn't, like, me just jumping in. There was a ton of people pinging me and going, have you seen what's happening here? I don't understand it, from various different languages and maintainers.
Normally, this would have probably been funneled through Pierre, but, you know… People tell Pierre, and then Pierre tells them to go and speak to me, so… I'm like, I don't maintain this, but fine, okay, I will have a chat with people about it.
But like I say.
**Juliano Costa (Dash0)** 12:25 Nope.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 12:25 As long as it's in the docs, as long as it's the sanctioned way through TCGC and end user.
I… you know, there's no… nobody can complain.
**Juliano Costa (Dash0)** 12:33 Yup, the, the, the point… so, like.
The problem is that we have plenty of stuff to demo, or to showcase, that we do not have the demo as of today. For instance, I know that, the OBE folks, they have their own demo on… on… Under the REPL, because to showcase eBPF instrumentation, you need an uninstrumented service.
So the main problem is the Demo SIG maintaining another version of the same demo. Like, we don't have the bandwidth, or we don't have the human power to…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 13:18 Don't have the bandwid.
**Juliano Costa (Dash0)** 13:19 I didn't do what I do, man.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 13:20 now, so…
**Tobias Oka** 13:20 And it was even… it was even how I originally got exposed to the demo, because I was having this conversation with Juliano, and I was like, oh, there are those use cases where it would be cool to have a non-instrumented demo, and we were discussing, like.
how would this even look like? I just, technically, like.
It's not really clear how you would even do such a thing.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 13:42 Thank you.
We had the lengthy conversation in Brussels.
About exactly this, about, you know, do we have, optionality in the demo?
Do we have accounting uninstrumented as, a potential solution, that doesn't have the SDKs and allows somebody with Docker profiles and Helm chart, changes to be able to switch between them?
And everything just became so complicated that it would actually take away from the real you know, value of the demo, which is that, you know, out of the box, oh, I can see how I instrument my code.
You know, I don't think anybody's got anything against the idea of sideloading the SDK.
But it needs to go through the docs. Let's do that.
And then, we can say, right, that's the right approach.
Which means that we then get docs on how to do it in Docker, we get docs on how to do it in an EC2 instance, we get docs on how to do it in all of these different scenarios, and then we can showcase those examples.
**Tobias Oka** 14:43 Yeah, and to do that with .NET will, I think, still be a challenge. Like, yeah, I mean, that's the conversation I took away from… or what I took away from the conversation with Jotre, was that I tried to understand how this would even technically work at .NET. Like, yeah, I think we would basically…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 15:03 So I would stay well away from .NET.
So… Just to be clear.
I'm a Microsoft MVP, I work with Microsoft DevDiv, most of the people who work on Aspire, which is the people pushing OTEL right now, are my friends.
I know a lot about where they go, and if we change things in that direction, it will tip some boats. And that won't be a good thing.
**Tobias Oka** 15:30 In what direction are things going?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 15:33 So everything now in .NET is Aspire.
Aspire as a… as adopted hotel as a standard.
It nearly didn't.
when there was the whole, dependencies and EOL stuff, around how OTAL works.
they were about to ditch the OTL SDKs completely and move on to .NET Monitor, But that got mitigated.
And they've kept with hotel, but, you know, if we start saying, no, this isn't the one true approach in hotel, and that contradicts with what the approach is in Aspire.
which is Microsoft's big bet, then there's gonna be a lot more contention.
**Tobias Oka** 16:14 Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 16:14 It might mean they ditch it from the service templates.
**Tobias Oka** 16:18 I think it anyway needs to be a language-specific approach, because every language kind of behaves a bit differently, so…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 16:25 Yeah, I mean, you don't even depend on the… you know, the idea of depending on the OTel API isn't a thing in .NET.
you shouldn't depend on the OTL API, you should depend on the system.diagnostics.activity.
**Tobias Oka** 16:36 Yeah, I remember instrumenting a .NET application a while ago, and reading the docs, and I was like, where the heck is the API? And then I found out about this. Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 16:45 Yeah. It's because… so it's because, I mean, in Microsoft World, this is because we've had that since 2014.
activity sources existed in 2014 when they took a bet on, OpenCensus, which is why the API more maps to OpenCensus than it does OpenTelemetry and then was repurposed. And span is a type in .NET, Which is more of a byte array, which is optimized, so you can't use the word span to mean span.
So, yes, anyway, I can talk a lot about the history of .NET.
But yeah, I think, you know, we have to take an instrumentation-specific approach to each one of them. You know, Java, for instance, usually… I mean, the accepted approach for Java is always to sideload the Java Agent SDK jar.
That's always the recommended approach.
However, there are then two recommended approaches for how you instrument your code.
you can either use the XML to instrument your methods and do that in a side-loaded way, or you can actually go in and annotate your methods and do it that way. We should probably show both of those. Do we show both of those? No.
**Tobias Oka** 17:55 I would never show XML. XML sucks. Like, that's my… my take. I mean, it's better…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 18:02 and Jason.
**Tobias Oka** 18:03 Which is…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 18:04 you know, better than YAML, so… So yeah, you know, that's… that's my stance, is let's debate it in the docs, let's debate it, as what is the approach that we want to push out in the Getting Started Guide.
So that we can say, this is how you do this in the demo, and then change the demo.
**Tobias Oka** 18:34 Yep.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 18:38 So the other point of this as well was, we have two different deployment methods and two different ways of running the, Two different ways of running the… we've got the Kubernetes Helm charts.
And we've got running Docker Compose locally.
**Tobias Oka** 18:54 Yup.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 18:55 Those are the two ways that we've got to run this, and obviously, there's potential that you can run each… some of the individual applications can run on their own.
Which of those is the ones that we're gonna support?
is the more interesting thing. When we're talking about the Docker stuff, the Docker Compose, like, sideloading a second Docker container is actually not hard.
If we want to use the injector.
But where do we grab the injector from? Where do we install the injector? Is this part the Docker image, or is this part of the Kubernetes approach? That was the other thing that was a little bit interesting to me, was if we are going to go down the injector approach.
Should this be the Kubernetes operator sidecaring things in, in the Kubernetes world?
And then in the Docker world, what do we do?
Do we just say that we don't support Docker anymore? Or do we actually build the injectors into each one of the Docker images, and do it that way, and then say that we don't do it via the operator in Kubernetes?
**Tobias Oka** 19:49 Docker also has something that is similar to init containers, I forgot how it's called.
where you could do something that is very similar to Kubernetes, but then again.
I'm not very much in… dockerland slash… kind of… quote-unquote manually managed container lands, and I'm not sure if that's really a best practice.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 20:11 No. But you've also got, like, how do we run this in Fargate, which is a very real use case that people do.
**Tobias Oka** 20:17 We run this.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 20:18 with, the containers inside of Lambda.
how do we run this in Azure Container Apps? How does this relate to running things with OpenShift?
But this is why we do it through the docs, and not side-channel it through packaging, because that's where we answer those questions, and say, we need a doc on how to do it in X, and then we can go and Implement it.
**Tobias Oka** 20:44 So, basically… the docs… and I mean, like, I'm just, like, a noob here, as you're seeing, right? But, so basically, the… when you are… Kind of introducing When you have been introducing new approaches to something, like, traditionally.
how do they actually come into being? Is it that, first, something is… kind of implemented somewhere, like… like the… like the injection, and then over time, some, like, approaches of how that might be used, approaching… get created in people's minds, then the… then the docs get changed, and then it comes into the demo. Because, you know.
The ability to do so, like, exists.
Already, one could say kind of coincidentally.
But, like, nevertheless, it exists. Like, what is actually the source of truth? Where are things kind of stemming from?
when we're doing something new in OpenTelemetry.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 21:52 I say it happens in a few different places, so… And I think each of the different changes has different origins, so if you were doing SEMCOV, for instance.
then you need to go and show it somewhere, which is why Service Criticality ended up in the demo, to be able to show where that came from.
If you're in… if it's a new instrumentation approach.
Then that needs to be guides.
in the hotel demo on, this is a way to do it.
So, there is a guide section.
There's, like, OpenTelemetry for Ops is one, there's OpenTelemetry for Dev is another one, I think.
I can't remember the names of them, we've… They've been moved around quite a lot, over the years.
But we used to have a specific guide section, which is what Dan's been pushing for on the blueprints. So, you know, these are established patterns.
On how to do it.
Where you would implement those patterns is not in the demo. You wouldn't go and change the way that the… you could do a branch of the demo to show this is how it could work.
But that's not particularly necessary, other than being able to show this is an approach that works. You know, build the comprehensive doc site that says, this is how you get started with SDK sideloading, or whatever, what hybrid ops approaches, or whatever you want to call it.
Then, to me.
The next step would have to be change the way that getting started works for each individual language.
Because if the getting started approach shows how you do a program CS, how you do a, a tracer.js.
And then in the demo, that's not the way it works, that's gonna be… A little bit of a disjointed experience.
But you start with something like this, to me, as a guide inside of the hotel demo. Sorry, inside of the, the hotel docs that says, this is an approach to side-loading SDKs.
Everybody can see it. Everybody can say, yes, that's a better approach.
And then… You know, we'll get the impetus behind it.
I wouldn't say there is a, yes, this is exactly how you would implement… you would go about building a new approach to instrumentation.
I don't think we're that mature.
**Tobias Oka** 24:23 Okay, I mean, yeah, makes a lot of sense to me.
So, me, again, not being super experienced, like, with all of the different SIGs, where… would I actually get going? Like.
like, is there, like, a particular repo where I would open an issue, or, like, is there a channel on Slack where I would kick this off? What people would I be talking to?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 24:58 open to other opinions, I have opinions, but I've been talking a lot, so…
**Juliano Costa (Dash0)** 25:04 Well, I think that the idea that Martin brought up, and the example that he shared regarding the service criticality.
Was a good success case.
Where the user is suggesting service criticality. He came to the demo and said, hey, I want to introduce this.
And we were like, no, thank you.
And he farted it, then used the demo to showcase the thing, and then presented to the… to the spec.
group to dispex Inc.
Then they approved and accepted the service criticality into, a semantic convention in hotel. Once that got in, then he came back to us and said, hey, now it's part of the semantic conventions, can we have it on the demo? And we were like, yeah, that's awesome, thank you.
So, that was a case. In your case, Yeah.
the… I don't know if blueprints are… reference implementations is the best place to start here, Martin, because In his case, he wants to… So, I think the idea of having a PLC in a fork, with… This approach, or the solution that you come up with.
And then, bringing that back to the… to the team.
The problem is that which team that would be.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 26:45 So, the owner of each of the Getting Started languages, the owner of each one of the languages on the docs.
Is the individual language sakes.
So, for something like this, if we're not going to go at this as a generalized approach.
I would say…
**Tobias Oka** 27:05 Each one of them.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 27:05 the languages.
**Tobias Oka** 27:06 Yes.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 27:07 You need to go in and put a Getting Started Guide.
For, you know, getting started with side-loaded instrumentation, or whatever you want to call it.
It needs to go in there.
They need to approve it.
And say, yes, we are changing the Getting Started Guide to that now.
So, if you went into the .NET one.
**Juliano Costa (Dash0)** 27:27 Well, we don't need to change, we can have an extra one. Like, in Java, I think we have 4 different ways of getting started.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 27:36 Yeah, but what the demo does is map to the first one on the list.
**Juliano Costa (Dash0)** 27:40 Not necessarily. In Java, we have the Java agent, with ad service and, fraud detection, that is Kotlin, but we recently had a Spring app.
And in the Spring app, we wanted to showcase a different approach, so we… we had the Spring Initializer, Spring whatever it's called.
That's fine.
**Shenoy Pratik** 28:05 Yeah, yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 28:05 Yeah, so if you look at the docs for Java, the first one is the agent, and we have that.
**Juliano Costa (Dash0)** 28:10 Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 28:12 And then there is another section on there for the Spring Boot Starter.
And the Agent Getting Started Guide, because there's multiple ways to do the agent as well.
What I'm referring to is the getting started guide for the Agent is what maps to… Broad detection, I think it is.
**Juliano Costa (Dash0)** 28:30 Ad service, I think?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 28:32 Is it ad service? It's there.
**Juliano Costa (Dash0)** 28:35 Anyways, yeah, I… yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 28:38 But I think that's where it needs to be, and the, you know, especially like we were talking about the .NET one, for instance, you know, that needs to be… the way that you want to do it needs to be a… a section inside of that .NET guide.
And either, I mean, I think bare minimum for me, is the first thing that somebody hits when they look at the .NET Getting Started Guide. There is an example of that in the demo.
If we do another one as well?
Great.
But it needs to be immediately obvious to somebody to be able to go, like, okay, because I use this in my workshops.
when I'm showing people how to do the .NET stuff, I will show them the instrumentation of the cart service for .NET.
And say, look, this is a real-ish application, and this is how it's instrumented.
going from the getting started Gox in OTEL over to that, and saying, look, this is how you do it.
So… I… I would say we do need that change, if we want to change.
what the cart service does, using .NET as an example.
If we want to change the instrumentation, the way that the CART service is instrumented for the SDKs.
It should be changed on the .NET docs.
**Tobias Oka** 29:50 To be honest, I still don't… to be honest, you know, after our discussion, like, I don't really think we should necessarily change the existing services.
Because… I mean… maybe for Java, there could be an argument, because you anyway kind of have, by default, to put in the Java agent, so maybe that's kind of the closest to where a change might make sense, but I… for the other languages, I think this is more… An option that you would want as the default when you Build this in an organization that has, like, a separate platform or ops team.
Where, you know, The person who puts… like, the… some manual annotations or stuff against the API into the code is different from the person that then afterwards has to… kind of… Deal with the whole… Open telemetry system and, like, the telemetry backend and all of that stuff.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 31:00 I mean, I can… I can go into my opinions about that specifically, if you want.
**Tobias Oka** 31:05 Feel free.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 31:08 That's a completely different debate.
**Tobias Oka** 31:10 Yeah.
Yeah, no, it's just, like, this is a reality that exists in many companies. Whether or not that's good, I mean.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 31:22 So, I think there's another analogy here.
And we talked about this, Juliano, in, Brussels, which is the declarative config stuff.
And how… Ultimately, that is going to be the preferred path.
for all of OTEL, is to use the declarative config to change the instrumentations that are added, to do things like changing sampling strategies, and propagation, and essentially doing the entire SDK setup.
that will be the recommended way in OTEL, is don't configure things in code, is to use the declarative config and load that in. That's what we will likely end up showcasing once that is completely GA across all the languages.
In the demo.
Because that's what… hotel is moving towards.
that's coming from end user, that's coming from TC, that's, you know, the entire thing.
That, to me, is where those configurations live. Like, oh, I'm the person managing the backend. Okay, push out your declarative config on all your, On all your applications, and the applications will just feed that in.
Sideloading the SDK is a different thing to that.
And that's not gone through that same rigor.
**Tobias Oka** 32:45 Actually, I wasn't aware of the declarative thing, I'll have to read up on that.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 32:55 But yeah, I completely agree that zero code is a thing that a lot of organizations need.
The ones where the… SRE, not real SREs, the SRE team, can only sideload things through Using zero code.
And in those scenarios, nobody uses actual, custom instrumentation, because they don't really care.
100%, those organizations exist.
I just… those, in my experience, aren't 90% of the customers.
And especially not the vocal part of OTEL.
**Tobias Oka** 33:34 Yeah, so, I mean, I can't talk to, you know, what is the most vocal part, right? I'm just seeing that there is A use case for it, right?
And…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 33:46 100% there is, yeah.
**Tobias Oka** 33:47 Yeah, and I'm just seeing, like, what is the way to make that happen without making the rest of the community suffer? Because that cannot be the, like, the goal, right? To make everyone else suffer, because… like, some, some small group, like, wants something or needs something, yeah.
So I, like, basically what I am… what I take away is, to go, through the docs, do it language by language, and actually, you know, think about, okay, what approach, actually, like, for which languages does this even make sense? Because again, like, for .NET, I'm not very convinced that this even does make sense, and I hear you concur with me there.
And so, Yeah, I mean, that's gonna be my approach, like, basically, like, taking, like, removing the PRs for now.
maybe I will make a… make a… make a… make a temporary fork. I don't think that's, like, really the big question, if that… like, I have a code there, I can make a fork, that's not really the problem. But, Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 35:01 make some PRs into docs.
**Tobias Oka** 35:03 Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 35:03 Look at the languages, like, do what you're saying, like, the… Work out which languages you think this makes sense in.
**Tobias Oka** 35:10 Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 35:11 work out how you would tell people to do this in the docs. Where would it live in the docs for that language that says, this is how we would recommend you do this, why that is useful, under what scenarios is that useful, over zero-code instrumentation? How does it differ to the zero-code instrumentation? Yeah.
Find the place for it in the docs.
**Tobias Oka** 35:33 And that gets… and then get… and then get… and then basically get… get people's input on, okay, like.
What even would for… for example, Java be the right approach to do this sideloading?
Okay, yeah, sounds like a good approach.
No.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 35:57 Sorry, I've talked through most of this, and I've scared everyone off.
**Tobias Oka** 36:01 I mean, for me.
**Juliano Costa (Dash0)** 36:02 Personally, yeah.
**Shenoy Pratik** 36:04 This was useful. This was useful to know the voice of the community, and then understand the pain points, so that… Yeah. Even as a domestic maintainers and community, we understand the influence And the things that we need to do going forward. That was really helpful, Madam. Thanks for all that.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 36:23 So yeah, I'm planning on being a little bit closer to, Demo, because I've got a ton of extra things that… We're pulling in some new scenarios.
And a lot of those are around custom instrumentation, and how to showcase incidents that affect You know, smaller segments of users and that kind of stuff that you can only really find through custom instrumentation, and we need to do a few more of those.
Making the services a bit more robust, and… I've just implemented OpenTelemetry Postgres, for instance, which will do Postgres tracing with SQL Commenter.
**Tobias Oka** 37:05 Oh, that is… that is very interesting.
**Shenoy Pratik** 37:06 192.
**Tobias Oka** 37:07 Yeah.
**Juliano Costa (Dash0)** 37:09 And that should be really… Where is the PR?
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 37:12 It is currently under by Practical Hotel.org.
Because I've just created a brand new, library called OpenTelemetry-Postgres. If you go to practical-hotel, practical-hotel slash OpenTelemetry post-postgres, there is a, a repo there that's, me and my dev minion, otherwise known as Claude, built out, Which is a…
**Tobias Oka** 37:40 Yeah.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 37:41 a very, I mean, kinda does what PG tracing does, but does it in a very different way.
A nanosecond OVAD.
Level.
But it'll use SQL comments and stuff and runs things out of band.
But, yeah, there's a few things like that that I'm gonna try and get, ported over from our demo that we use inside of ONICOM.
But, yeah, I've also implemented some more Kafka things, some non-act events and stuff like that.
**Tobias Oka** 38:19 Nice.
like, my company is probably not going to be super happy about that hint, but anyway, the code is open source, right? So, for database tracing, for different database engines, Datadog has built something that basically does this sort of, kind of.
Trace context propagation via context… via comments.
I mean, every database language engine needs, obviously, looks slightly, slightly differently, but… It's open source that can be taken inspiration from.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 38:51 Yeah, so this one was, specifically built on the idea that you shouldn't have to recompile Postgres. You can sideload the release into a Postgres container that already exists.
**Tobias Oka** 39:02 Yep.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 39:03 Which is very.
**Tobias Oka** 39:03 It's the same thing with the, like… But the Datadog approach is basically also not recompiling, but it's basically, like, how can you… How can you… Like, work with existing, schemas, or, like, reporting schemas and stuff to… to… Like, pull stuff together that kind of works a bit like a trace, but isn't really a trace.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 39:33 Yeah, I think there's… PG tracing does way more than the real… all I wanted was server spans from the database that can include a query plan.
And to do that without having to, make it push a query plan back on the request, and use all the instrumentation libraries. So… But yeah.
**Tobias Oka** 39:52 Pretty difficult.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 39:53 But yeah, it's stuff like that, that we're, like, we're getting into a point now where we want more data, and be able to showcase some more of the things around the demo that aren't just the languages.
Because we historically haven't really instrumented Postgres.
So, I also added a thing to the Helm charts, which I'm… Working on at the moment, which is to add in the… resource URLs, resource annotations.
So, everything will get resource.opentelemetry.io slash service name.
In the demo, so metrics from K8s get attributed to individual services, which they don't do right now.
So, yeah, I've been working a lot on the demo for Honeycomb recently, and… So yeah, I will be getting a little bit closer to the demo, and probably submitting some more PRs, and stuff like that, and… If there is stuff that I can help out with reviewing stuff, please let me know.
I cannot commit time ahead of time, which is why I wouldn't be… trying to be a contributor or maintainer, long-term, but, you know, if there's stuff that you need help with, I'm absolutely here to help. And, you know, I will absolutely review some PRs for you and stuff like that. I just… I can't give you a commitment.
Of time.
So…
**Juliano Costa (Dash0)** 41:14 Please do that. That's her any…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 41:15 Tell me.
**Juliano Costa (Dash0)** 41:16 That's already helpful, yeah, and also you joining the SIG and giving us the master class is already helpful, so thank you.
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 41:26 It's fine, I have a shit ton of historic knowledge in my head.
So…
**Tobias Oka** 41:32 Could notice that today.
**Juliano Costa (Dash0)** 41:36 Appreciate it, appreciate it, Martin. Guys, I need to drop, so… Tobias, would you be able to… roll back the service that we have there on the… on the issue, the 4252 that I opened.
**Tobias Oka** 41:55 I mean, at least I can… I can open a PR for it, you will have to approve it.
**Juliano Costa (Dash0)** 42:01 Yeah, yeah, yeah.
**Tobias Oka** 42:02 Yeah.
**Juliano Costa (Dash0)** 42:05 And, I think that's the first step, at least on the demo side.
Then we can… if you need help on opening a PR on docs and stuff, just let me know. I know some folks, and I can help.
**Tobias Oka** 42:20 Yeah.
**Juliano Costa (Dash0)** 42:21 Yeah, everyone is…
**Martin Thwaites (Hound Technology Inc. dba Honeycomb)** 42:23 Tag me as well, I'm happy to provide, you know, some… Some backup on the docs PRs.
I want to be clear, like, if this is the right approach, I am 100% behind it.
And I will help as much as I can with pushing it through.
**Tobias Oka** 42:38 Cool.
Thanks a lot.
Much appreciated.
All right.
**Juliano Costa (Dash0)** 42:43 Thanks, everyone.
**Shenoy Pratik** 42:44 Thanks. Talk to you. Bye-bye.
