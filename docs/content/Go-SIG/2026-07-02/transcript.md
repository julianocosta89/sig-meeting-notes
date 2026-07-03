SIG: Go SIG
Date: 2026-07-02
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:18 Hey, how y'all doing?
**Kathie Huang** 01:20 Hi, good evening.
**Puneet Singh** 01:21 flow.
**Israel Blancas** 01:22 Hi, baby.
**Tyler Yahn** 01:30 Sorry, just getting set up over here.
I guess we're pretty early on. If you haven't yet, go ahead and add your name to the attendees list.
And if you have agenda items, please go ahead and add them as well, and yeah, we can get started here in just a second.
Robert, do cool down for you?
Awesome. Okay.
Coming up on 3 minutes in, so we could probably, get started here.
Yeah, cool. So, thanks everyone for joining. If, I don't think anybody else, yeah, I guess Dave is not on yet. Okay. Awesome. So first up, kathy, you want to talk about this PR?
**Kathie Huang** 02:38 Yeah, so before, I had merged a PR to add an Azure Container Apps detector to this Go SDK, but I was adding a detector in the collector contribo to delegate to this Go detector.
But then, David, said that, oh, like, I think I linked the collector contrib there, but he said, oh, like, is the Azure Container Apps detector emitting the service instance ID?
resource attribute, I'd be surprised if that was the case. I was like, yeah. And he was like, oh, I must have missed that in my initial review, because I guess the default detector in the Go SDK, like, populates the service instance ID, so we want to choose a different resource attribute.
And he added this to the release, milestone, so I was wondering if, like.
Yeah, I propose using Fast.instance, because that's what the GCP, like, the Google Cloud Run detector uses, but every other SDK for the Azure Container Apps detector uses service.instanceID, so… And the Azure-managed OTel agent, like, the Azure's, like, own version of the collector that they, recommend for Azure Canary Apps OTEL instrumentation also uses service.instanceID, so it's just kind of weird that this is a… a different… different resource attribute being used compared to all the other, like, SDKs and detectors, but I just wanted to bring this up since it was… since the other detector, or the Azure Container Apps detector is part of the release.
**Tyler Yahn** 04:28 Hmm.
Yeah, that's interesting. Robert's gonna stand up. Yeah, I don't see David on yet. Go ahead, Robert.
**Pellared** 04:39 Is there anything in the semantic conventions regarding this?
**Kathie Huang** 04:44 like, both fast. instance and service instance ID are semantic conventions, but I guess it's just, like, the interpretation of the semantic convention that's… that's the issue here.
**Pellared** 04:54 Yeah, yeah.
But is there, like, are you also working to clarify it in the semantic convention as well?
**Kathie Huang** 05:00 I could, I could, if we come to a decision. I could say, like, oh, fast.instance means the replica name for Azure Container Apps.
But nothing has been specified already.
**Tyler Yahn** 05:16 Hmm.
Yeah, is the Azure Container Apps, this is, like, the name for, like, their FAS solution?
**Kathie Huang** 05:26 Fast is the name for GCP. For Azure Container Apps, like, there's nothing specified about what the replica name, like, what resource attribute the replica name should be.
**Tyler Yahn** 05:36 Oh, sorry, I'm talking a little bit more ignorant. Like, like, the functions as a Service offering in Azure is called the Azure Container Apps.
**Kathie Huang** 05:45 No, it's more… that's Azure Function, so technically, like, Azure Container Apps isn't really… a function as a service, so we could use, what the Node SDK uses, which is azure.container underscore apps.instanceID. I think I, like, linked it in one of the discussions.
But that would involve adding that to the semantic conventions, I think.
**Tyler Yahn** 06:13 Oh, oh, I see.
**Pellared** 06:15 I renders some… Aren't there some semantic conventions for containers? Shouldn't it be just something like container instance ID, or something like that?
**Kathie Huang** 06:25 Yeah, we could… Try that… Although… although it's not technically the… instance idea of the container, it's like the replica name of the Azure Container app?
Which is, like, the equivalent of, like, an instance, but…
**Tyler Yahn** 06:46 Yeah, it's not… yeah, right, like, the container semantics, I think, are more for, like, when you're running, like, Docker locally, or VM, right? And, like, this is… Or a cloud platform thing, right?
Hmm.
Let's see, cloud doesn't have anything?
Probably not.
Yeah, I, I don't know.
Yeah, I, I… I'm with David, we probably want to have the service instance ID not be… the, containers app. I imagine, like, so, just for historical reference here, like.
this, this has always kind of been a tricky one. In fact, it's actually changed a few times.
Over the life of it, so I imagine that's why you're seeing, some conflicting implementations out there. It's just from, like, maybe they were implemented prior to it being changed to this random UUID, or… or just ignored it, I don't know.
I do think it's right to have it as a random UAD, UAD, having the other… Yeah, like, I just don't know what the other, if this should be a FAS instance, if it should be something else.
Yeah, the only concern I have for setting it to the fast instance is that somebody is going to actually expect it to be, like, then running a function as a service system, and, like, this is going to cause confusion for them. Using the node approach, like you were saying, where there's essentially, like, a one-off for what they do here.
seems a little bit more applicable. Obviously, you're stepping outside of semantic conventions at that point, but, like, if semantic conventions isn't covering this, it seems like that's applicable. I don't know if there's a really good answer here, though, I guess is kind of what I'm getting to.
I do think it's kind of a bug to not do this. I don't know if it's, like, the end of the world, but .
**Kathie Huang** 09:01 I see. What's the historical reason for having service instance ID populated with a random UUID?
**Tyler Yahn** 09:09 Yeah, that's a good question. So, I think it's uniformity in, like, the form that it actually is, and it's, guaranteed that it's unique, so there's not actually, like, Especially handling restarts, so if, like, this particular thing gets a restart, say your tracer provider gets a restart, it generates a new, resource.
it would have a new EUID. If you use the same, like, replica name, then it would not, is, I think, the concern. So, like, it's… it was… it was more to show a life cycle, I think was kind of, like, the big thing that you wanted to communicate in the service instance ID, because it would literally be a new instance.
Yeah, that's the historical reference.
Whether you agree with that or not, I think is, Anyways, that's a discussion from years ago.
So, yeah, so, like, that's where that comes from.
**Kathie Huang** 10:05 I see. Yeah, this is weird, because, like, the… the version of the collector that Azure owns also uses service instance IDs, so I wonder, like.
if maybe I can, like, try communicating with the Azure folks to see if they'd be open to, like, a more… more precise, attribute for the replica name, but that would be, like, a longer conversation.
**Tyler Yahn** 10:30 Yeah, agreed. Especially if they're using this somewhere internal in, like, their backends, like, that becomes pretty problematic for a lot of people.
Yeah. Is this resource detector going to be used inside Azure, or are you trying to switch, or do you know if they're trying to switch to using this, or are they just going to keep doing.
**Kathie Huang** 10:48 I don't know. I could… I could see if they would want to, but I don't know what they use right now.
**Tyler Yahn** 10:56 Okay. Yeah, I mean, I… I don't want to let… perfection get in the way of good enough here? So, like, if David's okay with going in this direction, I'm fine with going in this direction.
I… yeah, the only concern I have is just, like, the accuracy of this fast instance, and whether, like, maybe it's just worth switching to, like, the one-off node implementation, that's, like, not defined as bantic conventions at this point.
**Kathie Huang** 11:22 Right, so if we switch to the one-off one, would that just be hard-coding it here, and then, like, I guess later.
I would open a PR in a semantic mentions repo.
**Tyler Yahn** 11:31 Yeah.
**Kathie Huang** 11:32 buying that.
**Tyler Yahn** 11:33 Okay.
**Kathie Huang** 11:33 And then I would, like, come back to this one, and then, like.
**Tyler Yahn** 11:36 Yeah.
**Kathie Huang** 11:36 The semantic version.
**Tyler Yahn** 11:37 I think… I think that that seems fine, especially if there are no, like, existing semantic conventions that define this. Doing this, getting it out, and then following up with semantic conventions, and like, and maybe they come back to you and say, like.
No, just use Fast Instance, and then we can switch to that. But, like, I don't know what… like, I'd rather have them make that decision than, us, just because go… is, one language out of all the implementations that could be doing this, right? So it's rather to have consistency across the languages. Obviously, as you can see, like, Node has made a different determination on what the solution is here, so, like.
Yeah, this is where, like, that conflict kind of comes in, and we would rather not, like, propagate the conflict. So, yeah, if you could take that on as an action item, that'd be really helpful to the project as a whole, yeah.
**Kathie Huang** 12:18 Okay, sounds good. I can do that, yeah.
**Tyler Yahn** 12:19 Okay.
Cool.
**Puneet Singh** 12:22 I'm just anticipating that, you know, there might be some future effort that will be needed to to, you know, I don't know, synchronize the implementation between different languages? Like, are all SDKs implementing the same You know, use of the… attribute?
Between the different resource detector.
I don't know.
**Tyler Yahn** 12:50 Yeah, you're not the first to think of this, so this is not also restricted to, resources. Just keep that in mind, like, this is… this is just more of a general question around semantic conventions, and whether an implementation is actually compliant, and it isn't even scoped to the OTEL implementations, so, like.
Like, it's actually a huge can of worms. There's a lot of tooling now that exists with Weaver, and so there's also, like, the ability, and I think there's even projects started on this.
Where you can evaluate telemetry that's being produced and whether it complies with semantic conventions, as well as, like, its own schema. So telemetry schemas are also a cool thing.
I say this, like, because I'm very familiar with this, like, in the OB space, like, we are actually producing a lot of, like, other attributes that are not a part of, like, standard semantic conventions, but we still want to communicate to users that, like, we've extended beyond, or, like, we don't conflict.
But then it's also, like, how do you validate that? So, like, yeah, to your point, like, it'd be great if there's, like, a standardized project across OTEL that would take, like.
all implementations and say, like, here's the validation schema, which, like, is defined in semantic conventions, run it through Weaver, give me the telemetry you're producing, and then you get, like, some sort of CI check, or you get some sort of, like, score saying, like.
Yeah, you've complied or you haven't complied.
that's, like, some projects do that actually independently. I know that, like, in Obi, we do that, but some projects, like, that's not a big thing. So, yeah, I think that there's, like, a push at a higher level to try to get this, like.
uniformly looked at, but it's still, like, a work in progress, to what… to your point, yeah.
I mean, it's huge. If you really have some desire to work on it, like, I'm sure that help there could always be be, be welcomed, yeah.
But yeah, good point, yeah.
Because, yeah, I mean, you run into these exact problems, which we're in right now.
Okay, cool.
Moving on… Unless, Kathy, you needed something else on that one, I think we're done, right?
**Kathie Huang** 14:55 No, yeah, I'm good. I think last question would be, like, is this, like, a blocker to the release? Like, should I, like.
like, update the PR with whatever we decided to choose, like, the node-specific, like, the more… the one-off Semantic Convention right now.
**Tyler Yahn** 15:10 Yeah, it is a blocker to the PR, er, to the release, it's not… an imminent release, for other reasons not related to this PR. So, like, I think you have a little bit of time. If you want, you can just add a comment there, because David's not on the call, just pointing out, like, what we talked about in the SIG meeting, and that, like, this is the direction we're just going to go in for the time being.
And, yeah, and like, just to give them a heads up, that's the change, and, like, we can try to get this in.
**Kathie Huang** 15:35 Sounds good. Thanks.
**Tyler Yahn** 15:36 Yep.
Okay, Puneet, you want to talk about, status remapping in hotel gRPC?
**Puneet Singh** 15:49 Yep.
So, I think this was a request from a user. What they wanted was to have a different custom set of error codes and non-error codes per method level, actually. So, I looked into the semantic convention. It does have a option that it allows you to… I mean, the language says that it's, like, should, not must, so you are, allowed to override the behavior.
Of, you know, that what would be considered as error versus non-error codes.
But, the complete, you know, like, giving a full access would be to give user an option to execute a mapping function.
Versus something that is more restrictive, like, David suggested that to start with the most restrictive option to classify between error and non-error codes, which is applied across all methods.
option in middle, which I think of, is to provide that option, but at the per-method level. But I'm looking for two things. One is that the… for immediate resolution and… what is the path and what would be the path for long-term resolution? Is it something that has to be, discussed at the spec level? That is two of my questions, actually.
So just to have, you know, some sort of… To see if there is any consensus on the, you know, taking for immediate versus also for long-term mitigation.
**Tyler Yahn** 17:22 Yeah, good question. So, I think that, like, You copied your… you know, explicitly says that, like, you can configure it to set it to be okay, right? So, I think the spec… Has already technically, like.
weighed in on this, and you or us adding something specifically in the gRPC instrumentation is, I think, completely compliant with the specification, with what we're trying to do here. So, yeah, I think that we should feel empowered to make the change locally.
I do think that, like, if you are trying to represent, like.
communities that also use things other than Go, like, getting this into the, semantic conventions, maybe? Or, yeah, probably semantic conventions, because, like, the specification really isn't about, like, instrumentation implementations, it's more about, like, the API and SDKs. But, like, the semantic conventions really are about the, implementations.
I think this is, like, a good place, I think in the… especially even in the semantic conventions, they have, like, gRPC status code definitions there, and, like, what you're supposed to do.
**Pellared** 18:27 to the agenda.
**Tyler Yahn** 18:29 Okay, yeah. So, like, I think that that's something that, like, yeah, it's worth maybe calling out there. I don't think it should block getting some sort of implementation here, and, like, trying to define something here, I think that that's fine.
Especially, yeah, for, I think, a variety of reasons, but I think it's worth adding. I think it's a good idea.
the exact form of it, I'm not 100% sure yet, like, I'd have to look through some possibilities here, but yeah, I think, like, in general, I support the idea of adding this, and then… Bringing this to the specification level. Robert, did you have thoughts?
**Pellared** 19:05 My only thought was checking if other languages are having these options.
Unless you have already told it, and I'm…
**Tyler Yahn** 19:14 Oh yeah, so that's the other thing, is like, Yeah, I mean, having other languages having this option, I think, is also a good thing. The other thing I wanted to mention is that, like, the… declarative configuration should probably also be looked at. So, if there's instrumentation for gRPC, like, how would this, like, get mapped to declarative configuration? Because I think if you put in the semantic conventions, that's great, but you still need a way to configure it, so, like, I think that would be the next step, after it's defined there, is, I guess, the only thing I would say.
**Puneet Singh** 19:42 Right, I think that makes more sense, that this should be driven from the config level versus, you know, allowing user to submit a function which we don't know about, and gets to execute in the hot path, which is the exact concern that David also highlighted, so… so yeah. So what I understand is, for now, I think.
**Tyler Yahn** 20:02 So, just to be clear on that one, though, like, you'd still need a function in the gRPC instrumentation, or you need some sort of option, maybe not a function, but you need an option, right? Because declarative configuration accepts YAML, and then it needs to then, like, turn something on, right, or it needs to set something up.
So, that process still needs some option to do that. That's what I'm saying, like, the exact form of that option, I don't know, like, if there's, like, an anonymous function being passed here, yeah, maybe that's not the right form, but, like… Declarative configuration is, I think, great, but we still parse that and then turn that into interotation, right? So, like, we would need to have an option in the gRPC package.
**Pellared** 20:40 There's also one…
**Puneet Singh** 20:41 That makes sense.
**Pellared** 20:42 cloud.
I am not 100% sure why this is a shoot, not a must.
I think there was also one discussion, which was not about the mapping.
But about, like, kind of overriding… overriding the status for a concrete handler. So, I mean that, for instance, you have multiple methods, which would, normally, you know, which will return, for instance, internal status, but for one of them, you do not want to treat it as error.
So you just pass it as a context, for instance, you have some context magic that, for this, you know, for this handler, you want to overwrite it, but not for everyone, or for some, you know.
So, I would like to check if there's anything in the history, when this, you know, semantics were created, why it is not a must and a should, because I…
**Tyler Yahn** 21:35 I thought it must… because it was stable.
And it was already released.
Adding in another requirement would not be… it would be a breaking change to the specification.
But yeah, it was pointed out that, like, it's confusing.
For… and… And the incorrect behavior for instrumentation to go in and say, like, actually, this isn't… it wasn't… it wasn't necessarily, like, the confusion of it being, like, okay, it was the confusion that it went from unset to okay, was, I think, like, the big thing, because a lot of instrumentation were, like.
saying, like, hey, this request was great, like, I'm gonna say okay, but, like, really, the interpretation doesn't know if it was okay or not. It actually hasn't evaluated it, other than, like, very standardized, like, it knows it's not error signals, right? It doesn't know if it's actually okay. The ability to set okay was that for, yeah, users, especially, like, an HTTP interpretation.
they can take, like, they can find, like, an active span, and say, like, hey, I know you say this is, like, an error, but for gRPC status messages, or particular HTTP status messages, I know that, like, that's not actually an error, I'm gonna set it to be okay.
So that's why it's still possible to set, like, error to OK. The goal, though, is that for instrumentation, doesn't go from, like, unset to okay, is kind of the concern.
But I don't think that that's what's being proposed here. I think it's more like, we already have error codes that are coming in, and we want users to have the optionality to say, like, don't set the span to, error in these particular instances.
So yeah, I mean, I think there's a lot there, but I think that that seems reasonable to… to go for.
**Puneet Singh** 23:24 So, From what I'm understanding, that I should try to resolve this first at the spec level to, you know, to fix that what the mapping should look like, and then then move to the actual implementation. Is that the…
**Tyler Yahn** 23:42 I would… I would probably say parallel.
I mean, serial is one form of parallel, but, like, the implementation… like, having it at the spec level and defining, like, what that mapping is, like, that's really good for, like, the semantics. The syntax in Go still needs to be debated based on, like, what I'm seeing from David, right? Like, the form of that option is a debate on itself. So… Yeah, I mean, I think that that's, like, just… Yeah.
There's already, like, semantics around what errors in gRPC we should consider actual errors or not.
So I actually don't know if there's too much semantic… Like, conversation, other than the fact that, like, it should be, like, configurable, or… or essentially, like, in the semantic conventions, I envision seeing, like, that status page being updated, saying something to the effect of, like.
Here's the default recommended. Languages can also provide user overrides for each one of these, or something like that.
But yeah, I think that, like.
If you wanted to start pushing that in our local instrumentation, I think that that's also fine.
**Puneet Singh** 24:54 All right.
**Tyler Yahn** 24:56 I mean, the specifications as you can, right? It's compliant.
So, yeah.
Cool.
Alright, Penny, any other follow-up on that?
**Puneet Singh** 25:09 No, I think, that's more or less, I think, yeah.
**Tyler Yahn** 25:14 Cool.
Robert, next up, you want to talk about the logs API stability?
**Pellared** 25:20 Because so, I think we are close. You want to share, or should I share?
**Tyler Yahn** 25:27 Yeah, I can share.
**Pellared** 25:28 Okay.
So… I, I think from the API perspective, you know, in the published API, exported API perspective.
I think we… we are in a shape that we can start reviewing, making the compliant, you know, the compliance of the API and SDK, so I try to, I tried to double-check all of the existing issues, and I also recreated some which were already closed, because I thought that we have done it so long ago that things may have changed, and also the spec also have changed since we've done this, like, I don't know, 2 years ago, or something like that.
So I created it, and I have a question regarding the process. Like, initially, I didn't want to do it myself, because I was, you know, kind of designing all of those things, but right now, I start to… I think that maybe… if I do it together with AI, like, I will check myself and then ask also AI to validate the compliance, then maybe it will be good enough, but yeah, your own… from the maintainers, you know, you're only here, Tyler, I thought maybe also other maintainers will be here if they approve this approach.
**Tyler Yahn** 26:44 Yeah, I mean… Yeah, like, we, we… yeah.
You're the only one that's held yourself to the standard. Like, when we've done audits before, it's not necessarily… Yeah, like, it's… it's more asking for proof, I think, is the key here.
Like, in these issues, we're not asking you to say, like, yep, looks good. Like, that…
**Pellared** 27:10 I know.
**Tyler Yahn** 27:10 Right? I'm asking you to, like, show me in, yeah, like, in each comment, like.
here is how I can show you that this is… this is compliant. Here is how I can show you that this… so it's, like, if the issue's all about proof, and, like, by the end of it, like, you get to show that, like, everything's proved, or everything's not, and then, like, closing it, like, that… that's more what we're asking for anyway. So, like.
it's… it's an audit trail. So, like, yeah, like, if you… if you did that, and then somebody came back and read all of your things and said, like, actually, hold on, like, that's not valid? Like, there's nothing stopping us from reviewing it after you've closed it, or after you've posted that. So, like… No, I would… I would say feel… Yeah, and able to do that. Like, and then… I guess, also.
Just, now that we've been doing this for a while, like, it is extremely helpful when, like.
you know, after the fact the specification changes, or that specification says that, like, it was never intended to be interpreted a particular way, it shows that we have interpreted it one way, or we have found these sort of things. So, like, it's more, I think, helpful. Yeah, exactly. It helps show the historical thought of our maintainer process here. So then, I think.
As long as you're not just putting, like, yup, looks good, like, then I think it… You doing it independently is totally fine, yeah.
**Pellared** 28:26 Okay, I'll try to do it that way.
**Tyler Yahn** 28:29 Yeah, absolutely.
**Pellared** 28:30 And… and I think that… Right, because I was thinking, you know, how to follow up from this HCR now, because I know that we have some, I don't know, some little performance issues in the logs SDK, some place for improvements.
But I thought that maybe at this point of time, it's worth checking the API, because it may, you know, it may also then affect the internals, etc. So I thought that we were right now in a good place for making this audit.
**Tyler Yahn** 28:58 Yeah, sounds good.
**Pellared** 28:59 Okay, this one's double check. Thank you.
**Tyler Yahn** 29:02 Yeah, perfect.
Awesome.
Okay, that's the end of the written agenda.
I've already stopped sharing my screen. Cool. Any other topics folks wanted to talk about? Interesting projects they're working on?
Fun things they've seen in hotel in general.
Well, cool. Alright, if not, we can end the meeting early here. It's good seeing y'all. Thanks all for the contributions and all the hard work. We'll see y'all in a week's time, or asynchronous. Bye.
**Pellared** 29:38 Thanks, everybody. Bye.
