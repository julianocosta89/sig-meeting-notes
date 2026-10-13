SIG: Kotlin SIG
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rafael Nicolau** 00:34 Hello, good afternoon.
**Jamie Lynch (Palo Alto Networks)** 00:38 Hey, bud.
**Rafael Nicolau** 00:41 Just me to be sure. Can you hear me?
**Jamie Lynch (Palo Alto Networks)** 00:44 Yeah, I can. Can you hear me okay?
**Rafael Nicolau** 00:46 Yeah. Just fine. Great.
**Jamie Lynch (Palo Alto Networks)** 00:49 Hey Val, I'm Jamie. I think I've been reviewing your PRs.
**Rafael Nicolau** 00:56 Yes, yes, yes, I'm Rafael, as we've spoken before. I don't know if… is anyone joining, this afternoon?
**Jamie Lynch (Palo Alto Networks)** 01:04 Yeah, it… Typically, like, typically folks will kind of, like, jump in, and I can see that Jason has added a couple of items to the agenda, but I think folks might just be a couple of minutes late.
**Rafael Nicolau** 01:18 Alright.
**Jamie Lynch (Palo Alto Networks)** 01:24 So where were you based Rafael?
**Rafael Nicolau** 01:27 Portugal. I'm from Lisbon. Born and raised, basically.
How about you?
**Jamie Lynch (Palo Alto Networks)** 01:35 I'm based in Manchester, but yeah, thanks for… thanks for joining.
**Rafael Nicolau** 01:41 Okay.
**Jamie Lynch (Palo Alto Networks)** 01:44 So what we normally do is there's this document here. I'll just paste it in my chat. And if anyone has any topics that they want to discuss, you.
are welcome to basically add them as an item down here.
And also feel free to add yourself as an attendee.
**Rafael Nicolau** 02:06 Okay. That's a document that's linked on the readme. Right?
**Jamie Lynch (Palo Alto Networks)** 02:10 I think it's linked on the README. I've also just pasted it in the Zoom chat.
**Rafael Nicolau** 02:15 Okay, thanks.
**Jamie Lynch (Palo Alto Networks)** 02:21 Hey, Jason.
**Jason Plumb** 02:23 Hey, good morning, good afternoon.
**Rafael Nicolau** 02:26 Hi there.
**Jason Plumb** 02:31 Look at me front loading a couple of pretty nonspecific topics.
**Jamie Lynch (Palo Alto Networks)** 02:36 Yeah, I got confused. I thought that was from last week because one of them is quite similar to the Android.
**Jason Plumb** 02:42 It's been… Yeah.
Yeah, the ContribFest thing is, I think, my participation in ContribFest… we'll just jump right in. My participation in ContribFest is, kind of combining both Android and Kotlin to see from those two groups, like, what we can bring together.
For ContribFest, which, for those who are not familiar with it, is going to be an in-person session at KubeCon next month.
And… And during that session, we get people who are first-time contributors to OpenTelemetry to pick a project that they like, that we have in-room support for, and how to teach them to go through, like, looking at contributing MD, cloning the repo, forking the repo, cloning their fork.
and contributing their first PR. That's the goal, is to get people comfortable with the open source process for open telemetry, because every project's slightly different, and literally every repo is also slightly different, and then going through and committing their… yeah, getting their first PR up and getting eyes on stuff. So, with that.
**Jamie Lynch (Palo Alto Networks)** 03:46 Cool.
**Jason Plumb** 03:47 We should tee up some issues that we think are good. Not just first contribution, I think we need to be a little bit careful about that, because I know right now a lot of repos have a lot of, agentic eyes on them, and good first issues get sniped, like, very quickly. So, if we don't have that label yet, I can create that one. There's, like, a ContribFest label that we can put on stuff.
And it's okay for them to be a little contrived, too. Like, we shouldn't let them be, like.
Super, like, nothing burgers, but we should find stuff that, like.
someone can do within an hour. Someone new to the project can do within an hour, is the goal. And, yeah, I just want to get that… get that ball churning, because it'll… it'll be here before we know it.
**Jamie Lynch (Palo Alto Networks)** 04:35 Okay, cool.
Do you know… how many issues we're kind of wanting for this? Like,
**Jason Plumb** 04:45 I think 10 would be more than enough. I think 5 would be a reasonable start.
**Jamie Lynch (Palo Alto Networks)** 04:52 Okay, cool.
**Jason Plumb** 04:53 The only time crunch is like by early, like mid, I think it's the first or the beginning of the second week of November, I think is Kubecon. So.
We have nearly a month, almost a month, yeah.
**Jamie Lynch (Palo Alto Networks)** 05:04 And you're, you're going to be attending that one, is that right?
**Jason Plumb** 05:08 Oh, yeah, I should be in the room, yeah.
**Jamie Lynch (Palo Alto Networks)** 05:12 Okay.
Awesome. I'm happy to… Take a look at that and kind of section off some issues for that, unless you've magically become less swamped.
**Jason Plumb** 05:28 No, I think that's great. I would love help on this and I will do my best to also create some as I can.
**Jamie Lynch (Palo Alto Networks)** 05:35 Yeah, I think that would be cool, particularly if we're finding new contributors who Might not necessarily… not necessarily be aware.
**Jason Plumb** 05:45 Yeah, totally.
Or even people that are like, oh, this session sounds interesting. Oh, yeah, I've been wondering about Kotlin, you know, like that kind of stuff.
Yeah.
As an aside, before we get to the next topic, have you… or anyone else attempted to use, the PR stacks yet?
**Jamie Lynch (Palo Alto Networks)** 06:09 I have not, no. It should be enabled now.
**Jason Plumb** 06:14 Yeah.
**Jamie Lynch (Palo Alto Networks)** 06:14 I could give that a go with some of the propagation changes, to be honest. Okay. That'll probably speed things up.
**Jason Plumb** 06:24 Cool, yeah, I'm just tempted to see it in… I'm curious to see… I'm anxious and excited to see it in action, so that's why I bring it up.
**Jamie Lynch (Palo Alto Networks)** 06:32 add an action so I can remember to do that.
**Jason Plumb** 06:36 Cool.
**Jamie Lynch (Palo Alto Networks)** 06:41 Yeah, I think… I'm hopeful that that might make things quicker for developing individual features, because right now it's kind of like, I think it works well for working on A wide number of features at once.
Maybe you have something that's depending on something else. Snack works quite well.
**Jason Plumb** 07:04 Yeah. We're, like, taking a thousand line change and slicing it up into, like, more bite sized units. Yeah. Totally.
Okay.
So entities, I've been joining the spec call since we moved to Android. I can finally do that. And.
entities have come up a few times, and also being talked about in Java, because I think they are available. Like, I think that API is becoming stable, maybe.
It's not complete, but it's at least, I think you can… I think you can poke at entities and get them into the resource. So I think that there's work being done to stabilize that in Java. I think it's stable in the spec.
My question around that is, I know that we… I think we've even… I know that the shortlist for stabilization in Kotlin contained resource.
I don't know that we've stabilized it yet, and should we, give consideration to entities early on?
with the asterisk that I know that one of the primary, not the only, but the primary target for this API and this SDK eventually will be Android, and Android has a very specific interest in entities, with the expectation that one day in our near future, entities will probably be where the session lives.
And maybe user information, too, but, like, the session for sure. And so, should we begin thinking about those earlier rather than later?
And if it's already later, that's fine too, but, like, it might already be later.
Since we have a lot of the resource stuff.
Build.
**Jamie Lynch (Palo Alto Networks)** 08:43 Yeah, I mean… I guess, from a very high-level perspective, it makes sense to me if you think that the API is kind of stabilizing, and other SDKs, like Java, are beginning to implement this.
I think it would make sense to do it now, rather than when… We've got… Like.
Everything.
Yeah, we don't want to be in a situation where we've marked the API as stable like a month ago and then had to change something because This new concept has come out.
**Jason Plumb** 09:21 Yeah, I mean, I think it… at least in Java and other languages, I think, like, JavaScript, I think it was able to fit within the existing… APIs without being breaking, but there might be some rough edges there for sure.
**Jamie Lynch (Palo Alto Networks)** 09:38 Okay, and backing up a little bit, so entities, is it just kind of like a formalized way of defining what's in a resource, or is it something else? I've not really looked into the… concepts too much.
**Jason Plumb** 09:55 Yeah, as a name, I think entities is, like, so abstract, but then again, kind of so is resource, at least within, like, computer science. Like, those two things kind of are intangibles, at least they don't anchor something specific in my brain.
But the way I understand it is, an entity is, like.
Kind of like a domain area within a resource.
It's a descriptor, and even though the resource is itself immutable, you can produce a new representation of the resource with a different entity. So that's kind of what… I think what the API is the ability to Make a new resource from an existing resource with different entities on it.
So that's…
**Jamie Lynch (Palo Alto Networks)** 10:43 Okay.
**Jason Plumb** 10:44 It's a way of like skirting around the mutability issue.
By providing a new representation of the resource.
**Jamie Lynch (Palo Alto Networks)** 10:54 Okay.
Got it.
It's still…
**Jason Plumb** 10:59 I feel like I also am not doing a great job of explaining it.
**Jamie Lynch (Palo Alto Networks)** 11:03 I'm sure it would probably make sense once.
then implementation is there. I always find that helps.
**Jason Plumb** 11:11 Yeah, and there are some in Java. I can probably go find that API and link to it.
**Jamie Lynch (Palo Alto Networks)** 11:21 Cool.
Yeah, I think… Well, I guess as an action.
How would you feel about me just.
Creating like a milestone with a couple of issues.
To initially start looking at this.
**Jason Plumb** 11:42 Yeah, that's cool. I think that makes a lot of sense. Yeah.
And I'm looking at our API… component stability matrix, and I don't see resource listed in there at all, actually.
**Jamie Lynch (Palo Alto Networks)** 11:59 Hmm.
**Carlos Alberto Cortez (Dash0)** 12:01 Oh, really? Interesting.
**Jason Plumb** 12:03 Yeah, it's not in the Matrix. I mean, we have modules for that, though, don't we?
Or is it baked into something else?
**Carlos Alberto Cortez (Dash0)** 12:12 Oh, you mean here?
Sorry.
**Jamie Lynch (Palo Alto Networks)** 12:18 We definitely have an implementation for it, it might just not be documented, perhaps?
That sounds like another thing to check.
**Jason Plumb** 12:32 Yeah, what… There is an API for resource, right?
**Carlos Alberto Cortez (Dash0)** 12:39 Jason, were you talking about the specification or the Kotlin side when you said.
**Jason Plumb** 12:44 I'm talking about the specification. I'm asking about the specification.
**Carlos Alberto Cortez (Dash0)** 12:47 That's weird, yeah. We should have, yeah.
Okay, I will follow up on that.
Yeah, and resource-wise, well, there's an API, but it's part of the SDK.
**Jason Plumb** 13:05 Okay, so it's… that's probably why it's not in there, then, if it's an API that's part of the SDK.
**Carlos Alberto Cortez (Dash0)** 13:11 Yeah, but it should be there. I mean, a lot of stuff that is part of the SDK says API is there, like, environment variables, like, you could argue that.
**Jason Plumb** 13:22 Yeah, that matrix, though, that I was talking about is only the pure API. It's not SDK. Okay. And like Jamie said, there is an implementation.
And it's probably in the SDK, so I was looking in the wrong spot.
**Carlos Alberto Cortez (Dash0)** 13:35 Okay. Yeah.
**Jason Plumb** 13:42 Yeah, there, I see it now. Yeah, it just took me a few clicks, sorry.
**Carlos Alberto Cortez (Dash0)** 13:47 Better be safe than sorry.
**Jason Plumb** 13:53 It's here. That's where it lives.
**Jamie Lynch (Palo Alto Networks)** 14:05 Go ahead.
**Jason Plumb** 14:07 Cool. Yeah. And so there's some API that's described in the spec now about resource detectors, and they're a thing that can I don't know. It's a collaborator for doing entity stuff.
**Jamie Lynch (Palo Alto Networks)** 14:20 Yeah, I think we've actually got that interface and a couple of implementations.
**Jason Plumb** 14:24 Okay.
That's cool. So we might not be too far off.
Anyway, yeah, I think a milestone is a good way to proceed.
I… Yeah, I think that having some concrete stuff within that would help us to get organized on it.
And I'm not… I'm not trying to, assert any priority on it. I… there's other, like, existing momentum that I don't want this to deter from, so I think that's a good way of kind of responding to this.
**Jamie Lynch (Palo Alto Networks)** 14:53 No, I think it's always good to kind of be aware of what's being added in and Even if we can't get around to it, we should create milestones.
**Jason Plumb** 15:03 Killer. Thanks for doing that.
**Jamie Lynch (Palo Alto Networks)** 15:06 Cool. Next item, so just a quick update on… propagation. So currently I've been kind of working on refactoring some of the propagators so that they basically only require the context parameter to extract a span.
So previously by requiring They required a, span factory, let me see… no.
So yeah, I've basically been removing span factory and kind of Extracting it from the context itself, so… Yeah, I think after that, the main thing… is probably… Trying to figure out.
How to create for context implementation. So.
Yeah, I was going to try and follow the JavaScript SDK for that.
So the way they do that is there's a context interface and then you can import a module.
Depending on which implementation you want for… Like, browser or Node.
So.
I think I'll try and have a look at that this week if I get some time and maybe use that to trial out her PR stack feature.
So I don't think there's… Too many actions for her, just… Sharing where I'm at.
**Carlos Alberto Cortez (Dash0)** 16:53 Yeah, thank you so much for that. I will do a quick review. Yeah, this is the right direction.
**Jamie Lynch (Palo Alto Networks)** 17:01 Awesome. Yeah, it feels like we're nearly getting there.
Cool.
Does anyone else have anything they want to discuss?
**Rafael Nicolau** 17:17 Well, nothing from my side. It's just the first meeting here, just trying to get to know you all, getting some more context, so… Nothing done.
**Jason Plumb** 17:25 Yeah, Rafael, welcome. I know that Jamie already gave you a hello, and welcome to the project. You have the repo link, you've cloned it, have you tried building it?
**Rafael Nicolau** 17:34 Yes, I actually have a couple contributions merged already, so I'm just now trying to, yeah, join the meetings. I've been contributing for the past 3 weeks, I want to say.
**Jason Plumb** 17:46 Awesome.
**Rafael Nicolau** 17:46 Well, you've.
**Jason Plumb** 17:47 Been more in the loop than I have for the last three weeks. Thank you.
**Rafael Nicolau** 17:50 You're welcome.
**Jamie Lynch (Palo Alto Networks)** 17:57 Awesome. We can call it there then and everyone can get a bit of time back.
**Jason Plumb** 18:03 Awesome.
**Jamie Lynch (Palo Alto Networks)** 18:03 Cool. Thanks, everyone.
**Carlos Alberto Cortez (Dash0)** 18:05 See you.
**Jason Plumb** 18:05 Yeah, thanks.
Take care.
Bye.
